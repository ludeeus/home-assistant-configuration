#!/bin/bash

cd /home/homeassistant/.homeassistant
source /srv/homeassistant/bin/activate
hass --script check_config

git add .
git status
echo 'Enter the commit message:'
read commitMessage

git commit -m "$commitMessage"
git push -f origin master

exit
