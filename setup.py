from setuptools import find_packages, setup

with open("./README.md", "r") as readme:
    description = readme.read()
setup(
    name="numwords",
    version="2.0.0",
    description="",
    long_description=description,
    long_description_content_type="text/markdown",
    author="Ankur Goswami",
    author_email="ankurgoswami1401@gmail.com",
    url="https://github.com/TheAnkurGoswami/NumWords",
    packages=["numwords"],
    install_requires=["typing"],
    python_requires=">=3.8",
    license="MIT License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
