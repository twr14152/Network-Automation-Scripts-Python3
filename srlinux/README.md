# SR_linux

These devices are supposedly built on Yang models so in theory it will help me better understand model driven programmability.

These devices can be managed by Cli or through RPCs:
  * gRPC server
    * gNMI
    * gNOI
  * json/rpc server

So I have gotten json/rpc to work. I've gotten some ospf and interface configurations to apply.  I have been unsuccessful getting ospf to establish a simple adjacency.
The documentation on json/rpc is not bad. However the path formats are wierd and require some trial and error to get correct (ie... reading the error messages make it pretty clear whats wrong).

