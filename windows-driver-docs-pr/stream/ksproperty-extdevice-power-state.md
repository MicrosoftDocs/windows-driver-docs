---
title: KSPROPERTY_EXTDEVICE_POWER_STATE
description: The KSPROPERTY_EXTDEVICE_POWER_STATE property sets or gets the power state of an external device.
keywords: ["KSPROPERTY_EXTDEVICE_POWER_STATE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_EXTDEVICE_POWER_STATE
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/20/2021
ms.localizationpriority: medium
---

# KSPROPERTY_EXTDEVICE_POWER_STATE

The **KSPROPERTY_EXTDEVICE_POWER_STATE** property sets or gets the power state of an external device.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Device | [**KSPROPERTY_EXTDEVICE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extdevice_s) | ULONG |

The property value (operation data) is a ULONG that specifies the external device's power state.

## Remarks

The **PowerState** member of the KSPROPERTY_EXTDEVICE_S structure specifies the external device's power setting. The **PowerState** member may be set to equal on or standby. For example, a battery-powered external device, such as a DV camcorder may be powered off. An AC-powered DVHS device may be placed in standby. If a device is in standby, it may be powered-on later.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_EXTDEVICE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extdevice_s)
