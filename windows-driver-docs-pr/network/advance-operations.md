---
title: Advance Operations
description: Advance Operations
ms.assetid: 42554221-201d-4014-900d-435a47b3afa1
keywords:
- network data WDK , advance operations
- data WDK networking , advance operations
- packets WDK networking , advance operations
- advance operations WDK networking
- sending data WDK networking
- receiving data WDK networking
- freeing MDLs
- reducing use
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Advance Operations





Advance operations decrease the size of the used data space in a [**NET\_BUFFER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_net_buffer) structure or in all of the NET\_BUFFER structures in a [**NET\_BUFFER\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_net_buffer_list) structure.

Drivers use the following advance functions:

[**NdisAdvanceNetBufferDataStart**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisadvancenetbufferdatastart)

[**NdisAdvanceNetBufferListDataStart**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisadvancenetbufferlistdatastart)

Advance operations can sometimes free MDLs that are associated with a NET\_BUFFER structure. To provide the mechanism for freeing MDLs, a driver can provide an optional entry point for a [**NetFreeMdl**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-net_buffer_free_mdl_handler) functions. If the entry point is **NULL**, NDIS uses a default method to allocate MDLs. MDLs must only be freed within a *NetFreeMdl* using that reciprocal of the mechanism that was used to allocate the MDL in the [**NetAllocateMdl**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-net_buffer_allocate_mdl_handler) function.

To obtain the new **DataLength**, NDIS subtracts the driver-specified *DataOffsetDelta* from the current **DataLength** . If a previous retreat operation allocated new data space, the advance operation can free such previously allocated memory. If an advance operation does not free memory, NDIS simply adds the *DataOffsetDelta* to the current **DataOffset** to obtain the new **DataOffset** . If the advance operation freed memory, NDIS adjusts the **DataOffset** accordingly.

For the send complete case, advance operations can free memory that was allocated in previous retreat operations. For better performance, drivers should allocate enough total data size before sending to accommodate the retreat operations of all the underlying drivers.

For the receive indication case, advance operations simply adjust the **DataOffset** and **DataLength** accordingly. After the advance operation, the headers of lower layers remain in the *unused data space*.

 

 





