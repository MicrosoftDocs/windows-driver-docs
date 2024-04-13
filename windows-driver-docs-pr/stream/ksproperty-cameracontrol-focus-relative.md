---
title: KSPROPERTY_CAMERACONTROL_FOCUS_RELATIVE
description: The KSPROPERTY_CAMERACONTROL_FOCUS_RELATIVE property specifies the focus setting of the camera.
keywords: ["KSPROPERTY_CAMERACONTROL_FOCUS_RELATIVE Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_CAMERACONTROL_FOCUS_RELATIVE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/14/2021
---

# KSPROPERTY_CAMERACONTROL_FOCUS_RELATIVE

The **KSPROPERTY_CAMERACONTROL_FOCUS_RELATIVE** property specifies the focus setting of the camera.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | Yes | Filter or node | [**KSPROPERTY_CAMERACONTROL_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s) or [**KSPROPERTY_CAMERACONTROL_NODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s) | LONG |

The property value (operation data) is a LONG that specifies a camera's relative focus setting. The size of the value represents the speed at which the focal point changes; a higher value represents a higher speed.

| Value | Description |
|--|--|
| 0 | Stop focus motion. |
| Positive value | Start moving the focus closer to the object. |
| Negative value | Start moving the focus farther away from the object. |

## Remarks

When making a set request, provide one of the values in the preceding table in the **Value** member of the **KSPROPERTY_CAMERACONTROL_NODE_S** structure.

When making a get request, the client receives one of the values in the preceding table in the **Value** member of the **KSPROPERTY_CAMERACONTROL_NODE_S** structure. The value indicates the current focus setting for the camera.

Note that a particular device might support only a certain speed range. To determine the range of speeds supported by the device, an application can issue a **KSPROPERTY_TYPE_BASICSUPPORT** request. You can specify **KSPROPERTY_TYPE_BASICSUPPORT** in the **Flags** member of the [**KSPROPERTY_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_item) structure.

Some devices support only a single focus speed. In this case, the sign of the **Value** member simply indicates whether the lens should shorten its focus or lengthen it.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY_CAMERACONTROL_NODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s)
