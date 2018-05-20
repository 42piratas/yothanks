'''
This script gets the updated dictionary of contributors 'all_time_contributors'
created by 'scraphub.py', compares it with the saved dictionary of
contributors stored in the file 'contributors.json', saves the new entries
in the dictionary 'new_contributors', which will be used later by 'mailer.py',
and then updates 'contributors.json' with the new entries as well
'''

import json

from pathlib import Path
from colorama import init, Back, Style  # https://pypi.org/project/colorama/

from scraphub import all_time_contributors  # full dictionary of contributors

init()  # initialise Colorama

contributors_file = Path("../ref/contributors.json")

new_contributors = {}


def find_new_contributors():
    '''Compares the file of previous contributors with the updated list of
    contributors and adds the new ones, if any, to a dictionary'''

    with open(contributors_file, 'r') as jsonfile:
        data_from_file = json.load(jsonfile)

        # Create a dictionary of new contributors only
        for contributor in all_time_contributors:
            if contributor not in data_from_file:
                new_contributors[contributor] = [
                    all_time_contributors[contributor][0],
                    all_time_contributors[contributor][1]]


def upd_contributors():
    '''Updates the records of contributors'''

    # Here we are actually saving everyone from all-time
    with open(contributors_file, 'w') as jsonfile:
        json.dump(all_time_contributors, jsonfile, sort_keys=True, indent=4)


if __name__ == "__main__":

    find_new_contributors()

    # eactivated/commented to not update contributors.json in test mode
    # upd_contributors()

    if new_contributors is False:
        print(Back.BLUE + "NO NEW CONTRIBUTORS :~(")
        print('\n')
        quit()

    else:
        print('\n')
        print(Back.BLUE + "NEW CONTRIBUTORS" + Style.RESET_ALL)
        print(Back.GREEN + "{:<30} {:<30} {:<40}"
              .format('LOGIN', 'NAME', 'EMAIL') + Style.RESET_ALL)

        for new_contributor in new_contributors:
            print("{:<30} {:<30} {}".format(new_contributor,
                                            new_contributors[new_contributor][0],
                                            new_contributors[new_contributor][1]))
        print('\n')
