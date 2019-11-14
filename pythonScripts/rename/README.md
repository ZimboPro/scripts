# Renaming files and/or folders by deleting parts of the name or replace a part of the name

## How it works

The script takes in the flags and searches the current directory and finds names that contain the
specified string and the either deletes or replaces that part of the name.

### Delete option

eg `python3 creator.py -d "es"`
or
`python3 creator.py --delete "es"`

This will delete the first "es" in the name

test > tt
testTest > ttTest

### Replace option

This option works with the delete option

eg `python3 creator.py -d "es" -r "oo"`
or
`python3 creator.py -d "es" --replace "oo"`

test > toot
testTest > tootTest

### Recursive option

By adding `-R` or `--recursive` to any of the other options will allow the script to search all sub-directories

## NOTE

This script requires python3
