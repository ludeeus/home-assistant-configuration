"""
A component which allows you to controll some hassbian-config functions from Home Assistant.
For more details about this component, please refer to the documentation at
https://github.com/ludeeus/hassbian-config_custom_component
"""

import subprocess
import logging
from homeassistant.core import callback

DOMAIN = 'hassbian_config'

INSTALL_SUITES = ('appdaemon', 'cloud9', 'hue', 'samba', 'tradfri')
UPGRADE_SUITES = ('appdaemon', 'cloud9', 'hassbian-script')

ATTR_SUITE = 'suite'
ATTR_BETA = 'beta'
ATTR_DEV = 'dev'

_LOGGER = logging.getLogger(__name__)

def setup(hass, config):

	def install_suite_service(call):
		suite = call.data.get(ATTR_SUITE)
		if suite in INSTALL_SUITES:
			_LOGGER.info('The suite %s is now beeing installed.', suite)
			subprocess.call(['sudo', 'hassbian-config', 'install', suite, '--accept', '--force'])
			hass.components.persistent_notification.create('The suite has been installed.', title='HASSBIAN-CONFIG')
		else:
			_LOGGER.error('The suite %s does not exist, or can not be installed automatically.', suite)
	def upgrade_suite_service(call):
		suite = call.data.get(ATTR_SUITE)
		dev = call.data.get(ATTR_DEV)
		beta = call.data.get(ATTR_BETA)
		if suite in UPGRADE_SUITES:
			if (dev == True) or (dev == "true"):
				_LOGGER.info('The suite %s is now beeing upgraded.', suite)
				subprocess.run(['sudo', 'hassbian-config', 'upgrade', suite, '--accept', '--dev'])
				hass.components.persistent_notification.create('The suite has been upgraded.', title='HASSBIAN-CONFIG')
			elif (beta == True) or (beta == "true"):
				_LOGGER.info('The suite %s is now beeing upgraded.', suite)
				subprocess.run(['sudo', 'hassbian-config', 'upgrade', suite, '--accept', '--beta'])
				hass.components.persistent_notification.create('The suite has been upgraded.', title='HASSBIAN-CONFIG')
			else:
				_LOGGER.info('The suite %s is now beeing upgraded.', suite)
				subprocess.run(['sudo', 'hassbian-config', 'upgrade', suite, '--accept'])
				hass.components.persistent_notification.create('The suite has been upgraded.', title='HASSBIAN-CONFIG')
		else:
			_LOGGER.error('The suite %s does not exist, or can not be upgraded automatically.', suite)

	#Register the services:
	hass.services.register(DOMAIN, 'install_suite', install_suite_service)
	hass.services.register(DOMAIN, 'upgrade_suite', upgrade_suite_service)

	return True
