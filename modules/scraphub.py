'''
This script outputs a dictionary containing all-time contributors
from all repositories linked to the GH Access Token provided
'''

from github import Github  # http://pygithub.readthedocs.io
from colorama import init, Back, Style  # https://pypi.org/project/colorama

from secrets import githubtoken

init()  # initialise Colorama

# Authentication using GitHub Access Token
octocat = Github(githubtoken)

# Get all repositories OWNED by the user
gh_user = octocat.get_user()
repos = [repo for repo in gh_user.get_repos()
         if repo.owner.login == gh_user.login]

# Create a list with all-time contributors
contributors = []
for repo in repos:
    for contributor in repo.get_collaborators():
        if contributor not in contributors:
            contributors.append(contributor)

# Create a dictionary where KEY = GH_USERNAME : VALUE = [NAME, EMAIL]
all_time_contributors = {}
for n in range(len(contributors)):
    all_time_contributors[contributors[n].login] = [
        contributors[n].name, contributors[n].email]

# If called directly, outputs ALL-TIME-CONTRIBUTORS to the terminal
if __name__ == "__main__":
    repositories = [r.name for r in repos]

    print('\n')
    print(Back.RED + "REPOSITORIES SCRAPPED" + Style.RESET_ALL)
    print(repositories)

    print('\n')
    print(Back.BLUE + "ALL-TIME CONTRIBUTORS" + Style.RESET_ALL)
    print(Back.GREEN + "{:<30} {:<30} {:<40}".format('LOGIN', 'NAME', 'EMAIL') + Style.RESET_ALL)
    for contributor in all_time_contributors:
        print("{:<30} {:<30} {}".format(contributor,
                                        all_time_contributors[contributor][0],
                                        all_time_contributors[contributor][1]))
    print('\n')
