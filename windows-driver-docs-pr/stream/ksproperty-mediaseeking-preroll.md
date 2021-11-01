---
title: KSPROPERTY_MEDIASEEKING_PREROLL
description: The KSPROPERTY_MEDIASEEKING_PREROLL property retrieves the amount of preroll in 100-nanosecond units required on a filter.
keywords: ["KSPROPERTY_MEDIASEEKING_PREROLL Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_MEDIASEEKING_PREROLL
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 10/22/2021
ms.localizationpriority: medium
---

# KSPROPERTY_MEDIASEEKING_PREROLL

The **KSPROPERTY_MEDIASEEKING_PREROLL** property retrieves the amount of preroll in 100-nanosecond units required on a filter.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Filter | [**KSPROPERTY**](/windows-hardware/drivers/stream/ksproperty-structure) | LONGLONG |

## Remarks

This property returns the number of 100-nanosecond units of preroll as a value of type LONGLONG.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[KSPROPSETID_MediaSeeking](kspropsetid-mediaseeking.md)

[**KSPROPERTY**](/windows-hardware/drivers/stream/ksproperty-structure)
