---
title: Protocol Driver Buffer Management
description: Protocol Driver Buffer Management
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Protocol Driver Buffer Management





A protocol driver must manage [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure pools and [**NET\_BUFFER**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer) structure pools for send operations. To create these pools, drivers call the following functions:

[**NdisAllocateNetBufferListPool**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocatenetbufferlistpool)

[**NdisAllocateNetBufferPool**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocatenetbufferpool)

Protocol drivers can use the following functions to allocate structures from the pools:

[**NdisAllocateNetBufferAndNetBufferList**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocatenetbufferandnetbufferlist)

[**NdisAllocateNetBufferList**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocatenetbufferlist)

[**NdisAllocateNetBuffer**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocatenetbuffer)

Calling **NdisAllocateNetBufferAndNetBufferList** is more efficient than calling **NdisAllocateNetBufferList** followed by **NdisAllocateNetBuffer**. However, **NdisAllocateNetBufferAndNetBufferList** only creates one NET\_BUFFER structure on the NET\_BUFFER\_LIST structure. To use **NdisAllocateNetBufferAndNetBufferList**, the driver must set the *AllocateNetBuffer* parameter to **TRUE** when it calls **NdisAllocateNetBufferListPool**.

Protocol drivers can use OID requests to query the back-fill and context space requirements of the underlying drivers. A protocol driver should determine the back-fill and context requirements for a binding in the *Opening* or *Restarting* states. The driver should allocate sufficient back-fill and context space for the entire stack. If necessary, a protocol driver can free the pools and reallocate them in the *Restarting* state.

Protocol drivers use the following functions to free the pools:

[**NdisFreeNetBufferListPool**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisfreenetbufferlistpool)

[**NdisFreeNetBufferPool**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisfreenetbufferpool).

Protocol drivers use the following functions to free the structures allocated from the pools:

[**NdisFreeNetBufferList**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisfreenetbufferlist)

[**NdisFreeNetBuffer**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisfreenetbuffer)

Drivers should free NET\_BUFFER structures allocated with **NdisAllocateNetBuffer** before freeing the associated NET\_BUFFER\_LIST structure. NET\_BUFFER structures allocated with **NdisAllocateNetBufferAndNetBufferList** are freed when the driver calls **NdisFreeNetBufferList** for the associated NET\_BUFFER\_LIST structure.

 

