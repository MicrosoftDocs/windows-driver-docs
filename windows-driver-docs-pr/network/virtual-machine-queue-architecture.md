---
title: Virtual Machine Queue (VMQ) Overview
description: The NDIS virtual machine queue (VMQ) architecture provides several advantages for virtualization.
ms.date: 07/06/2022
---

# Virtual Machine Queue (VMQ) Overview

The NDIS Virtual Machine Queue (VMQ) interface supports Microsoft Hyper-V network performance improvements in NDIS 6.20 and later in Windows Server 2008 R2 and later versions of Windows Server.

The VMQ interface supports:

- Classification of received packets in network adapter hardware by using the destination media access control (MAC) address to route the packets to different receive queues.

- Shared memory; For more information see [NDIS Memory Management Interface](/windows-hardware/drivers/ddi/_netvista/).

- Scaling to multiple processors by processing packets for different virtual machines on different processors.

The NDIS VMQ architecture provides advantages for virtualization such as:

-   Virtualization impacts performance and VMQ helps overcome those effects.

-   VMQ supports live migration.

-   VMQ coexists with NDIS task offloads and other optimizations.

This section provides high-level information about the NDIS VMQ interface. You should read this section before writing an NDIS driver that supports VMQ.

For information about writing VMQ drivers, see [Writing VMQ Drivers](writing-vmq-drivers.md).

> [!NOTE]
> Be sure to study the [NDIS Virtual Miniport Driver sample](https://github.com/Microsoft/Windows-driver-samples/tree/main/network/ndis/netvmini/6x), especially the vmq.c and vmq.h source files.

This section includes the following topics:

[Introduction to NDIS Virtual Machine Queue (VMQ)](introduction-to-ndis-virtual-machine-queue--vmq-.md)

[VMQ Components](vmq-components.md)

[VMQ Receive Queues](vmq-receive-queues.md)

[VMQ Receive Filters](vmq-receive-filters.md)

[Security Issues with NDIS Virtual Machine (VM) Shared Memory](security-issues-with-ndis-virtual-machine--vm--shared-memory.md)

[NDIS VMQ Live Migration Support](ndis-vmq-live-migration-support.md)

[NDIS VM Queue States](ndis-virtual-machine-queue-states.md)

 

 
