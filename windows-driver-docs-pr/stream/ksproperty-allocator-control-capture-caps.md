---
title: KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_CAPS
description: The KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_CAPS property informs the Overlay Mixer of the capture capabilities of the video port (that is if capture support is available).
keywords: ["KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_CAPS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_CAPS
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/12/2021
---

# KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_CAPS

The **KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_CAPS** property informs the Overlay Mixer of the capture capabilities of the video port (that is if capture support is available).

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_CAPS_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_allocator_control_capture_caps_s) | ULONG |

The property value (operation data) is a ULONG the specifies whether interleaved capture is supported.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_CAPS_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_allocator_control_capture_caps_s)
