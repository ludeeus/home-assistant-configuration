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

CONF_INSTALLATION = 'installation'
CONF_BRANCH = 'branch'
ATTR_INSTALL = 'install'
ATTR_BRANCH = 'branch'

SCAN_INTERVAL = timedelta(seconds=300)

ICON = 'mdi:package-up'
PLATFORM_NAME = 'versions'
PLATFORM_VERSION = '0.0.3'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_INSTALLATION, default='venv'): cv.string,
    vol.Optional(CONF_BRANCH, default='stable'): cv.string,
})

_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_devices, discovery_info=None):
    installation = config.get(CONF_INSTALLATION)
    branch = config.get(CONF_BRANCH)
    add_devices([HomeAssistantVersion(installation, branch)])

class HomeAssistantVersion(Entity):
    def __init__(self, installation, branch):
        self._installation = installation
        self._branch = branch
        self._state = None
        self.update()

    def update(self):
        if self._installation == 'venv':
            if self._branch == 'beta' or self._branch == 'rc':
                base_url = 'https://pypi.org/pypi/homeassistant/json'
                get_version = requests.get(base_url, timeout=5).json()['releases']
                all_versions = []
                for versions in sorted(get_version, reverse=True):
                    all_versions.append(versions)
                num = 0
                controll = 0
                while controll < 1:
                    name = all_versions[num]
                    if '.8.' in name or '.9.' in name:
                        num = num +1
                    else:
                        controll = 1
                        version = name
            elif self._branch == 'stable':
                base_url = 'https://pypi.org/pypi/homeassistant/json'
                version = requests.get(base_url, timeout=5).json()['info']['version']
            else:
                _LOGGER.error('The defined installation is not valid: %s', self._installation)
        elif self._installation == 'hassbian':
            base_url = 'https://pypi.org/pypi/homeassistant/json'
            version = requests.get(base_url, timeout=5).json()['info']['version']
        elif self._installation == 'docker':
            base_url = 'https://registry.hub.docker.com/v1/repositories/homeassistant/home-assistant/tags'
            get_version = requests.get(base_url, timeout=5).json()
            num = -1
            controll = 0
            while controll < 1:
                name = get_version[num]['name']
                if self._branch == 'beta' or self._branch == 'rc':
                    if 'd' in name or 'r' in name:
                        num = num -1
                    else:
                        controll = 1
                        version = name
                elif self._branch == 'stable':
                    if 'b' in name or 'd' in name or 'r' in name:
                        num = num -1
                    else:
                        controll = 1
                        version = name
                else:
                    _LOGGER.error('The defined branch is not valid: %s', self._branch)
        elif self._installation == 'hassio':
            if self._branch == 'beta' or self._branch == 'rc':
                base_url = 'https://s3.amazonaws.com/hassio-version/beta.json'
            elif self._branch == 'stable':
                base_url = 'https://s3.amazonaws.com/hassio-version/stable.json'
            else:
                _LOGGER.error('The defined branch is not valid: %s', self._branch)
            version = requests.get(base_url, timeout=5).json()['homeassistant']['default']
        else:
            _LOGGER.error('The defined installation is not valid: %s', self._installation)
        self._state = version
    @property
    def name(self):
        return 'HA version ' + self._installation + ' ' + self._branch
    @property
    def state(self):
        return self._state
    @property
    def icon(self):
        return ICON
    @property
    def device_state_attributes(self):
        return {
            ATTR_INSTALL: self._installation,
            ATTR_BRANCH: self._branch,
        }
