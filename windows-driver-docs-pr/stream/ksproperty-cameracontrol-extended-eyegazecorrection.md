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
ms.date: 09/19/2022
ms.topic: article
---

# KSPROPERTY_CAMERACONTROL_EXTENDED_EYEGAZECORRECTION

**KSPROPERTY_CAMERACONTROL_EXTENDED_EYEGAZECORRECTION** is a property ID used to control the eye gaze correction on the driver.

This property ID controls an in-stream correction that a driver can perform to enable high quality image correction for use with preview and recorded images. The in-stream correction need to be enabled and disabled in the driver in a uniform way, so that the features may be controlled by either Windows or an application.

Examples of setting KSPROPERTY controls can be found in the [AVStream Camera Sample Driver](https://github.com/Microsoft/Windows-driver-samples/tree/main/avstream/avscamera) on GitHub.

## Update to KSPROPERTY_CAMERACONTROL_EXTENDED_EYEGAZECORRECTION control

Starting in Windows 11, version 22H2, Stare mode has been introduced to existing eye gaze correction control as an optional capability.

**KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_STARE** is a new flag added to the **KSPROPERTY_CAMERACONTROL_EXTENDED_EYEGAZECORRECTION** control that is used to control the Stare (also known as Teleprompter) mode on the driver.

While the Eye Gaze Correction (also known as Eye Contact) solves for the geometrical problem of camera-display offset, many video scenarios require the user to be looking down at the screen for extended periods of time while also speaking – imagine reading a presentation/document in a call.

Stare is a more aggressive form of Eye Contact that continually shifts the pixels of the eyes to make it look like you are speaking with your audience even though you might be reading off a script and moving the eyeball rapidly.

## Usage summary table

| Scope | Control | Type |
|--|--|--|
| Version 1 | Filter | Synchronous |

The following flags can be placed in the **KSCAMERA_EXTENDEDPROP_HEADER.Flags** field to control the teleprompter mode. The default should be Off.

```cpp
#define KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_OFF   0x0000000000000000
#define KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_ON    0x0000000000000001
#define KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_STARE 0x0000000000000002
```

If the driver supports this control, it must support EYEGAZECORRECTION_OFF and one or more of the other flags.

If the driver does not support eye gaze correction, the driver should not implement this control.

The SET call of this control shall take effect even when the video or photo pin is in the KSSTATE_RUN state. In a GET call, the driver should return the current settings in Flags field.

The following table describes the flag capabilities.

| Flag | Description |
|--|--|
| **KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_OFF** | This is a mandatory capability. When specified, the eye gaze correction is disabled in the driver. |
| **KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_ON** | This is a mandatory capability. When specified, the eye gaze correction is enabled in the driver. |
| **KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_STARE** | This is an optional capability. When specified together with KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_ON, the stare/teleprompter mode is enabled in the driver. |

> [!NOTE]
> From a SET perspective, the stare mode will be enabled only when both **KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_STARE** and **KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_ON** are set at the same time. **KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_OFF** needs to be exclusive to the other two bits.

The table below contains the descriptions and requirements for the [KSCAMERA_EXTENDEDPROP_HEADER](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure fields when using the control.

| Member | Description |
|--|--|
| Version | This must be 1. |
| PinId | This must be **KSCAMERA_EXTENDEDPROP_FILTERSCOPE** (0xFFFFFFFF). |
| Size | This must be **sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VALUE)**. |
| Result | Unused, must be 0. |
| Capability | Must be a bitwise OR of the supported **KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_*** flags defined above. |
| Flags | This is a read/write field. This can be any one of the KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_* flags defined above except STARE(which needs to be set together with ON to take effect), or valid combinations of the bits. From a SET perspective, the stare mode will be enabled only when both KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_STARE and KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_ON are set at the same time. KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_OFF needs to be exclusive to the other two bits. |

## Requirements

**Minimum supported client:** Windows 11, version 22H2

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[Background segmentation portrait mode and eye gaze stare mode driver sample](background-segmentation-portrait-mode-eye-gaze-stare-mode-driver-sample.md)

[KSPROPERTY_CAMERACONTROL_EXTENDED_BACKGROUNDSEGMENTATION](ksproperty-cameracontrol-extended-backgroundsegmentation.md)

[KSCAMERA_EXTENDEDPROP_HEADER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header)
