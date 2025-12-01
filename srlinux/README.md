# SR_Linux - notes

Links: 
- https://documentation.nokia.com/srlinux/
- https://yang.srlinux.dev/v25.10.1/tree
- https://learn.srlinux.dev/

These devices are built on yang models so in theory it will help me better understand model driven programmability.

SR Linux has a couple of interfaces you can use for programmability:
* json/rpc sever - Use requests library to interface with this server for device configuration and management.
* gRPC server- Uses gNMI for device configuration and telemetry

Lab set up to get familiar with the interface Cli, as well as the two programmabile interfaces:
 
 sw1 (rid 1.1.1.1) eth-1/1.0 (192.168.0.0/31) <----> (192.168.0.1/31) eth-1/1.0 (rid 2.2.2.2) sw2

json/rpc
- json_rpc/update_intf_description.py - update interface config
- json_rpc/enable_ospf.py - build the ospf
- json_rpc/get_info.py - validation code
```
List of things needed to get ospf adj built between the sw1 and sw2.
network-instance default
ospf version 2
ospf router id x.x.x.x
ospf instance default
ospf network point-to-point
admin enable ospf in network-instance default
admin enable ospf interface eth 1/1.0
```




