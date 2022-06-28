---
title: KSPROPERTY_CAMERACONTROL_TILT
description: User-mode clients use the KSPROPERTY_CAMERACONTROL_TILT property to get or set a camera's tilt setting. This property is optional.
keywords: ["KSPROPERTY_CAMERACONTROL_TILT Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_TILT
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/18/2021
---

# KSPROPERTY_CAMERACONTROL_TILT

User-mode clients use the **KSPROPERTY_CAMERACONTROL_TILT** property to get or set a camera's tilt setting. This property is optional.

### Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter or node | [**KSPROPERTY_CAMERACONTROL_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s) or [**KSPROPERTY_CAMERACONTROL_NODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s) | LONG |

The property value (operation data) is a LONG that specifies a camera's tilt setting. This value is expressed in degrees.

Positive values point the imaging plane up. Negative values point the imaging plane down, as shown in the following illustration.

![illustration showing camera tilt values.](images/cam-tilt-1.png)

Every video capture minidriver that supports this property must define a range and default value for this property. The range for the device must -180 through +180. The default value must be 0.

> [!CAUTION]
> When writing or testing an app, you should be aware that in practice, some drivers define a custom range of tilt values and custom step values that might not be based on typical units. Drivers might implement the tilt control either physically or digitally.

## Remarks

The **Value** member of the KSPROPERTY_CAMERACONTROL_S structure specifies the tilt setting.

For cameras using the [Platform DMFT](https://docs.microsoft.com/en-us/windows-hardware/drivers/stream/uvc-camera-implementation-guide#platform-device-mft) for face-based 3A, the Pan control impacts the output window of the camera. The face coordinates produced by the Platform DMFT will be relative to this modified output window, so the camera is responsible for remapping the ROI coordinates to the camera's full field of view when the current field of view is modified by the Pan control.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_CAMERACONTROL_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s)
