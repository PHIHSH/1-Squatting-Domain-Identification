#!/bin/bash

echo "check your python and pip version first"
echo "Passed version is Python 3 and pip3"
python3 --version
pip3 --version

echo "Install dependences - tldextract and idna"

sudo pip3 install tldextract

sudo pip3 install idna

echo "Make the urlCrazy executable"
chmod +x ./squatting/urlcrazy-0.5/urlcrazy


echo "Done!"