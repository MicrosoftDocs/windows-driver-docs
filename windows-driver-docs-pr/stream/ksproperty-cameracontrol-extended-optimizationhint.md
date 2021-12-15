---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_OPTIMIZATIONHINT (application performance strategy)
description: Camera drivers may optimize their capture operation based on hints provided by the application. This property informs the driver to set its performance strategy based on what operation is likely used the most.
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_OPTIMIZATIONHINT Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_OPTIMIZATIONHINT
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 07/08/2020
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_OPTIMIZATIONHINT (application performance strategy)

Camera drivers may optimize their capture operation based on hints provided by the application. This property informs the driver to set its performance strategy based on what operation is likely used the most. For example, when optimized for photo, the camera driver may program the sensor to optimize sensor exposure speed and resolution for lower latency from photo capture trigger to image capture. Similarly, when optimized for video, the camera driver may program the sensor for higher frame rate but at a lower resolution.

## Usage summary table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | [**KSPROPERTY**](ksproperty-structure.md) | [**KSCAMERA_EXTENDEDPROP_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) |

The property value (operation data) contains a [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure and a [**KSCAMERA\_EXTENDEDPROP\_VALUE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value) structure.

The total property data size is **sizeof**(KSCAMERA\_EXTENDEDPROP\_HEADER) + **sizeof**(KSCAMERA\_EXTENDEDPROP\_VALUE). The **Size** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) is set to this total property data size.

The **Capability** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) contains a bitwise OR combination of one or more of the following optimization hints.

| Optimization hint | Description |
|--|--|
| KSCAMERA\_EXTENDEDPROP\_OPTIMIZATION\_PHOTO | Camera operation is optimized for photos |
| KSCAMERA\_EXTENDEDPROP\_OPTIMIZATION\_VIDEO | Camera operation is optimized for video |

The **Flags** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) contains the optimization currently set for the camera (one value).

The default optimization type is KSCAMERA\_EXTENDEDPROP\_OPTIMIZATION\_PHOTO. If this property is supported by the camera driver, then both optimization types must be supported.

This property control is synchronous and not cancelable.

## Remarks

### Optimization modes

**KSCAMERA\_EXTENDEDPROP\_OPTIMIZATION\_PHOTO**

All camera drivers must be in this mode until explicitly informed to use the KSCAMERA\_EXTENDEDPROP\_OPTIMIZATION\_VIDEO mode. The purpose of this mode is to optimize the camera hardware for photo operations. Video operations must still be functional in this mode.

**KSCAMERA\_EXTENDEDPROP\_OPTIMIZATION\_VIDEO**

This mode indicates that the camera will likely be used for video operations. The camera driver should optimize the hardware for video operations for this mode. Photo operations must be functional, but there resource usage priority is for video operations.

### Getting the property

When responding to a KSPROPERTY\_TYPE\_GET request, the driver sets the members of the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) to the following.

| Member | Value |
|--|--|
| Version | 1 |
| PinId | KSCAMERA_EXTENDEDPROP_FILTERSCOPE (0xFFFFFFFF) |
| Size | sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VALUE) |
| Result | 0 |
| Capability | Optimization values supported |
| Flags | The current optimization value setting |

If no optimization mode was previously set, then the driver sets **Flags** to KSCAMERA\_EXTENDEDPROP\_OPTIMIZATION\_PHOTO (default).

### Setting the property

When the property is set, a KSPROPERTY\_TYPE\_SET request, the **Flags** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) will contain the optimization mode to set.

## Requirements

**Version:** Available starting with Windows 8.1

**Header:** Ksmedia.h (include Ksmedia.h)

## See also

[**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header)

[**KSCAMERA\_EXTENDEDPROP\_VALUE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value)
