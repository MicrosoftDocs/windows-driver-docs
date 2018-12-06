---
title: Virtual Machine Queue (VMQ) in NDIS 6.20
description: Virtual Machine Queue (VMQ) in NDIS 6.20
ms.assetid: fb48b019-4646-426d-b10e-d760788f9985
keywords:
- NDIS 6.20 WDK , virtual machine queue (VMQ)
- virtual machine queue (VMQ) WDK NDIS 6.20
- VMQ WDK NDIS 6.20
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Virtual Machine Queue (VMQ) in NDIS 6.20





NDIS 6.20 introduces the virtual machine queue (VMQ) interface to support Microsoft Hyper-V network performance improvements. NDIS 6.20 and later drivers must provide information about VMQ capabilities during initialization. However, VMQ support is optional.

The VMQ interface in NDIS 6.20 and later supports:

-   Classification of received packets by using the destination MAC address to route the packets to different receive queues.

-   NIC ability to use DMA to transfer packets directly to a Hyper-V child partition's shared memory.

-   Scaling to multiple processors by processing packets for different Hyper-V partitions on different processors.

Microsoft Hyper-V network performance enhancements also provide chimney support for Hyper-V child partitions with no driver changes.

For more information about VMQ, see [Virtual Machine Queue (VMQ)](virtual-machine-queue--vmq-.md).

 

 





