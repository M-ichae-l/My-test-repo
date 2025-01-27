# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
import os
import subprocess

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Ameba Arduino SDK download'
copyright = '2024 zzw All rights reserved'
author = 'zzw'
release = 'v1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'recommonmark',
    'sphinx_markdown_tables',
    'sphinx.ext.intersphinx',
    'sphinx_tabs.tabs',
    'sphinx_tags',  # Enable tagging
]


tags_overview_title = "Overview"
tags_page_title = 'Tag: '
tags_page_header = 'overview'
tags_create_tags = True

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_context = {
    "display_github": True,
    "github_user": "M-ichae-l",
    "github_repo": "My-test-repo",
    "github_version": "main",
    "conf_py_path": "/source/",
}

html_logo = '_static/Realtek_logo.png'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]
html_output = '_build/html'

numfig = True
