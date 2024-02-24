# -- Build Options ----------------------------------------------------

ablog_doctrees = '../../build/pt/.doctrees'
ablog_website = '../../build/pt/_website'

# -- Blog Options ----------------------------------------------------

blog_baseurl = 'https://artur-rios.com'
blog_feed_fulltext = True
blog_path = 'blog'
blog_post_pattern = 'blog/*/*'
blog_title = 'Tech Craftsman'
blog_feed_subtitle = 'Tecnologia e pensamentos.'

blog_authors = {
    'Artur Rios': ('Artur Rios', None),
}

blog_languages = {
    'pt': ('Portuguese', None),
}

# -- ABlog Sidebars -------------------------------------------------------

html_sidebars = {
    'index': ['profile.html'],
    'about': ['profile.html'],
    'blog': ['ablog/categories.html', 'ablog/tagcloud.html', 'ablog/archives.html'],
    'blog/**': ['ablog/postcard.html', 'ablog/recentposts.html', 'ablog/archives.html'],
}

# -- Options for HTML output ----------------------------------------------

html_css_files = ['css/custom.css']
html_favicon = '../_static/images/favicon.png'
html_file_suffix = None
html_search_language = 'pt'
html_short_title = 'Tech Craftsman'
html_show_sourcelink = False
html_show_sphinx = True
html_show_copyright = True
html_split_index = False
html_static_path = ['../_static']
html_title = 'The Tech Craftsman'
html_use_index = True

html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    'search_bar_text': 'Pequise neste site...',
    'icon_links': [
        {
            'name': 'GitHub',
            'url': 'https://github.com/artur-rios',
            'icon': 'fa-brands fa-github',
        },
        {
            'name': 'LinkedIn',
            'url': 'https://www.linkedin.com/in/artur-rios',
            'icon': 'fa-brands fa-linkedin',
        },
    ],
}

fontawesome_included = True

# Output file base name for HTML help builder.
htmlhelp_basename = 'TechCraftsmenBlogdoc'

# -- Post Options -----------------------------------------------------------

post_auto_excerpt = 1
post_auto_image = 1
post_redirect_refresh = 1

# -- Sphinx Options -----------------------------------------------------------

exclude_patterns = [
    'build',
    '**/.ipynb_checkpoints/*',
    '.github/*',
    '.history',
    'github_submodule/*',
    'LICENSE.md',
    'README.md',
]

extensions = [
    'ablog',
    'myst_parser',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
]

master_doc = 'index'
needs_sphinx = '1.2'
pygments_style = 'sphinx'
source_suffix = '.md'
templates_path = ['_templates']
todo_include_todos = False

# -- Myst Options ----------------------------------------------------
myst_update_mathjax = False

# General information about the project.
author = 'Artur Rios'
language = 'pt'
project = 'Tech Craftsmen Blog'
copyright = '2024, Artur Rios'
release = '1.0.0'
version = '1.0'
