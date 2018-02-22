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
    # Package dir and where parameter must be set to properly install the package
    package_dir={'': 'src'},
    packages=find_packages(where='src', exclude='tests'),
    install_requires=[],
    tests_require=[
        'nose',
        'tox'
    ],
    test_suite='nose.collector'
)
