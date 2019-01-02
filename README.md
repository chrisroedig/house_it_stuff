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

To skip the lengthy host prepping
```
ansible-playbook -i hosts rileypi.yml --skip-tags=hostprep
```
Role based tasks are tagged, helps run just one thing as needed
