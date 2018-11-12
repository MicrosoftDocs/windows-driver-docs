---
title: Allocating Network Data Pools in an NDIS 6.0 Miniport Driver
description: Allocating Network Data Pools in an NDIS 6.0 Miniport Driver
ms.assetid: 80afe825-208f-4c21-b53f-32506bee9177
keywords:
- pools WDK networking
- data pools WDK networking
- network data pools WDK networking
- allocating data pools
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Allocating Network Data Pools in an NDIS 6.0 Miniport Driver





Before sending and receiving [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) and [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures, the miniport driver must allocate a NET\_BUFFER pool and a NET\_BUFFER\_LIST pool. NDIS 6.0 drivers do not allocate packet pools with the [**NdisAllocatePacketPool**](https://msdn.microsoft.com/library/windows/hardware/ff550780) function. To allocate a pool, NDIS 6.0 miniport drivers call the [**NdisAllocateNetBufferListPool**](https://msdn.microsoft.com/library/windows/hardware/ff561611) and [**NdisAllocateNetBufferPool**](https://msdn.microsoft.com/library/windows/hardware/ff561613) functions.

Each NET\_BUFFER\_LIST structure that the driver uses to indicate received network data has at least one associated NET\_BUFFER structure. A driver that indicates received data should therefore allocate a NET\_BUFFER\_LIST pool with a pre-allocated NET\_BUFFER in each NET\_BUFFER\_LIST. To create such a pool, call the **NdisAllocateNetBufferListPool** function with the **fAllocateNetBuffer** member of the [**NET\_BUFFER\_LIST\_POOL\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh205394) structure set to **TRUE**.

The miniport driver's [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) function should call the [**NdisFreeNetBufferListPool**](https://msdn.microsoft.com/library/windows/hardware/ff562590) and [**NdisFreeNetBufferPool**](https://msdn.microsoft.com/library/windows/hardware/ff562592) functions to free the NET\_BUFFER\_LIST and NET\_BUFFER pools, respectively. These functions replace the [**NdisFreePacketPool**](https://msdn.microsoft.com/library/windows/hardware/ff551995) function. The driver passes these functions the pool handle that the associated allocation functions returned.

For more information about NDIS 6.0 data buffer management, see [Miniport Driver Buffer Management](miniport-driver-buffer-management.md).

 

 





