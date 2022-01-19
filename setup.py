from setuptools import find_packages
from setuptools import setup

VERSION = '0.0.3'

setup(
    name='fetch_import',
    version=VERSION,
    author="zmaplex",
    author_email="zmaplex@gmail.com",
    description="Import Python packages from remote.",
    url="https://github.com/zmaplex/fetch_import",
    packages=find_packages(),
    zip_safe=False,
)