---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ISO
description: This property selects the ISO setting for the camera. The ISO setting is chosen from a group of presets or set to automatic.
ms.assetid: 8BA03479-2AB8-4390-83F0-84C3519DB991
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_ISO Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_ISO
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

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ISO


This property selects the ISO setting for the camera. The ISO setting is chosen from a group of presets or set to automatic.

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
<td><p>Pin</p></td>
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>[<strong>KSCAMERA_EXTENDEDPROP_HEADER</strong>](https://msdn.microsoft.com/library/windows/hardware/dn567563)</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) contains a [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) structure and a [**KSCAMERA\_EXTENDEDPROP\_VALUE**](https://msdn.microsoft.com/library/windows/hardware/dn567564) structure. The **KSCAMERA\_EXTENDEDPROP\_VALUE** is required but not used.

The total property data size is **sizeof**(KSCAMERA\_EXTENDEDPROP\_HEADER) + **sizeof**(KSCAMERA\_EXTENDEDPROP\_VALUE). The **Size** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) is set to this total property data size.

The **Capability** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) contains a bitwise OR combination of one or more of the following ISO settings.

| ISO                                | Description                   |
|------------------------------------|-------------------------------|
| KSCAMERA\_EXTENDEDPROP\_ISO\_AUTO  | The ISO setting is automatic. |
| KSCAMERA\_EXTENDEDPROP\_ISO\_50    | ISO 50                        |
| KSCAMERA\_EXTENDEDPROP\_ISO\_80    | ISO 80                        |
| KSCAMERA\_EXTENDEDPROP\_ISO\_100   | ISO 100                       |
| KSCAMERA\_EXTENDEDPROP\_ISO\_200   | ISO 200                       |
| KSCAMERA\_EXTENDEDPROP\_ISO\_400   | ISO 400                       |
| KSCAMERA\_EXTENDEDPROP\_ISO\_800   | ISO 800                       |
| KSCAMERA\_EXTENDEDPROP\_ISO\_1600  | ISO 1600                      |
| KSCAMERA\_EXTENDEDPROP\_ISO\_3200  | ISO 3200                      |
| KSCAMERA\_EXTENDEDPROP\_ISO\_6400  | ISO 6400                      |
| KSCAMERA\_EXTENDEDPROP\_ISO\_12800 | ISO 12800                     |
| KSCAMERA\_EXTENDEDPROP\_ISO\_25600 | ISO 25600                     |

 

The **Flags** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) contains the current ISO setting for the camera. The camera driver may support a subset of the ISO settings. If this property control is supported, the driver must support KSCAMERA\_EXTENDEDPROP\_ISO\_AUTO.

This property control is asynchronous.

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
<td>The pin ID for the photo pin.</td>
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
<td>KSCAMERA_EXTENDEDPROP_CAPS_ASYNCCONTROL | (ISO settings supported).</td>
</tr>
<tr class="even">
<td>Flags</td>
<td>The current ISO value setting (only one value).</td>
</tr>
</tbody>
</table>

 

If no ISO was previously set, then **Flags** is set to KSCAMERA\_EXTENDEDPROP\_ISO\_AUTO (default).

### <span id="Setting_the_property"></span><span id="setting_the_property"></span><span id="SETTING_THE_PROPERTY"></span>Setting the property

When the property is set, a KSPROPERTY\_TYPE\_SET request, the **Flags** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) will contain the ISO setting to enable.

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

 

 






