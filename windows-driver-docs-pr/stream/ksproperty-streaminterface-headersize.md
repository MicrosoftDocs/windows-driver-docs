---
title: KSPROPERTY\_STREAMINTERFACE\_HEADERSIZE
description: The KSPROPERTY\_STREAMINTERFACE\_HEADERSIZE property queries a pin for the size of stream header this pin uses.
keywords: ["KSPROPERTY_STREAMINTERFACE_HEADERSIZE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_STREAMINTERFACE_HEADERSIZE
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_STREAMINTERFACE\_HEADERSIZE


The KSPROPERTY\_STREAMINTERFACE\_HEADERSIZE property queries a pin for the size of stream header this pin uses.

## <span id="ddk_ksproperty_streaminterface_headersize_ks"></span><span id="DDK_KSPROPERTY_STREAMINTERFACE_HEADERSIZE_KS"></span>


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
<td><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

## Remarks

See the **StreamHeaderSize** member of [**KSPIN**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin) for more information.

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


[**KSPROPERTY**](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier)

[**KSPIN**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin)

