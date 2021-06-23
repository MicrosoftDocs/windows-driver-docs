---
title: KSPROPERTY_CAMERACONTROL_EXTENDED_EYEGAZECORRECTION
description: KSPROPERTY_CAMERACONTROL_EXTENDED_EYEGAZECORRECTION is a property ID used to control the eye gaze correction on the driver.
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_EYEGAZECORRECTION Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_EYEGAZECORRECTION
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 06/24/2021
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY_CAMERACONTROL_EXTENDED_EYEGAZECORRECTION

**KSPROPERTY_CAMERACONTROL_EXTENDED_EYEGAZECORRECTION** is a property ID used to control the eye gaze correction on the driver.

This property ID controls an in-stream correction that a driver can perform to enable high quality image correction for use with preview and recorded images. The in-stream correction need to be enabled and disabled in the driver in a uniform way, so that the features may be controlled by either Windows or an application.

Examples of setting KSPROPERTY controls can be found in the [AVStream Camera Sample Driver](https://github.com/microsoft/Windows-driver-samples/tree/master/avstream/avscamera) on GitHub.

## Usage summary table

| Scope | Control | Type |
|--|--|--|
| Version 1 | Filter | Synchronous |

The following flags can be placed in the **KSCAMERA_EXTENDEDPROP_HEADER.Flags** field to control eye gaze correction. The default should be KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_OFF.

```cpp
#define KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_OFF     0x0000000000000000
#define KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_ON      0x0000000000000001
```

If the driver supports this control, it must support KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_ON and KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_OFF.

If the driver does not support eye gaze correction, the driver should not implement this control.

The SET call of this control shall take effect even when the video or photo pin is in the **KSSTATE_RUN** state. In a GET call, driver should return the current settings in Flags field.

The following table describes the flag capabilities.

| Flag | Description |
|--|--|
| KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_OFF | This is a mandatory capability. When specified, the eye gaze correction is disabled in the driver. |
| KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_ON | This is a mandatory capability. When specified, the eye gaze correction is enabled in the driver.  |

The following table contains the descriptions and requirements for the [KSCAMERA_EXTENDEDPROP_HEADER](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure fields when using the control.

| Member | Description |
|--|--|
| Version | This must be 1. |
| PinId | KSCAMERA_EXTENDEDPROP_FILTERSCOPE (0xFFFFFFFF) |
| Size | This must be sizeof([KSCAMERA_EXTENDEDPROP_HEADER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header)) + sizeof([KSCAMERA_EXTENDEDPROP_VALUE](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value)) |
| Result | Unused, must be 0. |
| Capability | Must be a bit wise **OR** of the supported ***KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_XXX*** flags defined above. |
| Flags | This is a read/write field. This can be any one of the ***KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_XXX*** flags defined above. |

## Requirements

**Minimum supported client:** Windows 11

**Header:** ksmedia.h (include Ksmedia.h)
