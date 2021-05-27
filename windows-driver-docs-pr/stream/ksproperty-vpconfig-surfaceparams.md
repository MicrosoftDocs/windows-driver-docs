---
title: KSPROPERTY\_VPCONFIG\_SURFACEPARAMS
description: The KSPROPERTY\_VPCONFIG\_SURFACEPARAMS property specifies the video port surface settings..
keywords: ["KSPROPERTY_VPCONFIG_SURFACEPARAMS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_VPCONFIG_SURFACEPARAMS
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_VPCONFIG\_SURFACEPARAMS


The KSPROPERTY\_VPCONFIG\_SURFACEPARAMS property specifies the video port surface settings..

## <span id="ddk_ksproperty_vpconfig_surfaceparams_ks"></span><span id="DDK_KSPROPERTY_VPCONFIG_SURFACEPARAMS_KS"></span>


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
<td><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksvpsurfaceparams" data-raw-source="[&lt;strong&gt;KSVPSURFACEPARAMS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksvpsurfaceparams)"><strong>KSVPSURFACEPARAMS</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSVPSURFACEPARAMS structure that describes the surface pitch and *x* and *y* origin.

## Requirements

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


[**KSPROPERTY**](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier)

[**KSVPSURFACEPARAMS**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksvpsurfaceparams)

