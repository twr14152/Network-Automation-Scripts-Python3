# SR_linux - notes

These devices are built on yang models so in theory it will help me better understand model driven programmability.

So from a maanagement standpoint json/rpc server and gRPC server are options a couple of automation options

Lab set up to get familiar with cli and json rpc is two instances of srlinux connected as such:
 
 sw1 (rid 1.1.1.1) eth-1/1.0 (192.168.0.0/31) <----> (192.168.0.1/31) eth-1/1.0 (rid 2.2.2.2) sw2

- json-rpc/enable_ospf.py
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




