---
title: Allocating Memory in an NDIS 6.0 Miniport Driver
description: Allocating Memory in an NDIS 6.0 Miniport Driver
ms.assetid: e3ae6c37-d200-49b4-b4dd-4b2bc4a00647
keywords:
- allocating memory
- memory WDK networking
- miniport adapters WDK networking , memory
- adapters WDK networking , memory
- porting miniport drivers WDK networking , adapters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Allocating Memory in an NDIS 6.0 Miniport Driver





The [**NdisAllocateMemoryWithTagPriority**](https://msdn.microsoft.com/library/windows/hardware/ff561606) function replaces the [**NdisAllocateMemory**](https://msdn.microsoft.com/library/windows/hardware/ff550762) and [**NdisAllocateMemoryWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff550767) functions. In addition to specifying the miniport adapter handle, pool size, and tag, **NdisAllocateMemoryWithTagPriority** requires an allocation priority that indicates the importance of the request. The priority is the same as that defined for the [**ExAllocatePoolWithTagPriority**](https://msdn.microsoft.com/library/windows/hardware/ff544523) function.

 

 





