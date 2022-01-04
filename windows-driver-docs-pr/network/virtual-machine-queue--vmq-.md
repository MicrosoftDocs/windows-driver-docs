---
title: Virtual Machine Queue (VMQ) Overview
description: Virtual Machine Queue (VMQ) Overview
ms.date: 11/30/2021
ms.custom: contperf-fy22q2
---

# Virtual Machine Queue (VMQ) Overview

The NDIS Virtual Machine Queue (VMQ) interface supports Microsoft Hyper-V network performance improvements in NDIS 6.20 and later in Windows Server 2008 R2 and later versions of Windows Server.

- [Virtual Machine Queue Architecture](virtual-machine-queue-architecture.md) describes the high-level concepts of the VMQ architecture.

- [Writing VMQ Drivers](writing-vmq-drivers.md) provides more detailed information about writing NDIS VMQ drivers.

> [!NOTE]
> Be sure to study the [NDIS Virtual Miniport Driver sample](https://github.com/Microsoft/Windows-driver-samples/tree/master/network/ndis/netvmini/6x), especially the vmq.c and vmq.h source files.

The VMQ interface supports:

- Classification of received packets in network adapter hardware by using the destination media access control (MAC) address to route the packets to different receive queues.

- Shared memory; For more information see [NDIS Memory Management Interface](/windows-hardware/drivers/ddi/_netvista/).

- Scaling to multiple processors by processing packets for different virtual machines on different processors.

## Related Topics

- [Virtual Machine Queue Architecture](virtual-machine-queue-architecture.md)
- [Writing VMQ Drivers](writing-vmq-drivers.md)
