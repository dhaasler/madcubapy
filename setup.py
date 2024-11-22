from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'The MADCUBA python package'
LONG_DESCRIPTION = 'Package with tools and utilities to use MADCUBA products.'

# Setting up
setup(
    name="madcubapy", 
    version=VERSION,
    author="David Haasler Garcia",
    author_email="dhaasler@cab.inta-csic.es",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        "numpy", "matplotlib", "astropy",
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
