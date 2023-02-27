---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FLASHMODE (normal and sequence)
description: The flash property control sets flash mode operation for both normal and sequence photo mode of the camera.
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_FLASHMODE Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_FLASHMODE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 07/08/2020
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FLASHMODE (normal and sequence)

The flash property control sets flash mode operation for both normal and sequence photo mode of the camera.

## Usage summary table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | [**KSPROPERTY**](ksproperty-structure.md) | [**KSCAMERA_EXTENDEDPROP_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) |

The property value (operation data) contains a [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure and a [**KSCAMERA\_EXTENDEDPROP\_VALUE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value) structure.

The total property data size is **sizeof**(KSCAMERA\_EXTENDEDPROP\_HEADER) + **sizeof**(KSCAMERA\_EXTENDEDPROP\_VALUE). The **Size** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) is set to this total property data size.

The **Capability** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) contains a bitwise OR combination of one or more of the following flash modes that are supported by the driver.

| Flash mode | Description |
|--|--|
| KSCAMERA\_EXTENDEDPROP\_FLASH\_OFF | Flash is off. |
| KSCAMERA\_EXTENDEDPROP\_FLASH\_ON | Flash is on at the default intensity level. |
| KSCAMERA\_EXTENDEDPROP\_FLASH\_ON\_ADJUSTABLEPOWER | Flash is on at a specific power level. |
| KSCAMERA\_EXTENDEDPROP\_FLASH\_AUTO | Flash is automatic based on lighting conditions. |
| KSCAMERA\_EXTENDEDPROP\_FLASH\_AUTO\_ADJUSTABLEPOWER | Flash is automatic based on lighting conditions at a specific power level. |

The following feature flags can be combined with the previous flash settings except for KSCAMERA\_EXTENDEDPROP\_FLASH\_OFF.

| Flash feature | Description |
|--|--|
| KSCAMERA\_EXTENDEDPROP\_FLASH\_REDEYEREDUCTION | Enable redeye reduction feature. This flag can be combined with any other setting. |
| KSCAMERA\_EXTENDEDPROP\_FLASH\_SINGLEFLASH | Set flash for only one trigger. This feature is ignored when the camera is not in photo sequence mode. |
| KSCAMERA\_EXTENDEDPROP\_FLASH\_MULTIFLASHSUPPORTED | Set flash to trigger on every sequence frame. This feature is ignored when the camera is not in photo sequence mode. |

The **Flags** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) contains the flash mode currently set for the camera.

The default flash mode for a camera is KSCAMERA\_EXTENDEDPROP\_FLASH\_OFF. If the camera supports flash, KSCAMERA\_EXTENDEDPROP\_FLASH\_OFF, KSCAMERA\_EXTENDEDPROP\_FLASH\_ON, and KSCAMERA\_EXTENDEDPROP\_FLASH\_AUTO are required modes. The KSCAMERA\_EXTENDEDPROP\_FLASH\_AUTO\_ADJUSTABLEPOWER and KSCAMERA\_EXTENDEDPROP\_FLASH\_AUTO\_ADJUSTABLEPOWER modes are optional.

If photo sequence mode is supported by the camera, the flash control property is required with support for KSCAMERA\_EXTENDEDPROP\_FLASH\_SINGLEFLASH.

This property control is synchronous and not cancelable.

## Remarks

### Getting the property

When responding to a KSPROPERTY\_TYPE\_GET request, the driver sets the members of the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) to the following.

| Member | Value |
|--|--|
| Version | 1 |
| PinId | KSCAMERA_EXTENDEDPROP_FILTERSCOPE (0xFFFFFFFF) |
| Size | sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VALUE) |
| Result | 0 |
| Capability | Flash mode values supported |
| Flags | (The current flash mode value setting) &#x7c; (flash feature flags) |

When the torch mode is KSCAMERA\_EXTENDEDPROP\_FLASH\_ON\_ADJUSTABLEPOWER or KSCAMERA\_EXTENDEDPROP\_FLASH\_ON\_ADJUSTABLEPOWER, the **Value.ull** member of [**KSCAMERA\_EXTENDEDPROP\_VALUE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value) contains an intensity level value between 0 - 100. An intensity of 0 indicates a minimum level and an intensity of 100 indicates a maximum intensity level. When the adjustable power flags are not set, the value for the normalized intensity setting is returned in **Value.ull**.

If no flash mode was previously set, then **Flags** is set to KSCAMERA\_EXTENDEDPROP\_FLASH\_OFF (default).

### Setting the property

When the property is set, a KSPROPERTY\_TYPE\_SET request, the **Flags** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) will contain the torch mode to set. The **Value.ull** member of [**KSCAMERA\_EXTENDEDPROP\_VALUE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value) will contain the intensity level to set if **Flags** is KSCAMERA\_EXTENDEDPROP\_FLASH\_ON\_ADJUSTABLEPOWER or KSCAMERA\_EXTENDEDPROP\_FLASH\_AUTO\_ADJUSTABLEPOWER.

## Requirements

**Version:** Available starting with Windows 8.1

**Header:** Ksmedia.h (include Ksmedia.h)

## See also

[**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header)

[**KSCAMERA\_EXTENDEDPROP\_VALUE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value)
