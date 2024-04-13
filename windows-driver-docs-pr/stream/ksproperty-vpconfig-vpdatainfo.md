---
title: KSPROPERTY_VPCONFIG_VPDATAINFO
description: The KSPROPERTY\_VPCONFIG\_VPDATAINFO property indicates the initial configuration state of the video port.
keywords: ["KSPROPERTY_VPCONFIG_VPDATAINFO Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_VPCONFIG_VPDATAINFO
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
---

# KSPROPERTY\_VPCONFIG\_VPDATAINFO


The KSPROPERTY\_VPCONFIG\_VPDATAINFO property indicates the initial configuration state of the video port.

## <span id="ddk_ksproperty_vpconfig_vpdatainfo_ks"></span><span id="DDK_KSPROPERTY_VPCONFIG_VPDATAINFO_KS"></span>


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
<td><p>Yes</p></td>
<td><p>No</p></td>
<td><p>Pin</p></td>
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-structure" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](./ksproperty-structure.md)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_amvpdatainfo" data-raw-source="[&lt;strong&gt;KS_AMVPDATAINFO&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_amvpdatainfo)"><strong>KS_AMVPDATAINFO</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KS\_AMVPDATAINFO structure that describes the properties of the video port.

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

[**KS\_AMVPDATAINFO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_amvpdatainfo)
