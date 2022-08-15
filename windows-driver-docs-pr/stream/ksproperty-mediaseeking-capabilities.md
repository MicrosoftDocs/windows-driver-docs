---
title: KSPROPERTY_MEDIASEEKING_CAPABILITIES
description: The KSPROPERTY_MEDIASEEKING_CAPABILITIES property retrieves the media-seeking capabilities of a filter.
keywords: ["KSPROPERTY_MEDIASEEKING_CAPABILITIES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_MEDIASEEKING_CAPABILITIES
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 10/22/2021
---

# KSPROPERTY_MEDIASEEKING_CAPABILITIES

The **KSPROPERTY_MEDIASEEKING_CAPABILITIES** property retrieves the media-seeking capabilities of a filter.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Filter | [**KSPROPERTY**]( /windows-hardware/drivers/stream/ksproperty-structure) | KS_SEEKING_CAPABILITIES |

## Remarks

The capabilities of a filter that this property retrieves include the ability to seek to an absolute position, to seek forwards or backwards in the media, to get the current position while in play or stop mode, to get the duration, or to play backwards. Note that these are capabilities of the filter as a whole; this property is designed to map to DirectShow seeking capabilities where such capabilities are queried only on a filter, not a pin, basis.

If this property is not supported, it is assumed that the filter does not require positional information and that the filter can be treated as a pass through.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[KSPROPSETID_MediaSeeking](kspropsetid-mediaseeking.md)

[**KSPROPERTY**]( /windows-hardware/drivers/stream/ksproperty-structure)
