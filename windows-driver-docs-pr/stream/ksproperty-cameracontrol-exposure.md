---
title: KSPROPERTY_CAMERACONTROL_EXPOSURE
description: User-mode clients use the KSPROPERTY_CAMERACONTROL_EXPOSURE property to get or set a digital camera's exposure time. This property is optional.
keywords: ["KSPROPERTY_CAMERACONTROL_EXPOSURE Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_CAMERACONTROL_EXPOSURE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/14/2021
---

# KSPROPERTY_CAMERACONTROL_EXPOSURE

User-mode clients use the **KSPROPERTY_CAMERACONTROL_EXPOSURE** property to get or set a digital camera's exposure time. This property is optional.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | Yes | Filter or node | [**KSPROPERTY_CAMERACONTROL_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s) or [**KSPROPERTY_CAMERACONTROL_NODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s) | LONG |

The property value (operation data) is a LONG that specifies the length of exposure.

This value is expressed in log base 2 seconds, thus, for values less than zero, the exposure time is 1/2n seconds. For positive values and zero, the exposure time is 2n seconds. For example:

| Value | Seconds |
|--|--|
| -7 | 1/128 |
| -6 | 1/64 |
| -5 | 1/32 |
| -4 | 1/16 |
| -3 | 1/8 |
| -2 | 1/4 |
| -1 | 1/2 |
| 0 | 1 |
| 1 | 2 |

## Remarks

The **Value** member of the KSPROPERTY_CAMERACONTROL_S structure specifies the length of exposure.

Every video capture minidriver that supports this property must define its own range and default value for this property.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_CAMERACONTROL_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s)
