# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import requests

data = """# Rust Application\n\n
- The application backing the GitHub Action is written in Rust
- [``none-shall-pass-rustic``](https://github.com/thevickypedia/none-shall-pass-rustic), is responsible for hyperlink validation in Markdown files.
- It accepts inputs provided as command-line arguments.
- The application extracts hyperlinks from Markdown content, validates them concurrently using multithreading, and logs the validation results.
- It can differentiate between local Markdown files and Wiki pages within the repository, expanding its validation scope.
"""

response = requests.get("https://raw.githubusercontent.com/thevickypedia/none-shall-pass-rustic/main/README.md")
if response.ok:
    data += f"\n\n#{response.text}"

with open("rustic.md", "w") as file:
    file.write(data)


def setup(app):
    app.add_css_file('theme.css')


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
    'recommonmark'
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
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "body_max_width": "100%"
}

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
