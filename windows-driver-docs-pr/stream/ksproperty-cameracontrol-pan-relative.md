---
title: KSPROPERTY_CAMERACONTROL_PAN_RELATIVE
description: The KSPROPERTY_CAMERACONTROL_PAN_RELATIVE property specifies a camera's rotation around the vertical axis.
keywords: ["KSPROPERTY_CAMERACONTROL_PAN_RELATIVE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_PAN_RELATIVE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/14/2021
---

# KSPROPERTY_CAMERACONTROL_PAN_RELATIVE

The **KSPROPERTY_CAMERACONTROL_PAN_RELATIVE** property specifies a camera's rotation around the vertical axis.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | Yes | Filter or node | [**KSPROPERTY_CAMERACONTROL_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s) or [**KSPROPERTY_CAMERACONTROL_NODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s) | LONG |

The property value (operation data) is a LONG that specifies a camera's relative pan setting. The size of the value represents the desired pan speed; a higher value represents a higher speed.

| Value | Description |
|--|--|
| 0 | Stop panning. |
| Positive value | Start panning to the right. |
| Negative value | Start panning to the left. |

## Remarks

The **Value** member of the [**KSPROPERTY_CAMERACONTROL_NODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s) structure specifies the relative pan.

Note that a particular device might support only a certain speed range. To determine the range of speeds supported by the device, an application can issue a **KSPROPERTY_TYPE_BASICSUPPORT** request. You can specify **KSPROPERTY_TYPE_BASICSUPPORT** in the **Flags** member of the [**KSPROPERTY_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_item) structure.

Some devices support only a single pan speed. In this case, the sign of the **Value** member indicates which direction to pan.

When making a set request, the client should supply one of the values in the preceding table in the **Value** member of the **KSPROPERTY_CAMERACONTROL_NODE_S** structure.

When making a get request, the client receives one of the values in the preceding table in the **Value** member of the **KSPROPERTY_CAMERACONTROL_NODE_S** structure. The value indicates the current pan status of the camera.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY_CAMERACONTROL_NODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s)
