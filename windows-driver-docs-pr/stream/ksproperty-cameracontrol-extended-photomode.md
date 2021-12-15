---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOMODE
description: This property sets or retrieves the photo mode setting for the camera.
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOMODE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOMODE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 07/08/2020
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOMODE

This property sets or retrieves the photo mode setting for the camera.

## Usage summary table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | [**KSPROPERTY**](ksproperty-structure.md) | [**KSCAMERA_EXTENDEDPROP_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) |

The property value (operation data) contains a [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure and a [**KSCAMERA\_EXTENDEDPROP\_PHOTOMODE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_photomode) structure. These specify the photo mode and the history frame counts when sequence mode is set.

The desired photo mode is set in the **Flags** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header). The photo mode is set to one of the following.

| Photo mode | Description |
|--|--|
| KSCAMERA\_EXTENDEDPROP\_PHOTOMODE\_NORMAL | Normal still photo operation |
| KSCAMERA\_EXTENDEDPROP\_PHOTOMODE\_SEQUENCE | Photo sequence capture operation |

The total property data size is **sizeof**(KSCAMERA\_EXTENDEDPROP\_HEADER) + **sizeof**(KSCAMERA\_EXTENDEDPROP\_PHOTOMODE). The **Size** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) is set to this total property data size.

> [!NOTE]
> Setting the photo mode is an asynchronous control operation and KSCAMERA\_EXTENDEDPROP\_CAPS\_ASYNCCONTROL must be set in the **Capability** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header).

## Remarks

When responding to a KSPROPERTY\_TYPE\_GET request, the driver sets the members of the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) to the following.

| Member | Value |
|--|--|
| Version | 1 |
| PinId | The pin ID for the photo pin |
| Size | sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_PHOTOMODE) |
| Result | An error value resulting from the attempt to acquire the photo mode data. Otherwise, 0. |
| Capability | KSCAMERA_EXTENDEDPROP_CAPS_ASYNCCONTROL |
| Flags | Current photo mode |

## Requirements

**Version:** Available starting with Windows 8.1

**Header:** Ksmedia.h (include Ksmedia.h)

## See also

[**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header)

[**KSCAMERA\_EXTENDEDPROP\_PHOTOMODE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_photomode)
