---
title: KSPROPERTY\_CAMERACONTROL\_PANTILT
description: The KSPROPERTY\_CAMERACONTROL\_PANTILT property specifies absolute pan and tilt settings.
ms.assetid: d6f151c9-a428-4d76-9854-5064d901643e
keywords: ["KSPROPERTY_CAMERACONTROL_PANTILT Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_PANTILT
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

# KSPROPERTY\_CAMERACONTROL\_PANTILT


The KSPROPERTY\_CAMERACONTROL\_PANTILT property specifies absolute pan and tilt settings.

## <span id="ddk_ksproperty_cameracontrol_pantilt_ks"></span><span id="DDK_KSPROPERTY_CAMERACONTROL_PANTILT_KS"></span>


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
<td><p>Filter or node</p></td>
<td><p>[<strong>KSPROPERTY_CAMERACONTROL_S2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564451) or [<strong>KSPROPERTY_CAMERACONTROL_NODE_S2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564421) depending on whether the request is for a filter or a node</p></td>
<td><p>Pair of LONG integers</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a pair of LONG integers that specify a camera's absolute pan and tilt settings. These values are expressed in arc-second units.

One arc second is 1/3600 of a degree. Acceptable values range from −180\*3600 to +180\*3600 arc seconds. If a pan or tilt value is not provided, the default is 0.

When making a pan request, specify a positive value to rotate the camera to the right and specify a negative value to rotate the camera to the left.

When making a tilt request, a positive value tilts the camera up and a negative value tilts the camera down.

Remarks
-------

The **Value1** member of the [**KSPROPERTY\_CAMERACONTROL\_S2**](https://msdn.microsoft.com/library/windows/hardware/ff564451) or [**KSPROPERTY\_CAMERACONTROL\_NODE\_S2**](https://msdn.microsoft.com/library/windows/hardware/ff564421) structures specifies the pan setting. The **Value2** member specifies the tilt setting.

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


[**KSPROPERTY\_CAMERACONTROL\_S2**](https://msdn.microsoft.com/library/windows/hardware/ff564451)

[**KSPROPERTY\_CAMERACONTROL\_NODE\_S2**](https://msdn.microsoft.com/library/windows/hardware/ff564421)

 

 






