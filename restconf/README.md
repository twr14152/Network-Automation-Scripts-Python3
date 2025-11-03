# Restconf

The lab I'm using for testing is containerlab and arista ceos for this. I notice that hostname look up using python requests is significantly slower than curl. If I use the IP address with python/requests I do not have the extremely slow response times. Not exactly sure why that is but its working better with IP addresssing.


This first example is how to configure a cisco ios xe device

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

View device interface state or config
req_intf_state_cfg.py
```
(lab_env) todd@todd-TOSHIBA-DX735:~/Code_folder/containerlab/containerlabs_sandbox/ceos_lab/lab3/scripts/restconf_stuff$ python req_intf_state_cfg.py 
Enter device: 172.20.20.6
Enter interface (example Ethernet1..): Ethernet1
You want the config (press 1) or state (press 2): 1
200
{
  "openconfig-interfaces:description": "connected to ceos2",
  "openconfig-interfaces:mtu": 0,
  "openconfig-interfaces:name": "Ethernet1",
  "openconfig-interfaces:type": "iana-if-type:ethernetCsmacd"
}
(lab_env) todd@todd-TOSHIBA-DX735:~/Code_folder/containerlab/containerlabs_sandbox/ceos_lab/lab3/scripts/restconf_stuff$ python req_intf_state_cfg.py 
Enter device: 172.20.20.6
Enter interface (example Ethernet1..): Ethernet1
You want the config (press 1) or state (press 2): 2
200
{
  "openconfig-interfaces:admin-status": "UP",
  "openconfig-interfaces:counters": {
    "carrier-transitions": "2",
    "in-broadcast-pkts": "5",
    "in-discards": "0",
    "in-errors": "0",
    "in-fcs-errors": "0",
    "in-multicast-pkts": "7229",
    "in-octets": "10870402",
    "in-pkts": "131926",
    "in-unicast-pkts": "124692",
    "out-broadcast-pkts": "0",
    "out-discards": "0",
    "out-errors": "0",
    "out-multicast-pkts": "0",
    "out-octets": "0",
    "out-pkts": "0",
    "out-unicast-pkts": "0"
  },
  "openconfig-interfaces:description": "connected to ceos2",
  "openconfig-platform-port:hardware-port": "Ethernet1-Port",
  "openconfig-interfaces:ifindex": 1,
  "arista-intf-augments:inactive": false,
  "openconfig-interfaces:last-change": "1762136595449047327",
  "openconfig-interfaces:management": false,
  "openconfig-interfaces:mtu": 0,
  "openconfig-interfaces:name": "Ethernet1",
  "openconfig-interfaces:oper-status": "UP",
  "openconfig-platform-transceiver:transceiver": "Ethernet1",
  "openconfig-interfaces:type": "iana-if-type:ethernetCsmacd"
}
(lab_env) todd@todd-TOSHIBA-DX735:~/Code_folder/containerlab/containerlabs_sandbox/ceos_lab/lab3/scripts/restconf_stuff$
```
Using requests to grab interface data and then present only what you want. In this case we want the interface name, state, packets in/out, and errors,
```
(lab_env) todd@todd-TOSHIBA-DX735:~/Code_folder/containerlab/containerlabs_sandbox/ceos_lab/lab3/scripts/restconf_stuff$ python req_intf_name_state_errors.py 
Enter host: 172.20.20.7
Enter interface you want to check: Ethernet1
Interface: Ethernet1
Status: UP
In Packets: 7709
Out Packets: 0
In Discards: 0
In Errors: 0
Out Discards: 0
Out Errors: 0
(lab_env) todd@todd-TOSHIBA-DX735:~/Code_folder/containerlab/containerlabs_sandbox/ceos_lab/lab3/scripts/restconf_stuff$ python req_intf_name_state_errors.py 
Enter host: 172.20.20.7
Enter interface you want to check: Ethernet1
Interface: Ethernet1
Status: UP
In Packets: 7711
Out Packets: 0
In Discards: 0
In Errors: 0
Out Discards: 0
Out Errors: 0
(lab_env) todd@todd-TOSHIBA-DX735:~/Code_folder/containerlab/containerlabs_sandbox/ceos_lab/lab3/scripts/restconf_stuff$ 

```
