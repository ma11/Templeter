# Templeter
Manage template files with tags for initializing project

## Installation
To install the program, simply clone the repository and run ```make install```.
By default, the program will be installed in your home directory, fell free to change this setting by changing the variable ```prefix``` in Makefile.

## Usage
The help message can be obtained by typing on command-line:
```Proj -h```

The program reads a template file containg some tags to be replaced. The value of these tags is written in a file called ```tags``` which is a python-style dictionnary. The software is distributed with a default tag file located in ```<instaldir>/templates/tags```. You can use a different tag file on command line by hitting
```Proj -t <othertagfile>```.

To use a template in the current folder, hit ```Proj <templatename> <filename>``` and the program will generate a file named ```<filename>``` using the template ```<templatename>``` where some tags will be replaced.

## Tags
The file containing tag definition is a python-style dictionnary. You can include on a tag definition some command to be exectued for computed value (ie. the date).

## Improving
Feel free to add new templates and more tags. Try to keep the templates general enough so that it will not be a one-shot template.
If the file ```TODOLIST``` exists, then some interesting features could be included.
