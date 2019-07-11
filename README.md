# python-3-migration-training
This repository contains examples for differences between Python 2 und Python 3. These are used for a training organized by Thomas Weber and Frank Reininghaus at work.

# Setting up the working environment
Jupyter is a very convenient tool for experiments in Python (and many other programming languages!).

## Linux
To set up the working environment on Linux in a virtualenv, run the following commands:

    virtualenv -p python3 jupyter
    cd jupyter/
    . bin/activate
    pip3 install jupyter modernize

Instead of telling pip3 the packages to install explicitly on the command line, you can also use the file `requirements.txt` from this repository:

    pip3 install -r requirements.txt

To run a Jupyter server with your home directory as the base directory (assumes that the virtualenv is already activated as above):

    cd ~
    jupyter notebook

A browser window showing your home directory should then open automatically (if not, the console log contains a URL that you can visit with your browser). You can then navigate through your home directory and create new Jupyter notebooks, or view existing notebooks.

Note that you can switch notebook cells to Python 2 mode with the magic command `%%python2`.

## Windows

A virtualenv with Jupyter can be set up also on Windows:

    C:/python37/Scripts/pip.exe install virtualenv
    virtualenv jupyter
    cd jupyter/Scripts
    activate.bat
    pip install jupyter modernize
