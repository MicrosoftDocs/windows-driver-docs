---
title: KSPROPERTY_CLOCK_PHYSICALTIME
description: Clients use the KSPROPERTY_CLOCK_PHYSICAL_TIME property to determine the current physical time of a clock.
keywords: ["KSPROPERTY_CLOCK_PHYSICALTIME Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CLOCK_PHYSICALTIME
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 10/18/2021
---

# KSPROPERTY_CLOCK_PHYSICALTIME

Clients use the **KSPROPERTY_CLOCK_PHYSICAL_TIME** property to determine the current physical time of a clock.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSPROPERTY**](./ksproperty-structure.md) | LONGLONG |

## Remarks

This property returns a value of type LONGLONG, representing the current physical time in 100-nanosecond units.

The physical time of a clock is an ever-progressing counter. Unlike the presentation time, it cannot reverse.

Clocks are not required to support a 100-nanosecond resolution. To determine the clock resolution, clients can use the [**KSPROPERTY_CLOCK_RESOLUTION**](ksproperty-clock-resolution.md) request.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSPROPERTY_CLOCK_CORRELATEDPHYSICALTIME**](ksproperty-clock-correlatedphysicaltime.md)

[**KSPROPERTY_CLOCK_CORRELATEDTIME**](ksproperty-clock-correlatedtime.md)