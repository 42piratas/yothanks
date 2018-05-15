- Requires [Python 3](https://www.python.org/downloads/)
- It might require that you allow less secure apps on your Gmail account > https://myaccount.google.com/lesssecureapps
- Clone this repository and install the requirements
```
$ git clone https://github.com/42piratas/yothanks.git
$ cd yothanks
$ pip install -r requirements.txt
```
- Double check to make sure that the `.gitignore` file cointains a rule to ignore `secrets*`
- Create an empty file `secrets.py` inside the `modules` folder
- Create an Access Token on GitHub > https://github.com/settings/tokens
- Add the GitHub Access Token to `secrets.py` file as follow:
```
githubtoken = "your_GitHub_Access_Token_here"
```
- Run a Python interpreter and run the following to register your GMail credentials with [yagmail](http://yagmail.readthedocs.io/en/latest/setup.html):
```
>>> import yagmail
>>> yagmail.register('your_gmail_username','your_gmail_password')
```
- Create a `.yagmail` file in your home folder, containing only `your_gmail_username`
- Update the file `thanks_template.txt` from the folder `ref` as you wish
- In the folder modules, `run yo_thanks.py`
```
python yo_thanks.py
```

## Test Mode
You can run the different modules individually to check the process in test mode.

- Run `scraphub.py` to check the repositories analyzed and the list of all-time contributors. This module won't change the `contributors.json` file.
- Add a test email address to the `secrets.py` file as `test_email = "your@email.com"`, then run `send_thanks.py`to receive an test email on that address.
- Run `update_contributors.py` to see the list of new contributors in the shell. This module won't change the file `contributors.json` either.
