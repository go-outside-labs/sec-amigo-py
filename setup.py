# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup


setup(
    name="amigo",
    version='0.0.3',
    provides=['amigo'],
    author="Mia Stein",
    setup_requires='setuptools'
    description="Amigo is a tool to manage Google Cloud Platform Security.",
    packages=find_packages(),
    install_requires=[
        "google_api_python_client==1.6.1",
        "tinydb==3.2.2",
        "jsondiff==1.1.1",
        "termcolor==1.1.0",
        "pyyaml==5.4"
    ],
    entry_points = {
        'console_scripts': ['amigo=amigo.amigo:main'],
    },
)
