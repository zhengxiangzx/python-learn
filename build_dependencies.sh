#!/usr/bin/env bash

# check to see if pipenv is installed
if [ -x "$(which pip3)" ]
then
    # check that there Pipfile exists in root directory
    if [ ! -e requirements.txt ]
    then
        echo 'ERROR - cannot find requirements.txt'
        exit 1
    fi

    # install packages to a temporary directory and zip it
    pip3 install -r requirements.txt --target ./packages

    # check to see if there are any external dependencies
    # if not then create an empty file to see zip with
    if [ -z "$(ls -A packages)" ]
    then
        touch packages/empty.txt
    fi

    # zip dependencies
    if [ ! -d packages ]
    then 
        echo 'ERROR - pip failed to import dependencies'
        exit 1
    fi

    cd packages
    zip -9mrv packages.zip .
    mv packages.zip ..
    cd ..

    # remove temporary directory and requirements.txt
    rm -rf packages
    rm requirements.txt
    
    # add local modules
    echo '... adding all modules from local utils package'
    zip -ru9 packages.zip dependencies -x dependencies/__pycache__/\*

    exit 0
else
    echo 'ERROR - pip3 is not installed .'
    exit 1
fi
