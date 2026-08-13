# yo-thanks

[![No Maintenance Intended](https://unmaintained.tech/badge.svg)](https://unmaintained.tech/)

**tl;dr** Easily send thank-you emails to the contributors of your projects on GitHub.

> [!NOTE]
> **Deprecated and archived.** This is kept public for the record. It is not maintained, and
> the GitHub and email APIs it leans on have moved on since it was written.

## what?

**YoThanks** scrapes all repositories linked to a certain `GitHub Access Token` and captures the names and (public) emails of all people who contributed to those repos. Then it compares this list of names and emails with the list of contributors from the file `contributors.json` to check if there's any new contributor since the last time the script was run --- and to those new contributors, *if any and if they have a public email*, the application sends an email based on the template from `thanks_template.txt`. Last but not least, the application then adds the new contributors to the files `contributors.json` and `CONTRIBUTORS.md`.

## how-to

Please, check the [INSTRUCTIONS](INSTRUCTIONS.md).

## lots of :heart: to

[Python](https://www.python.org), [PyGithub](https://pypi.org/project/PyGithub/), [yagmail](https://pypi.org/project/yagmail/), [Colorama](https://pypi.org/project/colorama/), [The Octocat](https://github.com/octocat)

<img src="https://octodex.github.com/images/daftpunktocat-guy.gif" alt="Octocat" width="200px"/>

## License

[MIT](LICENSE). Do what you like with it.

---
If it earned its keep, [coffee is appreciated](https://buymeacoffee.com/42piratas). ☕
