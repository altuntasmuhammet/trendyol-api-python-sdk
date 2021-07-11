import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "trendyol_api_python_sdk",
    version = "0.0.1",
    author = "Muhammed Ali Altuntas",
    author_email = "altuntasmuhammet96@gmail.com",
    description = ("Unofficial Trendyol API Python SDK"),
    license = "MIT",
    url="https://github.com/altuntasmuhammet/trendyol-api-python-sdk",
    packages=[
        'trendyol_sdk'
        ],
    long_description=read('README'),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.0",
)
