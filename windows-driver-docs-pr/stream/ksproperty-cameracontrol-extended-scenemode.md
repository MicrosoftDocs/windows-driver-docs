---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_SCENEMODE
description: The scene mode property selects a driver defined mode which represents a collection of preset controls.
ms.assetid: 32C350FF-AA54-4F28-8AD2-341A31648B60
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_SCENEMODE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_SCENEMODE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 09/11/2018
ms.localizationpriority: medium
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_SCENEMODE

The scene mode property selects a driver defined mode which represents a collection of preset controls. The driver determines the presets assigned to a scene mode and enables those control settings when a scene is selected.

## Usage Summary Table

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Get</th>
<th>Set</th>
<th>Target</th>
<th>Property descriptor type</th>
<th>Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Filter</p></td>
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header" data-raw-source="[&lt;strong&gt;KSCAMERA_EXTENDEDPROP_HEADER&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header)"><strong>KSCAMERA_EXTENDEDPROP_HEADER</strong></a></p></td>
</tr>
</tbody>
</table>

The property value (operation data) contains a [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure and a [**KSCAMERA\_EXTENDEDPROP\_VALUE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value) structure. The **KSCAMERA\_EXTENDEDPROP\_VALUE** is required but the **Value** member is ignored.

The total property data size is **sizeof**(KSCAMERA\_EXTENDEDPROP\_HEADER) + **sizeof**(KSCAMERA\_EXTENDEDPROP\_VALUE). The **Size** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) is set to this total property data size.

The **Capability** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) contains a bitwise OR combination of one or more of the following scene modes that are supported by the driver.

| Scene mode                                       | Description                                                           |
|--------------------------------------------------|-----------------------------------------------------------------------|
| KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_AUTO          | Automatic scent mode. Controls are at their auto settings.            |
| KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_MACRO         | Macro scene mode (driver defined).                                    |
| KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_PORTRAIT      | Portrait scene mode (driver defined).                                 |
| KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_SPORT         | Sport scene mode (driver defined).                                    |
| KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_SNOW          | Snow scene mode (driver defined).                                     |
| KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_NIGHT         | Night scene mode (driver defined).                                    |
| KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_BEACH         | Beach scene mode (driver defined).                                    |
| KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_SUNSET        | Sunset scene mode (driver defined).                                   |
| KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_CANDLELIGHT   | Candlelight scene mode (driver defined).                              |
| KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_LANDSCAPE     | Landscape scene mode (driver defined).                                |
| KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_NIGHTPORTRAIT | Night portrait scene mode (driver defined).                           |
| KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_BACKLIT       | Backlit scene mode (driver defined).                                  |
| KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_MANUAL        | Controls are manually changed and no pre-defined scene modes are set. |

The **Flags** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) contains the scene mode currently set for the camera. The default scene mode for a camera is always KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_AUTO.

This property control is asynchronous and not cancelable.

## Remarks

### Getting the property

When responding to a KSPROPERTY\_TYPE\_GET request, the driver sets the members of the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) to the following.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Member</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Version</td>
<td>1</td>
</tr>
<tr class="even">
<td>PinId</td>
<td>KSCAMERA_EXTENDEDPROP_FILTERSCOPE (0xFFFFFFFF).</td>
</tr>
<tr class="odd">
<td>Size</td>
<td><p>sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VALUE)</p></td>
</tr>
<tr class="even">
<td>Result</td>
<td>0</td>
</tr>
<tr class="odd">
<td>Capability</td>
<td>KSCAMERA_EXTENDEDPROP_CAPS_ASYNCCONTROL | (scene mode values supported).</td>
</tr>
<tr class="even">
<td>Flags</td>
<td>The current scene mode value setting (only one value).</td>
</tr>
</tbody>
</table>

If no scene mode was previously set, then **Flags** is set to KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_AUTO (default).

### Setting the property

When the property is set, a KSPROPERTY\_TYPE\_SET request, the **Flags** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) will contain the scene mode to enable.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available starting with Windows 8.1.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## See also

[**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header)

[**KSCAMERA\_EXTENDEDPROP\_VALUE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value)
