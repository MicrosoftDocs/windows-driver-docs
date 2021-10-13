---
title: Miniport Driver Buffer Management
description: Miniport Driver Buffer Management
keywords:
- buffers WDK NDIS miniport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Miniport Driver Buffer Management





Miniport drivers typically call [**NdisAllocateNetBufferListPool**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocatenetbufferlistpool) from [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) to create a pool of [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures. Miniport drivers use these structures to indicate received data.

Typically, a miniport driver that allocates a NET\_BUFFER\_LIST structure will allocate and queue one [**NET\_BUFFER**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer) structure on that NET\_BUFFER\_LIST structure. It is more efficient to preallocate NET\_BUFFER structures when you allocate a pool of NET\_BUFFER\_LIST structures than to allocate NET\_BUFFER\_LIST structures and NET\_BUFFER structures separately.

Miniport drivers can call **NdisAllocateNetBufferListPool** and set the *AllocateNetBuffer* parameter to **TRUE** to indicate that [**NET\_BUFFER**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer) structures are preallocated. In this case, a NET\_BUFFER structure is preallocated with each NET\_BUFFER\_LIST structure that the driver allocates from the pool. Such drivers must call [**NdisAllocateNetBufferAndNetBufferList**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocatenetbufferandnetbufferlist) to allocate structures from this pool.

Typically, a miniport driver calls **NdisAllocateNetBufferAndNetBufferList** from *MiniportInitializeEx* to allocate as many buffers as it will require for subsequent receive operations. In this case, the driver manages an internal list of free buffers.

The [*MiniportReturnNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_return_net_buffer_lists) function can prepare a returned NET\_BUFFER\_LIST structure for reuse in a subsequent receive indication. Although *MiniportReturnNetBufferLists* could return the NET\_BUFFER\_LIST structures to a pool (for example, it could call [**NdisFreeNetBufferList**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisfreenetbufferlist)), it can be more efficient to reuse the structures without returning them to the pool.

A miniport driver should free all the NET\_BUFFER\_LIST structures and associated data when NDIS halts the adapter. A driver can call **NdisFreeNetBufferList** to free the structures and the [**NdisFreeNetBufferListPool**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisfreenetbufferlistpool) function to free the NET\_BUFFER\_LIST pool.

 

