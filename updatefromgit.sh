cd /home/homeassistant/.homeassistant
git pull https://github.com/ludeeus/hass-config
ssh pi@localhost sudo systemctl restart home-assistant@homeassistant.service
