from setuptools import setup

with open("./README.md", "r") as readme:
    description = readme.read()
setup(
    name="numwords",
    version="1.0",
    description=description,
    author="Ankur Goswami",
    author_email="ankurgoswami1401@gmail.com",
    url="https://github.com/TheAnkurGoswami/NumWords",
    packages=["numwords"],
    install_requires=["math"],
    python_requires=">=3.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)