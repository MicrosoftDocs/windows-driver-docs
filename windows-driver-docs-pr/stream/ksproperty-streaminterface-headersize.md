---
title: KSPROPERTY\_STREAMINTERFACE\_HEADERSIZE
description: The KSPROPERTY\_STREAMINTERFACE\_HEADERSIZE property queries a pin for the size of stream header this pin uses.
ms.assetid: 45c2e10a-c223-4d96-9055-cf012dc50e7a
keywords: ["KSPROPERTY_STREAMINTERFACE_HEADERSIZE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_STREAMINTERFACE_HEADERSIZE
api_location:
- ks.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# KSPROPERTY\_STREAMINTERFACE\_HEADERSIZE


The KSPROPERTY\_STREAMINTERFACE\_HEADERSIZE property queries a pin for the size of stream header this pin uses.

## <span id="ddk_ksproperty_streaminterface_headersize_ks"></span><span id="DDK_KSPROPERTY_STREAMINTERFACE_HEADERSIZE_KS"></span>


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
<td><p>Pin</p></td>
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

See the **StreamHeaderSize** member of [**KSPIN**](https://msdn.microsoft.com/library/windows/hardware/ff563483) for more information.

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


[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

[**KSPIN**](https://msdn.microsoft.com/library/windows/hardware/ff563483)

 

 






