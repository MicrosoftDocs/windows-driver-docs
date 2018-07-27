---
title: KSPROPERTY\_MEDIASEEKING\_STOPPOSITION
description: The KSPROPERTY\_MEDIASEEKING\_STOPPOSITION property retrieves the stop media time on a filter.
ms.assetid: 5a2d6c47-8419-4f1d-a362-28bf17cbd0a5
keywords: ["KSPROPERTY_MEDIASEEKING_STOPPOSITION Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_MEDIASEEKING_STOPPOSITION
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

# KSPROPERTY\_MEDIASEEKING\_STOPPOSITION


The KSPROPERTY\_MEDIASEEKING\_STOPPOSITION property retrieves the stop media time on a filter.

## <span id="ddk_ksproperty_mediaseeking_stopposition_ks"></span><span id="DDK_KSPROPERTY_MEDIASEEKING_STOPPOSITION_KS"></span>


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
<td><p>Filter</p></td>
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>LONGLONG</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The stop media time is the time that can be set if a stop time is supported by the filter.

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


[KSPROPSETID\_MediaSeeking](kspropsetid-mediaseeking.md)

 

 






