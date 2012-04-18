import os.path
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "ukTOCs",
    version = "0.1.0",
    author = "Neil Albrock",
    author_email = "neil@atomised.coop",
    description = ("Self contained UK TOC definitions"),
    license = "MIT",
    keywords = "uk toc train",
    url = "https://github.com/neilalbrock/python-ukTOCs",
    packages=['ukTOCs'],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python"])