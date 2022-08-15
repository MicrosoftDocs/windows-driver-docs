---
title: KSPROPERTY_EXTDEVICE_ID
description: The KSPROPERTY_EXTDEVICE_ID property retrieves an external device's generalized system-wide Id.
keywords: ["KSPROPERTY_EXTDEVICE_ID Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_EXTDEVICE_ID
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/20/2021
---

# KSPROPERTY_EXTDEVICE_ID

The **KSPROPERTY_EXTDEVICE_ID** property retrieves an external device's generalized system-wide Id.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Device | [**KSPROPERTY_EXTDEVICE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extdevice_s) | DWORD array |

The property value (operation data) is a DWORD array that specifies the external device's unique node Id

## Remarks

The **NodeUniqueID** member of the **KSPROPERTY_EXTDEVICE_S** structure specifies the external device's unique node Id.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_EXTDEVICE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extdevice_s)
