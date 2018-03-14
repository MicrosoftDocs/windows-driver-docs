---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_MAXVIDFPS\_PHOTORES
description: This property control sets or retrieves the maximum frame rate possible on the capture (preview) video pins at a particular photo resolution.
ms.assetid: 80A2492B-447A-4ADE-9B0C-54FB53E4163D
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_MAXVIDFPS_PHOTORES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_MAXVIDFPS_PHOTORES
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_MAXVIDFPS\_PHOTORES


This property control sets or retrieves the maximum frame rate possible on the capture (preview) video pins at a particular photo resolution.

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

 

The property value (operation data) contains a [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) structure and a [**KSCAMERA\_MAXVIDEOFPS\_FORPHOTORES**](https://msdn.microsoft.com/library/windows/hardware/dn567567) structure. The photo frame rate in frames per second is returned as value in [**KSCAMERA\_EXTENDEDPROP\_VALUE**](https://msdn.microsoft.com/library/windows/hardware/dn567565).

There are no flags set in the **Flags** or **Capability** members of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) for this property.

The total property data size is **sizeof**(KSCAMERA\_EXTENDEDPROP\_HEADER) + **sizeof**(KSCAMERA\_MAXVIDEOFPS\_FORPHOTORES). The **Size** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) is set to this total property data size.

This property control is synchronous.

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
<td><p>sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_MAXVIDEOFPS_FORPHOTORES)</p></td>
</tr>
<tr class="even">
<td>Result</td>
<td>0</td>
</tr>
<tr class="odd">
<td>Capability</td>
<td>0</td>
</tr>
<tr class="even">
<td>Flags</td>
<td>0</td>
</tr>
</tbody>
</table>

 

The **Result** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) is always set to 0 for a get operation.

When the property data is requested, the driver will receive the **PhotoResWidth** and **PhotoResHeight** members of[**KSCAMERA\_MAXVIDEOFPS\_FORPHOTORES**](https://msdn.microsoft.com/library/windows/hardware/dn567567) set with the requested resolution. The driver will set the frames per second values for the specified resolution.

If capture or preview is not supported by the camera, the frames per second members must be set to 0.

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

[**KSCAMERA\_MAXVIDEOFPS\_FORPHOTORES**](https://msdn.microsoft.com/library/windows/hardware/dn567567)

 

 






