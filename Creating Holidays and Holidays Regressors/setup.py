# setup.py

from setuptools import setup, find_packages

setup(
    name='purolator',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    description='A package that provides a DataFrame as a global variable',
    author='Mehrdad Dadgar',
    author_email='mehrdad.dadgar@purolator.com',
)