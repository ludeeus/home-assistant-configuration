import logging

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'battery'
DEPENDENCIES = []

CONF_TEXT = 'entity_id'
DEFAULT_TEXT = 'none'

def setup(hass, config):
    # Get the text from the configuration. Use DEFAULT_TEXT if no name is provided.
    entity_id = config[DOMAIN].get(CONF_TEXT, DEFAULT_TEXT)

    # States are in the format DOMAIN.OBJECT_ID
    hass.states.set('Battery.entity_id', {{states.entity_id.attributes.battery}})

    return True
