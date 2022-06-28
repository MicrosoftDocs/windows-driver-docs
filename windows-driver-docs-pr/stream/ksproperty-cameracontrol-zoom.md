---
title: KSPROPERTY_CAMERACONTROL_ZOOM
description: User-mode clients use the KSPROPERTY_CAMERACONTROL_ZOOM property to get or set a camera's zoom setting. This property is optional.
keywords: ["KSPROPERTY_CAMERACONTROL_ZOOM Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_ZOOM
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/18/2021
---

# KSPROPERTY_CAMERACONTROL_ZOOM

User-mode clients use the **KSPROPERTY_CAMERACONTROL_ZOOM** property to get or set a camera's zoom setting. This property is optional.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter or node | [**KSPROPERTY_CAMERACONTROL_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s) or [**KSPROPERTY_CAMERACONTROL_NODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s) | LONG |

The property value (operation data) is a LONG that specifies a camera's zoom setting. This value is expressed in millimeters.

> [!CAUTION]
> When writing or testing an app, you should be aware that in practice, some drivers define a custom range of zoom values and custom step values that might not be based on typical units. Drivers might implement the zoom control either physically or digitally.

## Remarks

The **Value** member of the **KSPROPERTY_CAMERACONTROL_S** structure specifies the zoom.

Every video capture minidriver that supports this property must define a range and default value for this property. The range for the device must be 10 through 600. The default value must be 10.

For cameras using the [Platform DMFT](https://docs.microsoft.com/en-us/windows-hardware/drivers/stream/uvc-camera-implementation-guide#platform-device-mft) for face-based 3A, the Zoom control impacts the output window of the camera. The face coordinates produced by the Platform DMFT will be relative to this modified output window, so the camera is responsible for remapping the ROI coordinates to the camera's full field of view when the current field of view is modified by the Zoom control.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_CAMERACONTROL_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s)
