# strslice

Python 3 style emoji-safe string slicing for Python 2. Based on 
[uniseg-python](https://pypi.python.org/pypi/uniseg/) by 
[Masaaki Shibata](http://emptypage.jp/).

# Usage

```
>>> from strslice import strslice
>>> print(u'🏩')[0]
???
>>> print(strslice(u'🏩')[0])
🏩
```
