# yo, thanks!

### To-do
- ~~Only add contributors to the list of all-time contributors after sending them an email~~
- ~~Point out new contributors without public email~~
- ~~Email content must come from a template/separate file with a placeholder for contributor.name~~
- Security practices regarding access to GH
- ~~Security practices regarding access to SMPT~~
- Deal with exceptions
  - no contributors.json
  - empty contributors.json
  - no githubkey
  - no gmail info
- Point out repos from collaboration
- Test in a bigger domain of repositories
- add py.tests
- add logs
- Document the code
- Write a decent README witha  proper 'how-to'
- Automatically updated README with the number of all-time contributors
- Make it easier to setup
- Add license
- ~~Reorganize and pack~~

### How-to
- Requires [Python 3](https://www.python.org/downloads/)
- Double check to make sure that your `.gitignore` file cointains a rule to ignore `secrets*`
- Create a file `secrets.py` inside the `modules` folder
- Create a Access Token on GitHub > https://github.com/settings/tokens
- Add a GitHub Access Token to `secrets.py` file as follow:
```
githubtoken = "your_GitHub_Access_Token_here"
```
- Run a Python interpreter and run the following to register your GMail credentials with [yagmail](http://yagmail.readthedocs.io/en/latest/setup.html):
```
$ python # Or `python3` depending on your environment
>>> import yagmail
>>> yagmail.register('your_gmail_username','your_gmail_password')
```

- Create a `.yagmail` file in your home folder, containing only your Gmail `your_gmail_username`

### Lots of love to
[Python](https://www.python.org) [PyGithub](https://pypi.org/project/PyGithub/) [yagmail](http://pygithub.readthedocs.io) [Colorama](https://pypi.org/project/colorama/)
