---
title: KSPROPERTY_CAMERACONTROL_EXTENDED_DIGITALWINDOW
description: KSPROPERTY_CAMERACONTROL_EXTENDED_DIGITALWINDOW is a property ID that specifies the field of view and zoom of the camera while the camera is streaming.
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_DIGITALWINDOW Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_DIGITALWINDOW
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 06/24/2021
ms.topic: article
---

# KSPROPERTY_CAMERACONTROL_EXTENDED_DIGITALWINDOW

**KSPROPERTY_CAMERACONTROL_EXTENDED_DIGITALWINDOW** is a property ID that specifies the field of view and zoom of the camera while the camera is streaming.

This control is a potential substitute for pan, tilt and zoom.  This control only applies while the camera is actively streaming.  To be actively streaming means a preview or record pin must be in **KSSTATE_RUN**, ready and able to deliver frames.

On SET, if a stream is not active, this controls returns **STATUS_INVALID_DEVICE_STATE**.

Examples of setting KSPROPERTY controls can be found in the [AVStream Camera Sample Driver](https://github.com/Microsoft/Windows-driver-samples/tree/main/avstream/avscamera) on GitHub.

## Usage summary table

| Scope | Control | Type |
|--|--|--|
| Version 1 | Filter | Synchronous |

The following bit flags control the property ID in the driver:

```cpp
#define KSCAMERA_EXTENDEDPROP_DIGITALWINDOW_MANUAL             0x0000000000000000
#define KSCAMERA_EXTENDEDPROP_DIGITALWINDOW_AUTOFACEFRAMING    0x0000000000000001
```

## Capability description

The following flags can be placed in the **KSCAMERA_EXTENDEDPROP_HEADER.Flags** and **KSCAMERA_EXTENDEDPROP_HEADER.Capability** fields.

| Flag | Description |
|--|--|
| KSCAMERA_EXTENDEDPROP_DIGITALWINDOW_MANUAL | The Digital Window is controlled manually by the application. |
| KSCAMERA_EXTENDEDPROP_DIGITALWINDOW_AUTOFACEFRAMING | The camera automatically adjusts the Digital Window to focus on the dominate face in view. |

**KSCAMERA_EXTENDEDPROP_DIGITALWINDOW** is always a synchronous control.

The following table contains the requirements for the [KSCAMERA_EXTENDEDPROP_HEADER](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure fields when using the metadata control.

| Member | Description |
|--|--|
| Version | Must be 1. |
| PinId | KSCAMERA_EXTENDEDPROP_FILTERSCOPE (0xFFFFFFFF) |
| Size | Must be sizeof([KSCAMERA_EXTENDEDPROP_HEADER](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header))+ sizeof(**KSCAMERA_EXTENDEDPROP_DIGITALWINDOW_SETTING**)  |
| Result | Must contain 0.  This field is only used to return the result of the last asynchronous SET operation. |
| Capability | Must support KSCAMERA_EXTENDEDPROP_DIGITALWINDOW_MANUAL. May optionally support KSCAMERA_EXTENDEDPROP_DIGITALWINDOW_AUTOFACEFRAMING. |
| Flags | Must be KSCAMERA_EXTENDEDPROP_DIGITALWINDOW_MANUAL or KSCAMERA_EXTENDEDPROP_DIGITALWINDOW_AUTOFACEFRAMING. |

## KSCAMERA_EXTENDEDPROP_DIGITALWINDOW_SETTING

These parameters are read-only if KSCAMERA_EXTENDEDPROP_DIGITALWINDOW_AUTOFACEFRAMING is set in the Flags field.  If KSCAMERA_EXTENDEDPROP_DIGITALWINDOW_AUTOFACEFRAMING is set during a SET operation, the following parameters are ignored.

| Parameter | Description |
|--|--|
| OriginX | The origin of the digital window along the X-axis in Q24 format.  Must default to 0.  OriginX may not be less than PorchLeft nor greater than PorchRight – WindowSize. |
| OriginY | The origin of the digital window along the X-axis in Q24 format.  Must default to 0.  OriginX may not be less than PorchLeft nor greater than PorchRight – WindowSize. |
| WindowSize | The size of the digital window along both axis in Q24 format. This is the fraction of the full view visible along both the x and y axis.  WindowSize must default to 0x01000000 (1.0 in Q24). WindowSize may not be less than MinWindowSize nor larger than MaxWindowSize. In addition, WindowSize plus OriginX may not be greater than PorchRight; WindowsSize plus OriginY may not be greater than PorchBottom. |
| Reserved | Set to 0. |

## Requirements

**Minimum supported client:** Windows 11

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[KSCAMERA_EXTENDEDPROP_DIGITALWINDOW_CONFIGCAPS](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kscamera_extendedprop_digitalwindow_configcaps)

[KSCAMERA_EXTENDEDPROP_DIGITALWINDOW_CONFIGCAPSHEADER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kscamera_extendedprop_digitalwindow_configcapsheader)

[KSCAMERA_EXTENDEDPROP_DIGITALWINDOW_SETTING](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kscamera_extendedprop_digitalwindow_setting)

[KSCAMERA_METADATA_DIGITALWINDOW](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kscamera_metadata_digitalwindow)
