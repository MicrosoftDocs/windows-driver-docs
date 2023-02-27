---
title: KSPROPERTY_CAMERACONTROL_AUTO_EXPOSURE_PRIORITY
description: The KSPROPERTY_CAMERACONTROL_AUTO_EXPOSURE_PRIORITY property specifies whether the device can dynamically vary the frame rate.
keywords: ["KSPROPERTY_CAMERACONTROL_AUTO_EXPOSURE_PRIORITY Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_CAMERACONTROL_AUTO_EXPOSURE_PRIORITY
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/14/2021
---

# KSPROPERTY_CAMERACONTROL_AUTO_EXPOSURE_PRIORITY

The **KSPROPERTY_CAMERACONTROL_AUTO_EXPOSURE_PRIORITY** property specifies whether the device can dynamically vary the frame rate.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter or node | [**KSPROPERTY_CAMERACONTROL_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s), [**KSPROPERTY_CAMERACONTROL_NODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s) | ULONG |

The property value (operation data) is a ULONG that specifies whether frame rate can be dynamically varied by the device.

| Value | Description |
|--|--|
| 0 | Frame rate must remain constant. |
| 1 | Frame rate can be dynamically varied by the device. |

## Remarks

Auto-exposure priority determines whether the camera can dynamically vary the frame rate depending on lighting conditions.

Without auto-exposure, for instance, if the frame rate is 30 fps, the exposure time cannot exceed 33 ms.

With auto-exposure priority, however, the camera could compensate for low lighting by decreasing the frame rate. For instance, the camera could reduce frame rate to 25 fps, thereby lengthening exposure time to 40 ms.

**KSPROPERTY_CAMERACONTROL_AUTO_EXPOSURE_PRIORITY** maps to the **Low-Light Compensation** check box on the USB Video Class property page.

In order to use **KSPROPERTY_CAMERACONTROL_AUTO_EXPOSURE_PRIORITY**, you must set [**KSPROPERTY_CAMERACONTROL_EXPOSURE**](ksproperty-cameracontrol-exposure.md) to auto. In other words, the camera must be in auto-exposure mode for the auto-exposure-priority mode to be a valid option.

The default value for KSPROPERTY_CAMERACONTROL_AUTO_EXPOSURE_PRIORITY is zero.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY_CAMERACONTROL_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s)

[**KSPROPERTY_CAMERACONTROL_NODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s)
