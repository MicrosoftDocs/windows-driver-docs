---
title: KSPROPERTY_CROSSBAR_ROUTE
description: The KSPROPERTY_CROSSBAR_ROUTE property queries whether a particular routing is possible and to route a video or audio stream by specifying an output pin index and an input pin index. This property must be implemented.
keywords: ["KSPROPERTY_CROSSBAR_ROUTE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CROSSBAR_ROUTE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/18/2021
---

# KSPROPERTY_CROSSBAR_ROUTE

The **KSPROPERTY_CROSSBAR_ROUTE** property queries whether a particular routing is possible and to route a video or audio stream by specifying an output pin index and an input pin index. This property must be implemented.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | [**KSPROPERTY_CROSSBAR_ROUTE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_crossbar_route_s) | [**KSPROPERTY_CROSSBAR_ROUTE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_crossbar_route_s) |

The property value (operation data) is a **KSPROPERTY_CROSS_ROUTE_S** structure that specifies a particular routing and whether that routing is possible.

## Remarks

When routed to an input pin index of -1, an audio output pin should mute the output audio stream, such as when changing a channel.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_CROSSBAR_ROUTE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_crossbar_route_s)
