---
title: KSPROPERTY_MEDIASEEKING_POSITIONS
description: The KSPROPERTY_MEDIASEEKING_POSITIONS property sets the media time and/or the stop time on a filter.
keywords: ["KSPROPERTY_MEDIASEEKING_POSITIONS Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_MEDIASEEKING_POSITIONS
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 10/22/2021
---

# KSPROPERTY_MEDIASEEKING_POSITIONS

The **KSPROPERTY_MEDIASEEKING_POSITIONS** property sets the media time and/or the stop time on a filter.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| No | Yes | Filter | [**KSPROPERTY**](./ksproperty-structure.md) | [**KSPROPERTY_POSITIONS**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_positions) |

## Remarks

The **KSPROPERTY_POSITIONS** structure specifies the current position and stop position relative to the total duration of the stream.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSPROPERTY_POSITIONS**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_positions)

[**KSPROPERTY**](./ksproperty-structure.md)