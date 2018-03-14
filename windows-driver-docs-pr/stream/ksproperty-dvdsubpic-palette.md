---
title: KSPROPERTY\_DVDSUBPIC\_PALETTE
description: The KSPROPERTY\_DVDSUBPIC\_PALETTE property specifies the color palette that the subpicture stream uses.
ms.assetid: 9dafb956-4adf-45ec-b997-8ed35991f7d8
keywords: ["KSPROPERTY_DVDSUBPIC_PALETTE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_DVDSUBPIC_PALETTE
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

# KSPROPERTY\_DVDSUBPIC\_PALETTE


The KSPROPERTY\_DVDSUBPIC\_PALETTE property specifies the color palette that the subpicture stream uses.

## <span id="ddk_ksproperty_dvdsubpic_palette_ks"></span><span id="DDK_KSPROPERTY_DVDSUBPIC_PALETTE_KS"></span>


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
<td><p>[<strong>KSPROPERTY_SPPAL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565628)</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSPROPERTY\_SPPAL structure that describes the color palette to use for the subpicture display in the YUV color format.

Remarks
-------

The [**KSPROPERTY\_SPPAL**](https://msdn.microsoft.com/library/windows/hardware/ff565628) structure contains an array of 16 YUV elements. These elements correspond to the 4-bit color numbers requested within the subpicture command stream.

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


[**KSPROPERTY\_SPPAL**](https://msdn.microsoft.com/library/windows/hardware/ff565628)

 

 






