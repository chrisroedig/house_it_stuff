# House IT Stuff
automation to configure various IT related things in the house

- edit `hosts` with the proper IP of the raspberry pi
- edit `group_vars/all` with proper domain name and creds for influx server

To run all of it
```
ansible-playbook -i hosts rileypi.yml
```

To skip the lengthy host prepping
```
ansible-playbook -i hosts rileypi.yml --skip-tags=hostprep
```
