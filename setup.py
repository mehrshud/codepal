#!/usr/bin/env python
from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='codepal',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[]
)