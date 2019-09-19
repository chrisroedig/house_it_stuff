# House IT Stuff

## Setting Up
automation to configure various IT related things in the house

- make sure ansible (and python) is installed 
- make sure `sshpass` is installed
  - brew install https://raw.githubusercontent.com/kadwanev/bigboybrew/master/Library/Formula/sshpass.rb
- set up the hosts file
  - see below on how to prep the pi's SD card for first boot
  - boot the pi
  - `cp hosts.example hosts`
  - locate the pi on the network using `bin/findhosts`
  - edit with the proper IP of the raspberry pi

- set up the env vars
  - `cp env_vars.example.yml env_vars.yml`
  - update the values

## Running Things

To run all of it
```
bin/playbook
```

To run tagged plays.
for example, everything tagged with `restart` 
```
bin/playbook restart
```

To run tagged plays, but exclude some.
For example configure/restart nodeRed, but skip installing it
```
bin/playbook nodered install
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
