---
title: VMQ Send and Receive Operations
description: VMQ Send and Receive Operations
ms.assetid: 11f07534-f715-4ed5-b312-652fb3c7e8bb
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# VMQ Send and Receive Operations


## <a href="" id="ddk-virtual-machine-queue-overview-nr"></a>


This section provides information about implementing send and receive operations in NDIS drivers that support VMQ.

To support VMQ send and receive operations, the VMQ interface requires network adapter hardware that supports the VMQ filter operations. These filters determine the assignment of packets to receive queues.

This section includes the following topics:

[VMQ Filter Operations](vmq-filter-operations.md)

[Shared Memory in Receive Buffers](shared-memory-in-receive-buffers.md)

[VMQ Receive Path](vmq-receive-path.md)

[VMQ Transmit Path](vmq-transmit-path.md)

 

 





