---
title: KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_INTERLEAVE
description: The KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_INTERLEAVE property informs the Overlay Mixer if interleaved capture is possible.
keywords: ["KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_INTERLEAVE Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_INTERLEAVE
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/12/2021
---

# KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_INTERLEAVE

The **KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_INTERLEAVE** property informs the Overlay Mixer if interleaved capture is possible.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_CAPS_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_allocator_control_capture_caps_s) | ULONG |

The property value (operation data) is a ULONG the specifies whether interleaved capture is possible.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_INTERLEAVE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_allocator_control_capture_interleave_s)
