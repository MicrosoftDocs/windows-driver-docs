---
title: KSPROPERTY\_STREAMALLOCATOR\_FUNCTIONTABLE
description: The KSPROPERTY\_STREAMALLOCATOR\_FUNCTIONTABLE property retrieves the function table of the given allocator.
keywords: ["KSPROPERTY_STREAMALLOCATOR_FUNCTIONTABLE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_STREAMALLOCATOR_FUNCTIONTABLE
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_STREAMALLOCATOR\_FUNCTIONTABLE


The KSPROPERTY\_STREAMALLOCATOR\_FUNCTIONTABLE property retrieves the function table of the given allocator.

## <span id="ddk_ksproperty_streamallocator_functiontable_ks"></span><span id="DDK_KSPROPERTY_STREAMALLOCATOR_FUNCTIONTABLE_KS"></span>


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
<td><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksstreamallocator_functiontable" data-raw-source="[&lt;strong&gt;KSSTREAMALLOCATOR_FUNCTIONTABLE&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksstreamallocator_functiontable)"><strong>KSSTREAMALLOCATOR_FUNCTIONTABLE</strong></a></p></td>
</tr>
</tbody>
</table>

 

## Remarks

KSPROPERTY\_STREAMALLOCATOR\_FUNCTIONTABLE is only used by allocators supporting the DISPATCH\_LEVEL function interface. Allocators supporting this property must be able to allocate and free frames for IRQL of DISPATCH\_LEVEL and lower. This property is accessible only from kernel mode.

Because the DISPATCH\_LEVEL interface is closely associated with the IRP-based interface, acquiring the function table is likely to result in the creation of an internal notification event to allow pending I/O to be completed when frames are returned to the free list. When the handle to the allocator is closed, the function table pointers are invalid and the associated events are automatically disabled.

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


[**KSSTREAMALLOCATOR\_FUNCTIONTABLE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksstreamallocator_functiontable)

