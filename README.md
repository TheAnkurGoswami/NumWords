[![PyPI Downloads](https://static.pepy.tech/personalized-badge/numwords?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=PyPI%20Downloads)](https://pepy.tech/project/numwords)

NumWords module converts numbers from their numerical form to their international semantic form.
Current input limit is 10<sup>66</sup>-1.

# Usage:

## Convert integers
```python
from numwords import NumWords
NumWords.convert(12345)
```
```python
>>> "Twelve Thousand Three Hundred Fourty Five"
```

## Convert numbers with decimals

```python
NumWords.convert(12345.6789)
```
```python
>>> "Twelve Thousand Three Hundred Fourty Five Point Six Seven Eight Nine"
```

<br>

```python
NumWords.convert("12345.6789")
```
```python
>>> "Twelve Thousand Three Hundred Fourty Five Point Six Seven Eight Nine"
```

<br>

```python
NumWords.convert(12345.0)
```
```python
>>> "Twelve Thousand Three Hundred Fourty Five"
```