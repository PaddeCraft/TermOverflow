from setuptools import setup
from termoverflow.__init__ import VERSION

setup(
    name="termoverflow",
    version=VERSION,
    description="StackOverflow command-line client.",
    author="PaddeCraft",
    packages=["termoverflow"],
    install_requires=["rich", "typer", "requests", "markdownify"],
)
