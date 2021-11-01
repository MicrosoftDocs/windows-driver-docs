---
title: KSPROPERTY_EXTXPORT_STATE_NOTIFY
description: The KSPROPERTY_EXTXPORT_STATE_NOTIFY property sets or gets notification of transport mode and state change.
keywords: ["KSPROPERTY_EXTXPORT_STATE_NOTIFY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_EXTXPORT_STATE_NOTIFY
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/20/2021
ms.localizationpriority: medium
---

# KSPROPERTY_EXTXPORT_STATE_NOTIFY

The **KSPROPERTY_EXTXPORT_STATE_NOTIFY** property sets or gets notification of transport mode and state change.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Device | [**KSPROPERTY_EXTXPORT_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extxport_s) | [**KSPROPERTY_EXTXPORT_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extxport_s) |

The property value (operation data) is the **KSPROPERTY_EXTXPORT_S** structure that describes the current external transport whenever the transport state has changed.

## Remarks

The **KSPROPERTY_EXTXPORT_S** structure receives notification when the transport state has changed.

This call is a synchronous operation and will not return until the transport state has changed. It is not recommended for use since not all DV camcorders can support this operation.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_EXTXPORT_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extxport_s)
