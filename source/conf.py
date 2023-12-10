import os
import sys
sys.path.insert(0, os.path.abspath('C:\\Users\\kanuy\\Desktop\\ESIEE-IT\\L3\\Projets\\Python\\ESIEE_IT_SEO'))
sys.path.insert(0, 'C:\\Users\\kanuy\\Desktop\\ESIEE-IT\\L3\\Projets\\Python\\ESIEE_IT_SEO\\parasiteFilter.py')

    # Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'audit_seo'
copyright = '2023, smercellus'
author = 'smercellus'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
