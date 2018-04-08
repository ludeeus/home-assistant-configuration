"""
A component which allows you to controll some hassbian-config functions from Home Assistant.
For more details about this component, please refer to the documentation at
https://github.com/ludeeus/hassbian-config_custom_component
"""

import subprocess
import logging
from pathlib import Path
from homeassistant.core import callback

DOMAIN = 'hassbian_config'

INSTALL_SUITES = ('appdaemon', 'cloud9', 'hue', 'mosquitto', 'samba', 'tradfri')
UPGRADE_SUITES = ('appdaemon', 'cloud9', 'hassbian-script', 'homeassistant')

ATTR_SUITE = 'suite'
ATTR_BETA = 'beta'
ATTR_DEV = 'dev'
ATTR_VERSION = 'version'
HASSBIAN_CONFIG_DIR = Path("/usr/local/bin/hassbian-config")

_LOGGER = logging.getLogger(__name__)

def setup(hass, config):
	def install_suite_service(call):
		suite = call.data.get(ATTR_SUITE)
		if suite in INSTALL_SUITES:
			_LOGGER.info('The suite %s is now beeing installed.', suite)
			subprocess.call(['sudo', 'hassbian-config', 'install', suite, '--accept'])
			hass.components.persistent_notification.create('The suite **'+suite+'** has been installed.', 'HASSBIAN-CONFIG')
		else:
			_LOGGER.error('The suite %s does not exist, or can not be installed automatically.', suite)
	def upgrade_suite_service(call):
		suite = call.data.get(ATTR_SUITE)
		dev = call.data.get(ATTR_DEV)
		beta = call.data.get(ATTR_BETA)
		version = call.data.get(ATTR_VERSION)
		if suite in UPGRADE_SUITES:
			_LOGGER.info('The suite %s is now beeing upgraded.', suite)
			if (dev == True) or (dev == "true"):
				subprocess.run(['sudo', 'hassbian-config', 'upgrade', suite, '--accept', '--dev'])
			elif (beta == True) or (beta == "true"):
				subprocess.run(['sudo', 'hassbian-config', 'upgrade', suite, '--accept', '--beta'])
			else:
				if (version == None):
					subprocess.run(['sudo', 'hassbian-config', 'upgrade', suite, '--accept'])
				else:
					subprocess.run(['sudo', 'hassbian-config', 'upgrade', suite+'='+str(version), '--accept'])
			hass.components.persistent_notification.create('The suite **'+suite+'** has been upgraded.', 'HASSBIAN-CONFIG')
		else:
			_LOGGER.error('The suite %s does not exist, or can not be upgraded automatically.', suite)

	if HASSBIAN_CONFIG_DIR.is_file():
		_LOGGER.info('hassbian-config found, registering services.')
		hass.services.register(DOMAIN, 'install_suite', install_suite_service)
		hass.services.register(DOMAIN, 'upgrade_suite', upgrade_suite_service)
	else:
		_LOGGER.error('hassbian-config not found, services will not be registered...')
	return True
