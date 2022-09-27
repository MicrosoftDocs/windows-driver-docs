---
title: KSPROPERTY_CAMERACONTROL_EXTENDED_BACKGROUNDSEGMENTATION
description: KSPROPERTY_CAMERACONTROL_EXTENDED_BACKGROUNDSEGMENTATION is a property ID used to control the background blur on the driver.
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_BACKGROUNDSEGMENTATION Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_BACKGROUNDSEGMENTATION
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 09/19/2022
ms.topic: article
---

# KSPROPERTY_CAMERACONTROL_EXTENDED_BACKGROUNDSEGMENTATION

**KSPROPERTY_CAMERACONTROL_EXTENDED_BACKGROUNDSEGMENTATION** is a property ID used to control the background blur on the driver.

This property controls an in-stream correction that a driver can perform to enable high quality image correction for use with preview and recorded images. The in-stream correction need to be enabled and disabled in the driver in a uniform way, so that the features may be controlled by either Windows or an application.

Examples of setting KSPROPERTY controls can be found in the [AVStream Camera Sample Driver](https://github.com/Microsoft/Windows-driver-samples/tree/main/avstream/avscamera) on GitHub.

## Update to KSPROPERTY_CAMERACONTROL_EXTENDED_BACKGROUNDSEGMENTATION control

Starting in Windows 11, version 22H2, Shallow focus mode has been introduced to the existing background segmentation control as an optional capability.

 **KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_SHALLOWFOCUS** is a new flag added to the KSPROPERTY_CAMERACONTROL_EXTENDED_BACKGROUNDSEGMENTATION control that is used to control the Bokeh (shallow focus mode) on the driver. This is a version of Background blur **KSPROPERTY_CAMERACONTROL_EXTENDED_BACKGROUNDSEGMENTATION**, where the emphasis is less on privacy and more on making the background of the user look like from a higher quality camera with depth of field effect. This visually will make the foreground subject stand out, similar to how portrait mode photography on many mobile phones has become popular.

## Usage summary table

| Scope | Control | Type |
|--|--|--|
| Version 1 | Filter | Synchronous |

The following flags can be placed in the **KSCAMERA_EXTENDEDPROP_HEADER.Flags** field to control shallow focus mode.

```cpp
#define KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_OFF          0x0000000000000000
#define KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_BLUR         0x0000000000000001
#define KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_MASK         0x0000000000000002
#define KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_SHALLOWFOCUS 0x0000000000000004
```

If the driver supports this control, it must support BACKGROUNDSEMENTATION_OFF and one or more of the other flags.

If the driver does not support background segmentation, the driver should not implement this control.

The SET call of this control shall take effect even when the video or photo pin is in the KSSTATE_RUN state. In a GET call, driver should return the current settings in Flags field.

The following table describes the flag capabilities.

| Flag | Description |
|--|--|
| **KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_OFF** | This is a mandatory capability. When specified, the background segmentation is disabled in the driver. This is the default value. |
| **KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_BLUR** | This is an optional capability. When specified, background blur is enabled in the driver and applies to frame if possible. |
| **KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_MASK** | This is an optional capability. When specified, background mask metadata production is enabled in the driver (if possible given the MediaType used as expressed via the set of KSPROPERTY_CAMERACONTROL_EXTENDED_ BACKGROUNDSEGMENTATION_CONFIGCAPS returned in the *Size* field of the KSCAMERA_EXTENDEDPROP_HEADER). Note that this can be supported not only for color cameras but also depth and IR cameras. |
| **KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_SHALLOWFOCUS** | This is an optional capability. When specified together with KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_BLUR , the shallow focus is enabled in the driver. |

> [!NOTE]
> From a SET perspective, **KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_SHALLOWFOCUS** needs to be added along with **KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_BLUR** to take effect;  They can also be set along with **KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_MASK**.

The table below contains the descriptions and requirements for the [KSCAMERA_EXTENDEDPROP_HEADER](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure fields when using the control.

| Member | Description |
|--|--|
| Version | This must be 1. |
| PinId | This must be **KSCAMERA_EXTENDEDPROP_FILTERSCOPE** (0xFFFFFFFF). |
| Size | This must be **sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VALUE)**. |
| Result | Unused, must be 0. |
| Capability | Must be a bitwise OR of the supported **KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION _*** flags defined above. |
| Flags | This is a read/write field. This can be any one of the **KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION _*** flags defined above except SHALLOWFOCUS (which needs to be set together with BLUR to take effect), or valid combinations of the bits. From a SET perspective, shallow focus mode will be enabled only when both SHALLOWFOCUS and BLUR are set at the same time, they can be set along with MASK.|

## Requirements

**Minimum supported client:** Windows 11, version 22H2

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[Background segmentation portrait mode and eye gaze stare mode driver sample](background-segmentation-portrait-mode-eye-gaze-stare-mode-driver-sample.md)

[KSPROPERTY_CAMERACONTROL_EXTENDED_EYEGAZECORRECTION](ksproperty-cameracontrol-extended-eyegazecorrection.md)

[KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_CONFIGCAPS](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kscamera_extendedprop_backgroundsegmentation_configcaps)

[KSCAMERA_EXTENDEDPROP_HEADER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header)
