# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

project = 'madcubapy'
copyright = '2024, David Haasler García'
author = 'David Haasler García'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_design',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # For Google/NumPy style docstrings
    'sphinx.ext.viewcode',  # To link source code
    'sphinx.ext.githubpages',  # Optional: For GitHub Pages
    'sphinx_gallery.gen_gallery',
]

# Sphinx-gallery
sphinx_gallery_conf = {
    'examples_dirs': [
        '../../examples',
        '../../tutorials',
    ],  # path to your example scripts
    'gallery_dirs': [
        'gallery_examples',
        'gallery_tutorials',
    ],  # path to save generated gallery
    'filename_pattern': '.*',           # Match all files
    'plot_gallery': 'True',             # Enable plot rendering
}

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
# html_css_files = [
#     'custom_dark_theme.css',
# ]
html_logo = "_static/logo.png"
