# -- Build Options ----------------------------------------------------

ablog_doctrees = '../../build/en/.doctrees'
ablog_website = '../../build/en/_website'

# -- Blog Options ----------------------------------------------------

blog_baseurl = 'https://www.techcraftsman.blog'
blog_feed_fulltext = True
blog_path = 'blog'
blog_post_pattern = 'blog/*/*'
blog_title = 'Tech Craftsman'
blog_feed_subtitle = 'Technology and thoughts.'

blog_authors = {
    'Artur Rios': ('Artur Rios', None),
}

blog_languages = {
    'en': ('English', None),
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
html_js_files = ["js/custom.js"]
html_favicon = '../_static/images/favicon.png'
html_file_suffix = None
html_search_language = 'en'
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
    'search_bar_text': 'Search this site...',
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
    "external_links": [
        {"name": "Homepage", "url": "https://www.artur-rios.tech?lang=en"},
    ],
    'navbar_end': ['theme-switcher', 'navbar-icon-links', 'btn-location-pt'],
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
language = 'en'
project = 'Tech Craftsmen Blog'
copyright = '2024, Artur Rios'
release = '1.0.0'
version = '1.0'
