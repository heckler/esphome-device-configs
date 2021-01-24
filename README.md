# ESPHome Device Configs

CAH, 2019-03-26 Configuration definitions for local ESPHome devices.

For information on removing secrets from the repository, see this link: <https://github.com/heckler/home-assistant-config/blob/master/secrets_cleanup.md>

## Device-specific configurations

- [ESP32 Camera modules](docs/esp32cam.md)
- [Flashing Sonoff devices with ESPHome](docs/sonoff_flashing.md)

------------------------------------------------------------------------------------------------

## Initial configuration

### Environment setup

- Getting started guide: [ESPHome Getting Started](https://esphome.io/guides/getting_started_command_line.html)
- WSL: ESPHome should already be configured via the wsl_provision bootstrap script

To update ESPHome:

> pip3 install --upgrade esphome
> pip3 install --upgrade virtualenv

To install a specific version:

> pip3 uninstall esphome
> pip3 install -Iv esphome==1.14.5

### Creating a new device config (using the wizard)

`esphome hello-world.yaml wizard`

### Building and deploying

`esphome hello-world.yaml run`

### ESPHome dashboard

There is a simple dashboard webserver in ESPHome.  From the folder where the device configs are stored, execute the following command:

`esphome . dashboard`

Then, navigate to the following address: [http://localhost:6052/](http://localhost:6052/)
