# pyGNMI

These scripts are just testing the (show/get) commands, and the (set/config) commands. Upon much trial and error I found that I could manipulate interface settings but was unable to adjust routing parameters using pyGNMI. So from what I can tell this is not yet a fill featured automation platform yet. Limitations with arista using openconfig read/write capabilites. A common problem amoungst vendors. So gNMI has 4 main features get, set, capabilites, and subscribe. I have yet to test subscribe functionality. Save that for another day...

So the first script shows how to pull data from the device(s)
```
$ python  get_intf_info_gnmi.py 
Enter host or hosts separated by ',': ceos1, ceos2, ceos3
Enter target interface (example Ethernet1):Loopback20
What do you want to look at (config, state, counters, capabilities): config
ceos1 interface configuration:
{
  "notification": [
    {
      "timestamp": 1761488757456086353,
      "prefix": null,
      "alias": null,
      "atomic": false,
      "update": [
        {
          "path": "interfaces/interface[name=Loopback20]/config",
          "val": {
            "openconfig-interfaces:description": "testing gNMI automation",
            "openconfig-interfaces:loopback-mode": "FACILITY",
            "openconfig-interfaces:name": "Loopback20",
            "openconfig-interfaces:type": "iana-if-type:softwareLoopback"
          }
        }
      ]
    }
  ]
}
ceos2 interface configuration:
{
  "notification": [
    {
      "timestamp": 1761488757903808509,
      "prefix": null,
      "alias": null,
      "atomic": false,
      "update": [
        {
          "path": "interfaces/interface[name=Loopback20]/config",
          "val": {
            "openconfig-interfaces:description": "testing gNMI automation",
            "openconfig-interfaces:loopback-mode": "FACILITY",
            "openconfig-interfaces:name": "Loopback20",
            "openconfig-interfaces:type": "iana-if-type:softwareLoopback"
          }
        }
      ]
    }
  ]
}
ceos3 interface configuration:
{
  "notification": [
    {
      "timestamp": 1761488758130981701,
      "prefix": null,
      "alias": null,
      "atomic": false,
      "update": [
        {
          "path": "interfaces/interface[name=Loopback20]/config",
          "val": {
            "openconfig-interfaces:description": "testing gNMI automation",
            "openconfig-interfaces:loopback-mode": "FACILITY",
            "openconfig-interfaces:name": "Loopback20",
            "openconfig-interfaces:type": "iana-if-type:softwareLoopback"
          }
        }
      ]
    }
  ]
}
$ cat get_intf_info_gnmi.py 
```
Gathering config, state, and counters examples. **The script was updated for multi device operation.
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
$ python  get_intf_info_gnmi.py 
Enter host or hosts separated by ',': ceos1, ceos2, ceos3
Enter target interface (example Ethernet1):Loopback20
What do you want to look at (config, state, counters, capabilities): config
ceos1 interface configuration:
{
  "notification": [
    {
      "timestamp": 1761488757456086353,
      "prefix": null,
      "alias": null,
      "atomic": false,
      "update": [
        {
          "path": "interfaces/interface[name=Loopback20]/config",
          "val": {
            "openconfig-interfaces:description": "testing gNMI automation",
            "openconfig-interfaces:loopback-mode": "FACILITY",
            "openconfig-interfaces:name": "Loopback20",
            "openconfig-interfaces:type": "iana-if-type:softwareLoopback"
          }
        }
      ]
    }
  ]
}
ceos2 interface configuration:
{
  "notification": [
    {
      "timestamp": 1761488757903808509,
      "prefix": null,
      "alias": null,
      "atomic": false,
      "update": [
        {
          "path": "interfaces/interface[name=Loopback20]/config",
          "val": {
            "openconfig-interfaces:description": "testing gNMI automation",
            "openconfig-interfaces:loopback-mode": "FACILITY",
            "openconfig-interfaces:name": "Loopback20",
            "openconfig-interfaces:type": "iana-if-type:softwareLoopback"
          }
        }
      ]
    }
  ]
}
ceos3 interface configuration:
{
  "notification": [
    {
      "timestamp": 1761488758130981701,
      "prefix": null,
      "alias": null,
      "atomic": false,
      "update": [
        {
          "path": "interfaces/interface[name=Loopback20]/config",
          "val": {
            "openconfig-interfaces:description": "testing gNMI automation",
            "openconfig-interfaces:loopback-mode": "FACILITY",
            "openconfig-interfaces:name": "Loopback20",
            "openconfig-interfaces:type": "iana-if-type:softwareLoopback"
          }
        }
      ]
    }
  ]
}
```
Now run the set config script
```
$ python set_intf_description_gnmi.py 
Enter host or hosts separated by ',': ceos1, ceos2, ceos3
Add/Change interface description
Enter interface: Loopback20
Enter interface description: [AVAILABLE FOR USE]
Set response:
{'timestamp': 1761489678288634591, 'prefix': None, 'response': [{'path': 'interfaces/interface[name=Loopback20]/config/description', 'op': 'UPDATE'}]}
Add/Change interface description
Enter interface: Loopback20
Enter interface description: [AVAILABLE FOR USE]
Set response:
{'timestamp': 1761489694003906084, 'prefix': None, 'response': [{'path': 'interfaces/interface[name=Loopback20]/config/description', 'op': 'UPDATE'}]}
Add/Change interface description
Enter interface: Loopback20
Enter interface description: [AVAILABLE FOR USE]
Set response:
{'timestamp': 1761489702607996402, 'prefix': None, 'response': [{'path': 'interfaces/interface[name=Loopback20]/config/description', 'op': 'UPDATE'}]}

```
Post change state
```
$ python get_intf_info_gnmi.py 
Enter host or hosts separated by ',': ceos1, ceos2, ceos3
Enter target interface (example Ethernet1):Loopback20
What do you want to look at (config, state, counters, capabilities): config
ceos1 interface configuration:
{
  "notification": [
    {
      "timestamp": 1761489978636707639,
      "prefix": null,
      "alias": null,
      "atomic": false,
      "update": [
        {
          "path": "interfaces/interface[name=Loopback20]/config",
          "val": {
            "openconfig-interfaces:description": "[AVAILABLE FOR USE]",
            "openconfig-interfaces:loopback-mode": "FACILITY",
            "openconfig-interfaces:name": "Loopback20",
            "openconfig-interfaces:type": "iana-if-type:softwareLoopback"
          }
        }
      ]
    }
  ]
}
ceos2 interface configuration:
{
  "notification": [
    {
      "timestamp": 1761489979073277396,
      "prefix": null,
      "alias": null,
      "atomic": false,
      "update": [
        {
          "path": "interfaces/interface[name=Loopback20]/config",
          "val": {
            "openconfig-interfaces:description": "[AVAILABLE FOR USE]",
            "openconfig-interfaces:loopback-mode": "FACILITY",
            "openconfig-interfaces:name": "Loopback20",
            "openconfig-interfaces:type": "iana-if-type:softwareLoopback"
          }
        }
      ]
    }
  ]
}
ceos3 interface configuration:
{
  "notification": [
    {
      "timestamp": 1761489979287548846,
      "prefix": null,
      "alias": null,
      "atomic": false,
      "update": [
        {
          "path": "interfaces/interface[name=Loopback20]/config",
          "val": {
            "openconfig-interfaces:description": "[AVAILABLE FOR USE]",
            "openconfig-interfaces:loopback-mode": "FACILITY",
            "openconfig-interfaces:name": "Loopback20",
            "openconfig-interfaces:type": "iana-if-type:softwareLoopback"
          }
        }
      ]
    }
  ]
}

```


