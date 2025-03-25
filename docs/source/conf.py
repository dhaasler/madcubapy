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
copyright = '2025, David Haasler García'
author = 'David Haasler García'
release = '0.5.5'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'numpydoc',
    'matplotlib.sphinxext.plot_directive',
    'sphinx_changelog',
    'sphinx_design',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',  # To link source code
    'sphinx_automodapi.automodapi',
    'sphinx_gallery.gen_gallery',
]

# numpydoc settings
numpydoc_show_class_members = False  # Controls whether class members are shown
numpydoc_class_members_toctree = False  # Prevents adding members to TOC

# Intersphinx external links
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'matplotlib': ('https://matplotlib.org/stable/', None),
    'astropy': ('https://docs.astropy.org/en/stable/', None),
}

default_role = 'py:obj'

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
html_css_files = [
    # 'custom_dark_theme.css',
    'remove_download_note.css',
]
html_logo = "_static/logos/docs-banner.png"
