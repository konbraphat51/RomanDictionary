"""Python setup.py for project_name package"""
import io
import os
from setuptools import find_packages, setup

def read_requirements(path):
    with open("requirements.txt") as req:
        content = req.read()
        reqs = content.split("\n")
        
    return reqs


setup(
    name="RomanDictionary",
    version="0.1",
    description="Dictionary which can search by romanized word",
    url="https://github.com/konbraphat51/RomanDictionary",
    author="konbraphat51",
    packages=find_packages(),
    install_requires=read_requirements("requirements.txt"),
)