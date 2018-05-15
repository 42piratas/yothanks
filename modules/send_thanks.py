'''
Sends emails to a list of recipients
Note that "recipients" must be a dictionary
where KEY=GH login && VALUE = [name, email]
'''

import yagmail #https://github.com/kootenpv/yagmail

from pathlib import Path
from colorama import init, Back, Style #https://pypi.org/project/colorama

from secrets import test_email

init() # initialise Colorama

email_subject = "MARKET Protocol - Welcome!" # Set your subject here!!!

thanks_template =  Path("../ref/thanks_template.txt")

with open(thanks_template) as f:
    thanks_template = f.read()

def send_thanks(recipients):

    yag = yagmail.SMTP()

    for recipient in recipients:
        txt = thanks_template.format(name=recipients[recipient][0])
        contents = [txt] # contents, attachments, to, cc, bcc -- all can be a list (plural) or a string (singular)
        yag.send(recipients[recipient][1], email_subject, contents)

if __name__ == "__main__":

    recipients = {}
    recipients['test'] = ['Test Name', test_email]
    send_thanks(recipients)

    print('\n')
    print(Back.BLUE + "THANKS SENT TO" + Style.RESET_ALL)

    print(Back.GREEN + "{:<30} {:<30} {:<30}"
          .format('LOGIN','NAME','EMAIL') + Style.RESET_ALL)
    for recipient in recipients:
        print("{:<30} {:<30} {}".format(recipient,
                                        recipients[recipient][0],
                                        recipients[recipient][1]))
    print('\n')
