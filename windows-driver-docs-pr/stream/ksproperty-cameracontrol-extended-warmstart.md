---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_WARMSTART
description: The warm start property control provides a hint for the driver to keep the camera pin ready to allow glitch-free operation.
ms.assetid: EAC20371-6228-48F1-85FF-FAECC835B070
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_WARMSTART Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_WARMSTART
api_type:
- NA
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_WARMSTART


The warm start property control provides a hint for the driver to keep the camera pin ready to allow glitch-free operation.

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

 

The property value (operation data) contains a [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) structure.

There are no flags set in the **Flags** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) for this property.

The total property data size is **sizeof**(KSCAMERA\_EXTENDEDPROP\_HEADER). The **Size** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) is set to this total property data size.

Warm start is enabled or disabled using the one of the following flags in the **Capability** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563).

| Warm start flags                                  | Description             |
|---------------------------------------------------|-------------------------|
| KSCAMERA\_EXTENDEDPROP\_WARMSTART\_MODE\_DISABLED | Warm start is disabled. |
| KSCAMERA\_EXTENDEDPROP\_WARMSTART\_MODE\_ENABLED  | Warm start is enabled.  |

 

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
<td><p>sizeof(KSCAMERA_EXTENDEDPROP_HEADER)</p></td>
</tr>
<tr class="even">
<td>Result</td>
<td>0</td>
</tr>
<tr class="odd">
<td>Capability</td>
<td><p>KSCAMERA_EXTENDEDPROP_CAPS_ASYNCCONTROL | KSCAMERA_EXTENDEDPROP_WARMSTART_MODE_DISABLED</p>
<p>-or-</p>
<p>KSCAMERA_EXTENDEDPROP_CAPS_ASYNCCONTROL | KSCAMERA_EXTENDEDPROP_WARMSTART_MODE_ENABLED</p></td>
</tr>
<tr class="even">
<td>Flags</td>
<td>0</td>
</tr>
</tbody>
</table>

 

The **Result** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) is always set to 0 for a get operation.

## <span id="see_also"></span>See also


[**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563)

 

 






