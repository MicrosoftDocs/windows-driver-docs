---
title: KSPROPERTY_VPCONFIG_SCALEFACTOR
description: The KSPROPERTY\_VPCONFIG\_SCALEFACTOR property sets the video port dimensions to user-defined specifications.
keywords: ["KSPROPERTY_VPCONFIG_SCALEFACTOR Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_VPCONFIG_SCALEFACTOR
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
---

# KSPROPERTY\_VPCONFIG\_SCALEFACTOR


The KSPROPERTY\_VPCONFIG\_SCALEFACTOR property sets the video port dimensions to user-defined specifications.

## <span id="ddk_ksproperty_vpconfig_scalefactor_ks"></span><span id="DDK_KSPROPERTY_VPCONFIG_SCALEFACTOR_KS"></span>


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
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-structure" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](./ksproperty-structure.md)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_amvpsize" data-raw-source="[&lt;strong&gt;KS_AMVPSIZE&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_amvpsize)"><strong>KS_AMVPSIZE</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KS\_AMVPSIZE structure that specifies the width and height of the video port.

## Remarks

When this property is used by KSPROPSETID\_VPVBIConfig, all property requests must return STATUS\_NOT\_IMPLEMENTED.

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


[**KSPROPERTY**](ksproperty-structure.md)

[**KS\_AMVPSIZE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_amvpsize)
