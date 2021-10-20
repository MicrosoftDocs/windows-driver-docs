---
title: KSPROPERTY_EXTXPORT_LOAD_MEDIUM
description: The KSPROPERTY_EXTXPORT_LOAD_MEDIUM property sets or gets an external device's load medium. For example eject, open tray, close tray, etc.
keywords: ["KSPROPERTY_EXTXPORT_LOAD_MEDIUM Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_EXTXPORT_LOAD_MEDIUM
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/20/2021
ms.localizationpriority: medium
---

# KSPROPERTY_EXTXPORT_LOAD_MEDIUM

The **KSPROPERTY_EXTXPORT_LOAD_MEDIUM** property sets or gets an external device's load medium. For example eject, open tray, close tray, etc.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Device | [**KSPROPERTY_EXTXPORT_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extxport_s) | ULONG |

The property value (operation data) is a ULONG that specifies the current load medium. For example eject, open tray or closed tray.

## Remarks

The **LoadMedium** member of the **KSPROPERTY_EXTXPORT_S** structure specifies the load medium.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_EXTXPORT_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extxport_s)
