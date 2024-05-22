---
title: KSPROPERTY_CAMERACONTROL_EXTENDED_FIELDOFVIEW2_CONFIGCAPS
description: KSPROPERTY_CAMERACONTROL_EXTENDED_FIELDOFVIEW2_CONFIGCAPS is a property ID that allows camera drivers to offer multiple fixed field of view (FoV) settings that users can select through the Camera settings page or applications.
keywords:
- KSPROPERTY_CAMERACONTROL_EXTENDED_FIELDOFVIEW2_CONFIGCAPS
ms.date: 04/03/2024
---

# KSPROPERTY_CAMERACONTROL_EXTENDED_FIELDOFVIEW2_CONFIGCAPS

**KSPROPERTY_CAMERACONTROL_EXTENDED_FIELDOFVIEW2_CONFIGCAPS** is a property ID that allows camera drivers to offer multiple fixed field of view (FoV) settings that users can select through the Camera settings page or applications.

- Field of View values reported in the **KSPROPERTY_CAMERACONTROL_EXTENDED_FIELDOFVIEW2_CONFIGCAPS** payload array must be sorted in descending order, for example, largest value first.

- All Field of View (FoV) values reported by **KSPROPERTY_CAMERACONTROL_EXTENDED_FIELDOFVIEW2_CONFIGCAPS** must be supported on all available media types that the driver chooses to support.

  - Drivers can do scaling and/or cropping to achieve FoVs on certain resolutions.

  - Exceptions can be made by supporting Camera Profiles and adding KSPROPERTY_CAMERACONTROL_EXTENDED_FIELDOFVIEW2 as BlockedControl. This will result in that the FIELDOFVIEW2 control is not supported at all when a profile that blocks it is used.

## Usage summary table

| Scope | Get | Set | Control | Type |
|--|--|--|--|--|
| Version 1 | Yes | No | Filter | Synchronous |

## KSCAMERA_EXTENDEDPROP_HEADER structure fields

The following table contains the requirements for the [**KSCAMERA_EXTENDEDPROP_HEADER**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure fields when using the control.

| Member | Description |
|--|--|
| Version | Must be 1. |
| PinId | KSCAMERA_EXTENDEDPROP_FILTERSCOPE (0xFFFFFFFF) |
| Size | Must be sizeof([**KSCAMERA_EXTENDEDPROP_HEADER**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header))+sizeof([**KSCAMERA_EXTENDEDPROP_FIELDOFVIEW2_CONFIGCAPS**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-kscamera_extendedprop_fieldofview2_configcaps)) |
| Result | Must contain 0. This field is only used to return the results of the last asynchronous SET operation. |
| Capability | Must be 0. |
| Flags | Must be 0. |

## KSPROPERTY_CAMERACONTROL_EXTENDED_FIELDOFVIEW2_CONFIGCAPS payload

The payload following the header structure is the mandatory [**KSCAMERA_EXTENDEDPROP_FIELDOFVIEW2_CONFIGCAPS**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-kscamera_extendedprop_fieldofview2_configcaps).

| Parameter | Description |
|--|--|
| DefaultDiagonalFieldOfViewInDegrees | The default field of view (FoV) value. Must be one of the values reported in the DiscreteFoVStops array. |
| DiscreteFoVStopsCount | Count of valid entries in DiscreteFovStops, maximum of 360, minimum of 1. |
| DiscreteFoVStops | Array of valid field of view (FoV) stops, only DiscreteFoVStopsCount are valid items. |
| Reserved | Set to 0. |

## Requirements

**Minimum supported client:** Windows 11, version 24H2

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSCAMERA_EXTENDEDPROP_FIELDOFVIEW2_CONFIGCAPS**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-kscamera_extendedprop_fieldofview2_configcaps)

[**KSCAMERA_EXTENDEDPROP_HEADER**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header)

[**KSCAMERA_EXTENDEDPROP_VALUE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value)

[KSPROPERTY_CAMERACONTROL_EXTENDED_FIELDOFVIEW2](ksproperty-cameracontrol-extended-fieldofview2.md)
