#! /Users/42piratas/.virtualenvs/yothanks/bin/python

'''
This script outputs a dictionary containing all-time contributors
from all repositories linked to the GH Access Token provided
'''

from github import Github  # http://pygithub.readthedocs.io

from secrets import githubtoken, organization

# Authentication using GitHub Access Token
octocat = Github(githubtoken)

# Get all repositories from the organization
# IF the user has push access to the respective repo
gh_org = octocat.get_organization(organization)

repos = []
for repo in gh_org.get_repos():
    if repo.permissions.push:
        # We are excluding contributors from repo 'docs'
        if repo.name != "docs":
            repos.append(repo)

# Create a list with all-time contributors
contributors = {}
for repo in repos:
    for contributor in repo.get_contributors():
        if contributor.login not in contributors:
            contributors[contributor.login] = {'name': contributor.name,
                                               'email': contributor.email,
                                               'avatar': contributor.avatar_url,
                                               'repos': [repo.name]}
        else:
            contributors[contributor.login]['repos'].append(repo.name)


# # If called directly, outputs ALL-TIME-CONTRIBUTORS to the terminal
if __name__ == "__main__":

    from colorama import init, Back, Style  # https://pypi.org/project/colorama
    init()  # initialise Colorama

    print('\n')
    print(Back.BLUE + "ALL-TIME CONTRIBUTORS" + Style.RESET_ALL)
    print(Back.GREEN + "{:<30} {:<30} {:<40}".format('LOGIN', 'NAME', 'EMAIL') + Style.RESET_ALL)
    for contributor in contributors:
        print("{!s:<30} {!s:<30} {}".format(contributor,
                                            contributors[contributor]['name'],
                                            contributors[contributor]['email']))
    print('\n')
