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
ms.date: 06/24/2021
ms.topic: article
---

# KSPROPERTY_CAMERACONTROL_EXTENDED_BACKGROUNDSEGMENTATION

**KSPROPERTY_CAMERACONTROL_EXTENDED_BACKGROUNDSEGMENTATION** is a property ID used to control the background blur on the driver.

This property controls an in-stream correction that a driver can perform to enable high quality image correction for use with preview and recorded images. The in-stream correction need to be enabled and disabled in the driver in a uniform way, so that the features may be controlled by either Windows or an application.

Examples of setting KSPROPERTY controls can be found in the [AVStream Camera Sample Driver](https://github.com/microsoft/Windows-driver-samples/tree/master/avstream/avscamera) on GitHub.

## Usage summary table

| Scope | Control | Type |
|--|--|--|
| Version 1 | Filter | Synchronous |

The following flags can be placed in the **KSCAMERA_EXTENDEDPROP_HEADER.Flags** field to control background blur. The default should be **KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_OFF**.

```cpp
#define KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_OFF    0x0000000000000000
#define KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_BLUR   0x0000000000000001
#define KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_MASK   0x0000000000000002
```

If the driver supports this control, it must support at least one capability flag (**KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_BLUR**) and **KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_OFF**.

If the driver does not support background segmentation, the driver should not implement this control.

The SET call of this control shall take effect even when the video or photo pin is in the **KSSTATE_RUN** state. In a GET call, driver should return the current settings in the Flags field.

The following table describes the flag capabilities.

| Flag | Description |
|--|--|
| **KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_OFF** | This is a mandatory capability. When specified, the background blur is disabled in the driver. |
| **KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_BLUR** | This is an optional capability. When specified, background blur is enabled in the driver. |
| **KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_MASK** | This is an optional capability. When specified, background mask metadata production is enabled in the driver (if possible given the MediaType used as expressed via the set of  **KSPROPERTY_CAMERACONTROL_EXTENDED_BACKGROUNDSEGMENTATION_CONFIGCAPS** returned in the Size field of the **KSCAMERA_EXTENDEDPROP_HEADER**). Note that this can be supported not only for color cameras but also depth and IR cameras. |

The following table contains the descriptions and requirements for the [KSCAMERA_EXTENDEDPROP_HEADER](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure fields when using the control.

| Member | Description |
|--|--|
| Version | This must be 1. |
| PinId | KSCAMERA_EXTENDEDPROP_FILTERSCOPE (0xFFFFFFFF) |
| Size | If the Capability field exposes support for **KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_MASK**, this must be sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + N * sizeof(KSPROPERTY_CAMERACONTROL_EXTENDED_ BACKGROUNDSEGMENTATION_CONFIGCAPS), where N can be inferred from (size - sizeof(KSCAMERA_EXTENDEDPROP_HEADER)) / sizeof(KSPROPERTY_CAMERACONTROL_EXTENDED_BACKGROUNDSEGMENTATION_CONFIGCAPS).<br><br>If the Capability field only exposes support for KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_BLUR, then this can also just be sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VALUE) but be aware that the DDI consumer will not know in advance in which stream configuration blur will be applied.<br><br>Note that for a SET call, only the **KSCAMERA_EXTENDEDPROP_HEADER** is considered. |
| Result | Indicates the error results of the last SET operation. If no SET operation has taken place, this must be 0. |
| Capability | Must be a bit wise **OR** of the supported ***KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_XXX*** flags defined above. |
| Flags | This is a read/write field. This can be any one of the ***KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_XXX*** flags defined above. |

## Requirements

**Minimum supported client:** Windows 11

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_CONFIGCAPS](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kscamera_extendedprop_backgroundsegmentation_configcaps)

[KSCAMERA_EXTENDEDPROP_HEADER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header)
