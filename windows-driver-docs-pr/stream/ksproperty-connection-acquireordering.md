---
title: KSPROPERTY_CONNECTION_ACQUIREORDERING
description: The KSPROPERTY_CONNECTION_ACQUIREORDERING property is an optional property that should be implemented on a pin when state change order is significant.
keywords: ["KSPROPERTY_CONNECTION_ACQUIREORDERING Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CONNECTION_ACQUIREORDERING
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 10/18/2021
---

# KSPROPERTY_CONNECTION_ACQUIREORDERING

The **KSPROPERTY_CONNECTION_ACQUIREORDERING** property is an optional property that should be implemented on a pin when state change order is significant. For example, the property should be implemented on communication sink pins if the sink requires pins connected to its communication source pins to be set to an Acquire state before the sink pins are set.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSPROPERTY**](./ksproperty-structure.md) | BOOL |

## Remarks

This property returns **TRUE** if state change ordering is significant. If **FALSE** is to be returned, the property need not be implemented.

This read-only property is used to determine whether the Stop-to-Acquire state change is significant for this communication sink pin. If the property is not implemented, the assumption is that ordering is not significant. For IRP-based data flow, this would be implemented by a pin when it forwards streaming IRPs rather than creating new IRPs for requests, and thus needs to indicate correct stack depth to the connected source pin. If the pin did not forward IRPs, then recalculation of stack depth would not be important, as the stack depth for the filter would be static.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[KSPROPSETID_Connection](kspropsetid-connection.md)