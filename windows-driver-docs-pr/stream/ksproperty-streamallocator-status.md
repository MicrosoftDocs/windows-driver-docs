---
title: KSPROPERTY_STREAMALLOCATOR_STATUS
description: The KSPROPERTY\_STREAMALLOCATOR\_STATUS property retrieves the current status of the specified allocator.
keywords: ["KSPROPERTY_STREAMALLOCATOR_STATUS Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_STREAMALLOCATOR_STATUS
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/28/2017
---

# KSPROPERTY\_STREAMALLOCATOR\_STATUS


The KSPROPERTY\_STREAMALLOCATOR\_STATUS property retrieves the current status of the specified allocator.

## <span id="ddk_ksproperty_streamallocator_status_ks"></span><span id="DDK_KSPROPERTY_STREAMALLOCATOR_STATUS_KS"></span>


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
<td><p>Allocator</p></td>
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-structure" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](./ksproperty-structure.md)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksstreamallocator_status" data-raw-source="[&lt;strong&gt;KSSTREAMALLOCATOR_STATUS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksstreamallocator_status)"><strong>KSSTREAMALLOCATOR_STATUS</strong></a></p></td>
</tr>
</tbody>
</table>

 

## Remarks

The status of the allocator indicates the framing specifications and the currently allocated frames.

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


[**KSSTREAMALLOCATOR\_STATUS**](/windows-hardware/drivers/ddi/ks/ns-ks-ksstreamallocator_status)
