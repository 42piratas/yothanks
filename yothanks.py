from contributors import new_contributors
from sendthanksto import sendthanksto
from colorama import init, Back, Style #https://pypi.org/project/colorama/

init() # initialise Colorama

if bool(new_contributors) == False:
    print(Back.BLUE + "NO NEW CONTRIBUTORS :~(")
    quit()
else:
    sendthanksto(new_contributors)

    print(Back.BLUE + "THANKS SENT TO" + Style.RESET_ALL)
    print(Back.GREEN + "{:<30} {:<30} {:<30}"
          .format('LOGIN','NAME','EMAIL') + Style.RESET_ALL)

    for new_contributor in new_contributors:
        print("{:<30} {:<30} {}".format(new_contributor,
                                        new_contributors[new_contributor][0],
                                        new_contributors[new_contributor][1]))
    print('\n')
