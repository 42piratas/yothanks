# yo, thanks!

YoThanks scraps all repostiories linked to a certain GitHub Access Token and captures the names and (public) emails of all people who contributed to those repos. Then it compares this list of names and emails with the list of contributors from the file `contributors.json` to check if there's any new contributor since the last time it ran --- and for those new contributors, if any and if they have a public email, the application sends an email based on the template from `thanks_template.txt`. Last but not least, the application adds the new contributors to the file `contributors.json`.

## How-to
Please, check [INSTRUCTIONS.md](https://github.com/42piratas/yothanks/blob/master/INSTRUCTIONS.md)

## To-do
- ~~Only add contributors to the list of all-time contributors after sending them an email~~
- ~~Point out new contributors without public email~~
- ~~Email content must come from a template/separate file with a placeholder for contributor.name~~
- Security practices regarding access to GH
  - Encrypt GH's Access Token locally, requires a pass to decrypt every time (???)
  - Use same Gmail password as pk and then request Gmail pw every time (???)
- ~~Security practices regarding access to SMPT~~
- Deal with exceptions
  - no contributors.json
  - empty contributors.json
  - no githubkey
  - no gmail info
- Point out relationship contributors x repos
- Test in a bigger domain of repositories
- Add py.tests
- Add logs
- Document the code properly
- Write a decent README with a proper 'how-to'
- Automatically updated README with the number of all-time contributors
- Make it easier to setup
- Add license
- ~~Reorganize and pack~~

## Lots of love to
[Python](https://www.python.org), [PyGithub](https://pypi.org/project/PyGithub/), [yagmail](http://pygithub.readthedocs.io),  [Colorama](https://pypi.org/project/colorama/)
