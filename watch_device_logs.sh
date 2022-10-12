#!/bin/bash

# Monitor the logs of the ESPHome devices
# CAH 2022-06-14

echo "Starting to watch ESPHome logs ..."

mkdir -p logs
rm logs/*.log

esphome balcony_sensors.yaml logs    2>&1 >> logs/log_balcony_sensors.log    &
esphome balcony_sensors_02.yaml logs 2>&1 >> logs/log_balcony_sensors_02.log &
esphome fireplace_light.yaml logs    2>&1 >> logs/log_fireplace_light.log    &
esphome freezer_sensors.yaml logs    2>&1 >> logs/log_freezer_sensors.log    &
esphome irrigation_pump.yaml logs    2>&1 >> logs/log_irrigation_pump.log    &
esphome wakeup_light_01r.yaml logs   2>&1 >> logs/log_wakeup_light_01r.log   &
esphome wakeup_light_02g.yaml logs   2>&1 >> logs/log_wakeup_light_02g.log   &

echo "Watching ESPHome logs in the background:"

ls -la logs/log_*.log

echo "To kill them:  ps | grep esphome"

ps | grep esphome

