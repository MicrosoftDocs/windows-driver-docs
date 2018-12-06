---
title: KSPROPERTY\_SELECTOR\_SOURCE\_NODE\_ID
description: The KSPROPERTY\_SELECTOR\_SOURCE\_NODE\_ID property specifies the pin identifier of the source pin for a particular node.
ms.assetid: 7616e834-462c-4e2c-8a4f-ec20db042e3b
keywords: ["KSPROPERTY_SELECTOR_SOURCE_NODE_ID Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_SELECTOR_SOURCE_NODE_ID
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_SELECTOR\_SOURCE\_NODE\_ID


The KSPROPERTY\_SELECTOR\_SOURCE\_NODE\_ID property specifies the pin identifier of the source pin for a particular node.

## <span id="ddk_ksproperty_selector_source_node_id_ks"></span><span id="DDK_KSPROPERTY_SELECTOR_SOURCE_NODE_ID_KS"></span>


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
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Filter or node</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565219" data-raw-source="[&lt;strong&gt;KSPROPERTY_SELECTOR_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565219)"><strong>KSPROPERTY_SELECTOR_S</strong></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff565217" data-raw-source="[&lt;strong&gt;KSPROPERTY_SELECTOR_NODE_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565217)"><strong>KSPROPERTY_SELECTOR_NODE_S</strong></a></p></td>
<td><p>LONG</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

When making a set request, the client must specify a valid pin identifier in the **Value** member of the property descriptor structure.

When making a get request, the client receives the pin identifier in the **Value** member of the property descriptor structure.

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

 

 





