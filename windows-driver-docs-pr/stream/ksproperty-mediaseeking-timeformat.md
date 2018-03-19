---
title: KSPROPERTY\_MEDIASEEKING\_TIMEFORMAT
description: The KSPROPERTY\_MEDIASEEKING\_TIMEFORMAT property retrieves the current media time format for a filter.
ms.assetid: 3a7b6873-7351-4e87-8fa7-a804894c56bb
keywords: ["KSPROPERTY_MEDIASEEKING_TIMEFORMAT Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_MEDIASEEKING_TIMEFORMAT
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

# KSPROPERTY\_MEDIASEEKING\_TIMEFORMAT


The KSPROPERTY\_MEDIASEEKING\_TIMEFORMAT property retrieves the current media time format for a filter.

## <span id="ddk_ksproperty_mediaseeking_timeformat_ks"></span><span id="DDK_KSPROPERTY_MEDIASEEKING_TIMEFORMAT_KS"></span>


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
<td><p>GUID</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The property sets the current media time format that is returned as a time format GUID.

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

 

 






