# ESPHome Device Configs

CAH, 2019-03-26 Configuration definitions for local ESPHome devices.

For information on removing secrets from the repository, see this link: <https://github.com/heckler/home-assistant-config/blob/master/secrets_cleanup.md>

## Device-specific configurations

- [ESP32 Camera modules](docs/esp32cam.md)
- [Flashing Sonoff Basic devices with ESPHome](docs/flashing_sonoff_basic.md)
- [Flashing Sonoff Basic R4 (Magic Switch) devices with ESPHome](docs/flashing_sonoff_basic_r4_magic.md)
- [Flashing Sonoff B1 LED bulbs with ESPHome](docs/flashing_sonoff_b1.md)
- [Configuration instructions for the WLED modules](docs/wled_modules.md)

------------------------------------------------------------------------------------------------

## Initial configuration

### Environment setup

- Getting started guide: [ESPHome Getting Started](https://esphome.io/guides/getting_started_command_line.html)
- WSL: ESPHome should already be configured via the wsl_provision bootstrap script

Optional (VS Code): use the DevContainer in this repository for an isolated, reproducible ESPHome environment.

1. Install the VS Code Dev Containers extension.
2. Open this folder in VS Code and run: `Dev Containers: Reopen in Container`.
3. Wait for the initial container build to complete. The container installs `esphome==2026.6.2` automatically.
4. Verify the install inside the container:

```bash
esphome version
```

5. Start the dashboard from this repository root:

```bash
esphome dashboard .
```

Notes for USB serial flashing from DevContainer:

1. The DevContainer config binds `/dev` and uses `--privileged`, so serial devices (for example `/dev/ttyUSB0`) are available in the container.
2. Ensure your host user has serial permissions (typically membership in the `dialout` group on Linux).
3. Replug USB devices after opening the container if a serial device is not visible.

To update ESPHome:

```bash
pip3 install --upgrade esphome
pip3 install --upgrade virtualenv
```

To install a specific version:

```bash
pip3 uninstall esphome
pip3 install -Iv esphome==2026.6.2
```

The pip commands above are for local (non-DevContainer) installations.

### Updating ESPHome in the DevContainer

When a new ESPHome release is available, update the pinned version in the DevContainer config.

1. Edit the pinned version in `.devcontainer/devcontainer.json` by changing `postCreateCommand` from `esphome==...` to the new release.
2. In VS Code, run `Dev Containers: Rebuild Container`.
3. Confirm the new version:

```bash
esphome version
```

4. Run a quick config validation from the repository root:

```bash
esphome config balcony_sensors.yaml
```

### Creating a new device config (using the wizard)

`esphome hello-world.yaml wizard`

### Building and deploying

`esphome hello-world.yaml run`

### ESPHome dashboard

There is a simple dashboard webserver in ESPHome.  From the folder where the device configs are stored, execute the following command:

`esphome . dashboard`

Then, navigate to the following address: [http://localhost:6052/](http://localhost:6052/)

### Changing the name of a device via OTA

<https://esphome.io/components/esphome.html#changing-esphome-node-name>

1. Change the name of the device on the yaml
2. Use the `use_address` WiFi option to point to the old mDNS name
3. Upload the config, will rename the device, using the old name for OTA
4. Remove `use_address` and upload again (to confirm it finds the new name)
