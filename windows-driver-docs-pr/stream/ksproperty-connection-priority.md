---
title: KSPROPERTY_CONNECTION_PRIORITY
description: Clients use the KSPROPERTY_CONNECTION_PRIORITY property to get or set the priority of a connection.
keywords: ["KSPROPERTY_CONNECTION_PRIORITY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CONNECTION_PRIORITY
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 10/18/2021
ms.localizationpriority: medium
---

# KSPROPERTY_CONNECTION_PRIORITY

Clients use the **KSPROPERTY_CONNECTION_PRIORITY** property to get or set the priority of a connection.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | Yes | Pin | [**KSPROPERTY**](/windows-hardware/drivers/stream/ksproperty-structure) | [**KSPRIORITY**](/windows-hardware/drivers/ddi/ks/ns-ks-kspriority) |

## Remarks

This property returns a structure of type [**KSPRIORITY**](/windows-hardware/drivers/ddi/ks/ns-ks-kspriority) that contains a priority class and subclass.

One priority is greater than another if the **PriorityClass** member is greater, or if the **PriorityClass** members are identical and the **PrioritySubClass** member is greater.

The following predefined values of **PriorityClass** are available: **KSPRIORITY_LOW**, **KSPRIORITY_NORMAL**, **KSPRIORITY_HIGH**, and **KSPRIORITY_EXCLUSIVE**. Priority defaults to **KSPRIORITY_NORMAL**. KSPRIORITY_EXCLUSIVE indicates the connection has exclusive access to resources used by a pin.

The priority values have global significance: a client can use the reported values to set priorities between two different pins on two unrelated kernel streaming filters.

**KSPROPERTY_CONNECTION_PRIORITY** is optional. Clients treat pins that do not support it as having priority **KSPRIORITY_NORMAL**.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSPRIORITY**](/windows-hardware/drivers/ddi/ks/ns-ks-kspriority)

[**KSPIN_CONNECT**](/windows-hardware/drivers/ddi/ks/ns-ks-kspin_connect)
