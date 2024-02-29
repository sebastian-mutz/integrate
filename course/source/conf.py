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
project = 'INTEGRATE'
year = '2024'
author = 'Sebastian G. Mutz'
copyright = '{0}, {1}'.format(year, author)

# The short X.Y version.
version = '2024'
# The full version, including alpha/beta/rc tags.
release = '1.1'

# The name of the Pygments (syntax highlighting) style to use.
#pygments_style = 'sphinx'
#pygments_style = 'friendly'
pygments_style = 'trac'

templates_path = ['.']

# -- Options for HTML output ----------------------------------------------

html_logo = "img/integrateLogo_256_256.png"
#html_favicon = "img/climStatBannerSmall001"

html_theme = 'sphinx_rtd_theme'
import sphinx_rtd_theme
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# These paths are relative to html_static_path
html_css_files = [
    'css/style.css',
]

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
