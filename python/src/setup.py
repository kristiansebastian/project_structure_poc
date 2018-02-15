# coding=utf-8

from distutils.core import setup

from setuptools import find_packages

setup(
    name='tdd_course',
    version='1.0',
    description='TDD Course',
    author='Kristian Sebastian',
    author_email='kristian.sebastian@logitravelgroup.com',
    url='https://github.com/kristiansebastian/tdd_course',
    packages=find_packages(),
    install_requires=[
        'pymongo==3.6.0',
    ]
)
