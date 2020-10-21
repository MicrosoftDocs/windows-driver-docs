---
title: KSPROPERTY_CAMERACONTROL_EXTENDED_RELATIVEPANELOPTIMIZATION
description: KSPROPERTY_CAMERACONTROL_EXTENDED_RELATIVEPANELOPTIMIZATION is a property ID used to inform the driver of whether the camera is facing front or not, relative to the active display of the application.
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_RELATIVEPANELOPTIMIZATION Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_RELATIVEPANELOPTIMIZATION
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 07/07/2020
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_RELATIVEPANELOPTIMIZATION

**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_RELATIVEPANELOPTIMIZATION** is a property ID used to inform the driver of whether the camera is facing front or not, relative to the active display of the application. Windows will set the property when the new WinRT API property PanelBasedOptimizationControl.Panel is set.

Examples of setting KSProperty controls can be found in the [AVStream Camera Sample Driver](https://github.com/microsoft/Windows-driver-samples/tree/master/avstream/avscamera) on GitHub.

## Usage summary table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | [KSPROPERTY](/previous-versions/ff564262(v=vs.85)) | [KSCAMERA_EXTENDEDPROP_HEADER](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) |

## Remarks

The property request contains a [KSCAMERA_EXTENDEDPROP_HEADER](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure and a [KSCAMERA_EXTENDEDPROP_VALUE](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value) structure.

The total property data size is `sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VALUE)`.

The **Size** member of [KSCAMERA_EXTENDEDPROP_HEADER](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) is set to this total property data size.

The following are flags that can be placed in the **KSCAMERA_EXTENDEDPROP_HEADER.Flags** and **KSCAMERA_EXTENDEDPROP_HEADER.Capability** fields.

| Relative Panel Optimization mode | Description |
|--|--|
| KSCAMERA\_EXTENDEDPROP\_RELATIVEPANELOPTIMIZATION\_OFF | Camera will use normal mode of operation |
| KSCAMERA\_EXTENDEDPROP\_RELATIVEPANELOPTIMIZATION\_ON | Camera will use optimization relative to a position described in the value field |
| KSCAMERA\_EXTENDEDPROP\_RELATIVEPANELOPTIMIZATION\_DYNAMIC | Camera location hint can be dynamically adjusted while streaming without glitching the stream |

**KSCAMERA_EXTENDEDPROP_RELATIVEPANELOPTIMIZATION** is always a synchronous control.

Any app can read the property but only apps that have opened the camera for exclusive access can write to the property value.

A suitable error code will be returned if attempts are made to write the property without having exclusive mode access.

In regards to mapping this DDI to the PanelBasedOptimizationControl, the application using PanelBasedOptimizationControl will set the Panel value, which Windows will internally use to program the [**KSCAMERA_EXTENDEDPROP_VALUE**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value) field of the payload.

The **Capability** and **Flags** field will be controlled by Windows.

If the driver receives a SET operation while the camera device is streaming and the flag *KSCAMERA\_EXTENDEDPROP\_RELATIVEPANELOPTIMIZATION\_DYNAMIC** is not set, the driver will return a state-based error.

The following table contains the requirements for the [KSCAMERA_EXTENDEDPROP_HEADER](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure fields when using the metadata control.

| Member | Description |
|--|--|
| Version | This must be 1. |
| PinId | KSCAMERA_EXTENDEDPROP_FILTERSCOPE (0xFFFFFFFF) |
| Size | This must be sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VALUE) |
| Result | Indicates the error results of the last SET operation. If no SET operation has taken place, this must be 0. |
| Capability | Must be a bit wise **OR** of the supported ***KSCAMERA_EXTENDEDPROP_RELATIVEPANELOPTIMIZATION_XXX*** flags defined above. |
| Flags | This is a read/write field. This can be either **KSCAMERA_EXTENDEDPROP_RELATIVEPANELOPTIMIZATION_ON** or **KSCAMERA_EXTENDEDPROP_RELATIVEPANELOPTIMIZATION_OFF** flags defined above. |

If **KSCAMERA\_EXTENDEDPROP\_RELATIVEPANELOPTIMIZATION\_ON** is specified in the **Flags** field of the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header), the **Value.ul** field must specify the PLD for the relative direction the camera is currently facing.

This can be any of the enumeration values for ACPI PLD, but most frequently will be **Front**, **Back** or **Unknown**.

If **KSCAMERA\_EXTENDEDPROP\_RELATIVEPANELOPTIMIZATION\_OFF** is specified, for SET operations, the **Value** field is ignored.

For GET operations, the driver must return the direction that the camera is currently programmed for.

If **KSCAMERA\_EXTENDEDPROP\_RELATIVEPANELOPTIMIZATION\_OFF** is specified, or if no value has been set, the device's default PLD must be returned.

If **KSCAMERA\_EXTENDEDPROP\_RELATIVEPANELOPTIMIZATION\_ON** is specified, the most recently set value must be returned.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)