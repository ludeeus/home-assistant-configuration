# Hello there! 👋

So this is my Home Assistant instance 🎉

This repository exists mostly for my own amusement, but it may contain some things that others might find useful.

## Statistics from the instance

Value | Description
-- | --
32 | Total state objects
2 | Automations
1 | Binary sensors
2 | Groups
2 | Input booleans
3 | Media players
12 | Sensors
7 | Switches

## Hardware and general setup

For my setup I use an old Lenovo Yoga Pro 2, it has a touch screen so I have mounted it on the wall by the front door so I can easily access some controls in my Lovelace UI.

OS | Ubuntu desktop 18.04
-- | --
SSD | 512GB
RAM | 8GB
Processor | Intel® Core™ i7-4500U Processor
Connectivity | WiFi

For the installation method of Home Assistant I went with [the generic Linux installation of Hassio](https://www.home-assistant.io/hassio/installation/#alternative-install-on-a-generic-linux-host)

This method stores the files used by hassio/Home Assistant in `/usr/share/hassio`.

I have mounted a share from my NAS to the `/usr/share/hassio` dir, that way I can handle backups and replication on my NAS.

For my theme I use [slate](https://github.com/seangreen2/slate_theme) on all my devices for two reasons, it looks good and I can track it in HACS.

To access my instance I'm using my [Nabu Casa ❤️](https://www.nabucasa.com/) link.

## Core integrations that I use

- [AdGuard Home](https://www.home-assistant.io/components/adguard/)
- [Belkin WeMo](https://www.home-assistant.io/components/wemo/)
- [Default Config](https://www.home-assistant.io/components/default_config/)
- [File](https://www.home-assistant.io/components/file/)
- [Input Boolean](https://www.home-assistant.io/components/input_boolean/)
- [Met.no](https://www.home-assistant.io/components/met/)
- [Shell command](https://www.home-assistant.io/components/shell_command/)
- [Spotify](https://www.home-assistant.io/components/spotify/)


## custom_components that I use

A summary of custom_components that I use.

### [HACS (Home Assistant Community Store)](https://custom-components.github.io/hacs)

_Manage (Install, track, upgrade) and discover custom elements for Home Assistant._

I use this to discover new awesome stuff, and to keep the custom elements I use up to date with the latest version of it from the developer.

### [Generate readme](https://github.com/custom-components/readme)

_Generates this awesome readme file._

I use this integration to generate this readme, and to convert my lovelace configuration.


## Custom Lovelace plugins that I use

A summary of custom Lovelace plugins that I use.

### [Compact Custom Header](https://github.com/maykar/compact-custom-header)

_CCH - Customize the header and add enhancements to Lovelace. Features: kiosk mode, conditional header styling, per user/device views, swiping between views on mobile, and more._

I use this to get more screen space by minifying the space used by the header, and to lock my laptop that I have in the hallway by the door to one view.

### [Favicon Counter](https://github.com/custom-cards/favicon-counter)

_Show a notification count badge.._

I use this to show a badge on the Home Assistant tab in my browser when there are active [Persistent notifications](https://www.home-assistant.io/components/persistent_notification/)

### [Mini Graph Card](https://github.com/kalkih/mini-graph-card)

_Minimalistic graph card for Home Assistant Lovelace UI_

I use this to create beautiful statistics cards for my UI.

***

Like all other Home Assistant instances this is also a Work in Progress :D