---
title: KSPROPERTY\_CONNECTION\_STATE
description: The KSPROPERTY\_CONNECTION\_STATE property sets the current run state of the pin.
ms.assetid: f1a9e101-1398-4f16-bae9-f827e7d0c433
keywords: ["KSPROPERTY_CONNECTION_STATE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CONNECTION_STATE
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

# KSPROPERTY\_CONNECTION\_STATE


The KSPROPERTY\_CONNECTION\_STATE property sets the current run state of the pin.

## <span id="ddk_ksproperty_connection_state_ks"></span><span id="DDK_KSPROPERTY_CONNECTION_STATE_KS"></span>


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
<td><p>Filter or Pin</p></td>
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>[<strong>KSSTATE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566856)</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

This property returns one of the following values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>KSSTATE_STOP</p></td>
<td><p>The initial state of a pin. No data is actually being read or written. In this state, the pin uses the least amount of resources possible.</p></td>
</tr>
<tr class="even">
<td><p>KSSTATE_ACQUIRE</p></td>
<td><p>The pin is acquiring the resources necessary to read or write data.</p></td>
</tr>
<tr class="odd">
<td><p>KSSTATE_PAUSE</p></td>
<td><p>The pin is ready to read or write data, but data transfer is temporarily paused.</p></td>
</tr>
<tr class="even">
<td><p>KSSTATE_RUN</p></td>
<td><p>The state from which the pin can actually read or write data.</p></td>
</tr>
</tbody>
</table>

 

The pin only reads or writes data in the **KSSTATE\_RUN** state. Both individual pins and the KS filter as a whole may support this property.

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


[**KSSTATE**](https://msdn.microsoft.com/library/windows/hardware/ff566856)

 

 






