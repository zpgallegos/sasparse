from setuptools import setup, find_packages

setup_args = {
    "name": "sasparse",
    "description": "parser for SAS code",
    "url": "https://github.com/zpgallegos/sasparse",
    "author": "Zachary P. Gallegos",
    "author_email": "zpgallegos@gmail.com",
    "packages": find_packages(),
    "zip_safe": False
}

setup(**setup_args)
