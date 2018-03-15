---
title: KSPROPERTY\_VPCONFIG\_SURFACEPARAMS
description: The KSPROPERTY\_VPCONFIG\_SURFACEPARAMS property specifies the video port surface settings..
ms.assetid: cb8ebaea-4667-43c6-964f-89d55d4ff9be
keywords: ["KSPROPERTY_VPCONFIG_SURFACEPARAMS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_VPCONFIG_SURFACEPARAMS
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_VPCONFIG\_SURFACEPARAMS


The KSPROPERTY\_VPCONFIG\_SURFACEPARAMS property specifies the video port surface settings..

## <span id="ddk_ksproperty_vpconfig_surfaceparams_ks"></span><span id="DDK_KSPROPERTY_VPCONFIG_SURFACEPARAMS_KS"></span>


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
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Pin</p></td>
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>[<strong>KSVPSURFACEPARAMS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567237)</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSVPSURFACEPARAMS structure that describes the surface pitch and *x* and *y* origin.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

[**KSVPSURFACEPARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff567237)

 

 






