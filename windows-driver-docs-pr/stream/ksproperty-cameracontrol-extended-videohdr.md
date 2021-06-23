---
title: KSPROPERTY_CAMERACONTROL_EXTENDED_VIDEOHDR
description: KSPROPERTY_CAMERACONTROL_EXTENDED_VIDEOHDR is used to enable or disable high dynamic range (HDR) video on the driver. This is a pin level control for video pin only.
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_VIDEOHDR Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_VIDEOHDR
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 06/24/2021
ms.localizationpriority: medium
---

# KSPROPERTY_CAMERACONTROL_EXTENDED_VIDEOHDR

**KSPROPERTY_CAMERACONTROL_EXTENDED_VIDEOHDR** is used to enable or disable high dynamic range (HDR) video on the driver. This is a pin level control for video pin only.

## Usage summary table

| Get | Set | Target | Property Descriptor Type |
|--|--|--|--|
| Yes | Yes | Pin | KSPROPERTY_CAMERACONTROL_EXTENDED_VIDEOHDR |

The following flags can be placed in the KSCAMERA_EXTENDEDPROP_HEADER.Flags field to control video HDR. By default, driver should be set to VIDEOHDR_OFF.

```cpp
#define KSCAMERA_EXTENDEDPROP_VIDEOHDR_OFF      0x0000000000000000
#define KSCAMERA_EXTENDEDPROP_VIDEOHDR_ON       0x0000000000000001 
#define KSCAMERA_EXTENDEDPROP_VIDEOHDR_AUTO     0x0000000000000002 
```

If the driver supports this control, it must support VIDEOHDR_ON/VIDEOHDR_OFF.

If the driver does not support video HDR, the driver should not implement this control.

This control serves as a hint to the driver. When set to VIDEOHDR_ON, the driver should perform video HDR as the best effort.

The SET call of this control has no effect when the video pin is KSSTATE_RUN state. The driver shall reject the SET call received if video pin is in a running state and returns STATUS_INVALID_DEVICE_STATE. In a GET call, driver should return the current settings in the Flags field.

The following table describes the flag capabilities.

| Flag | Description |
|--|--|
| KSCAMERA_EXTENDEDPROP_VIDEOHDR_OFF | This is a mandatory capability. When specified, the video HDR is disabled in the driver and the driver shall not perform video HDR on the video stream. |
| KSCAMERA_EXTENDEDPROP_VIDEOHDR_ON | This is a mandatory capability. When specified, the video HDR is enabled in the driver and the driver shall perform video HDR as the best effort. This flag is mutually exclusive with the VIDEOHDR_AUTO and VIDEOHDR_OFF flags. |
| KSCAMERA_EXTENDEDPROP_VIDEOHDR_AUTO | This capability is optional. When specified, the driver that supports such capability will determine whether video HDR should be performed based on the scene analysis. This flag is mutually exclusive with the VIDEOHDR_ON and VIDEOHDR_OFF flags. |

The table below contains the descriptions and requirements for the [KSCAMERA_EXTENDEDPROP_HEADER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure fields when using the control.

| Member | Description |
|--|--|
| Version | This must be 1. |
| PinId | Must be the Pin ID associated with the video pin. |
| Size | This must be sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VALUE). |
| Result | Indicates the error results of the last SET operation. If no SET operation has taken place, this must be 0. |
| Capability | Must be a bitwise OR of the supported KSCAMERA_EXTENDEDPROP_VIDEOHDR_* flags defined above. |
| Flags | This is a read/write field. This can be any one of the KSCAMERA_EXTENDEDPROP_VIDEOHDR_* flags defined above. |

## Requirements

**Minimum supported client:** Windows 11

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[2.2.2.13 Video HDR Control](/windows-hardware/drivers/stream/uvc-extensions-1-5#22213-video-hdr-control)
