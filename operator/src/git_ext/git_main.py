import os

from git import Repo

repository_url = "git@github.com:Vetchu/kopf-test.git"
destination_path = "repo"

# Get the current timestamp (in seconds since the epoch)

file_path = "sample.tf"


def expand_ssh_key(ssh_key_path):
    expanded_key_path = os.path.expanduser(ssh_key_path)
    return expanded_key_path


def git_clone(repository_url, destination_path, ssh_key_path=None):
    if ssh_key_path:
        ssh_cmd = f"SSH_AUTH_SOCK=0 ssh-agent -s && ssh-add {expand_ssh_key(ssh_key_path)} && git"
    else:
        ssh_cmd = "git"

    repo = Repo.clone_from(
        repository_url, destination_path
    )  # env={'GIT_SSH_COMMAND': ssh_cmd})
    return repo


def update_and_push_file(repo_path, branch_name, file_path, new_content):
    repo = Repo(repo_path)

    # Create a new branch
    new_branch = repo.create_head(branch_name)
    new_branch.checkout()

    # Update the file with new content
    with open(os.path.join(repo_path, file_path), "w") as file:
        file.write(new_content)

    # Stage and commit changes
    repo.index.add([file_path])
    repo.index.commit("Update file in new branch")

    # Push the changes to the remote repository
    repo.git.push("origin", new_branch)
