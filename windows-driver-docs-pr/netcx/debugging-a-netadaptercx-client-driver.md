---
title: Debugging a NetAdapterCx client driver
description: Debugging a NetAdapterCx client driver
ms.assetid: EE8EA3DA-33E7-4EED-B991-38A21CAA699E
keywords:
- debugging NetAdapterCx client drivers, debugging NetAdapterCx client drivers
ms.date: 06/05/2017
ms.localizationpriority: medium
---

# Debugging a NetAdapterCx client driver

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

You can use [Windows Driver Framework Extensions (Wdfkd.dll)](https://msdn.microsoft.com/library/windows/hardware/ff551876) commands to debug your client driver.  In addition, [!ndiskd.netadapter](https://msdn.microsoft.com/library/windows/hardware/mt799821) will show networking-specific properties of your adapter.

Also, you can use the `!ndiskd.netrb` debugger extension with the address of a [**NET_RING_BUFFER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netringbuffer/ns-netringbuffer-_net_ring_buffer) structure to examine packets and fragments in a ring buffer.  This command gives you additional information, such as the number of elements in the ring buffer, along with the number of packets owned by the OS and the number of packets owned by the client.

You can use the following !ndiskd commands with a NetAdapterCx client driver:

*  [**!ndiskd.cxadapter**](https://msdn.microsoft.com/library/windows/hardware/mt808786)
    *  Given a NETADAPTER handle, show information about a NETADAPTER object.
*  [**!ndiskd.netqueue**](https://msdn.microsoft.com/library/windows/hardware/mt808789)
    *  Given a NETTXQUEUE or NETRXQUEUE handle, show information about a data path queue.
*  [**!ndiskd.netrb**](https://msdn.microsoft.com/library/windows/hardware/mt808790)
    *  Shows [**NET_RING_BUFFER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netringbuffer/ns-netringbuffer-_net_ring_buffer) information.
*  [**!ndiskd.netpacket**](https://msdn.microsoft.com/library/windows/hardware/mt808787)
    *  Shows information about a [**NET_PACKET**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacket/ns-netpacket-_net_packet).
*  [**!ndiskd.netpacketfragment**](https://msdn.microsoft.com/library/windows/hardware/mt808788)
    *  Shows information about a [**NET_PACKET_FRAGMENT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacket/ns-netpacket-_net_packet_fragment).
