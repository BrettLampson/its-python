# ------------------------------------------------------------------------------------------------ #
# PIPENV
# ------------------------------------------------------------------------------------------------ #

# Package management and virtual environment tool


# ------------------------------------------------------------------------------------------------ #
# CREATE A NEW PROJECT DIRECTORY

# /Brett/its-howto/pipenv/coingolf


# 1. cd into it, then start installing packages.  $pipenv install requests
# 2. creates a new virtual environment
# 3. creates a pipfile
# 4. creates a pipfile.lock (not supposed to touch)
# 5. Tells us:
#       a. run "pipenv shell" to activate this projects virtualenv


# ------------------------------------------------------------------------------------------------ #
# INSIDE THE pipfile
# TOML file type
# We can go in here add packages and run install command and they'll be added.

# [[source]]
# name = "pypi"
# url = "https://pypi.org/simple"
# verify_ssl = true

# [dev-packages]

# [packages]
# requests = "*"

# [requires]
# python_version = "3.7"


# ------------------------------------------------------------------------------------------------ #
# ACTIVATE VIRTUAL ENVIRONMENT
# pipenv shell


# ------------------------------------------------------------------------------------------------ #
# DEACTIVATE VIRTUAL ENVIRONMENT
# exit


# ------------------------------------------------------------------------------------------------ #
# LIST REQUIREMENTS FOR NEW PROJECT
# pipenv lock -r


# ------------------------------------------------------------------------------------------------ #
# INSTALL PACKAGES THAT WE DON'T WANT IN OUR PRODUCTION
# This will install pytest into [dev-packages]
# pipenv install pytest --dev


# ------------------------------------------------------------------------------------------------ #
# UNINSTALL PACKAGES
# uninstalls requests and removes it from pipfile
# pipenv uninstall requests


# ------------------------------------------------------------------------------------------------ #
# EDITING PIPFILE
# if we want to change version of python (lets pretend)
# make change in pipfile, save
# in terminal:
# pipenv --python 3.6


# ------------------------------------------------------------------------------------------------ #
# REMOVING A VIRTUAL ENVIRONMENT
# pipenv --rm


# ------------------------------------------------------------------------------------------------ #
# CREATE A VIRTUAL ENVIRONMENT (and packages) USING AN EXISTING PIPFILE
# pipenv install


# ------------------------------------------------------------------------------------------------ #
# PATH TO VIRTUAL ENVIRONMENT
# pipenv --venv


# ------------------------------------------------------------------------------------------------ #
# PRODUCTION READY, TESTS DONE!
# To update lock file with current dependencies using:
# pipenv lock
# then take your lock file and move it to your production environment
# pipenv install --ignore-pipfile
# this creates an environment using what is in the pipfile.lock and ignore pipfile used by default


# ------------------------------------------------------------------------------------------------ #
# CREATE A .ENV FILE
# Why? You might have several environments that have the same environment variable names.
# for example like a secret key

# within project directory create a .env file
# add environment variables that we want to be accessible in our environment
# SECRET_KEY = "insertmykeyinformation"
# To see this is done, in project folder run:
# pipenv run python
# import os
# os.environment['SECRET_KEY'] // returns insertmykeyinformation


# ------------------------------------------------------------------------------------------------ #
#
# pipenv graph
