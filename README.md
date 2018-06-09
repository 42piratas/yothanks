# yo, thanks!

YoThanks scraps all repostiories linked to a certain GitHub Access Token and captures the names and (public) emails of all people who contributed to those repos. Then it compares this list of names and emails with the list of contributors from the file `contributors.json` to check if there's any new contributor since the last time it ran --- and for those new contributors, if any and if they have a public email, the application sends an email based on the template from `thanks_template.txt`. Last but not least, the application adds the new contributors to the file `contributors.json`.

## How-to
Please, check [INSTRUCTIONS.md](https://github.com/42piratas/yothanks/blob/master/INSTRUCTIONS.md)

## Lots of love to
[Python](https://www.python.org), [PyGithub](https://pypi.org/project/PyGithub/), [yagmail](http://pygithub.readthedocs.io),  [Colorama](https://pypi.org/project/colorama/)
