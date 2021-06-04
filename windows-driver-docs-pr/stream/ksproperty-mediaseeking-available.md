---
title: KSPROPERTY\_MEDIASEEKING\_AVAILABLE
description: The KSPROPERTY\_MEDIASEEKING\_AVAILABLE property retrieves the media time span that is currently available on a filter.
keywords: ["KSPROPERTY_MEDIASEEKING_AVAILABLE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_MEDIASEEKING_AVAILABLE
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_MEDIASEEKING\_AVAILABLE


The KSPROPERTY\_MEDIASEEKING\_AVAILABLE property retrieves the media time span that is currently available on a filter.

## <span id="ddk_ksproperty_mediaseeking_available_ks"></span><span id="DDK_KSPROPERTY_MEDIASEEKING_AVAILABLE_KS"></span>


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
<th>Property Descriptor Type</th>
<th>Property Value Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>No</p></td>
<td><p>Filter</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_mediaavailable" data-raw-source="[&lt;strong&gt;KSPROPERTY_MEDIAAVAILABLE&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_mediaavailable)"><strong>KSPROPERTY_MEDIAAVAILABLE</strong></a></p></td>
</tr>
</tbody>
</table>

 

## Remarks

The media time span is the duration that within which a client can seek.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ks.h (include Ks.h)</td>
</tr>
</tbody>
</table>

## See also


[**KSPROPERTY\_MEDIAAVAILABLE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_mediaavailable)

[KSPROPSETID\_MediaSeeking](kspropsetid-mediaseeking.md)

