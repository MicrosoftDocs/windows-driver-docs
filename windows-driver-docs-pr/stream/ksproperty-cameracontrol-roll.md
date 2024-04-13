---
title: KSPROPERTY_CAMERACONTROL_ROLL
description: User-mode clients use the KSPROPERTY_CAMERACONTROL_ROLL property to get or set a camera's roll setting. This property is optional.
keywords: ["KSPROPERTY_CAMERACONTROL_ROLL Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_CAMERACONTROL_ROLL
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/18/2021
---

# KSPROPERTY_CAMERACONTROL_ROLL

User-mode clients use the **KSPROPERTY_CAMERACONTROL_ROLL** property to get or set a camera's roll setting. This property is optional.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter or node | [**KSPROPERTY_CAMERACONTROL_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s) or [**KSPROPERTY_CAMERACONTROL_NODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s) | LONG |

The property value (operation data) is a LONG that specifies a camera's roll setting. This value is expressed in degrees.

Positive values cause a clockwise rotation of the camera along the image-viewing axis. Negative values cause a counterclockwise rotation of the camera, as shown in the following illustration.

![illustration showing camera roll values.](images/cam-roll-1.png)

Every video capture minidriver that supports this property must define a range and default value for this property. The range for the device must be -180 through +180 and the default value must be 0.

## Remarks

The **Value** member of the KSPROPERTY_CAMERACONTROL_S structure specifies the roll setting.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_CAMERACONTROL_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s)
