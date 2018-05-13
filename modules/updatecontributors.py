'''
This script gets the updated dictionary of contributors 'all_contributors'
created by 'scraphub.py', compares it with the saved dictionary of
contributors stored in the file 'contributors.json', saves the new entries
in the dictionary 'new_contributors', which will be used later by 'mailer.py',
and then updates 'contributors.json' with the new entries as well
'''

import json

from colorama import init, Back, Style #https://pypi.org/project/colorama/

from .scraphub import all_contributors #full dictionary of contributors

init() # initialise Colorama

new_contributors = {}

def identifyNewContributors():
    with open('modules/contributors.json', 'r') as fp:
        data_from_file = json.load(fp)

        # Create a dictionary of new contributors only
        for contributor in all_contributors:
            if contributor not in data_from_file:
                new_contributors[contributor] = [all_contributors[contributor][0],
                                                 all_contributors[contributor][1]]

    return new_contributors
    return all_contributors

def updateFileContributors():
    # Save updated dictionary with all-time contributors to 'contributors.json'
    with open('modules/contributors.json', 'w') as fp:
          json.dump(all_contributors, fp, sort_keys=True, indent=4)

if __name__ == "__main__":

    identifyNewContributors()

    updateFileContributors()

    if bool(new_contributors) == False:
        print('\n')
        print(Back.BLUE + "NO NEW CONTRIBUTORS :~(")
        print('\n')
        quit()

    else:
        print('\n')
        print(Back.BLUE + "NEW CONTRIBUTORS" + Style.RESET_ALL)
        print(Back.GREEN + "{:<30} {:<30} {:<40}"
              .format('LOGIN','NAME','EMAIL') + Style.RESET_ALL)

        for new_contributor in new_contributors:
            print("{:<30} {:<30} {}".format(new_contributor,
                                            new_contributors[new_contributor][0],
                                            new_contributors[new_contributor][1]))
        print('\n')