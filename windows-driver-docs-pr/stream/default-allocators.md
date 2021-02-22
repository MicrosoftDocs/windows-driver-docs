---
title: Default Allocators
description: Default Allocators
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

If using the default allocator, minidrivers must set the KSALLOCATOR\_REQUIREMENTF\_SYSTEM\_MEMORY flag in the **RequirementsFlags** member of the relevant [**KSALLOCATOR\_FRAMING**](/windows-hardware/drivers/ddi/ks/ns-ks-ksallocator_framing) structure. When an IRP\_MJ\_CREATE is submitted and the create type is KSCREATE\_REQUEST\_ALLOCATOR, the filter forwards the IRP to the default allocator handler by calling the [**KsCreateDefaultAllocator**](/windows-hardware/drivers/ddi/ks/nf-ks-kscreatedefaultallocator) function. All remaining processing is handled by the default allocator.

 

