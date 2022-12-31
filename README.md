# PrivatePrefs

### Easily Keep API Keys out of GitHub 

It's often tempting to hard code sensitive data like API Keys, passwords, email addresses, usernames, etc directly into python scripts, but if it's checked into Version Control and pushed to public repository on GitHub, GitLab or Bitbucket, then your sensitive personal data will be compromised.

If sensitive data does end up in a public Repository it can be a real pain to remove, because you have to delete the sensitive data, purge it from the history, have github purge their cache. After the that you will still need to change your password or API Keys 😱.

This could have been prevented by using PrivatePrefs 😎. It's works by requiring you to enter sensitive information into the command line, then retrieve it using python, hopefully eliminating the temptation to hard code it. See here for more info (LINK TO HOW IT WORKS) 





[![Pytest - Coverage](https://img.shields.io/badge/Coverage-100%25-31c653)](https://github.com/DarrenHaba/privateprefs/actions)
[![Package CI](https://github.com/DarrenHaba/privateprefs/actions/workflows/ci.yml/badge.svg)](https://github.com/DarrenHaba/privateprefs/actions/workflows/ci.yml)

[![PyPI - Version](https://img.shields.io/pypi/v/privateprefs.svg)](https://pypi.org/project/privateprefs)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/privateprefs.svg)](https://pypi.org/project/privateprefs)

-----


Coming Soon - to a pip install near you!

In late stages of alpha testing, currently setting up CI pipeline, writing docs, completing CLI integration, etc.



**Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

Installation
------------
Use ``pip`` to install these utilities::

    pip install privateprefs

Usage
------------
#### Save value
```sh
# run from command line
privateprefs save "My Key" "My Value"
```

#### Load value
```python
import privateprefs as prefs
prefs.load("My Key")
```

### License
`privateprefs` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.


