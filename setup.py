"""
The setup.py file is an essential part of packaging and distributing python
projects. It is used by setuptools(or distutils in older python versions)
to defin ethe configuration of ypur project , such as its metadata, dependencied , and more
"""

from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return list of requirements
    """

    requirement_lst = []
    try:
        with open("requirements.txt","r") as file:
            # Read lines from the file
            lines = file.readlines()
            ## Process each line 
            for line in lines:
                requirement = line.strip()
                ## ignore the empty line and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
    return requirement_lst

                

setup(
    name="NetworkSecurity",
    version="0.1.0",
    author="Nikhil Singh",
    author_email="nitins706888@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
