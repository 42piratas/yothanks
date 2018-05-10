'''
Sends emails to a list of recipients
'''

import smtplib

from never_share import secret1, secret2, secret3
from colorama import init, Back, Style #https://pypi.org/project/colorama/

init() # initialise Colorama

# Recipients must be a dictionary
# where KEY=GH login && VALUE = [name, email]
def sendthanksto(recipients):

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(secret1, secret2)
    sender = secret1
    message = "Message_you_need_to_send"

    # for recipient in recipients:
    #     #s.sendmail(sender, recipients[recipient][1], message)
    #     print(sender, recipients[recipient][1], message)

    s.quit()

if __name__ == "__main__":

    # Recipients must be a dictionary
    # where KEY=GH login && VALUE = [name, email]
    recipients = {}
    recipients['test'] = ['Test Name', secret1]
    sendthanksto(recipients)

    print('\n')
    print(Back.BLUE + "THANKS SENT TO" + Style.RESET_ALL)

    print(Back.GREEN + "{:<30} {:<30} {:<30}"
          .format('LOGIN','NAME','EMAIL') + Style.RESET_ALL)
    for recipient in recipients:
        print("{:<30} {:<30} {}".format(recipient,
                                        recipients[recipient][0],
                                        recipients[recipient][1]))
    print('\n')
