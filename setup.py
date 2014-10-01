# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='supercaptcha',
    version='0.2.0',
    packages=['supercaptcha'],
    package_data={
        '':['fonts/*.ttf']
    },
    install_requires=[
        'django>=1.7',
        'pillow'
    ],
    author='Viktor Kotseruba',
    author_email='barbuzaster@gmail.com',
    description='captchafield for django newforms',
    license='MIT',
    keywords='forms web django',
)
