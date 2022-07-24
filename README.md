# fetch-deepl
[![pytest](https://github.com/ffreemt/fetch-deepl/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/ffreemt/fetch-deepl/actions)[![python](https://img.shields.io/static/v1?label=python+&message=3.8%2B&color=blue)](https://www.python.org/downloads/)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/fetch_deepl.svg)](https://badge.fury.io/py/fetch_deepl)

Fetch translation text from a deepl-fastapi API.

## Install it

```shell
pip install fetch-deepl

# pip install git+https://github.com/ffreemt/fetch-deepl
# poetry add git+https://github.com/ffreemt/fetch-deepl
# git clone https://github.com/ffreemt/fetch-deepl && cd fetch-deepl
```

## Use it
```python
from fetch_deepl import fetch_deepl

print(fetch_deepl("Tell me and I forget. Teach me and I remember. Involve me and I learn."))
# 告诉我，我就忘了。教导我，我就记住。让我参与，我就学

print(fetch_deepl("书山有路勤为径"))
# There is a path to the mountain of books and diligence is the path

print(fetch_deepl("There is a path to the mountain of books and diligence is the path", from_lang="en", to_lang="de"))
# Es gibt einen Weg zum Berg der Bücher und Fleiß ist der Weg

print(fetch_deepl("书山有路勤为径", from_lang="zh", to_lang="de"))
# Es gibt einen Weg durch die Berge des Lernens und des Fleißes
```

Supported languages can be obtained from deepl's homepage, as of today:
```python
from pprint import pprint
from fetch_deepl import lang_dict
pprint(lang_dict)
```
```shell
{'bg': 'Bulgarian',
 'cs': 'Czech',
 'da': 'Danish',
 'de': 'German',
 'el': 'Greek',
 'en': 'English',
 'es': 'Spanish',
 'et': 'Estonian',
 'fi': 'Finnish',
 'fr': 'French',
 'hu': 'Hungarian',
 'id': 'Indonesian',
 'it': 'Italian',
 'ja': 'Japanese',
 'lt': 'Lithuanian',
 'lv': 'Latvian',
 'pl': 'Polish',
 'pt': 'Portuguese',
 'ro': 'Romanian',
 'ru': 'Russian',
 'sk': 'Slovak',
 'sl': 'Slovenian',
 'sv': 'Swedish',
 'tr': 'Turkish',
 'zh': 'Chinese (simpl.)'}
```