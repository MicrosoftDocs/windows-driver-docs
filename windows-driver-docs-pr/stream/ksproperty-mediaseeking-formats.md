---
title: KSPROPERTY_MEDIASEEKING_FORMATS
description: The KSPROPERTY_MEDIASEEKING_FORMATS property retrieves the media time formats supported by a filter. This information is returned as a multiple item property.
keywords: ["KSPROPERTY_MEDIASEEKING_FORMATS Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_MEDIASEEKING_FORMATS
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 10/22/2021
---

# KSPROPERTY_MEDIASEEKING_FORMATS

The **KSPROPERTY_MEDIASEEKING_FORMATS** property retrieves the media time formats supported by a filter. This information is returned as a multiple item property.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Filter | [**KSPROPERTY**](./ksproperty-structure.md) | PVOID |

## Remarks

This property can return a multiple item property. The requester is responsible for supplying a buffer of adequate size.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[KSPROPSETID_MediaSeeking](kspropsetid-mediaseeking.md)

[**KSPROPERTY**](./ksproperty-structure.md)