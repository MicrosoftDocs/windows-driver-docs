---
title: KSPROPERTY_CONNECTION_STARTAT
description: KSPROPERTY_CONNECTION_STARTAT is an optional property that is implemented by filters that support starting when a specified event occurs.
keywords: ["KSPROPERTY_CONNECTION_STARTAT Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_CONNECTION_STARTAT
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 10/18/2021
---

# KSPROPERTY_CONNECTION_STARTAT

KSPROPERTY_CONNECTION_STARTAT is an optional property that is implemented by filters that support starting when a specified event occurs.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| No | Yes | Filter | [**KSPROPERTY**](./ksproperty-structure.md) | [**KSRELATIVEEVENT**](/windows-hardware/drivers/ddi/ks/ns-ks-ksrelativeevent) |

## Remarks

This property should only be requested when the pin is in a pause state, to transition the pin into a run state.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSRELATIVEEVENT**](/windows-hardware/drivers/ddi/ks/ns-ks-ksrelativeevent)

[**KSEVENT_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksevent_item)