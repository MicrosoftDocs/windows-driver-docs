---
title: KSPROPERTY_CAMERACONTROL_ZOOM_RELATIVE
description: The KSPROPERTY_CAMERACONTROL_ZOOM_RELATIVE property specifies the zoom status of the camera.
keywords: ["KSPROPERTY_CAMERACONTROL_ZOOM_RELATIVE Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_CAMERACONTROL_ZOOM_RELATIVE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/18/2021
---

# KSPROPERTY_CAMERACONTROL_ZOOM_RELATIVE

The **KSPROPERTY_CAMERACONTROL_ZOOM_RELATIVE** property specifies the zoom status of the camera.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter or node | [**KSPROPERTY_CAMERACONTROL_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s) or [**KSPROPERTY_CAMERACONTROL_NODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s) | LONG |

The property value (operation data) is a LONG that specifies a camera's relative zoom setting. The size of the value represents the desired zoom speed; a higher value represents a higher speed.

| Value | Description |
|--|--|
| 0 | Stop zoom lens motion. |
| Positive value | Start moving the zoom lens in the telephoto direction (initiate zoom-in). |
| Negative value | Start moving the zoom lens in the wide angle direction (initiate zoom-out). |

## Remarks

The **Value** member of the [**KSPROPERTY_CAMERACONTROL_NODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s) structure specifies the relative zoom.

Note that a particular device might support only a certain speed range. To determine the range of speeds supported by the device, an application can issue a **KSPROPERTY_TYPE_BASICSUPPORT** request. You can specify **KSPROPERTY_TYPE_BASICSUPPORT** in the **Flags** member of the [**KSPROPERTY_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_item) structure.

Some devices support only a single zoom speed. In this case, the sign of the **Value** member indicates whether the lens should zoom in or zoom out.

When making a set request, the client should supply one of the values in the preceding table in the **Value** member of the **KSPROPERTY_CAMERACONTROL_NODE_S** structure.

When making a get request, the client receives one of the values in the preceding table in the **Value** member of the **KSPROPERTY_CAMERACONTROL_NODE_S** structure. The value indicates the current zoom status of the camera.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY_CAMERACONTROL_NODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s)
