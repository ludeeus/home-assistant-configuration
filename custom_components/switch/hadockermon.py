'''
A component which allows you to interact with ha-dockermon.
https://github.com/philhawthorne/ha-dockermon

For more details about this component, please refer to the documentation at
https://github.com/HalfDecent/HA-Custom_components/hadockermon
'''
import requests
import logging
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from time import sleep
from datetime import timedelta
from homeassistant.core import ServiceCall
from homeassistant.components.switch import (SwitchDevice, 
    PLATFORM_SCHEMA, ENTITY_ID_FORMAT)

CONF_HOST = 'host'
CONF_PORT = 'port'
CONF_STATS = 'stats'
CONF_EXCLUDE = 'exclude'
CONF_INCLUDE = 'include'

ATTR_STATUS = 'status'
ATTR_IMAGE = 'image'
ATTR_MEMORY = 'memory'
ATTR_RX_TOTAL = 'network_rx_total'
ATTR_TX_TOTAL = 'network_tx_total'
ATTR_COMPONENT = 'component'

SCAN_INTERVAL = timedelta(seconds=30)

ICON = 'mdi:docker'
TIMEOUT = 5

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_HOST): cv.string,
    vol.Optional(CONF_PORT, default='8126'): cv.string,
    vol.Optional(CONF_STATS, default='False'): cv.string,
    vol.Optional(CONF_EXCLUDE, default=None): 
        vol.All(cv.ensure_list, [cv.string]),
    vol.Optional(CONF_INCLUDE, default=None): 
        vol.All(cv.ensure_list, [cv.string]),
})

def setup_platform(hass, config, add_devices_callback, discovery_info=None):
    baseurl = 'http://' + config.get(CONF_HOST) + ':' + config.get(CONF_PORT)
    dev = []
    include = config.get(CONF_INCLUDE)
    if include != None:
        for container in include:
            dev.append(ContainerSwitch(container, 
                False, config.get(CONF_STATS), baseurl))
    else:
        fetchcontainers = baseurl + '/containers'
        containers = requests.get(fetchcontainers).json()
        exclude = config.get(CONF_EXCLUDE)
        dev = []
        num = 0
        for items in containers:
            containername = containers[num]['Names'][0]
            container = str(containername[1:])
            num = num + 1
            if containername not in exclude:
                dev.append(ContainerSwitch(container, 
                    False, config.get(CONF_STATS), baseurl))
    add_devices_callback(dev, True)

class ContainerSwitch(SwitchDevice):
    def __init__(self, name, state, stats, baseurl):
        self._name = name
        self._state = state
        self._stats = stats
        self._status = None
        self._image = None
        self._component = 'hadockermon'
        self._memory_usage = None
        self._network_rx_total = None
        self._network_tx_total = None
        self._baseurl = baseurl

    def update(self):
        fetchurl = self._baseurl + '/container/' + self._name
        try:
            containerstate = requests.get(fetchurl, timeout=TIMEOUT).json()
        except Exception:
            serverstatus = 'not ok'
        else:
            serverstatus = 'ok'
            _LOGGER.debug("Fetching state for %s...", self._name)
        if serverstatus != 'ok':
            _LOGGER.debug("Error fetching state for %s...", self._name)
        else:
            state = containerstate['state']
            self._status = containerstate['status']
            self._image = containerstate['image']
            if state == 'running':
                if self._stats == 'True':
                    endpoint = '/stats'
                    statsurl = self._baseurl + '/container/' + self._name + endpoint
                    try:
                        containerstats = requests.get(statsurl, timeout=TIMEOUT).json()
                    except Exception:
                        _LOGGER.debug("Error fetching stats for %s...", self._name)
                    else:
                        _LOGGER.debug("Fetching stats form endpoint for %s...", self._name)
                        container_memory_usage = containerstats['memory_stats']['usage']/1024/1024
                        try:
                            container_network = containerstats['networks']
                        except Exception:
                            self._network_rx_total = None
                            self._network_tx_total = None
                        else:
                            container_network_rx_total = containerstats['networks']['eth0']['rx_bytes']/1024/1024
                            container_network_tx_total = containerstats['networks']['eth0']['tx_bytes']/1024/1024
                            self._network_rx_total = str(round(container_network_rx_total, 2)) + ' MB'
                            self._network_tx_total = str(round(container_network_tx_total, 2)) + ' MB'
                        self._memory_usage = str(round(container_memory_usage, 2)) + ' MB'
                self._state = True
            else:
                self._state = False

    @property
    def should_poll(self):
        return True

    @property
    def name(self):
        return self._name

    @property
    def icon(self):
        return ICON

    @property
    def device_state_attributes(self):
        if self._stats == 'True':
            return {
                ATTR_STATUS: self._status,
                ATTR_IMAGE: self._image,
                ATTR_COMPONENT: self._component,
                ATTR_MEMORY: self._memory_usage,
                ATTR_RX_TOTAL: self._network_rx_total,
                ATTR_TX_TOTAL: self._network_tx_total,
            }
        else:
            return {
                ATTR_STATUS: self._status,
                ATTR_IMAGE: self._image,
                ATTR_COMPONENT: self._component,
            }
            
    @property
    def is_on(self):
        return self._state

    def turn_on(self, **kwargs):
        if self._name.startswith("addon_"):
            addon = self._name.replace("addon_", "")
            self.hass.bus.async_fire(event_type='call_service', 
                event_data={'domain': 'hassio','service': 'addon_start',
                    'service_data': {'addon': addon}})
        else:
            endpoint = '/start'
            runcommand = self._baseurl + '/container/' + self._name + endpoint
            commandresponse = requests.get(runcommand)
        self._state = True
        sleep(5)
        self.schedule_update_ha_state()

    def turn_off(self, **kwargs):
        if self._name.startswith("addon_"):
            addon = self._name.replace("addon_", "")
            self.hass.bus.async_fire(event_type='call_service', 
                event_data={'domain': 'hassio','service': 'addon_stop',
                    'service_data': {'addon': addon}})
        else:
            endpoint = '/stop'
            runcommand = self._baseurl + '/container/' + self._name + endpoint
            commandresponse = requests.get(runcommand,)
        self._state = False
        sleep(5)
        self.schedule_update_ha_state()