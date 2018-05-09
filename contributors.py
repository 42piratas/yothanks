'''
This script gets the updated dictionary of contributors 'all_contributors'
created by 'scraphub.py', compares it with the saved dictionary of
contributors stored in the file 'contributors.json', saves the new entries
in the dictionary 'new_contributors', which will be used later by 'mailer.py',
and then updates 'contributors.json' with the new entries as well
'''

import json

from scraphub import all_contributors #full dictionary of contributors
from colorama import init, Back, Style #https://pypi.org/project/colorama/

init() # initialise Colorama

with open('contributors.json', 'r') as fp:
    data_from_file = json.load(fp)

# Create a dictionary with new contributors only
new_contributors = {}

for contributor in all_contributors:
    if contributor not in data_from_file:
        new_contributors[contributor] = [all_contributors[contributor][0], all_contributors[contributor][1]]

# Save updated dictionary with all-time contributors to 'contributors.json'
with open('contributors.json', 'w') as fp:
      json.dump(all_contributors, fp, sort_keys=True, indent=4)

if __name__ == "__main__":

    if bool(new_contributors) == False:
        print(Back.BLUE + "NO NEW CONTRIBUTORS :~(")
        print('\n')
        quit()

    else:
        print(Back.BLUE + "NEW CONTRIBUTORS" + Style.RESET_ALL)
        print(Back.GREEN + "{:<30} {:<30} {:<30}"
              .format('LOGIN','NAME','EMAIL') + Style.RESET_ALL)

        for new_contributor in new_contributors:
            print("{:<30} {:<30} {}".format(new_contributor,
                                            new_contributors[new_contributor][0],
                                            new_contributors[new_contributor][1]))
        print('\n')
