---
title: KSPROPERTY\_NUM\_SOURCES
description: The KSPROPERTY\_NUM\_SOURCES property specifies the number of input pins on the selector unit.
ms.assetid: 94d0f926-0551-4fe2-aa7f-2898e04c4b36
keywords: ["KSPROPERTY_NUM_SOURCES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_NUM_SOURCES
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# KSPROPERTY\_NUM\_SOURCES


The KSPROPERTY\_NUM\_SOURCES property specifies the number of input pins on the selector unit.

## <span id="ddk_ksproperty_num_sources_ks"></span><span id="DDK_KSPROPERTY_NUM_SOURCES_KS"></span>


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
<td><p>Filter or node</p></td>
<td><p>[<strong>KSPROPERTY_SELECTOR_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565219) or [<strong>KSPROPERTY_SELECTOR_NODE_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565217)</p></td>
<td><p>LONG</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

When making a get request, the client receives the number of available source pins in the **Value** member of the property descriptor structure.

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
<td>Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

 

 





