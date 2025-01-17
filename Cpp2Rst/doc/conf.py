# -*- coding: utf-8 -*-
#
# documentation build configuration file

import sys
sys.path.insert(0, "sphinxext/numpydoc")

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.mathjax',
              'sphinx.ext.intersphinx',
              'sphinx.ext.doctest',
              'sphinx.ext.todo',
              'sphinx.ext.viewcode',
              'sphinx.ext.autosummary',
              'numpydoc'
              ]

source_suffix = '.rst'

project = u'APP4TRIQS - An application skeleton'
copyright = u'2017-2018 N. Wentzell, O. Parcollet 2018-2019 The Simons Foundation, authors: N. Wentzell, D. Simons, H. Strand, O. Parcollet'
version = '@APP4TRIQS_VERSION@'

mathjax_path = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5"
templates_path = ['_templates']

html_theme = 'triqs'
html_theme_path = ['themes']
html_show_sphinx = False
html_context = {'header_title': 'app4triqs',
                'header_subtitle': 'An example application using cpp2py',
                'header_links': [['Install', 'install'],
                                 ['Documentation', 'documentation'],
                                 ['Issues', 'issues'],
                                 ['About app4triqs', 'about']]}
html_static_path = ['_static']
html_sidebars = {'index': ['sideb.html', 'searchbox.html']}

htmlhelp_basename = 'APP4TRIQSdoc'

intersphinx_mapping = {'python': ('http://docs.python.org/2.7', None)}
