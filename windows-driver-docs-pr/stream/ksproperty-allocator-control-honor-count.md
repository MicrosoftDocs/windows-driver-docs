---
title: KSPROPERTY_ALLOCATOR_CONTROL_HONOR_COUNT
description: The KSPROPERTY_ALLOCATOR_CONTROL_HONOR_COUNT property informs the Overlay Mixer how to determine the number of DirectDraw surfaces to allocate. This property is optional.
keywords: ["KSPROPERTY_ALLOCATOR_CONTROL_HONOR_COUNT Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_ALLOCATOR_CONTROL_HONOR_COUNT
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/12/2021
---

# KSPROPERTY_ALLOCATOR_CONTROL_HONOR_COUNT

The **KSPROPERTY_ALLOCATOR_CONTROL_HONOR_COUNT** property informs the Overlay Mixer how to determine the number of DirectDraw surfaces to allocate. This property is optional.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSPROPERTY**](./ksproperty-structure.md) | DWORD |

The property value (operation data) is a DWORD that specifies how the Overlay Mixer is to calculate the number of and use of overlay surfaces.

## Remarks

KSPROPERTY_ALLOCATOR_CONTROL_HONOR_COUNT property requests must return 1 to force the Overlay Mixer to use the number of surfaces specified in the [**KSPROPERTY_CONNECTION_ALLOCATORFRAMING**](ksproperty-connection-allocatorframing.md) property. A return value of zero causes the Overlay Mixer to calculate how many surfaces to allocate.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_CONNECTION_ALLOCATORFRAMING**](ksproperty-connection-allocatorframing.md)