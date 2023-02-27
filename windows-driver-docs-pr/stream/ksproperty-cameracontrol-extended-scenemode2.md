---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_SCENEMODE (ISP control parameters)
description: The KSPROPERTY\_CAMERACONTROL\_EXTENDED\_SCENEMODE property ID that is defined in the KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PROPERTY enumeration provides OEMs with capabilities to fine tune the scene mode along with any other ISP control parameters as needed.
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_SCENEMODE Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_SCENEMODE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 07/08/2020
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_SCENEMODE (ISP control parameters)

The **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_SCENEMODE** property ID that is defined in the [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PROPERTY**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ksproperty_cameracontrol_extended_property) enumeration provides OEMs with capabilities to fine tune the scene mode along with any other ISP control parameters as needed.

## Usage summary table

| Scope | Control | Type |
|--|--|--|
| Version 1 | Filter | Asynchronous |

The scene mode is used as a hint to guide the camera system to optimize its operation for certain conditions. Scene mode and other ISP controls such as White Balance, ISO, Exposure time, and EV compensation must be able to work independently without impacting each other.

- The changing of any other ISP control parameters must not change the existing scene mode. The driver is not required to change the scene mode to MANUAL after other ISP parameters are modified.

- Setting the auto scene mode must not change the existing settings for any other ISP controls. The driver is not required to revert to full auto mode for any other ISP controls.

**KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_AUTO**

This flag indicates the auto scene mode. The camera driver will automatically determine the best scene mode settings based on the scene and optimize the various ISP settings as needed for the scene.

**KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_MANUAL**

This flag is not applicable.

**KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_MACRO\\PORTRAIT\\SPORT\\SNOW\\NIGHT\\BEACH\\SUNSET\\CANDLELIGHT\\LANDSCAPE\\NIGHTPORTRAIT\\BACKLIT**

These flags indicate the corresponding scene mode as defined. The camera driver will use the scene mode specified as a hint to optimize the various ISP settings as needed (for example, for NIGHT, the ISP settings are optimized for night time environment).

The table below contains the descriptions and requirements for the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure fields when using the **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_SCENEMODE** property. The [**KSCAMERA\_EXTENDEDPROP\_VALUE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value) structure is ignored for **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_SCENEMODE**.

| Member | Value |
|--|--|
| Version | 1 |
| PinId | KSCAMERA_EXTENDEDPROP_FILTERSCOPE (0xFFFFFFFF) |
| Size | sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VALUE) |
| Result | This indicates the error results of the last SET operation. If no SET operation has taken place, this must be 0. The value 0 indicates no errors were detected. |
| Capability | This must be a bitwise OR of **KSCAMERA_EXTENDEDPROP_CAPS_ASYNCCONTROL** and any of the supported scene modes defined above. **KSCAMERA_EXTENDEDPROP_SCENEMODE_AUTO** must be supported if the camera driver supports this control. |
| Flags | This can be any of the supported scene modes shown above. |

## Requirements

**Header:** Ksmedia.h (include Ksmedia.h)
