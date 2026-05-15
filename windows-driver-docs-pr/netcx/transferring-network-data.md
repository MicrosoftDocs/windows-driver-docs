---
title: Introduction to the NetAdapterCx data path
description: Introduction to the NetAdapterCx data path
keywords:
- NetAdapterCx transferring network data, NetCx transferring network data
ms.date: 12/09/2022
ms.custom: 19H1
ms.topic: concept-article
---

# Introduction to the NetAdapterCx data path

In the NetAdapterCx model, network data is represented by packet descriptors and transferred through packet queues. The OS and the client driver transfer the packet descriptors to each other using a set of ring buffers associated with each packet queue.

The following video [Network Adapter Class Extension: Data Path](https://learn-video.azurefd.net/vod/player?id=cdb34b61-1a38-41a3-a6f1-8245cb73a179) introduces the data path model in NetAdapterCx.
> [!VIDEO https://learn-video.azurefd.net/vod/player?id=cdb34b61-1a38-41a3-a6f1-8245cb73a179]

The following topics explain in detail how to transfer network data in your NetAdapterCx client driver.

- [Packet descriptors and extensions](packet-descriptors-and-extensions.md)
- [Transmit and receive queues](transmit-and-receive-queues.md)
- [Introduction to net rings](introduction-to-net-rings.md)
- [Network data buffer management](network-data-buffer-management.md)
- [Introduction to hardware offloads](introduction-to-hardware-offloads.md)
