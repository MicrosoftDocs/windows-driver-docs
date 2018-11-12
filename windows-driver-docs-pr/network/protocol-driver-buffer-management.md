---
title: Protocol Driver Buffer Management
description: Protocol Driver Buffer Management
ms.assetid: 1f91b58e-d432-46c8-994e-d95c3aadfe43
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Protocol Driver Buffer Management





A protocol driver must manage [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure pools and [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure pools for send operations. To create these pools, drivers call the following functions:

[**NdisAllocateNetBufferListPool**](https://msdn.microsoft.com/library/windows/hardware/ff561611)

[**NdisAllocateNetBufferPool**](https://msdn.microsoft.com/library/windows/hardware/ff561613)

Protocol drivers can use the following functions to allocate structures from the pools:

[**NdisAllocateNetBufferAndNetBufferList**](https://msdn.microsoft.com/library/windows/hardware/ff561608)

[**NdisAllocateNetBufferList**](https://msdn.microsoft.com/library/windows/hardware/ff561609)

[**NdisAllocateNetBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff561607)

Calling **NdisAllocateNetBufferAndNetBufferList** is more efficient than calling **NdisAllocateNetBufferList** followed by **NdisAllocateNetBuffer**. However, **NdisAllocateNetBufferAndNetBufferList** only creates one NET\_BUFFER structure on the NET\_BUFFER\_LIST structure. To use **NdisAllocateNetBufferAndNetBufferList**, the driver must set the *AllocateNetBuffer* parameter to **TRUE** when it calls **NdisAllocateNetBufferListPool**.

Protocol drivers can use OID requests to query the back-fill and context space requirements of the underlying drivers. A protocol driver should determine the back-fill and context requirements for a binding in the *Opening* or *Restarting* states. The driver should allocate sufficient back-fill and context space for the entire stack. If necessary, a protocol driver can free the pools and reallocate them in the *Restarting* state.

Protocol drivers use the following functions to free the pools:

[**NdisFreeNetBufferListPool**](https://msdn.microsoft.com/library/windows/hardware/ff562590)

[**NdisFreeNetBufferPool**](https://msdn.microsoft.com/library/windows/hardware/ff562592).

Protocol drivers use the following functions to free the structures allocated from the pools:

[**NdisFreeNetBufferList**](https://msdn.microsoft.com/library/windows/hardware/ff562583)

[**NdisFreeNetBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff562582)

Drivers should free NET\_BUFFER structures allocated with **NdisAllocateNetBuffer** before freeing the associated NET\_BUFFER\_LIST structure. NET\_BUFFER structures allocated with **NdisAllocateNetBufferAndNetBufferList** are freed when the driver calls **NdisFreeNetBufferList** for the associated NET\_BUFFER\_LIST structure.

 

 





