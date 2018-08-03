---
title: KSPROPERTY\_DVDSUBPIC\_HLI
description: The KSPROPERTY\_DVDSUBPIC\_HLI property specifies the rectangle of the subpicture or screen to change, including the color or contrast.
ms.assetid: c3498ff8-11fe-4f53-8317-83a487684ac7
keywords: ["KSPROPERTY_DVDSUBPIC_HLI Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_DVDSUBPIC_HLI
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# KSPROPERTY\_DVDSUBPIC\_HLI


The KSPROPERTY\_DVDSUBPIC\_HLI property specifies the rectangle of the subpicture or screen to change, including the color or contrast.

## <span id="ddk_ksproperty_dvdsubpic_hli_ks"></span><span id="DDK_KSPROPERTY_DVDSUBPIC_HLI_KS"></span>


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
<td><p>[<strong>KSPROPERTY_SPHLI</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565627)</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSPROPERTY\_SPHLI structure that describes the DVD highlight information to change.

Remarks
-------

The [**KSPROPERTY\_SPHLI**](https://msdn.microsoft.com/library/windows/hardware/ff565627) structure describes the currently selected button from the DVD highlight information.

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


[**KSPROPERTY\_SPHLI**](https://msdn.microsoft.com/library/windows/hardware/ff565627)

 

 






