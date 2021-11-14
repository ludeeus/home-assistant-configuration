# Welcome 👋!

This is my Home Assistant installation.

## Some statistics about my installation:

Description | value
--|--
Installed version | 2021.12.0.dev20211114
Total entity objects | 2395
Entities in the [`automation`](https://www.home-assistant.io/components/automation) domain | 6
Entities in the [`binary_sensor`](https://www.home-assistant.io/components/binary_sensor) domain | 22
Entities in the [`device_tracker`](https://www.home-assistant.io/components/device_tracker) domain | 3
Entities in the [`input_datetime`](https://www.home-assistant.io/components/input_datetime) domain | 1
Entities in the [`input_text`](https://www.home-assistant.io/components/input_text) domain | 1
Entities in the [`light`](https://www.home-assistant.io/components/light) domain | 4
Entities in the [`media_player`](https://www.home-assistant.io/components/media_player) domain | 19
Entities in the [`person`](https://www.home-assistant.io/components/person) domain | 1
Entities in the [`script`](https://www.home-assistant.io/components/script) domain | 3
Entities in the [`sensor`](https://www.home-assistant.io/components/sensor) domain | 2326
Entities in the [`sun`](https://www.home-assistant.io/components/sun) domain | 1
Entities in the [`switch`](https://www.home-assistant.io/components/switch) domain | 6
Entities in the [`weather`](https://www.home-assistant.io/components/weather) domain | 1
Entities in the [`zone`](https://www.home-assistant.io/components/zone) domain | 1

## Core integrations that I use

Integration | Configuration
--|--
[<img src="https://brands.home-assistant.io/_/adguard/icon.png" height="24"/>](https://brands.home-assistant.io/_/adguard/icon.png) [AdGuard Home](https://home-assistant.io/integrations/adguard) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/automation/icon.png" height="24"/>](https://brands.home-assistant.io/_/automation/icon.png) [Automations](https://home-assistant.io/integrations/automation) | [./automations.yaml](./automations.yaml)
[<img src="https://brands.home-assistant.io/_/wemo/icon.png" height="24"/>](https://brands.home-assistant.io/_/wemo/icon.png) [Belkin WeMo](https://home-assistant.io/integrations/wemo) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/cast/icon.png" height="24"/>](https://brands.home-assistant.io/_/cast/icon.png) [Cast](https://home-assistant.io/integrations/cast) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/cloud/icon.png" height="24"/>](https://brands.home-assistant.io/_/cloud/icon.png) [Cloud](https://home-assistant.io/integrations/cloud) | [./packages/integrations/core/cloud.yaml](./packages/integrations/core/cloud.yaml)
[<img src="https://brands.home-assistant.io/_/cloudflare/icon.png" height="24"/>](https://brands.home-assistant.io/_/cloudflare/icon.png) [Cloudflare](https://home-assistant.io/integrations/cloudflare) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/default_config/icon.png" height="24"/>](https://brands.home-assistant.io/_/default_config/icon.png) [Default Config](https://home-assistant.io/integrations/default_config) | [./configuration.yaml](./configuration.yaml)
[<img src="https://brands.home-assistant.io/_/frontend/icon.png" height="24"/>](https://brands.home-assistant.io/_/frontend/icon.png) [Frontend](https://home-assistant.io/integrations/frontend) | [./packages/integrations/core/frontend.yaml](./packages/integrations/core/frontend.yaml)
[<img src="https://brands.home-assistant.io/_/github/icon.png" height="24"/>](https://brands.home-assistant.io/_/github/icon.png) [GitHub](https://home-assistant.io/integrations/github) | [./packages/integrations/core/github.yaml](./packages/integrations/core/github.yaml)
[<img src="https://brands.home-assistant.io/_/influxdb/icon.png" height="24"/>](https://brands.home-assistant.io/_/influxdb/icon.png) [InfluxDB](https://home-assistant.io/integrations/influxdb) | [./packages/integrations/core/influxdb.yaml](./packages/integrations/core/influxdb.yaml)
[<img src="https://brands.home-assistant.io/_/launch_library/icon.png" height="24"/>](https://brands.home-assistant.io/_/launch_library/icon.png) [Launch Library](https://home-assistant.io/integrations/launch_library) | [./packages/integrations/core/launch_library.yaml](./packages/integrations/core/launch_library.yaml)
[<img src="https://brands.home-assistant.io/_/logger/icon.png" height="24"/>](https://brands.home-assistant.io/_/logger/icon.png) [Logger](https://home-assistant.io/integrations/logger) | [./packages/integrations/core/logger.yaml](./packages/integrations/core/logger.yaml)
[<img src="https://brands.home-assistant.io/_/met/icon.png" height="24"/>](https://brands.home-assistant.io/_/met/icon.png) [Met.no](https://home-assistant.io/integrations/met) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/mobile_app/icon.png" height="24"/>](https://brands.home-assistant.io/_/mobile_app/icon.png) [Mobile App](https://home-assistant.io/integrations/mobile_app) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/netatmo/icon.png" height="24"/>](https://brands.home-assistant.io/_/netatmo/icon.png) [Netatmo](https://home-assistant.io/integrations/netatmo) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/plex/icon.png" height="24"/>](https://brands.home-assistant.io/_/plex/icon.png) [Plex](https://home-assistant.io/integrations/plex) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/rest_command/icon.png" height="24"/>](https://brands.home-assistant.io/_/rest_command/icon.png) [RESTful Command](https://home-assistant.io/integrations/rest_command) | [./packages/integrations/core/rest_command.yaml](./packages/integrations/core/rest_command.yaml)
[<img src="https://brands.home-assistant.io/_/rest/icon.png" height="24"/>](https://brands.home-assistant.io/_/rest/icon.png) [Rest](https://home-assistant.io/integrations/rest) | [./packages/integrations/core/rest.yaml](./packages/integrations/core/rest.yaml)
[<img src="https://brands.home-assistant.io/_/script/icon.png" height="24"/>](https://brands.home-assistant.io/_/script/icon.png) [Script](https://home-assistant.io/integrations/script) | [./scripts.yaml](./scripts.yaml)
[<img src="https://brands.home-assistant.io/_/sentry/icon.png" height="24"/>](https://brands.home-assistant.io/_/sentry/icon.png) [Sentry](https://home-assistant.io/integrations/sentry) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/spotify/icon.png" height="24"/>](https://brands.home-assistant.io/_/spotify/icon.png) [Spotify](https://home-assistant.io/integrations/spotify) | [./packages/integrations/core/spotify.yaml](./packages/integrations/core/spotify.yaml)
[<img src="https://brands.home-assistant.io/_/hassio/icon.png" height="24"/>](https://brands.home-assistant.io/_/hassio/icon.png) [Supervisor](https://home-assistant.io/integrations/hassio) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/synology_dsm/icon.png" height="24"/>](https://brands.home-assistant.io/_/synology_dsm/icon.png) [Synology](https://home-assistant.io/integrations/synology_dsm) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/tautulli/icon.png" height="24"/>](https://brands.home-assistant.io/_/tautulli/icon.png) [Tautulli](https://home-assistant.io/integrations/tautulli) | [./packages/integrations/core/tautulli.yaml](./packages/integrations/core/tautulli.yaml)
[<img src="https://brands.home-assistant.io/_/telegram/icon.png" height="24"/>](https://brands.home-assistant.io/_/telegram/icon.png) [Telegram BOT](https://home-assistant.io/integrations/telegram) | [./packages/integrations/core/telegram.yaml](./packages/integrations/core/telegram.yaml)
[<img src="https://brands.home-assistant.io/_/template/icon.png" height="24"/>](https://brands.home-assistant.io/_/template/icon.png) [Template](https://home-assistant.io/integrations/template) | [./packages/integrations/core/template.yaml](./packages/integrations/core/template.yaml)
[<img src="https://brands.home-assistant.io/_/tuya/icon.png" height="24"/>](https://brands.home-assistant.io/_/tuya/icon.png) [Tuya](https://home-assistant.io/integrations/tuya) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/uptimerobot/icon.png" height="24"/>](https://brands.home-assistant.io/_/uptimerobot/icon.png) [Uptime Robot](https://home-assistant.io/integrations/uptimerobot) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/version/icon.png" height="24"/>](https://brands.home-assistant.io/_/version/icon.png) [Version](https://home-assistant.io/integrations/version) | [./packages/integrations/core/version.yaml](./packages/integrations/core/version.yaml)



## The custom integrations that I use

### [<img src="https://brands.home-assistant.io/_/hacs/icon.png" height="24"/>](https://brands.home-assistant.io/_/hacs/icon.png) [HACS](https://github.com/hacs/integration)

_HACS gives you a powerful UI to handle downloads of all your custom needs._

**Version** | 1.17.1
--|--
**Author(s)** | @ludeeus

### [<img src="https://brands.home-assistant.io/_/breaking_changes/icon.png" height="24"/>](https://brands.home-assistant.io/_/breaking_changes/icon.png) [Breaking Changes](https://github.com/custom-components/breaking_changes)

_Component to show potential breaking_changes in the current published version based on your loaded components_


[**My configuration for Breaking Changes**](./packages/integrations/custom/breaking_changes.yaml)
**Version** | 21.4.0
--|--
**Author(s)** | @ludeeus

### [<img src="https://brands.home-assistant.io/_/readme/icon.png" height="24"/>](https://brands.home-assistant.io/_/readme/icon.png) [Generate Readme](https://github.com/custom-components/readme)

_Use Jinja and data from Home Assistant to generate your README.md file_

**Version** | 0.3.0
--|--
**Author(s)** | @ludeeus

## The custom lovelace plugins that I use

### [<img src="https://brands.home-assistant.io/_//icon.png" height="24"/>](https://brands.home-assistant.io/_//icon.png) [Sun Card](https://github.com/AitorDB/home-assistant-sun-card)

_Home assistant sun card based on Google weather design_

**Version** | v0.1.4
--|--

### [<img src="https://brands.home-assistant.io/_//icon.png" height="24"/>](https://brands.home-assistant.io/_//icon.png) [Mini Graph Card](https://github.com/kalkih/mini-graph-card)

_Minimalistic graph card for Home Assistant Lovelace UI_

**Version** | v0.10.0
--|--


***

Like all other Home Assistant instances this is also a Work in Progress :D

<!-- Footnotes -->
[^1]: UI Configuration