# pyGNMI

These scripts are just testing the (show/get) commands, and the (set/config) commands. Upon much trial and error I found that I could manipulate interface settings but was unable to adjust routing parameters using pyGNMI. So from what I can tell this is not yet a full featured automation platform with Arista. There are limitations in the openconfig implementaion on the ceos-lab platform with regard to making routing changes with the read/write capabilites. Looks like its only read only at this time.  There are four main features with gNMI get, set, capabilites, and subscribe. I have yet to test subscribe functionality. Save that for another day...

So the first script shows how to pull or "get" data from the device(s)
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
Get devices capabilities - output cropped as its too verbose.
```
$ python get_intf_info_gnmi.py 
Enter host or hosts separated by ',': ceos1
Enter target interface (example Ethernet1):
What do you want to look at (config, state, counters, capabilities): capabilities
ceos1 capabilities:
{
  "supported_models": [
    {
      "name": "arista-srte-augments",
      "organization": "Arista Networks, Inc.",
      "version": "1.1.1"
    },
    {
      "name": "openconfig-platform",
      "organization": "OpenConfig working group",
      "version": "0.31.0"
    },
    {
      "name": "arista-isis-augments",
      "organization": "Arista Networks, Inc.",
      "version": "1.14.0"
    },
    {
      "name": "arista-exp-eos-l2protocolforwarding",
      "organization": "Arista Networks, Inc.",
      "version": "1.1.0"
    },
    {
      "name": "arista-vlan-augments",
      "organization": "Arista Networks <http://arista.com/>",
      "version": "1.1.2"
    },
    {
      "name": "arista-netinst-deviations",
      "organization": "Arista Networks, Inc.",
      "version": "1.4.0"
    },
<cropped>
    {
      "name": "arista-exp-eos-vxlan-config",
      "organization": "Arista Networks <http://arista.com/>",
      "version": "0.2.1"
    },
    {
      "name": "openconfig-ptp-types",
      "organization": "OpenConfig working group",
      "version": "1.0.0"
    }
  ],
  "supported_encodings": [
    "json",
    "json_ietf",
    "ascii"
  ],
  "gnmi_version": "0.7.0"
}

```

The set functionality will update or change configuration settings on a device.

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
Now run the set config script to update interface description
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
            "openconfig-interfaces:description": "[AVAILABLE FOR USE]", <-- Updated interface description
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
            "openconfig-interfaces:description": "[AVAILABLE FOR USE]", <-- Updated interface description
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
            "openconfig-interfaces:description": "[AVAILABLE FOR USE]", <-- Updated interface description
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


