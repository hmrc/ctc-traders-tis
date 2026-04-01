import csv
import os
import re
import subprocess
import sys
from subprocess import CalledProcessError

import requests


class GitCommands:
    def __init__(self, repo_path):
        self.repo_path = repo_path

    def __prepare_git_command(self, command: list[str], print_stdout=False):
        def run():
            try:
                process_result = subprocess.run(
                    args=['git'] + command,
                    cwd=self.repo_path,
                    capture_output=True,
                    text=True, check=True
                )

                if print_stdout:
                    print(process_result.stdout)
                return True
            except CalledProcessError as e:
                print(f"{e.stderr}")

                return False

        return run

    def checkout(self, branch='main', create_new=False):
        create_new_option = ['-b'] if create_new else []
        checkout_command = ['checkout'] + create_new_option + [branch]

        return self.__prepare_git_command(checkout_command)

    def pull(self, branch='main', remote='origin'):
        pull_command = ['pull', remote, branch]

        return self.__prepare_git_command(pull_command)

    def add_all(self):
        add_all_command = ['add', '.']

        return self.__prepare_git_command(add_all_command)

    def commit(self, message):
        commit_command = ['commit', '-m', message]

        return self.__prepare_git_command(commit_command)

    def push(self, branch, remote='origin'):
        push_command = ['push', remote, branch]

        return self.__prepare_git_command(push_command)

    def diff(self, branch='main'):
        diff_command = ['diff', '--color=always', f'{branch}...']

        return self.__prepare_git_command(diff_command, print_stdout=True)

    def delete_branch(self, branch):
        delete_command = ['branch', '-D', branch]

        return self.__prepare_git_command(delete_command)


class GitHubClient:
    def __init__(self):
        self.token = os.getenv('GITHUB_TOKEN')
        if self.token is None:
            print(
                "Warning: GitHub token not found in the environment variables. "
                "Calls to the GitHub API will likely fail."
            )

        self.session = requests.session()
        self.base_url = 'https://api.github.com'
        self.session.headers.update({
            'Accept': 'application/vnd.github+json',
            'Authorization': f'Bearer {self.token}'
        })

    def __post(self, endpoint, data):
        url = f'{self.base_url}{endpoint}'
        return self.session.post(url, json=data)

    def create_pull_request(self, repo, owner, branch, title):
        create_pr_endpoint = f'/repos/{owner}/{repo}/pulls'

        request_data = {
            'title': title,
            'head': branch,
            'base': 'main'
        }

        response = self.__post(create_pr_endpoint, data=request_data)

        if response.status_code == requests.codes.created:
            print(
                f"PR creation for {branch} in {repo} successful")
        else:
            print(
                f"PR creation for {branch} in {repo} failed. "
                f"Error response: {response.text}")

    def prepare_pull_request(self, repo, owner, branch, title):
        return lambda: self.create_pull_request(repo, owner, branch, title)


def apply_until_false(*funcs):
    for func in funcs:
        if isinstance(func, list):
            for f in func:
                if not f():
                    break
        elif not func():
            break


def prepare_quick_links_update(
        guide_entry,
        quick_links_file_path,
        service_anchors: list[tuple[str, str]]
):
    service_to_new_link_dict = dict(service_anchors)

    all_services = service_to_new_link_dict.keys()
    all_services_pattern = '|'.join(all_services)

    service_anchor_regex = re.compile(
        rf"""(?<=<a href=")\S+(?=".*>({all_services_pattern})</a>)""")

    absolute_quick_links_file_path = os.path.join(
        guide_entry.path,
        quick_links_file_path
    )

    will_be_updated = False

    try:
        with open(absolute_quick_links_file_path) as fr:
            quick_links_file_content = fr.read()

            quick_links_file_updated_content = service_anchor_regex.sub(
                lambda match: service_to_new_link_dict[match.group(1)],
                quick_links_file_content
            )

            if quick_links_file_content != quick_links_file_updated_content:
                will_be_updated = True
    except FileNotFoundError:
        print(
            f"Quick links file not found for {guide_entry.name}. Skipping...")

    if will_be_updated:
        try:
            with open(absolute_quick_links_file_path, mode='w') as fw:
                fw.write(quick_links_file_updated_content)

            print(f"Quick links file updated for: {guide_entry.name}")

            return True
        except Exception as e:
            print(f"Quick links file update failed: {e}")
    else:
        print(
            f"Quick links file identical for {guide_entry.name}. No need for update")

    return None


def main(service_anchors: list[tuple[str, str]], guides_path):
    with os.scandir(guides_path) as it:
        print("Updating quick links...")

        quick_links_relative_file_path = os.path.join(
            'source',
            'documentation',
            'quick-links.html.md.erb'
        )

        github_client = GitHubClient()
        repo_owner = 'hmrc'

        for entry in it:
            if entry.is_dir() and entry.name.endswith('-guide'):
                prepared_quick_links_update = lambda: prepare_quick_links_update(
                    entry,
                    quick_links_relative_file_path,
                    service_anchors
                )

                update_commands = [prepared_quick_links_update]

                is_git_repo = os.path.isdir(
                    os.path.join(entry.path, '.git'))

                if is_git_repo:
                    git_commands = GitCommands(entry.path)

                    branch_name = f"update-quick-links-{os.urandom(2).hex()}"

                    commands_to_run_before_update = [
                        git_commands.checkout(),
                        git_commands.pull(),
                        git_commands.checkout(branch_name, create_new=True),
                    ]

                    commands_to_run_after_update = [
                        git_commands.add_all(),
                        git_commands.commit('update quick links'),
                        git_commands.push(branch_name),
                        git_commands.diff(),
                        github_client.prepare_pull_request(
                            entry.name,
                            repo_owner,
                            branch_name,
                            title="Update quick links"
                        )
                    ]

                    update_commands = (
                            commands_to_run_before_update
                            + update_commands
                            + commands_to_run_after_update
                    )

                    cleanup_commands = [
                        git_commands.checkout(),
                        git_commands.delete_branch(branch_name)
                    ]

                    apply_until_false(update_commands, cleanup_commands)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_guides>")

        sys.exit(1)

    guides_abs_path = os.path.abspath(os.path.expanduser(sys.argv[1]))

    if not os.path.isdir(guides_abs_path):
        print("Path provided is not a directory")

        sys.exit(1)

    rows = []

    try:
        with open('quicklinks.csv', newline='') as csv_fr:
            reader = csv.reader(csv_fr, delimiter=',')

            # skip header row
            header_row = next(reader)

            for row in reader:
                rows.append(tuple(row))
    except FileNotFoundError:
        print("Quick links CSV file doesn't exist")

        sys.exit(1)

    main(rows, guides_abs_path)
