---
title: Virtual Machine Queue (VMQ)
description: Virtual Machine Queue (VMQ)
ms.assetid: c502c7d6-bdf1-4656-b5a5-339250910f08
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Virtual Machine Queue (VMQ)





This section describes the NDIS virtual machine queue (VMQ) interface. The VMQ interface supports Microsoft Hyper-V network performance improvements in NDIS 6.20 and later in Windows Server 2008 R2 and later versions of Windows Server.

The [Virtual Machine Queue Architecture](virtual-machine-queue-architecture.md) documentation describes the high-level concepts of the VMQ architecture. The [Writing VMQ Drivers](writing-vmq-drivers.md) documentation provides the more detailed information about writing NDIS VMQ drivers.

**Note**  Be sure to study the [NDIS Virtual Miniport Driver sample](http://go.microsoft.com/fwlink/p/?LinkId=617918), especially the vmq.c and vmq.h source files.

 

The VMQ interface supports:

-   Classification of received packets in network adapter hardware by using the destination media access control (MAC) address to route the packets to different receive queues.

-   NIC ability to use DMA to transfer packets directly to a virtual machine's shared memory. For more information about shared memory, see [NDIS Memory Management Interface](https://msdn.microsoft.com/library/windows/hardware/ff564749).

-   Scaling to multiple processors by processing packets for different virtual machines on different processors.

This section includes the following topics:

-   [Virtual Machine Queue Architecture](virtual-machine-queue-architecture.md)
-   [Writing VMQ Drivers](writing-vmq-drivers.md)

 

 





