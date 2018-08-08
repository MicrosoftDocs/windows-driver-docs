---
title: KSPROPERTY\_CONNECTION\_STARTAT
description: KSPROPERTY\_CONNECTION\_STARTAT is an optional property that is implemented by filters that support starting when a specified event occurs.
ms.assetid: fcf76316-4016-4218-8530-5ef79794769a
keywords: ["KSPROPERTY_CONNECTION_STARTAT Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CONNECTION_STARTAT
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

# KSPROPERTY\_CONNECTION\_STARTAT


KSPROPERTY\_CONNECTION\_STARTAT is an optional property that is implemented by filters that support starting when a specified event occurs.

## <span id="ddk_ksproperty_connection_startat_ks"></span><span id="DDK_KSPROPERTY_CONNECTION_STARTAT_KS"></span>


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
<td><p>Filter</p></td>
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>[<strong>KSRELATIVEEVENT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566776)</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

This property should only be requested when the pin is in a pause state, to transition the pin into a run state.

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


[**KSRELATIVEEVENT**](https://msdn.microsoft.com/library/windows/hardware/ff566776)

[**KSEVENT\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff561862)

 

 






