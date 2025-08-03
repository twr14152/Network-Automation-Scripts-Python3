# Restconf
This repo is extremely out of date and lacking. At the time I started this it wasn't real clear how it should be used. If I can get more time I will try and update it. For now all I have is really one working example. I will try to get around to updating this befor too much longer.

08.03.2025_restconf_ex.py 
- configures loopback 72
- shows all the interfaces on the device.
```
pi@rasp4:~/Coding/python_folder/misc $ python3.12 08.03.2025_restconf_ex.py 
POST/PUT response:
201


GET response:
200
{
  "ietf-interfaces:interfaces": {
    "interface": [
      {
        "name": "GigabitEthernet1",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": true,
        "ietf-ip:ipv4": {
          "address": [
            {
              "ip": "10.10.20.148",
              "netmask": "255.255.255.0"
            }
          ]
        },
        "ietf-ip:ipv6": {
        }
      },
      {
        "name": "GigabitEthernet2",
        "description": "configured via SSH",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": true,
        "ietf-ip:ipv4": {
          "address": [
            {
              "ip": "10.10.21.1",
              "netmask": "255.255.255.240"
            }
          ]
        },
        "ietf-ip:ipv6": {
        }
      },
      {
        "name": "GigabitEthernet3",
        "description": "configured via NETCONF",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": true,
        "ietf-ip:ipv4": {
          "address": [
            {
              "ip": "10.10.22.16",
              "netmask": "255.255.255.0"
            }
          ]
        },
        "ietf-ip:ipv6": {
        }
      },
      {
        "name": "Loopback12",
        "type": "iana-if-type:softwareLoopback",
        "enabled": true,
        "ietf-ip:ipv4": {
          "address": [
            {
              "ip": "12.12.12.12",
              "netmask": "255.255.255.255"
            }
          ]
        },
        "ietf-ip:ipv6": {
        }
      },
      {
        "name": "Loopback22",
        "description": "configured via NETCONF",
        "type": "iana-if-type:softwareLoopback",
        "enabled": true,
        "ietf-ip:ipv4": {
          "address": [
            {
              "ip": "10.20.22.22",
              "netmask": "255.255.255.255"
            }
          ]
        },
        "ietf-ip:ipv6": {
        }
      },
      {
        "name": "Loopback72",
        "description": "configured via RESTCONF",
        "type": "iana-if-type:softwareLoopback",
        "enabled": true,
        "ietf-ip:ipv4": {
          "address": [
            {
              "ip": "10.72.72.72",
              "netmask": "255.255.255.255"
            }
          ]
        },
        "ietf-ip:ipv6": {
        }
      },
      {
        "name": "Loopback222",
        "description": "configured via NETCONF",
        "type": "iana-if-type:softwareLoopback",
        "enabled": true,
        "ietf-ip:ipv4": {
          "address": [
            {
              "ip": "222.20.22.22",
              "netmask": "255.255.255.255"
            }
          ]
        },
        "ietf-ip:ipv6": {
        }
      },
      {
        "name": "VirtualPortGroup0",
        "type": "iana-if-type:propVirtual",
        "enabled": true,
        "ietf-ip:ipv4": {
          "address": [
            {
              "ip": "172.16.32.1",
              "netmask": "255.255.255.0"
            }
          ]
        },
        "ietf-ip:ipv6": {
        }
      }
    ]
  }
}

pi@rasp4:~/Coding/python_folder/misc $
```
