# ESPHome Device Configs

CAH, 2019-03-26

Configuration definitions for local ESPHome devices.

## Initial configuration

### Environment setup

- Getting started guide: [ESPHome Getting Started](https://esphome.io/guides/getting_started_command_line.html)
- WSL: ESPHome should already be configured via the wsl_provision bootstrap script

### Creating a new device config (using the wizard)

`esphome hello-world.yaml wizard`

### Building and deploying

`esphome hello-world.yaml run`

### ESPHome dashboard

There is a simple dashboard webserver in ESPHome.  From the folder where the device configs are stored, execute the following command:

`esphome . dashboard`

Then, navigate to the following address: [http://localhost:6052/](http://localhost:6052/)

------------------------------------------------------------------------------------------------

## Device-specific configurations

### ESP32Cam

- Device: ESP32
- Board: esp-wrover-kit

#### Uploading the first firmware via an USB-serial adapter

1. Wring diagram for ESP32Cam (Wrover-kit) and CP21029 FTDI module:

![ESP32Cam programming: wiring diagram](images/ESP32-CAM-wiring-FTDI1.png)

2. Procedure to put the ESP32Cam module in programming state:

- Wire-up power, GND, Tx and Rx according to the diagram above
- Connect GPIO-0 to GND (shown in gray on the diagram above)

3. Upload the firwware via serial:

`esphome espcam01.yaml run --upload-port=/dev/ttyS4`

- Note: `/dev/ttyS4` above corresponds to serial port `COM4`
- Just before esphome starts to upload the firmware,  click the 'reset' button on the *bottom* of the module
- After uploading the firmware, disconnect GPIO-0 from GND and hit reset again to boot the new firmware

Since version `1.14.0` of ESPHome, the serial upload speed was increased from 115200 to 460800 baud. This causes problems with some USB-to-UART chips. If facing upload problems, use `esptoop.py` to upload the compiled firmware specifying a lower upload speed:

`~/.local/bin/esptool.py --before default_reset --after hard_reset --baud 115200 --chip esp8266 --port /dev/ttyS4 write_flash 0x0 espcam01/.pioenvs/espcam01/firmware.bin`

#### Module detection in Home-Assistant

- Go to Settings > Integrations, and add a new ESPHome integration
- For the hostname, use the device's hostname, for instance, `esp32cam01.local`
- Must be using Home Assistant v0.91 or greater for ESP32Cam integration
