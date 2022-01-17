from setuptools import setup
from setuptools import find_packages

VERSION = '0.0.1'

setup(
    name='fetch_import',  # package name
    version=VERSION,  # package version
    description='fetch_import',  # package description
    packages=find_packages(),
    zip_safe=False,
)