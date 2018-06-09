# Instructions

- Requires [Python 3](https://www.python.org/downloads/)
- It **might** require that you allow `less secure apps` on your Gmail account :sweat_smile: https://myaccount.google.com/lesssecureapps
- Clone this repository and install the requirements
```
$ git clone https://github.com/42piratas/yothanks.git
$ cd yothanks
$ pip install -r requirements.txt
```
- Double check to make sure the `.gitignore` file cointains a rule to ignore `secrets*`
- Create an empty file `secrets.py` inside the `modules` folder
- Create an Access Token on GitHub > https://github.com/settings/tokens
- Add the GitHub Access Token to `secrets.py` file as follow:
```
githubtoken = "your_GitHub_Access_Token_here"
```
<!--
- Run a Python interpreter and run the following to register your GMail credentials with [yagmail](http://yagmail.readthedocs.io/en/latest/setup.html):
```
 import yagmail
 yagmail.register('your_gmail_username','your_gmail_password')
```
  - For extra safety, create a `.yagmail` file in your home folder, containing only `your_gmail_username`
--->

- Update the file `thanks_template.txt` from the folder `ref` as you wish
- Access the folder `modules` and run `yo_thanks.py`
```
$ cd modules
$ python yo_thanks.py
```
- Or play with the different modules individually to see what happen :metal: