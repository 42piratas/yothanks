'''
Sends emails to a list of recipients
'''

import yagmail #https://github.com/kootenpv/yagmail

from pathlib import Path
from colorama import init, Back, Style #https://pypi.org/project/colorama

from nevershare_secrets import secret1, secret2

init() # initialise Colorama

email_subject = "MARKET Protocol - Welcome!" # Set your subject here!!!

thanks_template =  Path("../ref/thanks_template.txt")

with open(thanks_template) as f:
    thanks_template = f.read()

# Recipients must be a dictionary
# where KEY=GH login && VALUE = [name, email]
def send_thanks(recipients):

    # s = smtplib.SMTP('smtp.gmail.com', 587)
    # s.starttls()
    # s.login(secret1, secret2)
    # sender = secret1
    # message = "Message_you_need_to_send"

    # for recipient in recipients:
    #     s.sendmail(sender, recipients[recipient][1], message)
    #     print(sender, recipients[recipient][1], message)
    #
    # s.quit()

    yag = yagmail.SMTP()

    for recipient in recipients:
        txt = thanks_template.format(name=recipients[recipient][0])
        contents = [txt] # contents, attachments, to, cc, bcc -- all can be a list (plural) or a string (singular)
        yag.send(recipients[recipient][1], email_subject, contents)

if __name__ == "__main__":

    # Recipients must be a dictionary
    # where KEY=GH login && VALUE = [name, email]
    recipients = {}
    recipients['test'] = ['Test Name', secret1]
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
