hasscall = hass.services.call
def test_function( string):
	hasscall('persistent_notification', 'create', { 'title': 'test', 'message': string })
test_function('pass to function')	