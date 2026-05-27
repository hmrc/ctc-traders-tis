import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
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
                print(
                    f"Error when running git command in {self.repo_path}: {e.stderr}")

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

    def diff_branch(self, branch='main'):
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


def update_quick_links_for_guide(
        guide_entry,
        updated_quick_links_file_content
):
    quick_links_file_path = os.path.join(
        'source',
        'documentation',
        'quick-links.html.md.erb'
    )

    quick_links_file_absolute_path = os.path.join(
        guide_entry.path,
        quick_links_file_path
    )

    will_be_updated = False

    try:
        with open(quick_links_file_absolute_path) as fr:
            guide_quick_links_file_content = fr.read()

            guide_quick_links_file_split_at_heading = split_at_heading(
                guide_quick_links_file_content)

            guide_quick_links_file_front_matter = \
                guide_quick_links_file_split_at_heading[0]

            guide_quick_links_file_content_no_front_matter = \
                guide_quick_links_file_split_at_heading[1]

            if guide_quick_links_file_content_no_front_matter != updated_quick_links_file_content:
                will_be_updated = True
    except FileNotFoundError:
        print(
            f"Quick links file not found for {guide_entry.name}. Skipping...")

    if will_be_updated:
        try:
            with open(quick_links_file_absolute_path, mode='w') as fw:
                guide_updated_quick_links_file_content = (
                        guide_quick_links_file_front_matter
                        + "# Quick Links"
                        + updated_quick_links_file_content
                )

                fw.write(guide_updated_quick_links_file_content)

            print(f"Quick links file updated for: {guide_entry.name}")

            return True
        except Exception as e:
            print(f"Quick links file update failed: {e}")
    else:
        print(
            f"Quick links file identical for {guide_entry.name}. No need for update")

    return None


def main(guide_entries: list[GuideEntry], updated_quick_links_file_content):
    print("Updating quick links...")

    github_client = GitHubClient()
    repo_owner = 'hmrc'

    for guide_entry in guide_entries:
        if os.path.isdir(guide_entry.path):
            prepared_quick_links_update = lambda: update_quick_links_for_guide(
                guide_entry,
                updated_quick_links_file_content
            )

            update_commands = [prepared_quick_links_update]

            is_git_repo = os.path.isdir(
                os.path.join(guide_entry.path, '.git'))

            if is_git_repo:
                git_commands = GitCommands(guide_entry.path)

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
                    git_commands.diff_branch(),
                    github_client.prepare_pull_request(
                        guide_entry.name,
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
        else:
            print(f"{guide_entry.path} is not a directory. Skipping...")


@dataclass
class GuideEntry:
    name: str
    path: str


def grab_guides(quick_links_file_content):
    guides_regex = re.compile(
        r"""(?<=<a href=")https://[a-zA-Z0-9-.]+/(?:[a-zA-Z0-9-]+/)*(?:roadmaps|guides)/([a-zA-Z0-9-]+)(?<!ctc-traders-tis)/(?=".*>.*</a>)""")

    return guides_regex.findall(quick_links_file_content)


def preview_quick_links_update(guide_entries: list[GuideEntry],
                               quick_links_file_content):
    try:
        with tempfile.NamedTemporaryFile(mode='w') as tfw1:
            tfw1.write(quick_links_file_content)
            tfw1.flush()

            quick_links_file_path = os.path.join(
                'source',
                'documentation',
                'quick-links.html.md.erb'
            )

            for guide_entry in guide_entries:
                guide_quick_links_file_absolute_path = os.path.join(
                    guide_entry.path,
                    quick_links_file_path
                )

                try:
                    with open(guide_quick_links_file_absolute_path) as fr:
                        guide_quick_links_file_content = fr.read()

                        guide_quick_links_file_split_at_heading = split_at_heading(
                            guide_quick_links_file_content)

                        guide_quick_links_file_content_no_front_matter = \
                            guide_quick_links_file_split_at_heading[1]

                        with tempfile.NamedTemporaryFile(mode='w') as tfw2:
                            tfw2.write(
                                guide_quick_links_file_content_no_front_matter)
                            tfw2.flush()

                            process_result = subprocess.run(
                                args=['git', 'diff', '--color=always',
                                      tfw2.name, tfw1.name],
                                capture_output=True,
                                text=True
                            )

                            if process_result.returncode == 0:
                                print(
                                    f"Quick links file identical for {guide_entry.name}")
                            elif process_result.returncode == 1:
                                print(
                                    f"Update needed for {guide_entry.name}:")

                                print("".join(process_result.stdout.splitlines(
                                    keepends=True)[4:]))
                            else:
                                print(
                                    f"Error when previewing diff: {process_result.stderr}")
                except FileNotFoundError:
                    print(
                        f"Quick links file not found for {guide_entry.name}. Skipping...")
    except Exception as e:
        print(f"Preview operation failed: {e}")


def split_at_heading(content, heading="# Quick Links"):
    content_split_at_heading = content.split(heading, 1)

    content_front_matter = content_split_at_heading[0]

    content_no_front_matter = content_split_at_heading[1]

    return content_front_matter, content_no_front_matter


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python quicklink_update.py <path_to_guides>")
        print("Usage: python quicklink_update.py <path_to_guides> --preview")

        sys.exit(1)

    is_preview = False

    if len(sys.argv) == 3:
        if sys.argv[2] == '--preview':
            is_preview = True
        else:
            print("Usage: python quicklink_update.py <path_to_guides> --preview")

            sys.exit(1)

    quick_links_file_relative_path = os.path.join(
        '..',
        'source',
        'documentation',
        'quick-links.html.md.erb'
    )

    if not os.path.isfile(quick_links_file_relative_path):
        print("Quick links file must be present in order to update the links")

        sys.exit(1)

    try:
        with open(quick_links_file_relative_path) as fr:
            quick_links_file_content = fr.read()
    except FileNotFoundError:
        print(
            f"Quick links file not found for ctc-traders-tis")

        sys.exit(1)

    guides_abs_path = os.path.abspath(os.path.expanduser(sys.argv[1]))

    if not os.path.isdir(guides_abs_path):
        print("Path provided is not a directory")

        sys.exit(1)

    quick_links_file_content = split_at_heading(quick_links_file_content)[1]

    guides = grab_guides(quick_links_file_content)

    guide_entries = [GuideEntry(guide, os.path.join(guides_abs_path, guide))
                     for guide in guides]

    if is_preview:
        preview_quick_links_update(guide_entries, quick_links_file_content)
    else:
        main(guide_entries, quick_links_file_content)
