# yo, thanks!

**tl;dr** Easily send thank you emails to the contributors of your projects on GitHub.

## what? 

**YoThanks** scraps all repostiories linked to a certain `GitHub Access Token` and captures the names and (public) emails of all people who contributed to those repos. Then it compares this list of names and emails with the list of contributors from the file `contributors.json` to check if there's any new contributor since the last time the script was ran --- and to those new contributors, *if any and if they have a public email*, the application sends an email based on the template from `thanks_template.txt`. Last but not least, the application then adds the new contributors to the files `contributors.json` and `CONTRIBUTORS.md`.

## how-to  

Please, check the [INSTRUCTIONS](https://github.com/42piratas/yothanks/blob/master/INSTRUCTIONS.md).

## lots of :heart: to 

[Python](https://www.python.org), [PyGithub](https://pypi.org/project/PyGithub/), [yagmail](http://pygithub.readthedocs.io),  [Colorama](https://pypi.org/project/colorama/), [The Octocat](https://github.com/octocat) 

<img src="https://octodex.github.com/images/daftpunktocat-guy.gif" alt="Octocat" width="200px"/>
