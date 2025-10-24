# pyGNMI

So far of the model driven programmability subtypes gnmi or pygnmi has been the easiest for me to get up and running and play around with, I'm not doing anything special just getting the basics down. These scripts are just testing the show or get commands, and the set or config commands.

So the first script shows how to pull data from the device

```
$ python get_intf_info_gnmi.py 
Enter target interface (example Ethernet1):Ethernet2
What do you want to look at (config, state, counters): config
Interface configuration:
{
  "notification": [
    {
      "timestamp": 1761333153600784579,
      "prefix": null,
      "alias": null,
      "atomic": false,
      "update": [
        {
          "path": "interfaces/interface[name=Ethernet2]/config",
          "val": {
            "openconfig-interfaces:description": "to ceos3",
            "openconfig-interfaces:mtu": 0,
            "openconfig-interfaces:name": "Ethernet2",
            "openconfig-interfaces:type": "iana-if-type:ethernetCsmacd"
          }
        }
      ]
    }
  ]
}
```
```
$ python get_intf_info_gnmi.py 
Enter target interface (example Ethernet1):Ethernet2
What do you want to look at (config, state, counters): state
Interface status:
{
  "notification": [
    {
      "timestamp": 1761333168496781856,
      "prefix": null,
      "alias": null,
      "atomic": false,
      "update": [
        {
          "path": "interfaces/interface[name=Ethernet2]/state",
          "val": {
            "openconfig-interfaces:admin-status": "UP",
            "openconfig-interfaces:counters": {
              "carrier-transitions": "2",
              "in-broadcast-pkts": "0",
              "in-discards": "0",
              "in-errors": "0",
              "in-fcs-errors": "0",
              "in-multicast-pkts": "91661",
              "in-octets": "11932114",
              "in-pkts": "91973",
              "in-unicast-pkts": "312",
              "out-broadcast-pkts": "0",
              "out-discards": "0",
              "out-errors": "0",
              "out-multicast-pkts": "0",
              "out-octets": "0",
              "out-pkts": "0",
              "out-unicast-pkts": "0"
            },
            "openconfig-interfaces:description": "to ceos3",
            "openconfig-platform-port:hardware-port": "Ethernet2-Port",
            "openconfig-interfaces:ifindex": 2,
            "arista-intf-augments:inactive": false,
            "openconfig-interfaces:last-change": "1760708762301774501",
            "openconfig-interfaces:management": false,
            "openconfig-interfaces:mtu": 0,
            "openconfig-interfaces:name": "Ethernet2",
            "openconfig-interfaces:oper-status": "UP",
            "openconfig-platform-transceiver:transceiver": "Ethernet2",
            "openconfig-interfaces:type": "iana-if-type:ethernetCsmacd"
          }
        }
      ]
    }
  ]
}

```
```
$ python get_intf_info_gnmi.py 
Enter target interface (example Ethernet1):Ethernet2
What do you want to look at (config, state, counters): counters
Interface counters:
{
  "notification": [
    {
      "timestamp": 1761333180601018563,
      "prefix": null,
      "alias": null,
      "atomic": false,
      "update": [
        {
          "path": "interfaces/interface[name=Ethernet2]/state/counters",
          "val": {
            "openconfig-interfaces:carrier-transitions": "2",
            "openconfig-interfaces:in-broadcast-pkts": "0",
            "openconfig-interfaces:in-discards": "0",
            "openconfig-interfaces:in-errors": "0",
            "openconfig-interfaces:in-fcs-errors": "0",
            "openconfig-interfaces:in-multicast-pkts": "91662",
            "openconfig-interfaces:in-octets": "11932200",
            "openconfig-interfaces:in-pkts": "91974",
            "openconfig-interfaces:in-unicast-pkts": "312",
            "openconfig-interfaces:out-broadcast-pkts": "0",
            "openconfig-interfaces:out-discards": "0",
            "openconfig-interfaces:out-errors": "0",
            "openconfig-interfaces:out-multicast-pkts": "0",
            "openconfig-interfaces:out-octets": "0",
            "openconfig-interfaces:out-pkts": "0",
            "openconfig-interfaces:out-unicast-pkts": "0"
          }
        }
      ]
    }
  ]
}
```

The next script will change the interface description on ethernet1 of device clab-lab3-ceos1

Pre-change state

```
$ python get_intf_info_gnmi.py 
Enter target interface (example Ethernet1):Ethernet1
What do you want to look at (config, state, counters): state
Interface status:
{
  "notification": [
    {
      "timestamp": 1761333621770202036,
      "prefix": null,
      "alias": null,
      "atomic": false,
      "update": [
        {
          "path": "interfaces/interface[name=Ethernet1]/state",
          "val": {
            "openconfig-interfaces:admin-status": "UP",
            "openconfig-interfaces:counters": {
              "carrier-transitions": "4",
              "in-broadcast-pkts": "0",
              "in-discards": "0",
              "in-errors": "0",
              "in-fcs-errors": "0",
              "in-multicast-pkts": "91719",
              "in-octets": "124274196",
              "in-pkts": "1504460",
              "in-unicast-pkts": "1412741",
              "out-broadcast-pkts": "0",
              "out-discards": "0",
              "out-errors": "0",
              "out-multicast-pkts": "7",
              "out-octets": "518",
              "out-pkts": "7",
              "out-unicast-pkts": "0"
            },
            "openconfig-interfaces:description": "[add description]",       <---- Config will change this
            "openconfig-platform-port:hardware-port": "Ethernet1-Port",
            "openconfig-interfaces:ifindex": 1,
            "arista-intf-augments:inactive": false,
            "openconfig-interfaces:last-change": "1760731318246421813",
            "openconfig-interfaces:management": false,
            "openconfig-interfaces:mtu": 0,
            "openconfig-interfaces:name": "Ethernet1",
            "openconfig-interfaces:oper-status": "UP",
            "openconfig-platform-transceiver:transceiver": "Ethernet1",
            "openconfig-interfaces:type": "iana-if-type:ethernetCsmacd"
          }
        }
      ]
    }
  ]
}
```
Now run the set config script
```
$ python set_config_gnmi.py 
Set response:
{'timestamp': 1761333654396145219, 'prefix': None, 'response': [{'path': 'interfaces/interface[name=Ethernet1]/config/description', 'op': 'UPDATE'}]}
(lab_env) todd@todd-TOSHIBA-DX735:~/Code_folder/containerlab/containerlabs_sandbox/ceos_lab/lab3/scripts$ 
```
Post change state
```
$ python get_intf_info_gnmi.py 
Enter target interface (example Ethernet1):Ethernet1
What do you want to look at (config, state, counters): state
Interface status:
{
  "notification": [
    {
      "timestamp": 1761333678056116857,
      "prefix": null,
      "alias": null,
      "atomic": false,
      "update": [
        {
          "path": "interfaces/interface[name=Ethernet1]/state",
          "val": {
            "openconfig-interfaces:admin-status": "UP",
            "openconfig-interfaces:counters": {
              "carrier-transitions": "4",
              "in-broadcast-pkts": "0",
              "in-discards": "0",
              "in-errors": "0",
              "in-fcs-errors": "0",
              "in-multicast-pkts": "91727",
              "in-octets": "124285746",
              "in-pkts": "1504600",
              "in-unicast-pkts": "1412873",
              "out-broadcast-pkts": "0",
              "out-discards": "0",
              "out-errors": "0",
              "out-multicast-pkts": "7",
              "out-octets": "518",
              "out-pkts": "7",
              "out-unicast-pkts": "0"
            },
            "openconfig-interfaces:description": "connected to ceos2",     <------ Updated
            "openconfig-platform-port:hardware-port": "Ethernet1-Port",
            "openconfig-interfaces:ifindex": 1,
            "arista-intf-augments:inactive": false,
            "openconfig-interfaces:last-change": "1760731318246421813",
            "openconfig-interfaces:management": false,
            "openconfig-interfaces:mtu": 0,
            "openconfig-interfaces:name": "Ethernet1",
            "openconfig-interfaces:oper-status": "UP",
            "openconfig-platform-transceiver:transceiver": "Ethernet1",
            "openconfig-interfaces:type": "iana-if-type:ethernetCsmacd"
          }
        }
      ]
    }
  ]
}
```


