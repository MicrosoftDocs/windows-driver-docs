---
title: KSPROPERTY_CLOCK_TIME
description: Clients use the KSPROPERTY_CLOCK_TIME property to determine the current presentation time on a clock.
keywords: ["KSPROPERTY_CLOCK_TIME Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CLOCK_TIME
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 10/18/2021
ms.localizationpriority: medium
---

# KSPROPERTY_CLOCK_TIME

Clients use the **KSPROPERTY_CLOCK_TIME** property to determine the current presentation time on a clock.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSPROPERTY**](/windows-hardware/drivers/stream/ksproperty-structure) | LONGLONG |

## Remarks

This property returns a value of type LONGLONG, specifying the current presentation time in 100-nanosecond units.

The presentation time of a clock can be reversed, unlike the physical time. The presentation time of a clock typically represents a timestamp on an underlying data stream. For example, a clock for a DVD player can report the timestamp of the current position in the DVD as its presentation time.

Clocks are not required to support a 100-nanosecond resolution. To determine the clock resolution, clients can use the [**KSPROPERTY_CLOCK_RESOLUTION**](ksproperty-clock-resolution.md) request.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[KSPROPSETID_Clock](kspropsetid-clock.md)
