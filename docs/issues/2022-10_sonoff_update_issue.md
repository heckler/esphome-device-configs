# 2022-10-20 Issue updating Sonoff Basic devices

## Description

Several ESPHome devices on the network were running old builds, the oldest one being a Sonoff Basic running a build from version 1.16.2, built in Oct/2021; because this device was displaying some intermittent problems in Home Assistant (see <https://community.home-assistant.io/t/esphome-device-disconnected-in-home-assistant-and-wont-reconnect-automatically/475002/7>) it was decided to update it, and other devices in the network.

A round of updates to ESPHome version 2022.9.4 was performed; several NodeMCU-based (ESP12) devices were successfully updated, and reconnected in Home Assistant without issues.  Two Sonoff Basic (ESP01) devices failed to show-up on the network after the update.

Taking one of the devices down and connecting a serial monitor showed the device to be on a restart loop with following exception being logged while starting the process of connecting to WiFi:

```log
[I][logger:243]: Log initialized
[C][status_led:014]: Setting up Status LED...
[C][ota:465]: There have been 5 suspected unsuccessful boot attempts.
[I][app:029]: Running through setup()...
[C][switch.gpio:011]: Setting up GPIO Switch 'Irrigation Pump Relay'...
[D][switch:017]: 'Irrigation Pump Relay' Turning OFF.
[D][switch:037]: 'Irrigation Pump Relay': Sending state OFF
[D][switch:017]: 'Irrigation Pump Relay' Turning OFF.
[D][binary_sensor:034]: 'Irrigation Pump Button': Sending initial state OFF
[D][text_sensor:067]: 'Irrigation Pump Version': Sending state '2022.9.4 Oct 20 2022, 16:34:53'
[C][wifi:037]: Setting up WiFi...
[D][wifi:384]: Starting scan...
[D][sensor:126]: 'Irrigation Pump Uptime': Sending state 0.15500 s with 0 decimals of accuracy
[D][wifi:399]: Found networks:
[I][wifi:442]: - 'aria' [5m(C4:E9:84:BC:D9:A0) ▂▄▆█
[D][wifi:444]:     Channel: 7
[D][wifi:445]:     RSSI: -39 dB
[I][wifi:442]: - 'ubnt' [5m(FC:EC:DA:87:76:91) ▂▄▆█
[D][wifi:444]:     Channel: 11
[D][wifi:445]:     RSSI: -67 dB
[I][wifi:442]: - 'ubnt' [5m(74:83:C2:41:97:E2) ▂▄▆█
[D][wifi:444]:     Channel: 11
[D][wifi:445]:     RSSI: -71 dB

--------------- CUT HERE FOR EXCEPTION DECODER ---------------

Exception (28):
epc1=0x40223401 epc2=0x00000000 epc3=0x00000000 excvaddr=0x0ee60000 depc=0x00000000

>>>stack>>>

ctx: cont
sp: 3ffffa10 end: 3fffffc0 offset: 0190
3ffffba0:  00000005 3ffe8c89 3fff06a4 402079bb  
3ffffbb0:  0ee60001 000001bf 00000004 3fff248c  
3ffffbc0:  3fff2374 3fff2414 00000000 3fff2324  
3ffffbd0:  3ffffc60 3ffe8c89 3fff0b34 40210978  
3ffffbe0:  3ffffc30 3ffffc20 00000010 001b7716  
3ffffbf0:  000003eb 000003eb 3ffe85dc 402109a4  
3ffffc00:  3ffffc30 3ffffc20 00000010 3ffffc20  
3ffffc10:  3ffffc30 3ffffc20 00000010 40100f96  
3ffffc20:  000000c8 3ffe8c89 0000007a 00000083  
3ffffc30:  3fff2334 3ffffc60 3fff22ac 4022dce4  
3ffffc40:  00000009 3ffe8c89 3fff0b34 4020d415  
3ffffc50:  4025dccc 000000e2 0000ea60 00000000  
3ffffc60:  383a4137 32433a33 3a31343a 453a3739  
3ffffc70:  40220032 3fff1650 40223870 00000002  
3ffffc80:  00004bc6 00000000 00000000 fffffffe  
3ffffc90:  00000000 4bc6a7f0 94fdf3b6 001b77d4  
3ffffca0:  00000000 00000000 4bc6a7f0 00000000  
3ffffcb0:  0000000a 3fff0b34 40100641 00000000  
3ffffcc0:  00000000 4bc6a7f0 99999999 001b77d9  
3ffffcd0:  00000000 4bc6a7f0 a0000000 001b77e1  
3ffffce0:  00000000 00000000 4bc6a7f0 00000000  
3ffffcf0:  000017c1 00000000 40100641 00000000  
3ffffd00:  3fff2414 3fff0c34 3fff2224 3ffe9154  
3ffffd10:  3fff230c 3fff2224 3fff0a34 00000102  
3ffffd20:  3fff0b34 0000000a 3fff0b34 00000102  
3ffffd30:  3fff0b34 000017c1 3fff0b34 4020d7e8  
3ffffd40:  3fff0b34 0000000a 3ffef4cc 4022387c  
3ffffd50:  3fff0160 3ffffd70 3ffef4cc 40223948  
3ffffd60:  3fff0b34 0000000a 3ffef4cc 4020fded  
3ffffd70:  0000000b 0000000b 3fff185c 3fffff68  
3ffffd80:  0000002c 00000004 00000001 40100fc0  
3ffffd90:  3fff1068 3ffef59c 00000008 3fffff68  
3ffffda0:  3fff1084 3ffef5bc 3ffef4cc 40212318  
3ffffdb0:  3fff0cb4 00000017 0000001e 00000000  
3ffffdc0:  00000000 00000000 00000000 00000000  
3ffffdd0:  3ffffdd8 00000008 78656c66 73676f64  
3ffffde0:  00000000 00000000 00000000 00000000  
3ffffdf0:  00000000 00000000 00000000 00000000  
3ffffe00:  00000000 00000000 3ffffe10 00000005 <
3ffffe10:  53544151 00000049 00000000 00000000  
3ffffe20:  00000000 00000000 3ffffe30 00000009 <
3ffffe30:  66696175 34376961 00000037 00000000  
3ffffe40:  00000000 00000000 00000000 00000000  
3ffffe50:  00000000 00000000 00000000 00000000  
3ffffe60:  3ffffe68 00000004 61697261 00000000  
3ffffe70:  00000000 00000000 00000000 00000000  
3ffffe80:  3ffffe88 00000009 66696175 34376961  
3ffffe90:  00000037 00000000 00000000 00000000  
3ffffea0:  00000000 00000000 00000000 00000000  
3ffffeb0:  00000000 00000000 3ffffec0 00000005 <
3ffffec0:  73746171 00000069 00000000 00000000  
3ffffed0:  00000000 00000000 3ffffee0 00000009 <
3ffffee0:  66696175 34376961 00000037 00000000  
3ffffef0:  00000000 00000000 00000000 00000000  
3fffff00:  00000000 00000000 00000000 00000000  
3fffff10:  3fffff18 00000004 746e6275 00000000  
3fffff20:  00000000 00000000 00000000 00000000  
3fffff30:  3fffff38 00000009 66696175 34376961  
3fffff40:  00000037 00000000 00000000 00000000  
3fffff50:  00000000 00000000 00000000 00000000  
3fffff60:  00000000 00000000 3fff11cc 0000000b  
3fffff70:  3a69646d 2d77656e 00786f62 00687467  
3fffff80:  3fff15ac 3ffef520 0000ea60 feefeffe  
3fffff90:  feefeffe feefeffe feefeffe 3ffef8ec  
3fffffa0:  3fffdad0 00000000 3ffef8d8 4021fcf8  
3fffffb0:  feefeffe feefeffe 3ffe85d8 40100489  
<<<stack<<<

--------------- CUT HERE FOR EXCEPTION DECODER ---------------

 ets Jan  8 2013,rst cause:1, boot mode:(3,7)

load 0x4010f000, len 3460, room 16 
tail 4
chksum 0xcc
load 0x3fff20b8, len 40, room 4 
tail 4
chksum 0xc9
csum 0xc9
v00067730
~ld
```

## Troubleshooting

### Updating to ESPHome version 2022.10.0

Uploading a firmware compiled with the latest ESPHome version (2022.10.0 as of this reporting) did solve the issue, the device booted without issue and connected to the network.

It was not possible to identify from the [ESPhome release notes](https://github.com/esphome/esphome/releases/) what could've caused the issue.
