#! /Users/42piratas/.virtualenvs/yothanks/bin/python

'''
This script gets the updated dictionary of contributors 'contributors'
created by 'scraphub.py', compares it with the saved dictionary of
contributors stored in the file 'contributors.json', saves the new entries
in the dictionary 'new_contributors', which will be used later by 'send_thanks.py,
and last updates 'contributors.json' with the new entries
'''

import json

from pathlib import Path

from scraphub import contributors  # dictionary with all-time contributors

contributors_json = Path("../ref/contributors.json")
contributors_md = Path("../ref/CONTRIBUTORS.md")

new_contributors = {}


def find_new_contributors():
    '''Compares the file of previous contributors with the updated list of
    contributors and adds the new ones, if any, to a dictionary'''

    with open(contributors_json, 'r') as json_file:
        data_from_file = json.load(json_file)

        # Create a dictionary of new contributors only
        for contributor in contributors:
            if contributor not in data_from_file:
                new_contributors[contributor] = [
                    contributors[contributor]['name'],
                    contributors[contributor]['email'],
                    contributors[contributor]['repos']]


def upd_contributors():
    '''Updates records of contributors'''

    # Save all-time contributors to json file
    with open(contributors_json, 'w') as json_file:
        json.dump(contributors, json_file, sort_keys=True, indent=4)

    with open(contributors_md, 'w') as md_file:

        md_file.write("# Contributors \n")
        # md_file.write("---- | ---- | ---- | ---- | ---- | ---- | ---- \n")

        for contributor in contributors:

            # >>>>> TO ADD THE REPOS TO THE RECORDS
            # repos = ", ".join(contributors[contributor]['repos'])
            # Uncomment the line below to create record with repos
            # md_record = ("@{} contributed to {};   \n".format(contributor, repos))

            if contributors[contributor]['name'] != None:

                md_record = ('{} @{}    \n'.format(
                    contributors[contributor]['name'], contributor))
                #md_record = ("{} @{}    \n".format(contributors[contributor]['name'], contributor))
                md_file.write(md_record)
            else:
                md_record = ("@{}    \n".format(contributor))
                md_file.write(md_record)

            # >>>>> TO CREATE A TABLE WITH AVATARS
            # if contributors[contributor]['name'] != None:
            #
            #     md_record = ('| <img src="{}" width="100px;"/>    \n@{}    \n \n'.format(
            #         contributors[contributor]['avatar'], contributor))
            #     #md_record = ("{} @{}    \n".format(contributors[contributor]['name'], contributor))
            #     md_file.write(md_record)
            # else:
            #     md_record = ("@{}    \n".format(contributor))
            #     md_file.write(md_record)


if __name__ == "__main__":

    from colorama import init, Back, Style  # https://pypi.org/project/colorama
    init()  # initialise Colorama

    find_new_contributors()

    # COMMENT BELOW TO deactivated/commented to
    # not update contributors.json in test mode
    upd_contributors()

    if not new_contributors:
        print(Back.BLUE + "NO NEW CONTRIBUTORS :~(")
        print('\n')
        quit()

    else:
        print('\n')
        print(Back.BLUE + "NEW CONTRIBUTORS" + Style.RESET_ALL)
        print(Back.GREEN + "{:<30} {:<30} {:<40}"
              .format('LOGIN', 'NAME', 'EMAIL') + Style.RESET_ALL)

        for new_contributor in new_contributors:
            print("{!s:<30} {!s:<30} {}".format(new_contributor,
                                                new_contributors[new_contributor][0],
                                                new_contributors[new_contributor][1]))
        print('\n')
