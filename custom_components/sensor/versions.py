"""
A platform which allows you to get information about new versions.
For more details about this component, please refer to the documentation at
https://gitlab.com/custom_components/versions
"""
import logging
import requests
import voluptuous as vol
from datetime import timedelta
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import (PLATFORM_SCHEMA)

CONF_FLAVOR = 'flavor'

SCAN_INTERVAL = timedelta(seconds=300)

ICON = 'mdi:package-up'
PLATFORM_NAME = 'versions'
PLATFORM_VERSION = '0.0.1'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_FLAVOR, default='venv'): cv.string,
})

_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_devices, discovery_info=None):
    flavor = config.get(CONF_FLAVOR)
    add_devices([HomeAssistantVersion(flavor)])

class HomeAssistantVersion(Entity):
    def __init__(self, flavor):
        self._flavor = flavor
        self._state = None
        self.update()

    def update(self):
        if self._flavor == 'venv':
            base_url = 'https://pypi.org/pypi/homeassistant/json'
            version =  requests.get(base_url, timeout=5).json()['info']['version']
        elif self._flavor == 'hassbian':
            base_url = 'https://pypi.org/pypi/homeassistant/json'
            version =  requests.get(base_url, timeout=5).json()['info']['version']
        elif self._flavor == 'docker':
            base_url = 'https://registry.hub.docker.com/v1/repositories/homeassistant/home-assistant/tags'
            get_version = requests.get(base_url, timeout=5).json()
            num = -1
            controll = 0
            while controll < 1:
                name = get_version[num]['name']
                if 'b' in name or 'd' in name or 'r' in name:
                    num = num -1
                else:
                    controll = 1
                    version = name
        elif self._flavor == 'hassio':
            base_url = 'https://s3.amazonaws.com/hassio-version/stable.json'
            version =  requests.get(base_url, timeout=5).json()['homeassistant']['default']
        else:
            _LOGGER.error('The defined flavor is not valid: %s', self._flavor)
        self._state = version
    @property
    def name(self):
        return 'Home Assistant version'
    @property
    def state(self):
        return self._state
    @property
    def icon(self):
        return ICON