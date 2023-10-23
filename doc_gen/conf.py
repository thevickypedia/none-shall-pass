# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys

sys.path.insert(0, "../src")

project = 'none-shall-pass'
copyright = '2023, Vignesh Rao'
author = 'Vignesh Rao'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.napoleon',  # certain styles of doc strings
    'sphinx.ext.autodoc',  # generates from doc strings
    'sphinx_rtd_dark_mode'
]

# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#configuration
napoleon_google_docstring = True
napoleon_use_param = False

templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add docstrings from __init__ method
# Reference: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#confval-autoclass_content
autoclass_content = 'both'

# Include private methods/functions
# Reference: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#confval-autodoc_default_options
autodoc_default_options = {"members": True, "undoc-members": True, "private-members": True}

source_suffix = {
    '.rst': 'restructuredtext'
}

# Retain the function/member order
# Reference: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#confval-autodoc_member_order
autodoc_member_order = 'bysource'

# Make left pane scroll
html_css_files = ["static.css"]
