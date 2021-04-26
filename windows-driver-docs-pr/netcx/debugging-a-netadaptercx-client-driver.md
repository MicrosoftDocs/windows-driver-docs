---
title: Debugging a NetAdapterCx client driver
description: Debugging a NetAdapterCx client driver
keywords:
- debugging NetAdapterCx client drivers, debugging NetAdapterCx client drivers
ms.date: 06/17/2020
ms.localizationpriority: medium
ms.custom: 19H1
---

# Debugging a NetAdapterCx client driver

You can use [Windows Driver Framework Extensions (Wdfkd.dll)](../debugger/kernel-mode-driver-framework-extensions--wdfkd-dll-.md) commands to debug your client driver.  In addition, [!ndiskd.netadapter](../debugger/-ndiskd-netadapter.md) will show networking-specific properties of your adapter.

Also, you can use the `!ndiskd.netrb` debugger extension with the address of a [**NET_RING**](/windows-hardware/drivers/ddi/ring/ns-ring-_net_ring) structure to examine packets and fragments in a ring buffer.  This command gives you additional information, such as the number of elements in the ring buffer, along with the number of packets owned by the OS and the number of packets owned by the client.

You can use the following !ndiskd commands with a NetAdapterCx client driver:

*  [**!ndiskd.cxadapter**](../debugger/-ndiskd-cxadapter.md)
    *  Given a NETADAPTER handle, show information about a NETADAPTER object.
*  [**!ndiskd.netqueue**](../debugger/-ndiskd-netqueue.md)
    *  Given a NETTXQUEUE or NETRXQUEUE handle, show information about a data path queue.
*  [**!ndiskd.netrb**](../debugger/-ndiskd-netrb.md)
    *  Shows [**NET_RING**](/windows-hardware/drivers/ddi/ring/ns-ring-_net_ring) information.
*  [**!ndiskd.netpacket**](../debugger/-ndiskd-netpacket.md)
    *  Shows information about a [**NET_PACKET**](/windows-hardware/drivers/ddi/netpacket/ns-netpacket-_net_packet).
*  [**!ndiskd.netfragment**](../debugger/-ndiskd-netfragment.md)
    *  Shows information about a [**NET_PACKET_FRAGMENT**](/windows-hardware/drivers/ddi/netpacket/ns-netpacket-_net_packet_fragment).
