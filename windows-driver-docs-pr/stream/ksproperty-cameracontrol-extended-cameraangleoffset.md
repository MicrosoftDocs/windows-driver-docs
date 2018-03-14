---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_CAMERAANGLEOFFSET
description: The camera angle offset property provides read-only information about the pitch and yaw angle of the camera position. The pitch and yaw angle is defined to be an offset from horizontal and vertical axis.
ms.assetid: 06F62EB9-DAF7-486F-9940-24EA2224BCB0
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_CAMERAANGLEOFFSET Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_CAMERAANGLEOFFSET
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

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_CAMERAANGLEOFFSET


The camera angle offset property provides read-only information about the pitch and yaw angle of the camera position. The pitch and yaw angle is defined to be an offset from horizontal and vertical axis.

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
<td><p>No</p></td>
<td><p>Filter</p></td>
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>[<strong>KSCAMERA_EXTENDEDPROP_HEADER</strong>](https://msdn.microsoft.com/library/windows/hardware/dn567563)</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) contains a [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) structure and a [**KSCAMERA\_EXTENDEDPROP\_FIELDOFVIEW**](https://msdn.microsoft.com/library/windows/hardware/dn567562) structure.

The total property data size is **sizeof**(KSCAMERA\_EXTENDEDPROP\_HEADER) + **sizeof**(KSCAMERA\_EXTENDEDPROP\_FIELDOFVIEW). The **Size** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) is set to this total property data size.

The **Capability** and **Flags** members of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) are not used for this property.

If the driver cannot determine the correct field of view for the camera, the driver must not indicate support for this property.

This property control is synchronous.

Remarks
-------

If the camera sensor and the gyro sensor are both housed in the same physical chassis, it is recommended that the camera driver report the proper offset angle, which may be 0 degrees. If the camera sensor and the gyro sensor are not housed in the same physical chassis, drivers are recommended to not indicate support for this property.

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
<td><p>sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_CAMERAOFFSET)</p></td>
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

 

The driver sets the angle offsets the [**KSCAMERA\_EXTENDEDPROP\_CAMERAOFFSET**](https://msdn.microsoft.com/library/windows/hardware/dn567560) structure.

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

[**KSCAMERA\_EXTENDEDPROP\_CAMERAOFFSET**](https://msdn.microsoft.com/library/windows/hardware/dn567560)

 

 






