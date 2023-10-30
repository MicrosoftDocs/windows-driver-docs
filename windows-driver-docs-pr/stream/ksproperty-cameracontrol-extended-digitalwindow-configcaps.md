---
title: KSPROPERTY_CAMERACONTROL_EXTENDED_DIGITALWINDOW_CONFIGCAPS
description: KSPROPERTY_CAMERACONTROL_EXTENDED_DIGITALWINDOW_CONFIGCAPS is a property ID that specifies the scaling limits of the camera given all available resolutions.  This control must always be available to report the capabilities of the Digital Window control.
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_DIGITALWINDOW_CONFIGCAPS Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_DIGITALWINDOW_CONFIGCAPS
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 06/24/2021
---

# KSPROPERTY_CAMERACONTROL_EXTENDED_DIGITALWINDOW_CONFIGCAPS

**KSPROPERTY_CAMERACONTROL_EXTENDED_DIGITALWINDOW_CONFIGCAPS** is a property ID that specifies the scaling limits of the camera given all available resolutions.  This control must always be available to report the capabilities of the Digital Window control..

Examples of setting KSPROPERTY controls can be found in the [AVStream Camera Sample Driver](https://github.com/Microsoft/Windows-driver-samples/tree/main/avstream/avscamera) on GitHub.

## Usage summary table

| Scope | Control | Type |
|--|--|--|
| Version 1 | Filter | Synchronous |

## Capability description

There are no capability flags defined for **KSCAMERA_EXTENDEDPROP_DIGITALWINDOW_CONFIGCAPS**.

**KSCAMERA_EXTENDEDPROP_DIGITALWINDOW_CONFIGCAPS** is always synchronous.

The following table contains the requirements for the [KSCAMERA_EXTENDEDPROP_HEADER](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure fields when using the metadata control.

| Member | Description |
|--|--|
| Version | This must be 1. |
| PinId | KSCAMERA_EXTENDEDPROP_FILTERSCOPE (0xFFFFFFFF) |
| Size | Must be sizeof([KSCAMERA_EXTENDEDPROP_HEADER](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header)) +  sizeof(**KSCAMERA_EXTENDEDPROP_DIGITALWINDOW_CONFIGCAPSHEADER**) + (sizeof(**KSCAMERA_EXTENDEDPROP_DIGITALWINDOW_CONFIGCAPS**) * Count) |
| Result | Must contain 0.  This field is only used to return the result of the last asynchronous SET operation. |
| Capability | Must be 0.  |
| Flags | Must be 0.  |

## Requirements

**Minimum supported client:** Windows 11

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[KSCAMERA_EXTENDEDPROP_DIGITALWINDOW_CONFIGCAPS](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kscamera_extendedprop_digitalwindow_configcaps)

[KSCAMERA_EXTENDEDPROP_DIGITALWINDOW_CONFIGCAPSHEADER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kscamera_extendedprop_digitalwindow_configcapsheader)

[KSCAMERA_EXTENDEDPROP_DIGITALWINDOW_SETTING](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kscamera_extendedprop_digitalwindow_setting)

[KSCAMERA_METADATA_DIGITALWINDOW](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kscamera_metadata_digitalwindow)
