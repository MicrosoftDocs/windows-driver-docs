---
title: KSPROPERTY_CLOCK_FUNCTIONTABLE
description: Clients use the KSPROPERTY_CLOCK_FUNCTIONTABLE property to retrieve the entry points for querying time at DISPATCH_LEVEL, which enables filters to perform precise rate matching.
keywords: ["KSPROPERTY_CLOCK_FUNCTIONTABLE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CLOCK_FUNCTIONTABLE
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 10/18/2021
---

# KSPROPERTY_CLOCK_FUNCTIONTABLE

Clients use the **KSPROPERTY_CLOCK_FUNCTIONTABLE** property to retrieve the entry points for querying time at DISPATCH_LEVEL, which enables filters to perform precise rate matching.

This property fills in a [**KSCLOCK_FUNCTIONTABLE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksclock_functiontable) structure with function pointers that are valid until the file object for the clock is released.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSPROPERTY**](/windows-hardware/drivers/stream/ksproperty-structure) | [**KSCLOCK_FUNCTIONTABLE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksclock_functiontable) |

## Remarks

The *FileObject* parameter that the client supplies when it makes calls to these entry points specifies the file object underlying the file handle that was returned when the clock instance was created.

The *SystemTime* parameter points to the location to store the correlated system time. The system time is acquired using the function **KeQueryInterruptTime**.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSCLOCK_FUNCTIONTABLE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksclock_functiontable)

[**KeQueryInterruptTime**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kequeryinterrupttime)

[KS Clocks](ks-clocks.md)
