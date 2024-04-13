---
title: NetAdapterCx hardware offloads
description: Overview of hardware offloads in NetAdapterCx
keywords:
- WDF Network Adapter Class Extension Offloads, NetAdapterCx hardware offloads, NetAdapterCx Offloads, NetAdapter Offloads
ms.date: 10/09/2020
ms.custom: Fe
---

# Introduction to NetAdapterCx hardware offloads

To increase its performance, the Windows TCP/IP stack can offload some tasks to a network interface card (NIC) that has the appropriate task offload capabilities.

NetAdapterCx focuses on ease of offload configuration and management of offload capabilities. Client drivers only need to specify a simple configuration for their hardware offload capabilities and register callbacks to be notified of changes in capabilities. 

This guidance provides an overview of key concepts for hardware offloads in NetAdapterCx.

- Hardware offload capabilities are advertised by the network adapter hardware during initialization and must be advertised before calling [**NetAdapterStart**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterstart).
- The driver doesn't need to check standard registry keywords. NetAdapterCx checks the registry keywords and honors them when enabling the active offload capabilities.
- The *active* offload capabilities of the network adapter are those that the network adapter is currently programmed to perform. These are a subset of the hardware capabilities advertised by the client driver previously.
- The TCP/IP stack or an overlying protocol driver can request a change in active capabilities of the network adapter. Client drivers register callbacks with NetAdapterCx to be notified of changes in the active offload capabilities.
- If a packet extension is needed for an offload, it is automatically registered when the network adapter advertises support for the hardware offload.

Client drivers advertise a granular set of capabilities to NetAdapterCx for the network packet types their hardware can offload. For example, this can be whether IPv4 Options, IPv6 Extensions, TCP Options or any combinations of such are supported, etc. Certain hardware can only perform offload if the packet header offset is known, and the client driver of such hardware can also specify its limit on packet header offset. For example, if the hardware descriptor has only 8 bits to store layer 4 header offset, the client driver would set the Layer4HeaderOffset to 255. Any packets which are not covered by the client driver’s capabilities will be offloaded in software by NetAdapterCx.

If the hardware is not capable of handling a specific combination, the client driver should neither declare support for that capability nor perform a software fallback itself when it encounters such a packet. Instead, it should let NetAdapterCx to perform any necessary software fallback automatically.

> [!NOTE]
> If you would like NetAdapterCx to perform software fallback for offloads that are not supported by the hardware, the client driver must include the standardized keywords for that offload in the INF file. For example, if a client driver cannot perform RSC offload at all in hardware and needs NetAdapterCx to perform this offload in software, the *RscIpv4 and *RscIpv6 keywords must be included in the INF.

The following offloads are supported by NetAdapterCx and the Windows TCP/IP stack:

| Offload name | Description |
| --- | --- |
| [Checksum](checksum-offload.md) | Offloading the calculation and validation of IP and TCP checksums to the NIC. |
| [Generic send offload (GSO)](gso-offload.md) | Offloading segmentation of large TCP/UDP packets for IPv4 and IPv6. |
| [Receive Segment Coalescing (RSC)](rsc-offload.md) | Offloading coalescing of a sequence of received TCP segments for IPv4 and IPv6. |

For more information on configuring offloads and updating offloads when the TCP/IP stack or an overlying protocol driver requests a change to the net adapter's active capabilities, visit the corresponding offload reference page.