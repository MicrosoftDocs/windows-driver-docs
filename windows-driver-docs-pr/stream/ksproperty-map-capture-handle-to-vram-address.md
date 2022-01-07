---
title: KSPROPERTY_MAP_CAPTURE_HANDLE_TO_VRAM_ADDRESS
description: The KSPROPERTY_MAP_CAPTURE_HANDLE_TO_VRAM_ADDRESS property returns the capture driver's mapping of a VRAM surface handle to a VRAM physical address.To use VRAM transport, a capture minidriver must support this property.
keywords: ["KSPROPERTY_MAP_CAPTURE_HANDLE_TO_VRAM_ADDRESS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_MAP_CAPTURE_HANDLE_TO_VRAM_ADDRESS
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/22/2021
---

# KSPROPERTY_MAP_CAPTURE_HANDLE_TO_VRAM_ADDRESS

The **KSPROPERTY_MAP_CAPTURE_HANDLE_TO_VRAM_ADDRESS** property returns the capture driver's mapping of a VRAM surface handle to a VRAM physical address.

To use VRAM transport, a capture minidriver must support this property.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Pin | [**VRAM_SURFACE_INFO_PROPERTY_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-vram_surface_info_property_s) | DWORD |

## Return value

A **KSPROPERTY_MAP_CAPTURE_HANDLE_TO_VRAM_ADDRESS** returns **STATUS_SUCCESS** to indicate that it has completed successfully. Otherwise, the request returns an appropriate error code.

## Remarks

The capture driver should perform the mapping in the handler for this property.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**VRAM_SURFACE_INFO_PROPERTY_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-vram_surface_info_property_s)
