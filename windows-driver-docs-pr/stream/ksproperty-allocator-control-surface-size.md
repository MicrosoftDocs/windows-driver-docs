---
title: KSPROPERTY_ALLOCATOR_CONTROL_SURFACE_SIZE
description: The KSPROPERTY_ALLOCATOR_CONTROL_SURFACE_SIZE property informs client filters that provide DirectDraw surface allocators (such as the Overlay Mixer) that a capture operation is in progress and that Microsoft DirectDraw surfaces must be allocated at a fixed size regardless of the present size of the overlay. This property is optional.
keywords: ["KSPROPERTY_ALLOCATOR_CONTROL_SURFACE_SIZE Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_ALLOCATOR_CONTROL_SURFACE_SIZE
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/12/2021
---

# KSPROPERTY_ALLOCATOR_CONTROL_SURFACE_SIZE

The **KSPROPERTY_ALLOCATOR_CONTROL_SURFACE_SIZE** property informs client filters that provide DirectDraw surface allocators (such as the Overlay Mixer) that a capture operation is in progress and that Microsoft DirectDraw surfaces must be allocated at a fixed size regardless of the present size of the overlay. This property is optional.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSPROPERTY_ALLOCATOR_CONTROL_SURFACE_SIZE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_allocator_control_surface_size_s) | Pair of ULONGs |

The property value (operation data) is a pair of ULONGs that specify the width and height of overlay surfaces.

## Remarks

Minidrivers that support this property return a KSPROPERTY_ALLOCATOR_CONTROL_SURFACE_SIZE_S structure that describes the width and height of the required overlay surface. The Overlay Mixer allocates overlay surfaces of this size. If this is not the size specified in the MediaType during pin connection, then the video is scaled at the video port to this size. No other scaling at the video port occurs regardless of the scaling abilities of the VGA chip.

The Overlay Mixer always queries this new property if the mixer is connected to this property's upstream filter through a video port on its primary input pin. If that filter does not implement this property, the Overlay Mixer assumes that it is not capturing data and scales the video at the video port as necessary to keep the video displayed correctly.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_ALLOCATOR_CONTROL_SURFACE_SIZE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_allocator_control_surface_size_s)
