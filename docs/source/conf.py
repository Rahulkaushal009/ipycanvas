# -*- coding: utf-8 -*-
import sphinx_rtd_theme

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    # 'sphinx.ext.intersphinx',
    # 'sphinx.ext.autosummary',
    # 'sphinx.ext.viewcode',
    # 'jupyter_sphinx.embed_widgets',
]

templates_path = ['_templates']


master_doc = 'index'
source_suffix = '.rst'

# General information about the project.
project = 'ipycanvas'
author = 'Martin Renou'

exclude_patterns = []
highlight_language = 'python'
pygments_style = 'sphinx'

# Output file base name for HTML help builder.
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
htmlhelp_basename = 'ipycanvasdoc'

autodoc_member_order = 'bysource'
