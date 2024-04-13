---
title: KSPROPERTY_STREAM_ALLOCATOR
description: The KSPROPERTY\_STREAM\_ALLOCATOR property is an optional property that should be implemented if the pin allocates stream buffers or can provide an allocator
keywords: ["KSPROPERTY_STREAM_ALLOCATOR Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_STREAM_ALLOCATOR
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/28/2017
---

# KSPROPERTY\_STREAM\_ALLOCATOR


The KSPROPERTY\_STREAM\_ALLOCATOR property is an optional property that should be implemented if the pin allocates stream buffers or can provide an allocator

## <span id="ddk_ksproperty_stream_allocator_ks"></span><span id="DDK_KSPROPERTY_STREAM_ALLOCATOR_KS"></span>


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
<td><p>Yes</p></td>
<td><p>Pin</p></td>
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-structure" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](./ksproperty-structure.md)"><strong>KSPROPERTY</strong></a></p></td>
<td><p>HANDLE</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The returned value is always a **NULL** handle. However, support is determined by whether the call returns successfully.

The property sets the handle of the allocator assigned to the stream connection point. A connection point for KSPIN\_COMMUNICATION\_SOURCE checks the property to determine the handle of the allocator that should be used for data allocations. This property is typically set by a graph manager such as DirectShow.

An allocator handle is obtained and can be used to set the allocator for another filter pin. A filter using the allocator must reference the object to obtain a pointer to a file object and dereference the file object when a new allocator is assigned or when the connection is closed. The property can also be queried to determine if this connection point supports providing an allocator.

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
