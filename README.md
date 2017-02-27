#Home Assistant
My [Home Assistant](https://home-assistant.io) Config

Home Assistant Version: 0.39.1

[UI](https://i.gyazo.com/3fd1b15dd9ea2ad20495a493ccc8a047.png)

#Devices:
* Raspberry Pi 3B (Hassbian)
* Wemo
* Chrome Cast
* Chrome Cast Audio
* Apple TV 3.gen
* Apple TV 4.gen
* Apple iPad
* Apple iPhone

#Additional software
* Espeak
* Git

#Usefull notes
* Stop HA: ```sudo systemctl stop home-assistant@homeassistant.service```
* Start HA: ```sudo systemctl start home-assistant@homeassistant.service```
* Restart HA: ```sudo systemctl restart home-assistant@homeassistant.service```
* Activate Samba: ```sudo /home/pi/hassbian-scripts/install_samba.sh```


* New hassbian device:
```
cd /home/homeassistant/.homeassistant
sudo git init
sudo git pull https://github.com/ludeeus/hass-config
```
