---
title: Filter Driver Buffer Management
description: Filter Driver Buffer Management
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

A filter driver that creates buffers to support send or receive operations must manage [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure pools and [**NET\_BUFFER**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer) structure pools.

To create these pools, drivers call the following functions:

[**NdisAllocateNetBufferListPool**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocatenetbufferlistpool)

[**NdisAllocateNetBufferPool**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocatenetbufferpool)

Filter drivers can use the following functions to allocate structures from the pools:

[**NdisAllocateNetBufferAndNetBufferList**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocatenetbufferandnetbufferlist)

[**NdisAllocateNetBufferList**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocatenetbufferlist)

[**NdisAllocateNetBuffer**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocatenetbuffer)

Calling **NdisAllocateNetBufferAndNetBufferList** is more efficient than calling **NdisAllocateNetBufferList** followed by **NdisAllocateNetBuffer**. However, **NdisAllocateNetBufferAndNetBufferList** only creates one NET\_BUFFER structure on the NET\_BUFFER\_LIST structure. To use **NdisAllocateNetBufferAndNetBufferList**, the driver must set the *AllocateNetBuffer* parameter to **TRUE** when it calls **NdisAllocateNetBufferListPool**.

Filter drivers that originate send requests should determine the context and backfill space requirements of the underlying drivers. Filter drivers use restart attributes to determine the backfill requirements of underlying drivers. A filter driver should determine the backfill and context requirements in the *Restarting* state. The driver should allocate sufficient backfill and context space for the entire stack. If necessary, a filter driver can free the pools and reallocate them in the *Restarting* state.

Filter drivers use the following functions to free the pools:

[**NdisFreeNetBufferListPool**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisfreenetbufferlistpool)

[**NdisFreeNetBufferPool**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisfreenetbufferpool)

Filter drivers use the following functions to free the structures allocated from the pools:

[**NdisFreeNetBufferList**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisfreenetbufferlist)

[**NdisFreeNetBuffer**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisfreenetbuffer)

Drivers should free NET\_BUFFER structures allocated with **NdisAllocateNetBuffer** before freeing the associated NET\_BUFFER\_LIST structure. NET\_BUFFER structures allocated with **NdisAllocateNetBufferAndNetBufferList** are freed when the driver calls **NdisFreeNetBufferList** for the associated NET\_BUFFER\_LIST structure.

 

