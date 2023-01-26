from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Genie ASGI framework for Python'
LONG_DESCRIPTION = 'An ASGI framework for building async web services in Python'

# Setting up
setup(
    name="genie",
    version=VERSION,
    author="Abhimanyu Aryan (abhi...)",
    author_email="<abhi@xyz.app>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'web framework', 'async toolkit', 'http', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)