---
title: KSPROPERTY_CLOCK_CORRELATEDPHYSICALTIME
description: Clients use the KSPROPERTY_CLOCK_CORRELATEDPHYSICALTIME property to compare the current physical time on a clock to the current system time.
keywords: ["KSPROPERTY_CLOCK_CORRELATEDPHYSICALTIME Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CLOCK_CORRELATEDPHYSICALTIME
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 10/18/2021
ms.localizationpriority: medium
---

# KSPROPERTY_CLOCK_CORRELATEDPHYSICALTIME

Clients use the **KSPROPERTY_CLOCK_CORRELATEDPHYSICALTIME** property to compare the current physical time on a clock to the current system time.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSPROPERTY**](/windows-hardware/drivers/stream/ksproperty-structure) | [**KSCORRELATED_TIME**](/windows-hardware/drivers/ddi/ks/ns-ks-kscorrelated_time) |

## Remarks

The **KSCORRELATED_TIME** structure contains the current clock time in the **Time** member and the correlated physical time in the **SystemTime** member.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSPROPERTY_CLOCK_PHYSICALTIME**](ksproperty-clock-physicaltime.md)

[**KeQueryPerformanceCounter**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-kequeryperformancecounter)

[KS Clocks](ks-clocks.md)
