import os
import re
from setuptools import setup

def get_version():
    version_file = os.path.join(
        os.path.dirname(__file__), "NumWords", "__init__.py"
    )
    with open(version_file, "r") as f:
        version_match = re.search(
            r"^__version__ = ['\"]([^'"]*)['\"]",
            f.read(),
            re.M
        )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

with open("./README.md") as readme:
    long_description = readme.read() # Changed variable name for clarity

setup(
    name="numwords",
    version=get_version(), # Read version dynamically
    description="Convert numbers to words and words to numbers.", # Added a short description
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Ankur Goswami",
    author_email="ankurgoswami1401@gmail.com",
    url="https://github.com/TheAnkurGoswami/NumWords",
    packages=["numwords"],
    install_requires=["typing"], # 'typing' is in stdlib for Py3.5+; only needed for older Pythons or type checking.
                                # Consider removing if targeting Python 3.8+ primarily, as specified by python_requires.
    python_requires=">=3.8",
    license="MIT License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
