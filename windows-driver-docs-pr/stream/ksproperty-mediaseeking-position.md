---
title: KSPROPERTY_MEDIASEEKING_POSITION
description: KSPROPERTY_MEDIASEEKING_POSITION retrieves the media time of a filter.
keywords: ["KSPROPERTY_MEDIASEEKING_POSITION Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_MEDIASEEKING_POSITION
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 10/22/2021
---

# KSPROPERTY_MEDIASEEKING_POSITION

**KSPROPERTY_MEDIASEEKING_POSITION** retrieves the media time of a filter.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Filter | [**KSPROPERTY**](./ksproperty-structure.md) | LONGLONG |

## Remarks

The media time is returned as a value of type LONGLONG.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[KSPROPSETID_MediaSeeking](kspropsetid-mediaseeking.md)

[**KSPROPERTY**](./ksproperty-structure.md)