---
title: Allocating Memory in an NDIS 6.0 Protocol Driver
description: Allocating Memory in an NDIS 6.0 Protocol Driver
ms.assetid: abbbd151-d8b7-4413-9ccb-63ec570876ab
keywords:
- protocol drivers WDK networking , memory
- NDIS protocol drivers WDK , memory
- allocating memory
- memory WDK networking
- NdisAllocateMemory
- NdisAllocateMemoryWithTag
- NdisAllocateMemoryWithTagPriority
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Allocating Memory in an NDIS 6.0 Protocol Driver


## <a href="" id="ddk-allocating-memory-in-an-ndis-6-0-protocol-driver-nd"></a>


In NDIS 6.0, the [**NdisAllocateMemoryWithTagPriority**](https://msdn.microsoft.com/library/windows/hardware/ff561606) function replaces the [**NdisAllocateMemory**](https://msdn.microsoft.com/library/windows/hardware/ff550762) and [**NdisAllocateMemoryWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff550767) functions. In addition to specifying the protocol driver handle, pool size, and tag, **NdisAllocateMemoryWithTagPriority** requires an allocation priority that indicates the importance of the request. The priority is the same as that defined for the [**ExAllocatePoolWithTagPriority**](https://msdn.microsoft.com/library/windows/hardware/ff544523) function.

 

 





