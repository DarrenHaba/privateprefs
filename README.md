# PrivatePrefs

### PrivatePrefs - Easily keep sensitive data like API Keys, passwords, email addresses, usernames, etc. out of version control frameworks like GitHub 

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
must run from command line
```sm
privateprefs save "My Key" "My Value"
```

#### Load value
```python
import privateprefs as prefs
prefs.load("My Key")
```

### License
`privateprefs` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.


