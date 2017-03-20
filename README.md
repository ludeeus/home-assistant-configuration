# Home Assistant
My [Home Assistant](https://home-assistant.io) Config

<img src=https://raw.githubusercontent.com/ludeeus/hass-config/master/Files/hass.PNG></img>

### Devices:
* Raspberry Pi 3B (Hassbian)
* Wemo
* Chrome Cast
* Chrome Cast Audio
* Apple TV 3.gen
* Apple TV 4.gen
* Apple iPad
* Apple iPhone
* 433mhz RF Outlets (Unkown brand)

### Additional software
* Git
* <a href="https://github.com/nfarina/homebridge">Homebridge</a>

### Usefull notes
[Usefull commands](https://github.com/ludeeus/hass-config/wiki/Usefull-commands)
* Stop HA: ```sudo systemctl stop home-assistant@homeassistant.service```
* Start HA: ```sudo systemctl start home-assistant@homeassistant.service```
* Restart HA: ```sudo systemctl restart home-assistant@homeassistant.service```
* Activate Samba: ```sudo /home/pi/hassbian-scripts/install_samba.sh```
* View live logs: ```sudo journalctl -u home-assistant@homeassistant.service -f```
 
 
* New hassbian device:
```
cd /home/homeassistant/.homeassistant
sudo git init
sudo git pull https://github.com/ludeeus/hass-config
sudo systemctl restart home-assistant@homeassistant.service
cd

```

* Push local files to git:
```
cd /home/homeassistant/.homeassistant && sudo ./gitpush.sh

```

* Update form git and restart:
```
cd /home/homeassistant/.homeassistant && sudo git pull https://github.com/ludeeus/hass-config && sudo systemctl restart home-assistant@homeassistant.service && cd

```
