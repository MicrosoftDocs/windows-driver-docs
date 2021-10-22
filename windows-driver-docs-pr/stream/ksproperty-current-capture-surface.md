---
title: KSPROPERTY_CURRENT_CAPTURE_SURFACE
description: The KSPROPERTY_CURRENT_CAPTURE_SURFACE property gets or sets the type of capture memory used by a given pin.To use VRAM transport, a capture minidriver must support this property.
keywords: ["KSPROPERTY_CURRENT_CAPTURE_SURFACE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CURRENT_CAPTURE_SURFACE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/18/2021
ms.localizationpriority: medium
---

# KSPROPERTY_CURRENT_CAPTURE_SURFACE

The **KSPROPERTY_CURRENT_CAPTURE_SURFACE** property gets or sets the type of capture memory used by a given pin.

To use VRAM transport, a capture minidriver must support this property.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Pin | [**KSPROPERTY**](/windows-hardware/drivers/stream/ksproperty-structure) | [**CAPTURE_MEMORY_ALLOCATION_FLAGS**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-capture_memory_allocation_flags) |

## Return value

A **KSPROPERTY_CURRENT_CAPTURE_SURFACE** returns **STATUS_SUCCESS** to indicate that it has completed successfully. Otherwise, the request returns an appropriate error code.

## Remarks

Zero is an invalid value for [**CAPTURE_MEMORY_ALLOCATION_FLAGS**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-capture_memory_allocation_flags).

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**CAPTURE_MEMORY_ALLOCATION_FLAGS**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-capture_memory_allocation_flags)

[**KSPROPERTY**](ksproperty-structure.md)
