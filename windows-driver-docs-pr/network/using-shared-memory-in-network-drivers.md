---
title: Using Shared Memory in Network Drivers
description: Using Shared Memory in Network Drivers
ms.assetid: f7dfe785-6c1a-4f56-9018-76be9cdec7fc
keywords:
- network drivers WDK , shared memory
- memory WDK networking
- shared memory WDK networking
- sharing memory address space
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Shared Memory in Network Drivers





Miniport drivers for bus-master direct memory access (DMA) devices allocate shared memory for use by the network interface card (NIC) and the miniport driver.

[**NdisMAllocateSharedMemory**](https://msdn.microsoft.com/library/windows/hardware/ff562782) can be called by a bus-master miniport driver to allocate memory for permanent sharing between the network adapter and the miniport driver. This function returns a virtual address and a physical address for the shared memory. The addresses are valid until a call to [**NdisMFreeSharedMemory**](https://msdn.microsoft.com/library/windows/hardware/ff563589) frees the memory.

 

 





