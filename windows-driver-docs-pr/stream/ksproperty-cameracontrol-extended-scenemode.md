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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_SCENEMODE


The scene mode property selects a driver defined mode which represents a collection of preset controls. The driver determines the presets assigned to a scene mode and enables those control settings when a scene is selected.

### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

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
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>[<strong>KSCAMERA_EXTENDEDPROP_HEADER</strong>](https://msdn.microsoft.com/library/windows/hardware/dn567563)</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) contains a [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) structure and a [**KSCAMERA\_EXTENDEDPROP\_VALUE**](https://msdn.microsoft.com/library/windows/hardware/dn567564) structure. The **KSCAMERA\_EXTENDEDPROP\_VALUE** is required but the **Value** member is ignored.

The total property data size is **sizeof**(KSCAMERA\_EXTENDEDPROP\_HEADER) + **sizeof**(KSCAMERA\_EXTENDEDPROP\_VALUE). The **Size** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) is set to this total property data size.

The **Capability** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) contains a bitwise OR combination of one or more of the following scene modes that are supported by the driver.

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

 

The **Flags** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) contains the scene mode currently set for the camera. The default scene mode for a camera is always KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_AUTO.

This property control is asynchronous and not cancelable.

Remarks
-------

### <span id="Getting_the_property"></span><span id="getting_the_property"></span><span id="GETTING_THE_PROPERTY"></span>Getting the property

When responding to a KSPROPERTY\_TYPE\_GET request, the driver sets the members of the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) to the following.

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

### <span id="Setting_the_property"></span><span id="setting_the_property"></span><span id="SETTING_THE_PROPERTY"></span>Setting the property

When the property is set, a KSPROPERTY\_TYPE\_SET request, the **Flags** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) will contain the scene mode to enable.

Requirements
------------

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

## <span id="see_also"></span>See also


[**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563)

[**KSCAMERA\_EXTENDEDPROP\_VALUE**](https://msdn.microsoft.com/library/windows/hardware/dn567564)

 

 






