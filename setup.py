#!python
# -*- coding:utf-8 -*-
from __future__ import print_function
from setuptools import setup, find_packages
# import Simbiber

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="simbiber",
    version="0.7.0",
    author="Qiguang Chen",
    author_email="charleschen2333@gmail.com",
    description="a tool to fix and simplify bib automatically.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/MLNLP-World/SimBiber",
    include_package_data = True,
    install_requires=[
        "argparse",
        "bibtexparser>=1.2.0",
        "tqdm"
        ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        'Topic :: Text Editors :: Text Processing',
        'Topic :: Text Processing :: Filters',
        "Topic :: Text Processing :: Markup :: LaTeX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    entry_points={
        'console_scripts': ['simbiber = Simbiber.main:main'],
    },
    packages=['Simbiber'],
    package_dir={"Simbiber":"Simbiber"},
    package_data={
        "Simbiber": ["config/*.json","parserConfig.json","data/*.bib","out/*.bib"],
    },
    py_modules=['Simbiber.main', 'Simbiber.SimBiberTool', 'Simbiber.BibTool'],
)
