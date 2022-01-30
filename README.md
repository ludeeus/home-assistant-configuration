# Welcome 👋!

This is my Home Assistant installation.

## Some statistics about my installation:

Description | value
--|--
Installed version | 2022.3.0.dev20220130
Total entity objects | 2642
Entities in the [`automation`](https://www.home-assistant.io/components/automation) domain | 3
Entities in the [`binary_sensor`](https://www.home-assistant.io/components/binary_sensor) domain | 34
Entities in the [`button`](https://www.home-assistant.io/components/button) domain | 3
Entities in the [`device_tracker`](https://www.home-assistant.io/components/device_tracker) domain | 5
Entities in the [`input_datetime`](https://www.home-assistant.io/components/input_datetime) domain | 1
Entities in the [`input_text`](https://www.home-assistant.io/components/input_text) domain | 1
Entities in the [`light`](https://www.home-assistant.io/components/light) domain | 5
Entities in the [`media_player`](https://www.home-assistant.io/components/media_player) domain | 24
Entities in the [`person`](https://www.home-assistant.io/components/person) domain | 1
Entities in the [`script`](https://www.home-assistant.io/components/script) domain | 4
Entities in the [`sensor`](https://www.home-assistant.io/components/sensor) domain | 2551
Entities in the [`sun`](https://www.home-assistant.io/components/sun) domain | 1
Entities in the [`switch`](https://www.home-assistant.io/components/switch) domain | 6
Entities in the [`vacuum`](https://www.home-assistant.io/components/vacuum) domain | 1
Entities in the [`weather`](https://www.home-assistant.io/components/weather) domain | 1
Entities in the [`zone`](https://www.home-assistant.io/components/zone) domain | 1

## Core integrations that I use

Integration | Configuration
--|--
[<img src="https://brands.home-assistant.io/_/adguard/icon.png" height="24"/>](https://brands.home-assistant.io/_/adguard/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/adguard/icon.png" height="24"/>](https://brands.home-assistant.io/_/adguard/icon.png#gh-light-mode-only) [AdGuard Home](https://home-assistant.io/integrations/adguard) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/automation/icon.png" height="24"/>](https://brands.home-assistant.io/_/automation/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/automation/icon.png" height="24"/>](https://brands.home-assistant.io/_/automation/icon.png#gh-light-mode-only) [Automations](https://home-assistant.io/integrations/automation) | [./automations.yaml](./automations.yaml)
[<img src="https://brands.home-assistant.io/_/wemo/icon.png" height="24"/>](https://brands.home-assistant.io/_/wemo/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/wemo/icon.png" height="24"/>](https://brands.home-assistant.io/_/wemo/icon.png#gh-light-mode-only) [Belkin WeMo](https://home-assistant.io/integrations/wemo) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/cast/icon.png" height="24"/>](https://brands.home-assistant.io/_/cast/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/cast/icon.png" height="24"/>](https://brands.home-assistant.io/_/cast/icon.png#gh-light-mode-only) [Cast](https://home-assistant.io/integrations/cast) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/cloud/icon.png" height="24"/>](https://brands.home-assistant.io/_/cloud/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/cloud/icon.png" height="24"/>](https://brands.home-assistant.io/_/cloud/icon.png#gh-light-mode-only) [Cloud](https://home-assistant.io/integrations/cloud) | [./packages/integrations/core/cloud.yaml](./packages/integrations/core/cloud.yaml)
[<img src="https://brands.home-assistant.io/_/cloudflare/icon.png" height="24"/>](https://brands.home-assistant.io/_/cloudflare/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/cloudflare/icon.png" height="24"/>](https://brands.home-assistant.io/_/cloudflare/icon.png#gh-light-mode-only) [Cloudflare](https://home-assistant.io/integrations/cloudflare) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/default_config/icon.png" height="24"/>](https://brands.home-assistant.io/_/default_config/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/default_config/icon.png" height="24"/>](https://brands.home-assistant.io/_/default_config/icon.png#gh-light-mode-only) [Default Config](https://home-assistant.io/integrations/default_config) | [./configuration.yaml](./configuration.yaml)
[<img src="https://brands.home-assistant.io/_/frontend/icon.png" height="24"/>](https://brands.home-assistant.io/_/frontend/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/frontend/icon.png" height="24"/>](https://brands.home-assistant.io/_/frontend/icon.png#gh-light-mode-only) [Frontend](https://home-assistant.io/integrations/frontend) | [./packages/integrations/core/frontend.yaml](./packages/integrations/core/frontend.yaml)
[<img src="https://brands.home-assistant.io/_/github/icon.png" height="24"/>](https://brands.home-assistant.io/_/github/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/github/icon.png" height="24"/>](https://brands.home-assistant.io/_/github/icon.png#gh-light-mode-only) [GitHub](https://home-assistant.io/integrations/github) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/influxdb/icon.png" height="24"/>](https://brands.home-assistant.io/_/influxdb/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/influxdb/icon.png" height="24"/>](https://brands.home-assistant.io/_/influxdb/icon.png#gh-light-mode-only) [InfluxDB](https://home-assistant.io/integrations/influxdb) | [./packages/integrations/core/influxdb.yaml](./packages/integrations/core/influxdb.yaml)
[<img src="https://brands.home-assistant.io/_/launch_library/icon.png" height="24"/>](https://brands.home-assistant.io/_/launch_library/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/launch_library/icon.png" height="24"/>](https://brands.home-assistant.io/_/launch_library/icon.png#gh-light-mode-only) [Launch Library](https://home-assistant.io/integrations/launch_library) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/logger/icon.png" height="24"/>](https://brands.home-assistant.io/_/logger/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/logger/icon.png" height="24"/>](https://brands.home-assistant.io/_/logger/icon.png#gh-light-mode-only) [Logger](https://home-assistant.io/integrations/logger) | [./packages/integrations/core/logger.yaml](./packages/integrations/core/logger.yaml)
[<img src="https://brands.home-assistant.io/_/met/icon.png" height="24"/>](https://brands.home-assistant.io/_/met/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/met/icon.png" height="24"/>](https://brands.home-assistant.io/_/met/icon.png#gh-light-mode-only) [Met.no](https://home-assistant.io/integrations/met) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/mobile_app/icon.png" height="24"/>](https://brands.home-assistant.io/_/mobile_app/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/mobile_app/icon.png" height="24"/>](https://brands.home-assistant.io/_/mobile_app/icon.png#gh-light-mode-only) [Mobile App](https://home-assistant.io/integrations/mobile_app) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/netatmo/icon.png" height="24"/>](https://brands.home-assistant.io/_/netatmo/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/netatmo/icon.png" height="24"/>](https://brands.home-assistant.io/_/netatmo/icon.png#gh-light-mode-only) [Netatmo](https://home-assistant.io/integrations/netatmo) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/nanoleaf/icon.png" height="24"/>](https://brands.home-assistant.io/_/nanoleaf/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/nanoleaf/icon.png" height="24"/>](https://brands.home-assistant.io/_/nanoleaf/icon.png#gh-light-mode-only) [Nanoleaf](https://home-assistant.io/integrations/nanoleaf) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/plex/icon.png" height="24"/>](https://brands.home-assistant.io/_/plex/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/plex/icon.png" height="24"/>](https://brands.home-assistant.io/_/plex/icon.png#gh-light-mode-only) [Plex](https://home-assistant.io/integrations/plex) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/rest/icon.png" height="24"/>](https://brands.home-assistant.io/_/rest/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/rest/icon.png" height="24"/>](https://brands.home-assistant.io/_/rest/icon.png#gh-light-mode-only) [Rest](https://home-assistant.io/integrations/rest) | [./packages/integrations/core/rest.yaml](./packages/integrations/core/rest.yaml)
[<img src="https://brands.home-assistant.io/_/script/icon.png" height="24"/>](https://brands.home-assistant.io/_/script/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/script/icon.png" height="24"/>](https://brands.home-assistant.io/_/script/icon.png#gh-light-mode-only) [Script](https://home-assistant.io/integrations/script) | [./scripts.yaml](./scripts.yaml)
[<img src="https://brands.home-assistant.io/_/sentry/icon.png" height="24"/>](https://brands.home-assistant.io/_/sentry/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/sentry/icon.png" height="24"/>](https://brands.home-assistant.io/_/sentry/icon.png#gh-light-mode-only) [Sentry](https://home-assistant.io/integrations/sentry) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/spotify/icon.png" height="24"/>](https://brands.home-assistant.io/_/spotify/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/spotify/icon.png" height="24"/>](https://brands.home-assistant.io/_/spotify/icon.png#gh-light-mode-only) [Spotify](https://home-assistant.io/integrations/spotify) | [./packages/integrations/core/spotify.yaml](./packages/integrations/core/spotify.yaml)
[<img src="https://brands.home-assistant.io/_/hassio/icon.png" height="24"/>](https://brands.home-assistant.io/_/hassio/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/hassio/icon.png" height="24"/>](https://brands.home-assistant.io/_/hassio/icon.png#gh-light-mode-only) [Supervisor](https://home-assistant.io/integrations/hassio) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/synology_dsm/icon.png" height="24"/>](https://brands.home-assistant.io/_/synology_dsm/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/synology_dsm/icon.png" height="24"/>](https://brands.home-assistant.io/_/synology_dsm/icon.png#gh-light-mode-only) [Synology](https://home-assistant.io/integrations/synology_dsm) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/tautulli/icon.png" height="24"/>](https://brands.home-assistant.io/_/tautulli/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/tautulli/icon.png" height="24"/>](https://brands.home-assistant.io/_/tautulli/icon.png#gh-light-mode-only) [Tautulli](https://home-assistant.io/integrations/tautulli) | [./packages/integrations/core/tautulli.yaml](./packages/integrations/core/tautulli.yaml)
[<img src="https://brands.home-assistant.io/_/telegram/icon.png" height="24"/>](https://brands.home-assistant.io/_/telegram/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/telegram/icon.png" height="24"/>](https://brands.home-assistant.io/_/telegram/icon.png#gh-light-mode-only) [Telegram BOT](https://home-assistant.io/integrations/telegram) | [./packages/integrations/core/telegram.yaml](./packages/integrations/core/telegram.yaml)
[<img src="https://brands.home-assistant.io/_/template/icon.png" height="24"/>](https://brands.home-assistant.io/_/template/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/template/icon.png" height="24"/>](https://brands.home-assistant.io/_/template/icon.png#gh-light-mode-only) [Template](https://home-assistant.io/integrations/template) | [./packages/integrations/core/template.yaml](./packages/integrations/core/template.yaml)
[<img src="https://brands.home-assistant.io/_/tuya/icon.png" height="24"/>](https://brands.home-assistant.io/_/tuya/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/tuya/icon.png" height="24"/>](https://brands.home-assistant.io/_/tuya/icon.png#gh-light-mode-only) [Tuya](https://home-assistant.io/integrations/tuya) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/uptimerobot/icon.png" height="24"/>](https://brands.home-assistant.io/_/uptimerobot/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/uptimerobot/icon.png" height="24"/>](https://brands.home-assistant.io/_/uptimerobot/icon.png#gh-light-mode-only) [Uptime Robot](https://home-assistant.io/integrations/uptimerobot) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/version/icon.png" height="24"/>](https://brands.home-assistant.io/_/version/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/version/icon.png" height="24"/>](https://brands.home-assistant.io/_/version/icon.png#gh-light-mode-only) [Version](https://home-assistant.io/integrations/version) | Config flow[^1]
[<img src="https://brands.home-assistant.io/_/xiaomi_miio/icon.png" height="24"/>](https://brands.home-assistant.io/_/xiaomi_miio/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/xiaomi_miio/icon.png" height="24"/>](https://brands.home-assistant.io/_/xiaomi_miio/icon.png#gh-light-mode-only) [Xiaomi Miio](https://home-assistant.io/integrations/xiaomi_miio) | Config flow[^1]



## The custom integrations that I use

### [<img src="https://brands.home-assistant.io/_/hacs/icon.png" height="24"/>](https://brands.home-assistant.io/_/hacs/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/hacs/icon.png" height="24"/>](https://brands.home-assistant.io/_/hacs/icon.png#gh-light-mode-only) [HACS](https://github.com/hacs/integration)

_HACS gives you a powerful UI to handle downloads of all your custom needs._

**Version** | 1.20.0
--|--
**Author(s)** | @ludeeus

### [<img src="https://brands.home-assistant.io/_/breaking_changes/icon.png" height="24"/>](https://brands.home-assistant.io/_/breaking_changes/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/breaking_changes/icon.png" height="24"/>](https://brands.home-assistant.io/_/breaking_changes/icon.png#gh-light-mode-only) [Breaking Changes](https://github.com/custom-components/breaking_changes)

_Component to show potential breaking_changes in the current published version based on your loaded components_


[**My configuration for Breaking Changes**](./packages/integrations/custom/breaking_changes.yaml)
**Version** | 21.12.0
--|--
**Author(s)** | @ludeeus

### [<img src="https://brands.home-assistant.io/_/readme/icon.png" height="24"/>](https://brands.home-assistant.io/_/readme/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/readme/icon.png" height="24"/>](https://brands.home-assistant.io/_/readme/icon.png#gh-light-mode-only) [Generate Readme](https://github.com/custom-components/readme)

_Use Jinja and data from Home Assistant to generate your README.md file_

**Version** | 0.4.0
--|--
**Author(s)** | @ludeeus

## The custom lovelace plugins that I use

###  [Sun Card](https://github.com/AitorDB/home-assistant-sun-card)

_Home assistant sun card based on Google weather design_

**Version** | v0.1.4
--|--

###  [Mini Graph Card](https://github.com/kalkih/mini-graph-card)

_Minimalistic graph card for Home Assistant Lovelace UI_

**Version** | v0.11.0-dev.4
--|--


***

Like all other Home Assistant instances this is also a Work in Progress :D

<!-- Footnotes -->
[^1]: UI Configuration