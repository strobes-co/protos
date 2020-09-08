""" __Doc__ File handle class """
from setuptools import find_packages, setup
from __version__ import __version__


with open("README.md") as file:
    setup(
        name="Strobesbufs",
        license="GPLv3",
        description="Contains all the protos created by strobesbuf as a package to use",
        long_description=file.read(),
        long_description_content_type="text/markdown",
        author="Akhil Reni",
        version=__version__,
        author_email="akhil@wesecureapp.com",
        url="https://github.com/strobes-co/protos",
        packages=find_packages(),
        python_requires='>=3.6',
        include_package_data=True)
