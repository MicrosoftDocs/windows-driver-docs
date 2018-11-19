---
title: Default Allocators
description: Default Allocators
ms.assetid: ef61a33d-eabf-4449-8d11-cfd97aa2e403
keywords:
- default allocators WDK kernel streaming
- system memory allocators WDK kernel streaming
- memory allocators WDK kernel streaming
- multiple destination sinks WDK kernel streaming
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Default Allocators





The default allocator provides a system memory allocator for device drivers that transfer data from system memory and require specific memory allocation properties. When using the default allocator, a filter need only handle the allocator requirements request.

If using the default allocator, minidrivers must set the KSALLOCATOR\_REQUIREMENTF\_SYSTEM\_MEMORY flag in the **RequirementsFlags** member of the relevant [**KSALLOCATOR\_FRAMING**](https://msdn.microsoft.com/library/windows/hardware/ff560979) structure. When an IRP\_MJ\_CREATE is submitted and the create type is KSCREATE\_REQUEST\_ALLOCATOR, the filter forwards the IRP to the default allocator handler by calling the [**KsCreateDefaultAllocator**](https://msdn.microsoft.com/library/windows/hardware/ff561641) function. All remaining processing is handled by the default allocator.

 

 




