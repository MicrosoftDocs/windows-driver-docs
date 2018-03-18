---
title: Transferring network data
description: Transferring network data
ms.assetid: D2AC8269-F2D5-4FDC-A59E-6A35DBB18FF0
keywords:
- NetAdapterCx transferring network data, NetCx transferring network data
ms.author: windowsdriverdev
ms.date: 06/05/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Transferring network data

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

To watch a video that introduces the data path model in NetAdapterCx, see the [Network Adapter Class Extension: Data Path](https://aka.ms/netadapter/video3) video on Channel 9.

In the NetAdapterCx model, network data requests are stored in WDF queues. Each queue is associated with a ring buffer, which contains a group of packets and pointers to indicate where in the ring to read and write next.

The following topics explain how to transfer network data in your NetAdapterCx client driver.

- [Transmit and receive queues](transmit-and-receive-queues.md)
- [Datapath descriptors, packet descriptors, and packet extensions](datapath-descriptors-packet-descriptors-and-packet-extensions.md)
- [Using the ring buffer](using-the-ring-buffer.md)
- [Network data buffer management](network-data-buffer-management.md)
