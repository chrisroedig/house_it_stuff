# House IT Stuff

Automation to configure various IT related things in the house

## Architecture

- Main host
  - services via docker-compose and systemd
  - pihole - DNS server with ad/tracking prevention
  - mosquitto - mqtt broker (useful for home automaton
  - node-red - flow based programming environment for automation
  - homebridge - service to emulate Apple HomeKit accessories
  - data monitor - various scheduled scripts to gather, record and broadcast data from APIs
  - TICK stack - timeseries database an monitoring
  - Grafana - data visualization, dashboards alerting

- DMZ host
  - nginx for reverse proxy to internal web services

## Setting Up

- make sure ansible (and python) is installed 
- make sure `sshpass` is installed
  - brew install https://raw.githubusercontent.com/kadwanev/bigboybrew/master/Library/Formula/sshpass.rb
- set up the hosts file
  - see below on how to prep the pi's SD card for first boot
  - boot the pi
  - `cp hosts.yml.example hosts.yml`
  - locate the pi on the network using `bin/findhosts`
  - edit `hosts.yml` with the proper IP, username/password for the raspberry pi

- make the right config files are present (not in this repo)


## Running Things

Setting up the main host for internal services
```
playbook main.yml -i hosts.yml
```

Setting up the dmz host to proxy web services
```
playbook dmz.yml -i hosts.yml
```

## Prepping new Raspbian SD card

- Assuming **Raspbian GNU/Linux** as the OS
- Download and flash: https://www.raspberrypi.org/documentation/installation/installing-images/README.md
- Remount the SD, open a terminal, cd to the Volume (`/Volumes/boot` on mac OS)
- create an empty file `ssh` (enables ssh on boot)
- create the file `wpa_supplicant.conf` (configures wifi network access)

    ```
    country=US
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    network={
      ssid="--ssid--"
      psk="--psk--"
      key_mgmt=WPA-PSK
      }
    ```
  - boot the board with card inserted, it should show up on your wifi network
