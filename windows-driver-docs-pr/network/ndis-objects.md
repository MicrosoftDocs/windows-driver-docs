---
title: NDIS Objects
description: NDIS Objects
keywords:
- allocating generic NDIS objects
- generic NDIS objects WDK networking
ms.date: 03/02/2023
---

# NDIS Objects





Components that do not have an NDIS handle use the [**NdisAllocateGenericObject**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocategenericobject) function to allocate a generic NDIS object. A component must call the [**NdisFreeGenericObject**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreegenericobject) function to free a generic object that was created with **NdisAllocateGenericObject**.

For information about using generic objects, see [Obtaining Pool Handles](obtaining-pool-handles.md).

 

