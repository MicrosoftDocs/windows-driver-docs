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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_DVDSUBPIC\_PALETTE


The KSPROPERTY\_DVDSUBPIC\_PALETTE property specifies the color palette that the subpicture stream uses.

## <span id="ddk_ksproperty_dvdsubpic_palette_ks"></span><span id="DDK_KSPROPERTY_DVDSUBPIC_PALETTE_KS"></span>


### Usage Summary Table

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
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565628" data-raw-source="[&lt;strong&gt;KSPROPERTY_SPPAL&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565628)"><strong>KSPROPERTY_SPPAL</strong></a></p></td>
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

## See also


[**KSPROPERTY\_SPPAL**](https://msdn.microsoft.com/library/windows/hardware/ff565628)

 

 






