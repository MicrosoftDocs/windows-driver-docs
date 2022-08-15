---
title: KSPROPERTY_EXTDEVICE_CAPABILITIES
description: The KSPROPERTY_EXTDEVICE_CAPABILITIES property retrieves the capabilities of an external device.
keywords: ["KSPROPERTY_EXTDEVICE_CAPABILITIES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_EXTDEVICE_CAPABILITIES
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/20/2021
---

# KSPROPERTY_EXTDEVICE_CAPABILITIES

The **KSPROPERTY_EXTDEVICE_CAPABILITIES** property retrieves the capabilities of an external device.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Device | [**KSPROPERTY_EXTDEVICE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extdevice_s) | [**DEVCAPS**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagdevcaps) |

The property value (operation data) is a **DEVCAPS** structure that describes the capabilities of the external device.

## Remarks

The **Capabilities** member of the **KSPROPERTY_EXTDEVICE_S** structure specifies the external device's capabilities.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_EXTDEVICE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extdevice_s)

[**DEVCAPS**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagdevcaps)
