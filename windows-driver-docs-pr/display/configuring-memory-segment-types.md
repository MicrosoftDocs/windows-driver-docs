---
title: Configuring Memory Segment Types
description: Configuring Memory Segment Types
keywords:
- memory segments WDK display , configuring
- memory segments WDK display , types
ms.date: 07/01/2024
---

# Configuring Memory Segment Types

The video memory manager (*VidMm*) and display hardware only support certain types of memory segments. The kernel-mode display miniport driver (KMD) can therefore only configure segments of those types.

The KMD can configure memory-space segments and aperture-space segments, which are different in that:

* A memory-space segment consists of a medium that holds the bits of an allocation.

* An aperture-space segment is a virtual address space.

When a range in a memory-space segment is allocated, actual memory is allocated. When a range in an aperture-space segment is allocated, the virtual address space is redirected to physical pages that are allocated independently from either a video memory pool or system memory.

The KMD can configure the following types of memory segments:

* [Linear Memory-Space Segments](linear-memory-space-segments.md)

* [Linear Aperture-Space Segments](linear-aperture-space-segments.md)

* [AGP-Type Aperture-Space Segments](agp-type-aperture-space-segments.md)
