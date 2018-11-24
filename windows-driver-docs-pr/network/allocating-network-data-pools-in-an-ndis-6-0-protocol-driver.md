---
title: Allocating Network Data Pools in an NDIS 6.0 Protocol Driver
description: Allocating Network Data Pools in an NDIS 6.0 Protocol Driver
ms.assetid: 50ab57ef-f07e-473e-a55f-fd8bbd26730e
keywords:
- pools WDK networking
- data pools WDK networking
- network data pools WDK networking
- allocating data pools
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Allocating Network Data Pools in an NDIS 6.0 Protocol Driver





NDIS 6.0 drivers do not allocate packet pools by calling the [**NdisAllocatePacketPool**](https://msdn.microsoft.com/library/windows/hardware/ff550780) function, nor do they use [**NDIS\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff557086) structures. Instead, before sending and receiving [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) and [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures, the protocol driver must allocate a NET\_BUFFER pool and a NET\_BUFFER\_LIST pool. To allocate pools, NDIS 6.0 protocol drivers call the [**NdisAllocateNetBufferListPool**](https://msdn.microsoft.com/library/windows/hardware/ff561611) and [**NdisAllocateNetBufferPool**](https://msdn.microsoft.com/library/windows/hardware/ff561613) functions.

Each NET\_BUFFER\_LIST structure that a protocol driver uses to send network data has at least one associated NET\_BUFFER structure. A driver should therefore allocate a NET\_BUFFER\_LIST pool with a preallocated NET\_BUFFER in each NET\_BUFFER\_LIST. To create such a pool, call the **NdisAllocateNetBufferListPool** function with the **fAllocateNetBuffer** member of the [**NET\_BUFFER\_LIST\_POOL\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh205394) structure set to **TRUE**.

The protocol driver's [*ProtocolUnbindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570278) function should call the [**NdisFreeNetBufferListPool**](https://msdn.microsoft.com/library/windows/hardware/ff562590) and [**NdisFreeNetBufferPool**](https://msdn.microsoft.com/library/windows/hardware/ff562592) functions to free the NET\_BUFFER\_LIST and NET\_BUFFER pools, respectively. These functions replace the [**NdisFreePacketPool**](https://msdn.microsoft.com/library/windows/hardware/ff551995) function. The driver passes these functions the pool handle that the associated allocation functions returned.

Before freeing these pools, the driver should ensure that all outstanding send operations are complete and free all of the structures that were allocated from the pools.

For more information about NDIS 6.0 data buffer management, see [Protocol Driver Buffer Management](protocol-driver-buffer-management.md).

 

 





