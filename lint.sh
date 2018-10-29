#!/bin/bash

#set -v

# Lizard doesn't properly scan Python files without the extension. So, create a copy
# with the extension, and scan that.
cp cmake-tidy/cmake-tidy cmake-tidy/cmake-tidy.py
find . -name *.py \
    -exec lizard --CCN=10 --length=20 --arguments=6 --warnings_only --modified {} \;
rm cmake-tidy/cmake-tidy.py
