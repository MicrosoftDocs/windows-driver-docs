---
title: Configuring Memory Segment Types
description: Configuring Memory Segment Types
ms.assetid: a1fed4d6-60ae-42f2-9be0-98b667953606
keywords:
- memory segments WDK display , configuring
- memory segments WDK display , types
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Configuring Memory Segment Types


## <span id="ddk_configuring_memory_segment_types_gg"></span><span id="DDK_CONFIGURING_MEMORY_SEGMENT_TYPES_GG"></span>


The video memory manager and display hardware only support certain types of memory segments, so the display miniport driver can only configure segments of those types. The display miniport driver can configure memory-space and aperture-space segments, which are different in that a memory-space segment consists of a medium that holds the bits of an allocation while an aperture-space segment is a virtual address space. When a range in a memory-space segment is allocated, actual memory is allocated. When a range in an aperture-space segment is allocated, the virtual address space is redirected to physical pages that are allocated independently from either a video memory pool or system memory.

The display miniport driver can configure the following types of memory segments:

-   [Linear Memory-Space Segments](linear-memory-space-segments.md)

-   [Linear Aperture-Space Segments](linear-aperture-space-segments.md)

-   [AGP-Type Aperture-Space Segments](agp-type-aperture-space-segments.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Configuring%20Memory%20Segment%20Types%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




