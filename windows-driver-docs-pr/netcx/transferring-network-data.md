---
title: Transferring network data
description: Transferring network data
ms.assetid: D2AC8269-F2D5-4FDC-A59E-6A35DBB18FF0
keywords:
- NetAdapterCx transferring network data, NetCx transferring network data
ms.date: 06/05/2017
ms.localizationpriority: medium
---

# Transferring network data

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

To watch a video that introduces the data path model in NetAdapterCx, see the [Network Adapter Class Extension: Data Path](https://aka.ms/netadapter/video3) video on Channel 9.

In the NetAdapterCx model, network data is represented by packet descriptors and transferred through packet queues. The OS and the client driver transfer the packet descriptors to each other using a set of ring buffers associated with each packet queue.

The following topics explain in detail how to transfer network data in your NetAdapterCx client driver.

- [Packet descriptors and extensions](packet-descriptors-and-extensions.md)
- [Transmit and receive queues](transmit-and-receive-queues.md)
- [Using the Net Ring Iterator interface](using-the-net-ring-iterator-interface.md)
- [Network data buffer management](network-data-buffer-management.md)
