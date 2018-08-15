---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOMODE
description: This property sets or retrieves the photo mode setting for the camera.
ms.assetid: C9596B85-A07B-4DF7-852F-C9EBF43E1E44
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOMODE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOMODE
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

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOMODE


This property sets or retrieves the photo mode setting for the camera.

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

 

The property value (operation data) contains a [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) structure and a [**KSCAMERA\_EXTENDEDPROP\_PHOTOMODE**](https://msdn.microsoft.com/library/windows/hardware/dn567564) structure. These specify the photo mode and the history frame counts when sequence mode is set.

The desired photo mode is set in the **Flags** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563). The photo mode is set to one of the following.

| Photo mode                                  | Description                      |
|---------------------------------------------|----------------------------------|
| KSCAMERA\_EXTENDEDPROP\_PHOTOMODE\_NORMAL   | Normal still photo operation     |
| KSCAMERA\_EXTENDEDPROP\_PHOTOMODE\_SEQUENCE | Photo sequence capture operation |

 

The total property data size is **sizeof**(KSCAMERA\_EXTENDEDPROP\_HEADER) + **sizeof**(KSCAMERA\_EXTENDEDPROP\_PHOTOMODE). The **Size** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) is set to this total property data size.

**Note**  Setting the photo mode is an asynchronous control operation and KSCAMERA\_EXTENDEDPROP\_CAPS\_ASYNCCONTROL must be set in the **Capability** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563).

 

Remarks
-------

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
<td><p>sizeof(KSCAMERA_EXTENDEDPROP_HEADER) +</p>
<p>sizeof(KSCAMERA_EXTENDEDPROP_PHOTOMODE)</p></td>
</tr>
<tr class="even">
<td>Result</td>
<td><p>An error value resulting from the attempt to acquire the photo mode data.</p>
<p>Otherwise, 0.</p></td>
</tr>
<tr class="odd">
<td>Capability</td>
<td>KSCAMERA_EXTENDEDPROP_CAPS_ASYNCCONTROL</td>
</tr>
<tr class="even">
<td>Flags</td>
<td>Current photo mode.</td>
</tr>
</tbody>
</table>

 

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

[**KSCAMERA\_EXTENDEDPROP\_PHOTOMODE**](https://msdn.microsoft.com/library/windows/hardware/dn567564)

 

 






