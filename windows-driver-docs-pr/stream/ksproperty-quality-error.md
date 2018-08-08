---
title: KSPROPERTY\_QUALITY\_ERROR
description: The KSPROPERTY\_QUALITY\_ERROR property is an optional property that should be implemented if the pin supports quality management.
ms.assetid: a918ef13-f0a7-4eb9-b6ec-dcfec3098c1e
keywords: ["KSPROPERTY_QUALITY_ERROR Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_QUALITY_ERROR
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

# KSPROPERTY\_QUALITY\_ERROR


The KSPROPERTY\_QUALITY\_ERROR property is an optional property that should be implemented if the pin supports quality management.

## <span id="ddk_ksproperty_quality_error_ks"></span><span id="DDK_KSPROPERTY_QUALITY_ERROR_KS"></span>


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
<td><p>Yes</p></td>
<td><p>Pin</p></td>
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>[<strong>KSQUALITY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566728)</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

KSPROPERTY\_QUALITY\_ERROR has a property value of type [**KSQUALITY**](https://msdn.microsoft.com/library/windows/hardware/ff566728) structure. Use this structure to get or set the proportion of frames currently being used and the delta from optimal frame receipt time.

The class driver does not handle this property; the stream minidriver must provide handling on its own.

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

[**KSQUALITY**](https://msdn.microsoft.com/library/windows/hardware/ff566728)

 

 






