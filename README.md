[![PyPI Downloads](https://static.pepy.tech/personalized-badge/numwords?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=PyPI%20Downloads)](https://pepy.tech/project/numwords) \
[![PyPI version](https://badge.fury.io/py/numwords.svg)](https://badge.fury.io/py/numwords) \
[![CI Pipeline](https://github.com/TheAnkurGoswami/NumWords/actions/workflows/ci.yml/badge.svg)](https://github.com/TheAnkurGoswami/NumWords/actions/workflows/ci.yml)

NumWords module converts numbers from their numerical form to their international semantic form, and vice-versa.
Current input limit for number-to-word conversion is 10<sup>66</sup>-1.

# Usage:

## Convert numbers to words

### Convert integers
```python
from numwords import NumWords
NumWords.convert(12345)
```
```
>>> "Twelve Thousand Three Hundred Forty Five"
```

### Convert numbers with decimals

```python
NumWords.convert(12345.6789)
```
```
>>> "Twelve Thousand Three Hundred Forty Five Point Six Seven Eight Nine"
```

<br>

```python
NumWords.convert("12345.6789")
```
```
>>> "Twelve Thousand Three Hundred Forty Five Point Six Seven Eight Nine"
```

<br>

```python
NumWords.convert(12345.0)
```
```
>>> "Twelve Thousand Three Hundred Forty Five"
```

## Convert words to numbers

NumWords can also convert English number words to integers. This functionality is case-insensitive and handles spacing.

```python
from numwords import NumWords # If not already imported

NumWords.convert("one hundred twenty three")
```
```
>>> 123
```

```python
NumWords.convert("two million five hundred thousand sixty seven")
```
```
>>> 2500067
```

```python
NumWords.convert("minus fifty seven")
```
```
>>> -57
```

```python
NumWords.convert("ONE THOUSAND")
```
```
>>> 1000
```

## Contributing

Contributions are welcome! Please follow these guidelines:

- **Linting**: This project uses [Ruff](https://github.com/astral-sh/ruff) for linting and code style. Please run `make lint` to check your changes before committing.
- **Testing**: Ensure all tests pass by running `make test`. Add new tests for new features or bug fixes.
- **Commit Messages**: This project uses [Conventional Commits](https://www.conventionalcommits.org/) for automated versioning and changelog generation via `python-semantic-release`. Please format your commit messages accordingly (e.g., `feat: add new feature`, `fix: resolve bug`).
- **Workflow**:
    1. Fork the repository.
    2. Create a new branch for your feature or fix.
    3. Make your changes, ensuring linting and tests pass.
    4. Commit your changes following Conventional Commits.
    5. Push your branch and open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.