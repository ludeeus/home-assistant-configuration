# Welcome 👋!

This is my Home Assistant installation.

## Some statistics about my installation:

Description | value
--|--
Installed version | 2021.8.0b8
Total entity objects | 182
Entities in the [`automation`](https://www.home-assistant.io/components/automation) domain | 1
Entities in the [`binary_sensor`](https://www.home-assistant.io/components/binary_sensor) domain | 24
Entities in the [`camera`](https://www.home-assistant.io/components/camera) domain | 1
Entities in the [`configurator`](https://www.home-assistant.io/components/configurator) domain | 1
Entities in the [`cover`](https://www.home-assistant.io/components/cover) domain | 1
Entities in the [`device_tracker`](https://www.home-assistant.io/components/device_tracker) domain | 2
Entities in the [`input_datetime`](https://www.home-assistant.io/components/input_datetime) domain | 1
Entities in the [`input_text`](https://www.home-assistant.io/components/input_text) domain | 1
Entities in the [`media_player`](https://www.home-assistant.io/components/media_player) domain | 27
Entities in the [`person`](https://www.home-assistant.io/components/person) domain | 1
Entities in the [`select`](https://www.home-assistant.io/components/select) domain | 1
Entities in the [`sensor`](https://www.home-assistant.io/components/sensor) domain | 112
Entities in the [`sun`](https://www.home-assistant.io/components/sun) domain | 1
Entities in the [`switch`](https://www.home-assistant.io/components/switch) domain | 6
Entities in the [`weather`](https://www.home-assistant.io/components/weather) domain | 1
Entities in the [`zone`](https://www.home-assistant.io/components/zone) domain | 1

## Core integrations that I use

Integration | Configuration
--|--
[AdGuard Home](https://home-assistant.io/integrations/adguard) | Config flow (UI configuration)
[Belkin WeMo](https://home-assistant.io/integrations/wemo) | Config flow (UI configuration)
[Cast](https://home-assistant.io/integrations/cast) | Config flow (UI configuration)
[Cloud](https://home-assistant.io/integrations/cloud) | Hidden
[Cloudflare](https://home-assistant.io/integrations/cloudflare) | Config flow (UI configuration)
[Default Config](https://home-assistant.io/integrations/default_config) | Config flow (UI configuration)
[Frontend](https://home-assistant.io/integrations/frontend) | [./packages/integrations/core/frontend.yaml](./packages/integrations/core/frontend.yaml)
[InfluxDB](https://home-assistant.io/integrations/influxdb) | [./packages/integrations/core/influxdb.yaml](./packages/integrations/core/influxdb.yaml)
[LG webOS Smart TV](https://home-assistant.io/integrations/webostv) | [./packages/integrations/core/webostv.yaml](./packages/integrations/core/webostv.yaml)
[Logger](https://home-assistant.io/integrations/logger) | [./packages/integrations/core/logger.yaml](./packages/integrations/core/logger.yaml)
[Met.no](https://home-assistant.io/integrations/met) | Config flow (UI configuration)
[Netatmo](https://home-assistant.io/integrations/netatmo) | Config flow (UI configuration)
[Plex](https://home-assistant.io/integrations/plex) | Config flow (UI configuration)
[Rest](https://home-assistant.io/integrations/rest) | Hidden
[Sentry](https://home-assistant.io/integrations/sentry) | Config flow (UI configuration)
[Spotify](https://home-assistant.io/integrations/spotify) | Hidden
[Synology](https://home-assistant.io/integrations/synology) | Config flow (UI configuration)
[Template](https://home-assistant.io/integrations/template) | [./packages/integrations/core/template.yaml](./packages/integrations/core/template.yaml)
[Uptime Robot](https://home-assistant.io/integrations/uptimerobot) | Hidden
[Version](https://home-assistant.io/integrations/version) | [./packages/integrations/core/version.yaml](./packages/integrations/core/version.yaml)
[Wemo](https://home-assistant.io/integrations/wemo) | Config flow (UI configuration)


## The custom integrations that I use

### [HACS](https://github.com/hacs/integration)

_HACS gives you a powerful UI to handle downloads of all your custom needs._

**Version** | 1.13.2
--|--
**Author(s)** | @ludeeus

### [Netdaemon](https://github.com/net-daemon/integration)

_Helper integration for Home Assistant_

**Version** | 21.28.0
--|--
**Author(s)** | @net-daemon

### [Breaking Changes](https://github.com/custom-components/breaking_changes)

_Component to show potential breaking_changes in the current published version based on your loaded components_


[**My configuration for Breaking Changes**](./packages/integrations/custom/breaking_changes.yaml)
**Version** | 21.4.0
--|--
**Author(s)** | @ludeeus

### [Generate Readme](https://github.com/custom-components/readme)

_Use Jinja and data from Home Assistant to generate your README.md file_

**Version** | 0.3.0
--|--
**Author(s)** | @ludeeus

## The custom lovelace plugins that I use

### [Mini Graph Card](https://github.com/kalkih/mini-graph-card)

_Minimalistic graph card for Home Assistant Lovelace UI_

**Version** | v0.11.0-dev.4
--|--


***

Like all other Home Assistant instances this is also a Work in Progress :D