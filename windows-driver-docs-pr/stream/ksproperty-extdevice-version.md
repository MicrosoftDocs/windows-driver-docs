---
title: KSPROPERTY_EXTDEVICE_VERSION
description: The KSPROPERTY_EXTDEVICE_VERSION property retrieves the version of an external device.
keywords: ["KSPROPERTY_EXTDEVICE_VERSION Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_EXTDEVICE_VERSION
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/20/2021
ms.localizationpriority: medium
---

# KSPROPERTY_EXTDEVICE_VERSION

The **KSPROPERTY_EXTDEVICE_VERSION** property retrieves the version of an external device.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Device | [**KSPROPERTY_EXTDEVICE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extdevice_s) | WCHAR array |

The property value (operation data) is WCHAR array that contains the external device's version. The array is a free-format string.

## Remarks

The **pawchString** member of the **KSPROPERTY_EXTDEVICE_S** structure describes the external device's version.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_EXTDEVICE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extdevice_s)
