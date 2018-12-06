---
title: Configuring Memory Segment Types
description: Configuring Memory Segment Types
ms.assetid: a1fed4d6-60ae-42f2-9be0-98b667953606
keywords:
- memory segments WDK display , configuring
- memory segments WDK display , types
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Configuring Memory Segment Types


## <span id="ddk_configuring_memory_segment_types_gg"></span><span id="DDK_CONFIGURING_MEMORY_SEGMENT_TYPES_GG"></span>


The video memory manager and display hardware only support certain types of memory segments, so the display miniport driver can only configure segments of those types. The display miniport driver can configure memory-space and aperture-space segments, which are different in that a memory-space segment consists of a medium that holds the bits of an allocation while an aperture-space segment is a virtual address space. When a range in a memory-space segment is allocated, actual memory is allocated. When a range in an aperture-space segment is allocated, the virtual address space is redirected to physical pages that are allocated independently from either a video memory pool or system memory.

The display miniport driver can configure the following types of memory segments:

-   [Linear Memory-Space Segments](linear-memory-space-segments.md)

-   [Linear Aperture-Space Segments](linear-aperture-space-segments.md)

-   [AGP-Type Aperture-Space Segments](agp-type-aperture-space-segments.md)

 

 





