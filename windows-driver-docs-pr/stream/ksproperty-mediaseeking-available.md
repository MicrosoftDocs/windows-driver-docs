---
title: KSPROPERTY_MEDIASEEKING_AVAILABLE
description: The KSPROPERTY_MEDIASEEKING_AVAILABLE property retrieves the media time span that is currently available on a filter.
keywords: ["KSPROPERTY_MEDIASEEKING_AVAILABLE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_MEDIASEEKING_AVAILABLE
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 10/22/2021
---

# KSPROPERTY_MEDIASEEKING_AVAILABLE

The **KSPROPERTY_MEDIASEEKING_AVAILABLE** property retrieves the media time span that is currently available on a filter.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Filter | [**KSPROPERTY**](/windows-hardware/drivers/stream/ksproperty-structure) | [**KSPROPERTY_MEDIAAVAILABLE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_mediaavailable) |

## Remarks

The media time span is the duration that within which a client can seek.

## Requirements

k

## See also

[**KSPROPERTY_MEDIAAVAILABLE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_mediaavailable)

[KSPROPSETID_MediaSeeking](kspropsetid-mediaseeking.md)

[**KSPROPERTY**](/windows-hardware/drivers/stream/ksproperty-structure)
