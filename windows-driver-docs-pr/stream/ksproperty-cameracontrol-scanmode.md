---
title: KSPROPERTY\_CAMERACONTROL\_SCANMODE
description: The KSPROPERTY\_CAMERACONTROL\_SCANMODE property specifies the scanning mode of the camera sensor.
ms.assetid: ab5659b9-a94b-4127-a26e-49aac8de6fa8
keywords: ["KSPROPERTY_CAMERACONTROL_SCANMODE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_SCANMODE
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

# KSPROPERTY\_CAMERACONTROL\_SCANMODE


The KSPROPERTY\_CAMERACONTROL\_SCANMODE property specifies the scanning mode of the camera sensor.

## <span id="ddk_ksproperty_cameracontrol_scanmode_ks"></span><span id="DDK_KSPROPERTY_CAMERACONTROL_SCANMODE_KS"></span>


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
<th>Property Descriptor Type</th>
<th>Property Value Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Filter or node</p></td>
<td><p>[<strong>KSPROPERTY_CAMERACONTROL_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564439) or [<strong>KSPROPERTY_CAMERACONTROL_NODE_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564420)</p></td>
<td><p>LONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a LONG that specifies whether interlace mode should be enabled. A value of 0 indicates that the interlace mode is enabled, and a value of 1 indicates that the progressive (or non-interlace) mode is enabled.

Remarks
-------

The **Value** member of the KSPROPERTY\_CAMERACONTROL\_NODE\_S structure specifies whether interlace mode should be enabled.

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
<td><p>Available for Windows Vista and later versions of the Windows operating system.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSPROPERTY\_CAMERACONTROL\_NODE\_S**](https://msdn.microsoft.com/library/windows/hardware/ff564420)

 

 






