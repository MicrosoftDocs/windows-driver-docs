---
title: NDIS Objects
description: NDIS Objects
ms.assetid: 1a1338d7-f668-475b-99a9-4819de0a70c3
keywords:
- allocating generic NDIS objects
- generic NDIS objects WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS Objects





Components that do not have an NDIS handle use the [**NdisAllocateGenericObject**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisallocategenericobject) function to allocate a generic NDIS object. A component must call the [**NdisFreeGenericObject**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisfreegenericobject) function to free a generic object that was created with **NdisAllocateGenericObject**.

For information about using generic objects, see [Obtaining Pool Handles](obtaining-pool-handles.md).

 

 





