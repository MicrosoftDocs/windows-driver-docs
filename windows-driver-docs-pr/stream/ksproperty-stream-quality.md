---
title: KSPROPERTY\_STREAM\_QUALITY
description: The KSPROPERTY\_STREAM\_QUALITY property is an optional property that should be implemented if the pin generates Quality Management complaints.
ms.assetid: ed4d9baa-967a-41b3-b8b9-910b86230254
keywords: ["KSPROPERTY_STREAM_QUALITY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_STREAM_QUALITY
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

# KSPROPERTY\_STREAM\_QUALITY


The KSPROPERTY\_STREAM\_QUALITY property is an optional property that should be implemented if the pin generates Quality Management complaints.

## <span id="ddk_ksproperty_stream_quality_ks"></span><span id="DDK_KSPROPERTY_STREAM_QUALITY_KS"></span>


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
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Pin</p></td>
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>[<strong>KSQUALITY_MANAGER</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566730)</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

When this request is made, the pin connection in turn notifies the quality manager by providing [**KSQUALITY**](https://msdn.microsoft.com/library/windows/hardware/ff566728) structures with the given context parameter.

If a pin does not report quality problems, it does not need to support KSPROPERTY\_STREAM\_QUALITY.

Also see [Quality Management](https://msdn.microsoft.com/library/windows/hardware/ff568124).

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

[**KSQUALITY\_MANAGER**](https://msdn.microsoft.com/library/windows/hardware/ff566730)

[**KSQUALITY**](https://msdn.microsoft.com/library/windows/hardware/ff566728)

 

 






