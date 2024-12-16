from setuptools import setup, find_packages
from typing import List

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()     
   

__version__ = "0.0.4"
REPO_NAME = "MongoDB-Python-Connector-Package-PYPI"
PKG_NAME= "databaseautomation"
AUTHOR_USER_NAME = "RiH-137"
AUTHOR_EMAIL = "101rishidsr@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A light python package for connecting with database.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },


    # location for package --> package available inside the SRC folder

    package_dir={"": "src"},
    packages=find_packages(where="src"),
    )



