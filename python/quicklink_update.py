import csv
import os
import re
import subprocess
import sys
from subprocess import CalledProcessError

import requests


def prepare_git_command(command, repo_path, print_stdout=False):
    def run():
        try:
            process_result = subprocess.run(
                args=['git'] + command,
                cwd=repo_path,
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


def prepare_git_pull_request(owner, guide_repo, pr_branch):
    def create_pull_request():
        github_token = os.getenv('GITHUB_TOKEN')

        if github_token is not None:
            github_base_url = 'https://api.github.com'

            request_headers = {
                'Accept': 'application/vnd.github+json',
                'Authorization': f'Bearer {github_token}'
            }

            request_data = {
                'title': 'Update quick links',
                'head': pr_branch,
                'base': 'main'
            }

            create_pr_url = f'{github_base_url}/repos/{owner}/{guide_repo}/pulls'

            pr_request_response = requests.post(
                url=create_pr_url,
                json=request_data,
                headers=request_headers,
            )

            if pr_request_response.status_code == requests.codes.created:
                print(
                    f"PR creation for {pr_branch} in {guide_repo} successful")
            else:
                print(
                    f"PR creation for {pr_branch} in {guide_repo} failed. "
                    f"Error response: {pr_request_response.json()}")
        else:
            print("Warning: GitHub token not found. PR can't be created")

        return None

    return create_pull_request


def apply_until_false(*funcs):
    for func in funcs:
        if not func():
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

        for entry in it:
            if entry.is_dir() and entry.name.endswith('-guide'):
                prepared_quick_links_update = lambda: prepare_quick_links_update(
                    entry,
                    quick_links_relative_file_path,
                    service_anchors
                )

                commands_to_run = [prepared_quick_links_update]

                is_git_repo = os.path.isdir(
                    os.path.join(entry.path, '.git'))

                if is_git_repo:
                    branch_name = f"update-quick-links-{os.urandom(2).hex()}"

                    commands_to_run_before_update = [
                        prepare_git_command(
                            ['checkout', 'main'],
                            entry.path
                        ),
                        prepare_git_command(
                            ['pull', 'origin', 'main'],
                            entry.path
                        ),
                        prepare_git_command(
                            ['checkout', '-b', branch_name],
                            entry.path
                        ),
                    ]

                    commands_to_run_after_update = [
                        prepare_git_command(
                            ['add', '.'],
                            entry.path
                        ),
                        prepare_git_command(
                            ['commit', '-m', 'update quick links'],
                            entry.path
                        ),
                        prepare_git_command(
                            ['push', 'origin', branch_name],
                            entry.path
                        ),
                        prepare_git_command(
                            ['diff', '--color=always', 'main...'],
                            entry.path,
                            print_stdout=True
                        ),
                        prepare_git_pull_request(
                            "tudorsonycx",
                            entry.name,
                            branch_name
                        )
                    ]

                    commands_to_run = (
                            commands_to_run_before_update
                            + commands_to_run
                            + commands_to_run_after_update
                    )

                    apply_until_false(*commands_to_run)

                    cleanup_commands = [
                        prepare_git_command(
                            ['checkout', 'main'],
                            entry.path
                        ),
                        prepare_git_command(
                            ['branch', '-D', branch_name],
                            entry.path
                        )
                    ]

                    apply_until_false(*cleanup_commands)


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
