"""Main setup script."""

from setuptools import setup, find_packages

NAME = "bcubed"
VERSION = "1.5"
DESCRIPTION = "Simple extended BCubed implementation in Python for clustering evaluation"
AUTHOR = "Hugo Hromic"
AUTHOR_EMAIL = "hhromic@gmail.com"
URL = "https://github.com/hhromic/python-bcubed"
DOWNLOAD_URL = URL + "/tarball/" + VERSION

def _read_file(filename):
    with open(filename) as reader:
        return reader.read()

setup(
    name=NAME, version=VERSION, description=DESCRIPTION,
    author=AUTHOR, author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR, maintainer_email=AUTHOR_EMAIL,
    url=URL, download_url=DOWNLOAD_URL,
    requires=["numpy"],
    install_requires=["numpy"],
    provides=["bcubed"],
    keywords=["bcubed", "clustering", "evaluation"],
    classifiers=[
        "Environment :: Console",
        "Topic :: System :: Clustering",
        "Intended Audience :: Science/Research"
    ],
    license="Apache-2.0",
    platforms=["all"],
    long_description=_read_file("README.md"),
    long_description_content_type="text/markdown",
    packages=find_packages()
)
