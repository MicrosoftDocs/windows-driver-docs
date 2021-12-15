---
title: Allocator Properties
description: The PROPSETID_ALLOCATOR_CONTROL property set contains properties related to controlling the allocation and operations of video port surfaces.
keywords:
- allocator properties WDK video capture
- PROPSETID_ALLOCATOR_CONTROL
ms.date: 07/26/2021
---

# Allocator Properties

The [**PROPSETID_ALLOCATOR_CONTROL**](propsetid-allocator-control.md) property set contains properties related to controlling the allocation and operations of video port surfaces. User-mode filters, such as the Overlay Mixer, use PROPSETID_ALLOCATOR_CONTROL. The following table describes properties that are part of the PROPSETID_ALLOCATOR_CONTROL property set.

| PROPSETID_ALLOCATOR_CONTROL KS properties | Property description |
|--|--|
| [**KSPROPERTY_ALLOCATOR_CONTROL_HONOR_COUNT**](ksproperty-allocator-control-honor-count.md) | Controls how a filter determines the number of video port overlay surfaces to allocate. |
| [**KSPROPERTY_ALLOCATOR_CONTROL_SURFACE_SIZE**](ksproperty-allocator-control-surface-size.md) | Controls the dimensions of the video port overlay surface. |
| [**KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_CAPS**](ksproperty-allocator-control-capture-caps.md) | Describes the capture capabilities of the video port. |
| [**KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_INTERLEAVE**](ksproperty-allocator-control-capture-interleave.md) | Returns if the video port supports interleaved capture. |
