---
title: KSPROPERTY_STREAM_PRESENTATIONEXTENT
description: The clients sends a KSPROPERTY\_STREAM\_PRESENTATIONEXTENT request to query the stream extent.
keywords: ["KSPROPERTY_STREAM_PRESENTATIONEXTENT Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_STREAM_PRESENTATIONEXTENT
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/28/2017
---

# KSPROPERTY\_STREAM\_PRESENTATIONEXTENT


The clients sends a KSPROPERTY\_STREAM\_PRESENTATIONEXTENT request to query the stream extent.

## <span id="ddk_ksproperty_stream_presentationextent_ks"></span><span id="DDK_KSPROPERTY_STREAM_PRESENTATIONEXTENT_KS"></span>


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
<td><p>Pin</p></td>
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-structure" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](./ksproperty-structure.md)"><strong>KSPROPERTY</strong></a></p></td>
<td><p>LONGLONG</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The property returns the extent as a LONGLONG, with the same resolution format as the presentation time.

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


[**KSPROPERTY**](ksproperty-structure.md)
