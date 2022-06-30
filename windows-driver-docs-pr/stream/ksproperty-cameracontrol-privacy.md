---
title: KSPROPERTY_CAMERACONTROL_PRIVACY
description: The KSPROPERTY_CAMERACONTROL_PRIVACY property specifies whether to prevent video from being acquired by the camera sensor.
keywords: ["KSPROPERTY_CAMERACONTROL_PRIVACY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_PRIVACY
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/14/2021
---

# KSPROPERTY_CAMERACONTROL_PRIVACY

The **KSPROPERTY_CAMERACONTROL_PRIVACY** property specifies whether to prevent video from being acquired by the camera sensor.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No* | Filter or node | [**KSPROPERTY_CAMERACONTROL_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s) or [**KSPROPERTY_CAMERACONTROL_NODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s) | LONG |

The property value (operation data) is a LONG that specifies whether privacy mode is enable or disabled. A value of 0 indicates that the camera sensor can capture video images, and a value of 1 indicates that the camera sensor is prevented from capturing video images.

[*] Starting with Windows 11, **Set** support is disallowed on this control. Software-controllable privacy modes (e.g., control of camera blanking features, electromechanical shutter states, etc.) provide a false sense of security since they can be reversed by any application that writes this property. Camera privacy features such as shutters or kill switches must be exclusively controlled via physical interaction with the device, as described in [Camera privacy shutters and kill switches](camera-privacy-controls.md). 

## Remarks

The **Value** member of the **KSPROPERTY_CAMERACONTROL_NODE_S** structure specifies whether the camera sensor should capture video.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY_CAMERACONTROL_NODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s)
