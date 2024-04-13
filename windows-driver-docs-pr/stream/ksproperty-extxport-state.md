---
title: KSPROPERTY_EXTXPORT_STATE
description: The KSPROPERTY_EXTXPORT_STATE property sets or gets an external device's transport mode and state.
keywords: ["KSPROPERTY_EXTXPORT_STATE Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_EXTXPORT_STATE
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/20/2021
---

# KSPROPERTY_EXTXPORT_STATE

The **KSPROPERTY_EXTXPORT_STATE** property sets or gets an external device's transport mode and state.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Device | [**KSPROPERTY_EXTXPORT_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extxport_s) | [**TRANSPORT_STATE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-transport_state) |

The property value (operation data) is a **TRANSPORT_STATE** structure that describes the current mode and state of the external transport. For example when the mode is set to play, the state might be set to freeze (paused).

## Remarks

The **XPrtState** member of the **KSPROPERTY_EXTXPORT_S** structure specifies the mode and state.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_EXTXPORT_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extxport_s)

[**TRANSPORT_STATE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-transport_state)
