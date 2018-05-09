'''
This script outputs a dictionary containing all-time contributors
from all repositories linked to the authentication data provided
'''

from github import Github
from itertools import chain
from never_data import secret3
from colorama import init, Back, Style #https://pypi.org/project/colorama/

init() # initialise Colorama

# Authentication using GitHub access token
octocat = Github(secret3)

# OR using username and password
# g = Github("user", "password")

# Get all repositories
repos = octocat.get_user().get_repos()

# Create a list  with all contributors
# Note that this list cointains nested lists
contributors = [[_contributor for _contributor in _repo.get_collaborators()]
                for _repo in repos]

# Remove the nested lists, but keeps all itens within the root list
# Note that all itens are instances of <class 'github.NamedUser.NamedUser'>
contributors = list(chain.from_iterable(contributors))

# Remove duplicates
contributors_unique = list()
for _contributor in contributors:
    if _contributor not in contributors_unique:
        contributors_unique.append(_contributor)

# Create a dictionary where KEY = LOGIN, VALUE = [NAME, EMAIL]
all_contributors = {}
for n in range(len(contributors_unique)):
    all_contributors[contributors_unique[n].login] = [contributors_unique[n].name, contributors_unique[n].email]

if __name__ == "__main__":
    print(Back.BLUE +"ALL-TIME CONTRIBUTORS" + Style.RESET_ALL)
    print(Back.GREEN + "{:<20} {:<30} {:<30}".format('LOGIN','NAME','EMAIL') + Style.RESET_ALL)
    for contributor in all_contributors:
        print("{:<30} {:<30} {}".format(contributor,
                                        all_contributors[contributor][0],
                                        all_contributors[contributor][1]))
    print('n' * 2)
