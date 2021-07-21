---
title: Retreat Operations
description: Retreat Operations
keywords:
- network data WDK , retreat operations
- data WDK networking , retreat operations
- packets WDK networking , retreat operations
- retreat operations WDK networking
- sending data WDK networking
- receiving data WDK networking
- allocating MDLs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Retreat Operations





Retreat operations can increase the size of the used data space in a [**NET\_BUFFER**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer) structure or in all of the NET\_BUFFER structures in a [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure.

NDIS provides the following retreat functions:

[**NdisRetreatNetBufferDataStart**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisretreatnetbufferdatastart)

[**NdisRetreatNetBufferListDataStart**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisretreatnetbufferlistdatastart)

Retreat operations can sometimes allocate MDLs that are associated with a NET\_BUFFER structure. To provide the mechanism for allocating MDLs, a driver can provide an optional entry point for a [**NetAllocateMdl**](/windows-hardware/drivers/ddi/nblapi/nc-nblapi-net_buffer_allocate_mdl) function. If the entry point is **NULL**, NDIS uses a default method to allocate MDLs. MDLs must be freed within a [**NetFreeMdl**](/windows-hardware/drivers/ddi/nblapi/nc-nblapi-net_buffer_free_mdl) function that provides the reciprocal of the mechanism that was used to allocate the MDL.

To obtain the new **DataLength**, NDIS adds the driver-specified *DataOffsetDelta* to the current **DataLength** . If the size of the *unused data space* is greater than the *DataOffsetDelta*, a retreat operation reduces the **DataOffset** . In this case, the new **DataOffset** is the current **DataOffset** minus the *DataOffsetDelta* .

If the *DataOffsetDelta* is greater than **DataOffset**, a retreat operation allocates new data space. In this case, NDIS adjusts the **DataOffset** accordingly.

For send operations, NDIS allocates memory if there isn't enough *unused data space* to satisfy a retreat request. If no memory allocation is required, NDIS simply adjusts the **DataOffset** and **DataLength** . For better performance, drivers should allocate enough total data size before sending to accommodate the retreat operations of all the underlying drivers.

For the receive return case, NDIS simply adjusts the **DataOffset** and **DataLength** accordingly. The retreat operation reverses the advance operation that took place during receive processing. After the retreat operation, the *used data space* contains the header data that underlying drivers used during receive processing.

 

