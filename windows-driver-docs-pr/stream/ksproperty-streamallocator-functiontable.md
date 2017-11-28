---
title: KSPROPERTY\_STREAMALLOCATOR\_FUNCTIONTABLE
description: The KSPROPERTY\_STREAMALLOCATOR\_FUNCTIONTABLE property retrieves the function table of the given allocator.
ms.assetid: 5a55c808-2960-41c7-b242-69d1e10d0015
keywords: ["KSPROPERTY_STREAMALLOCATOR_FUNCTIONTABLE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_STREAMALLOCATOR_FUNCTIONTABLE
api_location:
- ks.h
api_type:
- HeaderDef
---

# KSPROPERTY\_STREAMALLOCATOR\_FUNCTIONTABLE


The KSPROPERTY\_STREAMALLOCATOR\_FUNCTIONTABLE property retrieves the function table of the given allocator.

## <span id="ddk_ksproperty_streamallocator_functiontable_ks"></span><span id="DDK_KSPROPERTY_STREAMALLOCATOR_FUNCTIONTABLE_KS"></span>


### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

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
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>[<strong>KSSTREAMALLOCATOR_FUNCTIONTABLE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566862)</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

KSPROPERTY\_STREAMALLOCATOR\_FUNCTIONTABLE is only used by allocators supporting the DISPATCH\_LEVEL function interface. Allocators supporting this property must be able to allocate and free frames for IRQL of DISPATCH\_LEVEL and lower. This property is accessible only from kernel mode.

Because the DISPATCH\_LEVEL interface is closely associated with the IRP-based interface, acquiring the function table is likely to result in the creation of an internal notification event to allow pending I/O to be completed when frames are returned to the free list. When the handle to the allocator is closed, the function table pointers are invalid and the associated events are automatically disabled.

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
<td>Ks.h (include Ks.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSSTREAMALLOCATOR\_FUNCTIONTABLE**](https://msdn.microsoft.com/library/windows/hardware/ff566862)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_STREAMALLOCATOR_FUNCTIONTABLE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





