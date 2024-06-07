# The Tech Craftsman

This is the repository with the source code of my personal blog, called ["The Tech Craftsman"](https://www.techcraftsman.blog).

## Tech stack

This blog is built using [ABlog](https://ablog.readthedocs.io/en/stable/index.html), which is powered by [Sphinx](https://www.sphinx-doc.org/en/master/), a [Python](https://www.python.org/) based tool, used to create documents as web pages.

The comment section is powered by [Giscus](https://giscus.app/)

All technologies used on this blog are free and open source

## Structure

- root - config files and scripts to build and test
- src - folder containing the source code

### Src structure

📦src  
 ┣ 📂en  
 ┃ ┣ 📂blog  
 ┃ ┣ 📂_templates  
 ┃ ┃ ┣ 📜btn-location-pt.html  
 ┃ ┃ ┣ 📜layout.html  
 ┃ ┃ ┗ 📜profile.html  
 ┃ ┣ 📜about.md  
 ┃ ┣ 📜conf.py  
 ┃ ┗ 📜index.md  
 ┣ 📂pt  
 ┃ ┣ 📂blog  
 ┃ ┣ 📂_templates  
 ┃ ┃ ┣ 📜btn-location-en.html  
 ┃ ┃ ┣ 📜layout.html  
 ┃ ┃ ┗ 📜profile.html  
 ┃ ┣ 📜about.md  
 ┃ ┣ 📜conf.py  
 ┃ ┗ 📜index.md  
 ┣ 📂_static  
 ┃ ┣ 📂css  
 ┃ ┃ ┗ 📜custom.css  
 ┃ ┣ 📂images  
 ┃ ┃ ┣ 📜en-us.png  
 ┃ ┃ ┣ 📜favicon.png  
 ┃ ┃ ┣ 📜profile.jpg  
 ┃ ┃ ┗ 📜pt-br.png  
 ┃ ┗ 📂js  
 ┃ ┃ ┗ 📜custom.js  

There's three main folders on the src. These are "en", where the source files for the English version of the blog are found, the "pt", where you can find the files for the portuguese version and, the _static, where the static files used on both versions are.
The static files include, custom css, JavaScript code and images. Each of the blog version source folders, contains a "blog" folder, where the blog posts are stored, organized by year and month of publication, a "_templates" folder with html snippets used accross the blog, "About"and "Index" pages, and the configuration file.

## Configuration

All the configuration is specific for each blog version, and can be found on the "conf.py" file. For more informations, refer to the [ABlog Documentation](https://ablog.readthedocs.io/en/stable/index.html)

## Build

Go to the project root folder and run `./make.bat` to build the blog. The build output can be found on the "build/\<blog version>" folder, created on project root. You can specify which version you want to build by passing the version as a parameter to the command. The versions are `en` and `pt`. If not passed, the command will build both versions.

### Build example

```cmd
./make.bat en
```

## Test

After building you can run the build locally. On the root folder, run the command `./serve.bat <blog version>`. Your default browser will open with the blog version you choose, running under `http://localhost:8000`. If not version is specified, the default version (en) will run.

### Test example

```cmd
./serve.bat pt
```
