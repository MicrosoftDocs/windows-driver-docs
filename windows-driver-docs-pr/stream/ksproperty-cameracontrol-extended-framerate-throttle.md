---
title: KSPROPERTY_CAMERACONTROL_EXTENDED_FRAMERATE_THROTTLE
description: KSPROPERTY_CAMERACONTROL_EXTENDED_FRAMERATE_THROTTLE is a dynamic control that reduces the frame rate of the video by a scale factor of the original frame rate.
ms.date: 04/04/2024
ms.topic: reference
---

# KSPROPERTY_CAMERACONTROL_EXTENDED_FRAMERATE_THROTTLE

**KSPROPERTY_CAMERACONTROL_EXTENDED_FRAMERATE_THROTTLE** is a dynamic control that reduces the frame rate of the video by a scale factor of the original frame rate.

## Usage summary table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | [**KSPROPERTY**](ksproperty-structure.md) | [**KSCAMERA_EXTENDEDPROP_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) |

The property value (operation data) contains a [**KSCAMERA_EXTENDEDPROP_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure and a [**KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_videoprocsetting) structure.

The total property data size is **sizeof**(KSCAMERA_EXTENDEDPROP_HEADER) + **sizeof**(KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING). The **Size** member of [**KSCAMERA_EXTENDEDPROP_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) is set to this total property data size.

The **Capability** member of [**KSCAMERA_EXTENDEDPROP_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) contains one of the following values.

| Frame rate throttle control | Description |
|--|--|
| KSCAMERA_EXTENDEDPROP_FRAMERATE_THROTTLE_OFF | Framerate Throttle is disabled. |
| KSCAMERA_EXTENDEDPROP_FRAMERATE_THROTTLE_ON | Framerate Throttle is enabled. |

The **Flags** member of [**KSCAMERA_EXTENDEDPROP_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) contains the flag currently set for the camera. KSCAMERA_EXTENDEDPROP_FRAMERATE_THROTTLE_OFF should be the default.

This property control is synchronous and not cancelable.

This control only applies while the camera is actively streaming. To be actively streaming means a preview or record pin must be in KSSTATE_RUN, ready and able to deliver frames. On a set if a stream isn't active, then this control should return STATUS_INVALID_DEVICE_STATE. Even as this is a Filter scope control, this shouldn't impact photo-pin or non-RGB streams such as IR/depth.

## Remarks

### Get the property

When responding to a KSPROPERTY_TYPE_GET request, the driver sets the members of the [**KSCAMERA_EXTENDEDPROP_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) to the following.

| Member | Value |
|--|--|
| Version | 1 |
| PinId | KSCAMERA_EXTENDEDPROP_FILTERSCOPE (0xFFFFFFFF) |
| Size | Must be **sizeof**(KSCAMERA_EXTENDEDPROP_HEADER) + **sizeof**(KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING) |
| Result | Must be 0. This field is used to return the result of last SET operation. |
| Capability | KSCAMERA_EXTENDEDPROP_FRAMERATE_THROTTLE_ON or 0x1 |
| Flags | This can either be KSCAMERA_EXTENDEDPROP_FRAMERATE_THROTTLE_ON or KSCAMERA_EXTENDEDPROP_FRAMERATE_THROTTLE_OFF. |

If no framerate throttle flag previously set, then the driver sets **Flags** to KSCAMERA_EXTENDEDPROP_FRAMERATE_THROTTLE_OFF. The members of the [**KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_videoprocsetting) structure that follows [**KSCAMERA_EXTENDEDPROP_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) are set according to the requirements of the framerate throttle mode.

### Set the property

When the property is set, a KSPROPERTY_TYPE_SET request, the **Flags** member of [**KSCAMERA_EXTENDEDPROP_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) contains the framerate throttle mode to set. The **VideoProc.Value** member of [**KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_videoprocsetting) must be ignored when **Flags** contains the KSCAMERA_EXTENDEDPROP_FRAMERATE_THROTTLE_OFF flag.

### Payload structure

The following table contains the descriptions and requirements for the **KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING** structure fields for the Framerate Throttle DDI. This structure is defined in ksmedia.h.

| Member | Description |
|--|--|
| Mode | This is unused and must be 0. |
| Min/Max/Step | The Max must be 100, which indicates no change in frame rate. The Step should be a factor of 100 such that Max % Step == 0. Min should be equal to at least one step size or a multiple of the step size. Min can't be 0. |
| VideoProc | The VideoProc.Value.ul must specify the scale factor percentage for this control. This value should be within the range of Min and Max, and it should be set to a multiple of the Step value.<br>By setting this value appropriately an application can make sure that the new frame rate never exceeds the original value, nor go to zero. For example, setting a value of 80 would produce a frame rate of 80% of the original frame rate. |
| Reserved | This is unused. This must be ignored by the driver. |

## Requirements

**Minimum supported client:** Windows 11, version 24H2

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSCAMERA_EXTENDEDPROP_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header)

[**KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_videoprocsetting)
