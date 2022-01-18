#!/bin/sh

# Creating workspace
mkdir github && cd github
git clone https://github.com/$1.git workspace
cd workspace
git fetch origin
git checkout switchable
git branch

# Getting all css files in project
CSS=$(find . -type f -name "*.css")
echo "CSS:"
echo $CSS
echo
# Getting all css files in project
SCSS=$(find . -type f -name "*.scss")
echo "SCSS:"
echo $SCSS
echo
# Getting all js files in project
JS=$(find . -type f -name "*.js")
echo "JS:"
echo $JS
echo

# Getting all html files in project
HTML=$(find . -type f -name "*.html")
echo "HTML:"
echo $HTML
echo
# Getting all htm files in project
HTM=$(find . -type f -name "*.htm")
echo "HTM:"
echo $HTM
echo

# For counting all files that minified
ITEMS=0

for c in $CSS
do
# Sending path to minifier.py
minifier $c
# Counting this files in items
ITEMS=$(($ITEMS + 1))
done

for s in $SCSS
do
# Sending path to minifier.py
minifier $s
# Counting this files in items
ITEMS=$(($ITEMS + 1))
done

for j in $JS
do
# Sending path to minifier.py
minifier $j
# Counting this files in items
ITEMS=$(($ITEMS + 1))
done

for h in $HTML
do
# Sending path to minifier.py
minifier $h
# Counting this files in items
ITEMS=$(($ITEMS + 1))
done

for hm in $HTM
do
# Sending path to minifier.py
minifier $hm
# Counting this files in items
ITEMS=$(($ITEMS + 1))
done

echo "Minified $ITEMS files"
