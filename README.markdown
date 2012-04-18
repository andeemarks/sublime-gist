# Sublime Gist - A Plugin for generating Gists

Sublime-text was created to allow seamless creating of Gists from the content of your [Sublime Text 2](http://www.sublimetext.com/2) editor window.

Currently only unauthorised Gist creation is supported.  I might get around to the OAuth side of things later so you can create personal Gists.

Note: there seems to be a more fully featured Sublime Text -> Gist plugin [here](https://github.com/condemil/Gist).

To date, this plugin has been tested with the following configurations:

* Sublime Text 2 Beta Build: 2181, Mac OS X Version 10.7.3, Python 2.7.1

##Installation

Go to your Packages subdirectory under Sublime Text 2 data directory:

* Windows: %APPDATA%\Sublime Text 2
* OS X: ~/Library/Application Support/Sublime Text 2
* Linux: ~/.config/sublime-text-2
* Portable Installation: Sublime Text 2/Data

Then clone this repository:

`git clone git://github.com/andeemarks/sublime-gist`

##Configuration

[TODO]

##Usage

[TODO - Probably need to have a key binding or menu option]

Sublime Gist works in two basic modes:

* If you have selected any text when you execute the command, only the selected text will be used for the Gist.  This applies to multiple selections as well.

* If no text is selected, then the entire file currently being editied when you execute the command will be used for the Gist.

In either case, the name of the Gist will be the same as a file currently being edited in Sublime Text.