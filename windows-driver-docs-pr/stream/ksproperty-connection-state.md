---
title: KSPROPERTY_CONNECTION_STATE
description: The KSPROPERTY_CONNECTION_STATE property sets the current run state of the pin.
keywords: ["KSPROPERTY_CONNECTION_STATE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CONNECTION_STATE
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 10/18/2021
ms.localizationpriority: medium
---

# KSPROPERTY_CONNECTION_STATE

The **KSPROPERTY_CONNECTION_STATE** property sets the current run state of the pin.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| No | Yes | Filter or Pin | [**KSPROPERTY**](/windows-hardware/drivers/stream/ksproperty-structure) | [**KSSTATE**](/windows-hardware/drivers/ddi/ks/ne-ks-ksstate) |

## Remarks

This property returns one of the following values:

| Value | Description |
|--|--|
| KSSTATE_STOP | The initial state of a pin. No data is actually being read or written. In this state, the pin uses the least amount of resources possible. |
| KSSTATE_ACQUIRE | The pin is acquiring the resources necessary to read or write data. |
| KSSTATE_PAUSE | The pin is ready to read or write data, but data transfer is temporarily paused. |
| KSSTATE_RUN | The state from which the pin can actually read or write data. |

The pin only reads or writes data in the **KSSTATE_RUN** state. Both individual pins and the KS filter as a whole may support this property.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSSTATE**](/windows-hardware/drivers/ddi/ks/ne-ks-ksstate)
