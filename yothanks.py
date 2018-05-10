from updatecontributors import *
from sendthanksto import sendthanksto
from colorama import init, Back, Style #https://pypi.org/project/colorama/

init() # initialise Colorama

new_contributors_with_email = {}
new_contributors_wo_email = {}

identifyNewContributors()

if bool(new_contributors) == False:
    print('\n')
    print(Back.BLUE + "SORRY, NO NEW CONTRIBUTORS :~(")
    print('\n')
    quit()

for contributor in new_contributors:
    if new_contributors[contributor][1] == None:
        new_contributors_wo_email[contributor] = [new_contributors[contributor][0], new_contributors[contributor][1]]
    else:
        new_contributors_with_email[contributor] = [new_contributors[contributor][0], new_contributors[contributor][1]]

if bool(new_contributors_with_email) == True:

    sendthanksto(new_contributors_with_email)

    print('\n')

    print(Back.BLUE + "THANKS SENT TO THE FOLLOWING NEW CONTRIBUTORS" + Style.RESET_ALL)
    print(Back.GREEN + "{:<30} {:<30} {:<40}"
          .format('LOGIN','NAME','EMAIL') + Style.RESET_ALL)

    for new_contributor in new_contributors_with_email:
        print("{:<30} {:<30} {}".format(new_contributor,
                                        new_contributors_with_email[new_contributor][0],
                                        new_contributors_with_email[new_contributor][1]))
    print('\n')

if bool(new_contributors_wo_email) == True:

    print('\n')

    print(Back.BLUE + "THE FOLLOWING NEW CONTRIBUTORS DON'T HAVE PUBLIC EMAIL ADDRESS" + Style.RESET_ALL)
    print(Back.GREEN + "{:<30} {:<30} {:<40}"
          .format('LOGIN','NAME','EMAIL') + Style.RESET_ALL)

    for new_contributor in new_contributors_wo_email:
        print("{:<30} {:<30} {}".format(new_contributor,
                                        new_contributors_wo_email[new_contributor][0],
                                        new_contributors_wo_email[new_contributor][1]))
    print('\n')

updateFileContributors()
