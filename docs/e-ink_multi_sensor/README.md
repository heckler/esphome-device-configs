# Multi-sensor board with e-ink display

CAH 2026-09-19

## Overview

This is an ESP32-based device with an e-ink display (WeAct 4.2" 3-color) and a number of sensors.  It will read indoor and outdoor temperatures as well as CO2, barometric pressure and relative humidity. The main components are:

- ESP32: YD-ESP32-S3 / ESP32-S3-WROOM-1 Dev N16R8 (44-pin)
- WeAct 4.2" 3-color e-ink display (white, black and red)
- BME280 sensor (Barometric pressure, temperature and relative humidity - to be placed outdoors)
- SCD41 (CO2, temperature and relative humidity - to be placed indoors)
- HC-SR501 PIR sensor (for updating the e-ink panel only when there's recent movement)
- WS2812b status LED (1-5 LEDs on a strip, to be defined)
- 2 capacitive switches for input

## GPIO allocation

|   GPIO | Function | Device             | Notes                    |
| -----: | -------- | ------------------ | ------------------------ |
|  GPIO4 | I²C SDA  | BME280 + SCD41     | Good general-purpose pin |
|  GPIO5 | I²C SCL  | BME280 + SCD41     | Good general-purpose pin |
|  GPIO6 | SPI CLK  | WeAct 4.2" e-paper | E-paper SPI              |
|  GPIO7 | SPI MOSI | WeAct 4.2" e-paper | E-paper SPI              |
|  GPIO8 | CS       | WeAct 4.2" e-paper | Chip select              |
|  GPIO9 | DC       | WeAct 4.2" e-paper | Data/command             |
| GPIO10 | RST      | WeAct 4.2" e-paper | Display reset            |
| GPIO11 | BUSY     | WeAct 4.2" e-paper | Display busy input       |
| GPIO12 | PIR OUT  | HC-SR501           | Digital input            |
| GPIO13 | DATA     | WS2812B            | Drives 1–5 LEDs          |
| GPIO14 | Switch 1 | Pushbutton/switch  | Digital input            |
| GPIO15 | Switch 2 | Pushbutton/switch  | Digital input            |
| GPIO16 | —        | Spare              | Keep available           |
| GPIO17 | —        | Spare              | Keep available           |
| GPIO18 | —        | Spare              | Keep available           |
| GPIO21 | —        | Spare              | Keep available           |

## Reserved GPIOs

|         GPIO | Reason                                               |
| -----------: | ---------------------------------------------------- |
|        GPIO0 | Boot/strapping                                       |
|        GPIO3 | Strapping                                            |
|    GPIO19/20 | Native USB D−/D+                                     |
| GPIO35/36/37 | N16R8 octal PSRAM                                    |
|    GPIO43/44 | USB-UART / UART0                                     |
|       GPIO45 | Strapping                                            |
|       GPIO46 | Strapping                                            |
|       GPIO48 | On-board RGB LED / special-purpose pin               |
|    GPIO39–42 | JTAG pins; usable, but better retained for debugging |

## ESPHome configuration

### ESP32 S3 board

```yaml
esp32:
  board: esp32-s3-devkitc-1
  framework:
    type: esp-idf
psram:
  mode: octal
  speed: 80MHz
```

### WeAct 4.2" 3-color e-ink panel

```yaml
spi:
  clk_pin: GPIO6
  mosi_pin: GPIO7

display:
  - platform: epaper_spi
    model: WeAct-4.2in-3c
    cs_pin: GPIO8
    dc_pin: GPIO9
    reset_pin: GPIO10
    busy_pin: GPIO11
```
