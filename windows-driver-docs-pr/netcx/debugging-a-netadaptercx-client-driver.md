---
title: Debugging a NetAdapterCx client driver
description: Debugging a NetAdapterCx client driver
ms.assetid: EE8EA3DA-33E7-4EED-B991-38A21CAA699E
keywords:
- debugging NetAdapterCx client drivers, debugging NetAdapterCx client drivers
ms.date: 06/17/2020
ms.localizationpriority: medium
ms.custom: 19H1
---

# Debugging a NetAdapterCx client driver

You can use [Windows Driver Framework Extensions (Wdfkd.dll)](https://docs.microsoft.com/windows-hardware/drivers/debugger/kernel-mode-driver-framework-extensions--wdfkd-dll-) commands to debug your client driver.  In addition, [!ndiskd.netadapter](https://docs.microsoft.com/windows-hardware/drivers/debugger/-ndiskd-netadapter) will show networking-specific properties of your adapter.

Also, you can use the `!ndiskd.netrb` debugger extension with the address of a [**NET_RING**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netringbuffer/ns-netringbuffer-_NET_RING) structure to examine packets and fragments in a ring buffer.  This command gives you additional information, such as the number of elements in the ring buffer, along with the number of packets owned by the OS and the number of packets owned by the client.

You can use the following !ndiskd commands with a NetAdapterCx client driver:

*  [**!ndiskd.cxadapter**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-ndiskd-cxadapter)
    *  Given a NETADAPTER handle, show information about a NETADAPTER object.
*  [**!ndiskd.netqueue**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-ndiskd-netqueue)
    *  Given a NETTXQUEUE or NETRXQUEUE handle, show information about a data path queue.
*  [**!ndiskd.netrb**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-ndiskd-netrb)
    *  Shows [**NET_RING**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netringbuffer/ns-netringbuffer-_NET_RING) information.
*  [**!ndiskd.netpacket**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-ndiskd-netpacket)
    *  Shows information about a [**NET_PACKET**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netpacket/ns-netpacket-_net_packet).
*  [**!ndiskd.netfragment**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-ndiskd-netfragment)
    *  Shows information about a [**NET_PACKET_FRAGMENT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netpacket/ns-netpacket-_net_packet_fragment).
