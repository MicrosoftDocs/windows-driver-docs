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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_CONNECTION\_STATE


The KSPROPERTY\_CONNECTION\_STATE property sets the current run state of the pin.

## <span id="ddk_ksproperty_connection_state_ks"></span><span id="DDK_KSPROPERTY_CONNECTION_STATE_KS"></span>


### Usage Summary Table

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
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566856" data-raw-source="[&lt;strong&gt;KSSTATE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566856)"><strong>KSSTATE</strong></a></p></td>
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

## See also


[**KSSTATE**](https://msdn.microsoft.com/library/windows/hardware/ff566856)

 

 






