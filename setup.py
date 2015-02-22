# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='supercaptcha-python3',
    version='0.2.1',
    packages=['supercaptcha'],
    package_data={
        '': ['fonts/*.ttf']
    },
    install_requires=[
        'django>=1.7',
        'pillow'
    ],
    author='Akulov Kirill',
    author_email='iceroute@gmail.com',
    description='captchafield for django newforms',
    license='MIT',
    keywords='forms web django python3',
)
