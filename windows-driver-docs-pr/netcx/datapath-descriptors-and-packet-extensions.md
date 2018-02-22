---
title: Datapath descriptors and packet extensions
description: Datapath descriptors and packet extensions
ms.assetid: 7B2357AE-F446-4AE8-A873-E13DF04D8D71
keywords:
- WDF Network Adapter Class Extension datapath descriptors and packet extensions, NetAdapterCx datapath descriptors, NetAdapterCx packet extensions
ms.author: windowsdriverdev
ms.date: 02/22/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Datapath descriptors and packet extensions

This topic introduces concepts underlying datapath descriptors and packet extensions in NetAdapterCx 1.2 and later.

## Overview

Datapath descriptors are small, runtime-extensible structures that describe a network packet. They can be used by different components in the system and are not limited in scope to specific APIs or header files. In NetAdapterCx, client drivers use datapath descriptors to interface with their datapath queue's ring buffers of packets and packet fragments. 

Packet extensions are attached to each datapath queue's core descriptor and are used by client drivers to share information with the upper layers. Packet extensions can hold information such as advanced offload tasks like checksum, LSO, and RSS hash, or they can hold application-specific details.

## History of datapath descriptors



Packet extensions in NetAdapterCx are analogous to the `NetBufferListInfo` array of values in the NDIS 6.*X* NET_BUFFER_LIST structure. That is, they contain information common to all the [NET_PACKET](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacket/ns-netpacket-_net_packet) structures in a datapath queue's ring buffer of packets. Unlike the array of PVOID pointers in a NET_BUFFER_LIST, however, packet extensions are arranged in memory as a flat block attached to the queue's core datapath descriptor. This makes them more CPU cache-friendly and offers several advantages:

1. 