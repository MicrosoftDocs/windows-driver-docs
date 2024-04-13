---
title: KSPROPERTY_MEDIASEEKING_PREROLL
description: The KSPROPERTY_MEDIASEEKING_PREROLL property retrieves the amount of preroll in 100-nanosecond units required on a filter.
keywords: ["KSPROPERTY_MEDIASEEKING_PREROLL Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_MEDIASEEKING_PREROLL
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 10/22/2021
---

# KSPROPERTY_MEDIASEEKING_PREROLL

The **KSPROPERTY_MEDIASEEKING_PREROLL** property retrieves the amount of preroll in 100-nanosecond units required on a filter.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Filter | [**KSPROPERTY**](./ksproperty-structure.md) | LONGLONG |

## Remarks

This property returns the number of 100-nanosecond units of preroll as a value of type LONGLONG.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[KSPROPSETID_MediaSeeking](kspropsetid-mediaseeking.md)

[**KSPROPERTY**](./ksproperty-structure.md)