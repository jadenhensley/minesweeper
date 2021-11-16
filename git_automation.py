import os, sys, subprocess

cmd_args = []

def get_git_status():
    git_status = subprocess.run("git status", stdout=subprocess.PIPE, shell=True)
    message = git_status.stdout.decode()
    return message

def git_pull():
    git_pull = subprocess.run("git pull", stdout=subprocess.PIPE, shell=True)
    message = git_pull.stdout.decode()
    return message

def git_push():
    git_push = subprocess.run('git push', stdout=subprocess.PIPE, shell=True)
    message = git_push.stdout.decode()
    return message

def git_add_all():
    git_add = subprocess.run("git add *", stdout=subprocess.PIPE, shell=True)


def git_commit_all(commit_message="adding project files"):
    git_add_all()
    print("added untracked files.")
    git_commit = subprocess.run(f'git commit -m "{commit_message}"', stdout=subprocess.PIPE, shell=True)
    
    
    if "nothing to commit" in git_pull():
        pass
    else:
        git_commit = subprocess.run(f'git commit -m "{commit_message}"', stdout=subprocess.PIPE, shell=True)
    git_push()

status = get_git_status()

if "untracked" in status:
    git_commit_all()
    print(get_git_status())

if "branch is ahead" in status:
    if ("Changes to be committed" in status) or ("Changes not staged for commit" in status):
        git_commit_all()
    git_push()
    print(get_git_status())


if "up to date" in status:
    if ("Changes to be committed" in status) or ("Changes not staged for commit" in status):
        git_commit_all()
    else:
        print('repository is up to date. nothing to do.')
if "behind" in status:
    print('repository is behind. need to pull from master/main branch')
    git_pull()