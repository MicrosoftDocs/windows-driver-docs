---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_SCENEMODE (driver defined mode)
description: The scene mode property selects a driver defined mode which represents a collection of preset controls.
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

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_SCENEMODE (driver defined mode)

The scene mode property selects a driver defined mode which represents a collection of preset controls. The driver determines the presets assigned to a scene mode and enables those control settings when a scene is selected.

## Usage summary table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | [**KSPROPERTY**](ksproperty-structure.md) | [**KSCAMERA_EXTENDEDPROP_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) |

The property value (operation data) contains a [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure and a [**KSCAMERA\_EXTENDEDPROP\_VALUE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value) structure. The **KSCAMERA\_EXTENDEDPROP\_VALUE** is required but the **Value** member is ignored.

The total property data size is **sizeof**(KSCAMERA\_EXTENDEDPROP\_HEADER) + **sizeof**(KSCAMERA\_EXTENDEDPROP\_VALUE). The **Size** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) is set to this total property data size.

The **Capability** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) contains a bitwise OR combination of one or more of the following scene modes that are supported by the driver.

| Scene mode | Description |
|--|--|
| KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_AUTO | Automatic scent mode. Controls are at their auto settings. |
| KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_MACRO | Macro scene mode (driver defined). |
| KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_PORTRAIT | Portrait scene mode (driver defined). |
| KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_SPORT | Sport scene mode (driver defined). |
| KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_SNOW | Snow scene mode (driver defined). |
| KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_NIGHT | Night scene mode (driver defined). |
| KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_BEACH | Beach scene mode (driver defined). |
| KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_SUNSET | Sunset scene mode (driver defined). |
| KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_CANDLELIGHT | Candlelight scene mode (driver defined). |
| KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_LANDSCAPE | Landscape scene mode (driver defined). |
| KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_NIGHTPORTRAIT | Night portrait scene mode (driver defined). |
| KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_BACKLIT | Backlit scene mode (driver defined). |
| KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_MANUAL | Controls are manually changed and no pre-defined scene modes are set. |

The **Flags** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) contains the scene mode currently set for the camera. The default scene mode for a camera is always KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_AUTO.

This property control is asynchronous and not cancelable.

## Remarks

### Getting the property

When responding to a KSPROPERTY\_TYPE\_GET request, the driver sets the members of the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) to the following.

| Member | Value |
|--|--|
| Version | 1 |
| PinId | KSCAMERA_EXTENDEDPROP_FILTERSCOPE (0xFFFFFFFF) |
| Size | sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VALUE) |
| Result | 0 |
| Capability | KSCAMERA_EXTENDEDPROP_CAPS_ASYNCCONTROL &#x7c; (scene mode values supported) |
| Flags | The current scene mode value setting (only one value) |

If no scene mode was previously set, then **Flags** is set to KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_AUTO (default).

### Setting the property

When the property is set, a KSPROPERTY\_TYPE\_SET request, the **Flags** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) will contain the scene mode to enable.

## Requirements

**Version:** Available starting with Windows 8.1

**Header:** Ksmedia.h (include Ksmedia.h)

## See also

[**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header)

[**KSCAMERA\_EXTENDEDPROP\_VALUE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value)
