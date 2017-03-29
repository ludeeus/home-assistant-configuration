cd /home/homeassistant/.homeassistant
git add .
echo 'Enter the commit message:'
read commitMessage
git commit -m "$commitMessage"
git push https://github.com/ludeeus/hass-config.git
exit
