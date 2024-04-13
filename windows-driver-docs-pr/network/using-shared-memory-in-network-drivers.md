---
title: Using Shared Memory in Network Drivers
description: Using Shared Memory in Network Drivers
keywords:
- network drivers WDK , shared memory
- memory WDK networking
- shared memory WDK networking
- sharing memory address space
ms.date: 04/20/2017
---

# Using Shared Memory in Network Drivers





Miniport drivers for bus-master direct memory access (DMA) devices allocate shared memory for use by the network interface card (NIC) and the miniport driver.

[**NdisMAllocateSharedMemory**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismallocatesharedmemory) can be called by a bus-master miniport driver to allocate memory for permanent sharing between the network adapter and the miniport driver. This function returns a virtual address and a physical address for the shared memory. The addresses are valid until a call to [**NdisMFreeSharedMemory**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismfreesharedmemory) frees the memory.

 

