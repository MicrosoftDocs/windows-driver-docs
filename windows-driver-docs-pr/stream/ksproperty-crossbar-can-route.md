---
title: KSPROPERTY_CROSSBAR_CAN_ROUTE
description: The KSPROPERTY_CROSSBAR_CAN_ROUTE property retrieves whether the device is capable of supporting a specified routing. This property must be implemented.
keywords: ["KSPROPERTY_CROSSBAR_CAN_ROUTE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CROSSBAR_CAN_ROUTE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/18/2021
ms.localizationpriority: medium
---

# KSPROPERTY_CROSSBAR_CAN_ROUTE

The **KSPROPERTY_CROSSBAR_CAN_ROUTE** property retrieves whether the device is capable of supporting a specified routing. This property must be implemented.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Filter | [**KSPROPERTY_CROSSBAR_ROUTE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_crossbar_route_s) | ULONG |

The property value (operation data) is a ULONG that specifies whether the streaming minidriver supports a specified routing between the two pins. A nonzero value indicates that routing is supported. If the minidriver does not support routing between the two pins, this value is zero.

## Remarks

The **CanRoute** member of the **KSPROPERTY_CROSSBAR_ROUTE_S** structure indicates if the device is capable of supporting a specified routing.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_CROSSBAR_ROUTE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_crossbar_route_s)
