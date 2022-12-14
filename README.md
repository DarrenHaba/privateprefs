PrivatePrefs
===============

### Easily Keep API Keys out of GitHub 

[![Pytest - Coverage](https://img.shields.io/badge/Coverage-100%25-31c653)](https://github.com/DarrenHaba/privateprefs/actions)
[![Package CI](https://github.com/DarrenHaba/privateprefs/actions/workflows/ci.yml/badge.svg)](https://github.com/DarrenHaba/privateprefs/actions/workflows/ci.yml)
[![GitHub](https://img.shields.io/badge/license-MIT-31c653)](https://github.com/DarrenHaba/privateprefs#license)
[![PyPI - Version](https://img.shields.io/pypi/v/privateprefs.svg)](https://pypi.org/project/privateprefs)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/privateprefs.svg)](https://pypi.org/project/privateprefs)
[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)

It's often tempting to hard code sensitive data like API Keys, passwords, email addresses, usernames, etc directly into python scripts, but if it's checked into Version Control and pushed to public repository on GitHub, GitLab or Bitbucket, then your sensitive personal data will be compromised.

If sensitive data does end up in a public Repository it can be a real pain to remove, because you have to delete the sensitive data, purge it from the history, have github purge their cache. After the that you will still need to change your password or API Keys 😱.

This could have been prevented by using PrivatePrefs 😎. It's works by requiring you to enter sensitive information into the command line, then retrieve it using python, hopefully eliminating the temptation to hard code it. See here for more info (LINK TO HOW IT WORKS) 

-----

**Table of Contents**

- [Installation](#installation)
- [Quick Start](#quick-start)
- [CLI Demo](#cli-demo)
- [License](#license)

Installation
------------
Use ``pip`` to install
```sh
pip install privateprefs
```


Quick Start
------------
#### Save string
###### *run from command line*
```sh
privateprefs save "my key" "abcd4321"
```
&nbsp;

#### Load string
###### *run in python*
```python
import privateprefs as prefs
prefs.load("my key")
```


CLI Demo
------------
use command line interface insert and manage key-value pairs

#### save first key-value pair
```sh
privateprefs save "my key1" "value 1"
```
&nbsp;

#### load key 
```sh
privateprefs load "my key1"
```
###### *returns* `loaded key='my key1' value='value 1'`
&nbsp;

#### save second key-value pair
```sh
privateprefs save "my key2" "value 2"    
```
&emsp;

#### list all stored key value pars
```sh
privateprefs list    
```

###### *returns*
```
    stored (key  :  value)
    -------------------------------------------------------------
    my key1   :   value 1
    my key2   :   value 2
    -------------------------------------------------------------
```
&emsp;

#### delete a single key-value pair
```sh
privateprefs delete "my key2"
```
&emsp;

#### delete all key-value pairs 
###### <sub> *-- WARNING ALL SAVED DATA WILL BE PERMANENTLY DELETED --* </sub>
```sh
privateprefs delete --all
```
&emsp;


### License
`privateprefs` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
