---
title: NetAdapterCx Offloads
description: NetAdapterCx offloads
ms.assetid: 85A819E2-6352-4DE9-9689-3DCEB9B0AAD8
keywords:
- WDF Network Adapter Class Extension Offloads, NetAdapterCx hardware offloads, NetAdapterCx Offloads, NetAdapter Offloads
ms.author: windowsdriverdev
ms.date: 07/15/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NetAdapterCx offloads

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

To increase its performance, the Microsoft TCP/IP transport can offload tasks to a network interface card (NIC) that has the appropriate task offload capabilities.

## Overview of Offloads in NetAdapterCx

NetAdapterCx focuses on ease of offload configuration and management of offload capabilities. The client drivers need to specify a simple configuration of their hardware offload capabilities and register callbacks to be notified of changes in capabilities.

1. The hardware offload capabilities are advertised by the network adapter during initialization.These specify the capabilities supported in the hardware of Network Adapter.
2. The driver doesn't need to worry about checking the Standard registry keywords. NetAdapterCx would check the registry keywords and honor them when enabling the active offload capabilities.
3. The active offload capabilities of the network adapter are the offload capabilities that the network adapter is currently programmed to perform. These would be a subset of the hardware capabilities advertized by the Client driver earlier.
4. The TCP/IP stack or an overlying protocol driver can request for change in active capabilities of the Network Adapter. Client drivers register callbacks with NetAdapterCx to be notified of changes in the active offload capabilities.
5. If a packet extension is needed for an offload, it is automatically registered when the network adapter advertises support for the hardware offload.
6. The hardware capabilities need to be advertized before calling Adapter Start.
7. Granular capabilities for offload are not specified. The client driver instead uses a software fallback for a granular capability that is not supported.


The client driver will advertise minimum set of capabilities to NetAdapterCx. These would not include the granular capability details of all the combinations supported by client driver. Ex: Whether IPOptions, IPExtensions or TCPOptions are supported etc. 
This would mean that the client driver is responsible to perform the offload on all combinations of an advertised capability i.e. support for IPv4 implies support for IPOptions, support for IPv6 implies support for IPExtensions and support for TCP implies support for TCPOptions. If the hardware is not capable of handling a specific combination, it should either not declare support for that capability or perform a software fallback when encountered with such a packet. NetAdapterCx will provide software fallbacks for most of the offloads. The client drivers can leverage these software fallbacks instead of writing their own.


The following offloads are supported in NetAdapterCx

- [Checksum](netadaptercx-checksum-offload.md)
- [Large Send Offload](netadaptercx-large-send-offload.md)
