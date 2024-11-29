from setuptools import setup, find_packages

VERSION = '0.0.4' 
DESCRIPTION = 'The MADCUBA python package.'
LONG_DESCRIPTION = 'Package with tools and utilities to work with MADCUBA products in python.'

# Setting up
setup(
    name="madcubapy", 
    version=VERSION,
    author="David Haasler García",
    author_email="dhaasler@cab.inta-csic.es",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url='https://github.com/dhaasler/madcubapy',
    packages=find_packages(),
    install_requires=[
        "astropy>=7.0.0",
        "matplotlib>=3.9.0",
        "numpy>=1.26.0"
    ],
    keywords=[
        'madcuba',
        'radio astronomy',
    ],
    classifiers= [
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
