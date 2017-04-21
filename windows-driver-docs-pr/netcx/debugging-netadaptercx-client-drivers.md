---
title: Debugging NetAdapterCx Client Drivers
---

# Debugging NetAdapterCx Client Drivers

You can use [Windows Driver Framework Extensions (Wdfkd.dll)](https://msdn.microsoft.com/library/windows/hardware/ff551876) commands to debug your client driver.  In addition, `!ndiskd.netadapter` will show networking-specific properties of your adapter.

Also, you can use the `!ndiskd.netrb` debugger extension with the address of a [**NET_RING_BUFFER**](net-ring-buffer.md) structure to examine packets and fragments in a ring buffer.  This command gives you additional information, such as the number of elements in the ring buffer, along with the number of packets owned by the OS and the number of packets owned by the client.

The full list of !ndiskd commands related to NetAdapterCx:

- !ndiskd.cxadapter: Given a NETADAPTER handle, show information about a NETADAPTER object
- !ndiskd.netqueue: Given a NETTXQUEUE or NETRXQUEUE handle, show information about a data path queue.
- !ndiskd.netrb: Shows NET_RING_BUFFER information.
- !ndiskd.netpacket: Shows information about a NET_PACKET.
- !ndiskd.netpacketfragment: Shows information about a NET_PACKET_FRAGMENT