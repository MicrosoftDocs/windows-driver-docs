---
title: KSPROPERTY_CAMERACONTROL_PANTILT_RELATIVE
description: The KSPROPERTY_CAMERACONTROL_PANTILT_RELATIVE property specifies horizontal or vertical rotation of the camera and can specify both simultaneously.
keywords: ["KSPROPERTY_CAMERACONTROL_PANTILT_RELATIVE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_PANTILT_RELATIVE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/14/2021
ms.localizationpriority: medium
---

# KSPROPERTY_CAMERACONTROL_PANTILT_RELATIVE

The **KSPROPERTY_CAMERACONTROL_PANTILT_RELATIVE** property specifies horizontal or vertical rotation of the camera and can specify both simultaneously.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter or node | [**KSPROPERTY_CAMERACONTROL_NODE_S2**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s2) or [**KSPROPERTY_CAMERACONTROL_S2**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s2) depending on whether the request is for a filter or a node | Pair of LONG integers |

The property value (operation data) is a pair of LONG integers that specify a camera's relative pan and tilt settings. The size of the value represents the desired pan speed; a higher value represents a higher speed.

| Value1 | Description |
|--|--|
| 0 | Stop the horizontal motion of the camera. |
| Positive value | Start panning to the right. |
| Negative value | Start panning to the left. |

The size of the value represents the desired tilt speed; a higher value represents a higher speed.

| Value2 | Description |
|--|--|
| 0 | Stop the vertical motion of the camera. |
| Positive value | Start rotating the camera up. |
| Negative value | Start rotating the camera down. |

## Remarks

When making a set request to pan the camera, the client should supply one of the values in the preceding table in **Value1** member of the property descriptor structure.

Similarly, when making a set request to tilt the camera, the client supplies one of the values in the preceding table in **Value2** member of the property descriptor structure.

When making a get request, the client receives the pan value in the **Value1** member and the tilt value in the **Value2** member of the **KSPROPERTY_CAMERACONTROL_S2** or **KSPROPERTY_CAMERACONTROL_NODE_S2** structure. The values indicate the current pan or tilt status of the camera.

Note that a particular device might support only a certain speed range. To determine the range of speeds supported by the device, an application can issue a **KSPROPERTY_TYPE_BASICSUPPORT** request. You can specify **KSPROPERTY_TYPE_BASICSUPPORT** in the **Flags** member of the [**KSPROPERTY_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_item) structure.

Some devices support only a single pan or tilt speed. In this case, the sign of the **Value1** or **Value2** member indicates which direction to pan.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY_CAMERACONTROL_S2**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s2)

[**KSPROPERTY_CAMERACONTROL_NODE_S2**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s2)
