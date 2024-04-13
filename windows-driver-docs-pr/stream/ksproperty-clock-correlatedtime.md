---
title: KSPROPERTY_CLOCK_CORRELATEDTIME
description: Clients use the KSPROPERTY_CLOCK_CORRELATEDTIME property to compare the current presentation time on a clock to the current system time.
keywords: ["KSPROPERTY_CLOCK_CORRELATEDTIME Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_CLOCK_CORRELATEDTIME
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 10/18/2021
---

# KSPROPERTY_CLOCK_CORRELATEDTIME

Clients use the **KSPROPERTY_CLOCK_CORRELATEDTIME** property to compare the current presentation time on a clock to the current system time.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSPROPERTY**](./ksproperty-structure.md) | [**KSCORRELATED_TIME**](/windows-hardware/drivers/ddi/ks/ns-ks-kscorrelated_time) |

## Remarks

The **KSCORRELATED_TIME** structure contains the current clock time in the **Time** member and the correlated physical time in the **SystemTime** member.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSPROPERTY_CLOCK_PHYSICALTIME**](ksproperty-clock-physicaltime.md)

[**KeQueryPerformanceCounter**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-kequeryperformancecounter)

[KS Clocks](ks-clocks.md)