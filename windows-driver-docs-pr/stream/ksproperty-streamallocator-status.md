---
title: KSPROPERTY\_STREAMALLOCATOR\_STATUS
description: The KSPROPERTY\_STREAMALLOCATOR\_STATUS property retrieves the current status of the specified allocator.
ms.assetid: af88253b-e72d-4ea9-855d-0a91e6e35d0f
keywords: ["KSPROPERTY_STREAMALLOCATOR_STATUS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_STREAMALLOCATOR_STATUS
api_location:
- ks.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_STREAMALLOCATOR\_STATUS


The KSPROPERTY\_STREAMALLOCATOR\_STATUS property retrieves the current status of the specified allocator.

## <span id="ddk_ksproperty_streamallocator_status_ks"></span><span id="DDK_KSPROPERTY_STREAMALLOCATOR_STATUS_KS"></span>


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
<td><p>[<strong>KSSTREAMALLOCATOR_STATUS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566866)</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The status of the allocator indicates the framing specifications and the currently allocated frames.

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


[**KSSTREAMALLOCATOR\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff566866)

 

 






