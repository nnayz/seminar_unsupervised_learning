# SP LaTeX Templates

This repository contains the following LaTeX templates:
* `beamersp` provides a `beamer` theme for presentation slides, as well as some helpful macros
* `postersp` is a template for conference posters
* `sharedsp` contains some common macros and definitions (not intended to be used directly)

When creating new presentations, please follow the same directory structure of `examples/beamer/advanced/`. This allows automatic incorporation of your slides into a different presentation with the `spimport` macro. Please feel free to expand the examples directory with useful stuff.

If you find bugs or would like to suggest improvements, please open an issue or create a merge request.

## Installation
_Note_: If you have downloaded the templates as a packaged `zip` file you do not need to clone the repoistory, just run the installation script.

### Linux / Mac 
The installation script is dumb and assumes you have a working LaTeX installation. You might need to install `biber` (e.g. `sudo apt install biber`) before proceeding.
Clone the repository and run the installation script: 
```
git clone https://git.informatik.uni-hamburg.de/sp/sandbox/latex-templates.git
cd latex-templates
./install.sh
```
This should install all relevant files into a location recognizeable by your LaTeX installation. Test your installation by compiling the provided examples.

###  Windows (experimental)
The following instructions assume you have git (and git-bash) installed, as well as either TeXLive or MiKTex.
In git-bash, run:
```
git clone https://git.informatik.uni-hamburg.de/sp/sandbox/latex-templates.git
cd latex-templates
./install.sh
```
For TeXLive that should suffice. If you are using MiKTeX, you will need to run the following in the windows command prompt (`cmd`, not git-bash):
```
initexmf --register-root=%USERPROFILE%\texmf
initexmf --update-fndb
```
Please check your installation by compiling the examples. Depending on your configuration, MiKTeX will probably install a bunch of dependencies automatically, so it might take a while on the first run.

## Backward Compatibility
Older versions of the `beamersp` template were named `beamersp2017`. The installation script creates a symbolic link to maintain backward compatibility and prevent older presentations from breaking (LaTeX will throw a harmless warning about this).

Note that if you still have old template files (`sty` files and the `theme` directory) in your presentation directory, LaTeX will use them instead of the installed files.

## Known Issues
* `imagesc` doesn't work on windows (probably)

## TODO
* Improve Windows support
* ~~Check if `imagesc` is working~~
* ~~Check and possibly fix `spimport`~~
* ~~Check if install script works on Mac~~
* ~~Installation procedure for windows~~
