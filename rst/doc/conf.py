# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'Benjamin D Moore Portfolio'
author = 'Benjamin D Moore'
release = '0.1'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Options for other output formats ----------------------------------------

# e.g., latex_documents = [(master_doc, 'projectname.tex', 'Project Name Documentation', 'Author Name', 'manual')]
