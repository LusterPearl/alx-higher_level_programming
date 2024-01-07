#!/usr/bin/python3
'''
Please list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”
You must use the GitHub API,
Print all commits by: `<sha>: <author name>` (one by line)
Write a Python script that takes 2 arguments in order to solve this challenge.
The first argument will be the repository name
The second argument will be the owner name
'''
import requests
from sys import argv


def fetch_commits(repo, owner):
    """Fetches and prints 10 most recent commits from a GitHub repository."""
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    headers = {
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28',
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            commits = response.json()[:10]
            for commit in commits:
                sha = commit['sha']
                author = commit['commit']['author']['name']
                print(f"{sha}: {author}")
        else:
            print(f"Error: {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")


if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage: ./100-github_commits.py <repository> <owner>")
        exit(1)

    repo = argv[1]
    owner = argv[2]

    fetch_commits(repo, owner)
