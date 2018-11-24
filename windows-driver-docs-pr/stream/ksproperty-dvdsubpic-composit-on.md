---
title: KSPROPERTY\_DVDSUBPIC\_COMPOSIT\_ON
description: The KSPROPERTY\_DVDSUBPIC\_COMPOSIT\_ON property enables or disables the display of the subpicture.
ms.assetid: f9dcf8ca-44fb-45e2-9993-813439c742ef
keywords: ["KSPROPERTY_DVDSUBPIC_COMPOSIT_ON Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_DVDSUBPIC_COMPOSIT_ON
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_DVDSUBPIC\_COMPOSIT\_ON


The KSPROPERTY\_DVDSUBPIC\_COMPOSIT\_ON property enables or disables the display of the subpicture.

## <span id="ddk_ksproperty_dvdsubpic_composit_on_ks"></span><span id="DDK_KSPROPERTY_DVDSUBPIC_COMPOSIT_ON_KS"></span>


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
<td><p>KSPROPERTY_COMPOSIT_ON</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSPROPERTY\_COMPOSIT\_ON (a type-defined Boolean). Specify **TRUE** to turn on the subpicture display, or specify **FALSE** to turn off the subpicture display.

Remarks
-------

If subpicture display is disabled then the decoder must still decode the subpicture data but not display it. This facilitates instant display when a subpicture-enable command is received.

There is a force-display subpicture command in the subpicture data command stream that can override the KSPROPERTY\_DVDSUBPIC\_COMPOSIT\_ON property.

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

 

 





