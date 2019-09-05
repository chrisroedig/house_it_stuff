# House IT Stuff
automation to configure various IT related things in the house

- set up the hosts file
  - `cp hosts.example hosts`
  - locate the pi on the network using `bin/findhosts`
  - edit with the proper IP of the raspberry pi

- set up the env vars
  - `cp env_vars.example.yml env_vars.yml`
  - update the values

To run all of it
```
ansible-playbook -i hosts rileypi.yml
```

## Prepping new Raspbian SD card

- Assuming **Raspbian GNU/Linux** as the OS
- Download and flash: https://www.raspberrypi.org/documentation/installation/installing-images/README.md
- Remount the SD, open a terminal, cd to the Volume
- create an empty file `ssh` (enables ssh on boot)
- create the file `wpa_supplicant.conf`

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
