from setuptools import find_packages,setup

from typing import List


HYPEN_E_DOT='-e .'
def get_requirements(filename):
    with open(filename, "r") as file:
        requirements = file.readlines()
        # Strip any newline characters
        requirements = [req.strip() for req in requirements]
    return requirements


setup(
name='mlproject',
version='0.0.1',
author='luckson',
author_email='lucksonmu3@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')


)
