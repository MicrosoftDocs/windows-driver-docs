---
title: KSPROPERTY_CLOCK_RESOLUTION
description: Clients use the KSPROPERTY_CLOCK_RESOLUTION property to determine the precision of a clock.
keywords: ["KSPROPERTY_CLOCK_RESOLUTION Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CLOCK_RESOLUTION
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 10/18/2021
---

# KSPROPERTY_CLOCK_RESOLUTION

Clients use the **KSPROPERTY_CLOCK_RESOLUTION** property to determine the precision of a clock.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSPROPERTY**](./ksproperty-structure.md) | [**KSRESOLUTION**](/windows-hardware/drivers/ddi/ks/ns-ks-ksresolution) |

## Remarks

The delay introduced in the **Error** member is in addition to that in the **Granularity** member. For example, a clock with a **Granularity** of one and **Error** of two would be able to issue clock event notifications every 300 nanoseconds.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSCLOCK_DISPATCH**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksclock_dispatch)

[**KSRESOLUTION**](/windows-hardware/drivers/ddi/ks/ns-ks-ksresolution)

[**KSPROPERTY_CLOCK_PHYSICALTIME**](ksproperty-clock-physicaltime.md)