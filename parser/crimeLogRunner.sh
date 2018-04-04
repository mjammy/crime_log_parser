#!/bin/bash

# call this function to write to stderr
echo_stderr ()
{
    echo "$@" >&2
}

# Check for git folder location
if [ -n $1 ]; then
    SAVE_LOC=$1;
    echo "Save location is '$SAVE_LOC'.";
else
    echo_stderr "ERROR: No save location folder argument given.";
    exit 1;
fi

echo "Running downloader.py...";
pipenv run python downloader.py -d $SAVE_LOC;
