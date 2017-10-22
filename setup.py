import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "morselate",
    version = "0.0.1",
    author = "Felipe Ferreira",
    author_email = "felipe.gomes.ferreira@gmail.com",
    description = ("Yet another morse encoder/decoder"),
    license = "BSD",
    keywords = "morsecode morse ",
    url = "https://github.com/SamambaMan/morselate",
    packages=['morselate'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)