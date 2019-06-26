---
title: Filter Driver Buffer Management
description: Filter Driver Buffer Management
ms.assetid: 92b38710-056d-4853-b266-ca86cee298b6
keywords:
- filter drivers WDK networking , buffers
- NDIS filter drivers WDK , buffers
- buffer management WDK NDIS filter
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filter Driver Buffer Management





Filter drivers create buffers to copy network data obtained from other drivers, or to initiate send or receive operations.

If a filter driver does not create buffers, the driver does not manage buffer pools. Such a driver simply passes on the buffers that it receives from other drivers.

A filter driver that creates buffers to support send or receive operations must manage [**NET\_BUFFER\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_net_buffer_list) structure pools and [**NET\_BUFFER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_net_buffer) structure pools.

To create these pools, drivers call the following functions:

[**NdisAllocateNetBufferListPool**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisallocatenetbufferlistpool)

[**NdisAllocateNetBufferPool**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisallocatenetbufferpool)

Filter drivers can use the following functions to allocate structures from the pools:

[**NdisAllocateNetBufferAndNetBufferList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisallocatenetbufferandnetbufferlist)

[**NdisAllocateNetBufferList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisallocatenetbufferlist)

[**NdisAllocateNetBuffer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisallocatenetbuffer)

Calling **NdisAllocateNetBufferAndNetBufferList** is more efficient than calling **NdisAllocateNetBufferList** followed by **NdisAllocateNetBuffer**. However, **NdisAllocateNetBufferAndNetBufferList** only creates one NET\_BUFFER structure on the NET\_BUFFER\_LIST structure. To use **NdisAllocateNetBufferAndNetBufferList**, the driver must set the *AllocateNetBuffer* parameter to **TRUE** when it calls **NdisAllocateNetBufferListPool**.

Filter drivers that originate send requests should determine the context and backfill space requirements of the underlying drivers. Filter drivers use restart attributes to determine the backfill requirements of underlying drivers. A filter driver should determine the backfill and context requirements in the *Restarting* state. The driver should allocate sufficient backfill and context space for the entire stack. If necessary, a filter driver can free the pools and reallocate them in the *Restarting* state.

Filter drivers use the following functions to free the pools:

[**NdisFreeNetBufferListPool**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisfreenetbufferlistpool)

[**NdisFreeNetBufferPool**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisfreenetbufferpool)

Filter drivers use the following functions to free the structures allocated from the pools:

[**NdisFreeNetBufferList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisfreenetbufferlist)

[**NdisFreeNetBuffer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisfreenetbuffer)

Drivers should free NET\_BUFFER structures allocated with **NdisAllocateNetBuffer** before freeing the associated NET\_BUFFER\_LIST structure. NET\_BUFFER structures allocated with **NdisAllocateNetBufferAndNetBufferList** are freed when the driver calls **NdisFreeNetBufferList** for the associated NET\_BUFFER\_LIST structure.

 

 





