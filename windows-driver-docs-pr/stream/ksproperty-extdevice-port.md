---
title: KSPROPERTY_EXTDEVICE_PORT
description: The KSPROPERTY_EXTDEVICE_PORT property retrieves an external device's port type.
keywords: ["KSPROPERTY_EXTDEVICE_PORT Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_EXTDEVICE_PORT
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/20/2021
---

# KSPROPERTY_EXTDEVICE_PORT

The **KSPROPERTY_EXTDEVICE_PORT** property retrieves an external device's port type.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Device | [**KSPROPERTY_EXTDEVICE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extdevice_s) | ULONG |

The property value (operation data) is a ULONG that specifies the external device's connection port. For example 1394 or USB.

## Remarks

The **DevPort** member of the KSPROPERTY_EXTDEVICE_S structure specifies the external device's port type. The **DevPort** member may be set to equal **DEV_PORT_1394**, **DEV_PORT_USB**, and so on. These tokens are defined in the *xprtdefs.h* file in the Microsoft DirectX SDK.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_EXTDEVICE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extdevice_s)
