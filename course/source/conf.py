# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

# -- General configuration ------------------------------------------------

# sphinx extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.extlinks',
    'sphinx.ext.ifconfig',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages'
]

if os.getenv('SPELLCHECK'):
    extensions += 'sphinxcontrib.spelling',
    spelling_show_suggestions = True
    spelling_lang = 'en_US'

# source_suffix = ['.rst', '.md']
source_suffix = '.rst'
# The master toctree document.
master_doc = 'index'
# General information about the project.
project = 'ClimStat'
year = '2019'
author = 'Sebastian G. Mutz'
copyright = '{0}, {1}'.format(year, author)

# The short X.Y version.
version = '2019'
# The full version, including alpha/beta/rc tags.
release = '1.0'

# The name of the Pygments (syntax highlighting) style to use.
#pygments_style = 'sphinx'
#pygments_style = 'friendly'
pygments_style = 'trac'

templates_path = ['.']

# -- Options for HTML output ----------------------------------------------

html_logo = "img/climStatBannerSmall.jpg"
#html_favicon = "img/climStatBannerSmall001"

# The theme to use for HTML and HTML Help pages.
import sphinx_py3doc_enhanced_theme
html_theme = "sphinx_py3doc_enhanced_theme"
html_theme_path = [sphinx_py3doc_enhanced_theme.get_html_theme_path()]

html_theme_options = {
    'codefont': 'monospace,sans-serif',
    'linkcolor': '#0072AA',
    'visitedlinkcolor': '#6363bb',
    'extrastyling': False,
}

html_use_smartypants = True
html_last_updated_fmt = '%b %d, %Y'
html_split_index = False

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
html_sidebars = {
   '**': ['searchbox.html', 
          'globaltoc.html'],
}
html_short_title = '%s-%s' % (project, version)

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False
