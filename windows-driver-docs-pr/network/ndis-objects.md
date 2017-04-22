---
title: NDIS Objects
description: NDIS Objects
ms.assetid: 1a1338d7-f668-475b-99a9-4819de0a70c3
keywords:
- allocating generic NDIS objects
- generic NDIS objects WDK networking
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NDIS Objects


## <a href="" id="ddk-ndis-6-0-objects-ng"></a>


Components that do not have an NDIS handle use the [**NdisAllocateGenericObject**](https://msdn.microsoft.com/library/windows/hardware/ff561603) function to allocate a generic NDIS object. A component must call the [**NdisFreeGenericObject**](https://msdn.microsoft.com/library/windows/hardware/ff561850) function to free a generic object that was created with **NdisAllocateGenericObject**.

For information about using generic objects, see [Obtaining Pool Handles](obtaining-pool-handles.md).

 

 





