---
title: KSPROPERTY\_TOPOLOGY\_NAME
description: The KSPROPERTY\_TOPOLOGY\_NAME property provides the localized Unicode string name of the node.
ms.assetid: ae12fe2f-9ccf-4949-b530-e7e33c846837
keywords: ["KSPROPERTY_TOPOLOGY_NAME Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_TOPOLOGY_NAME
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_TOPOLOGY\_NAME


The KSPROPERTY\_TOPOLOGY\_NAME property provides the localized Unicode string name of the node.

## <span id="ddk_ksproperty_topology_name_ks"></span><span id="DDK_KSPROPERTY_TOPOLOGY_NAME_KS"></span>


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
<td><p>No</p></td>
<td><p>Node</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566720" data-raw-source="[&lt;strong&gt;KSP_NODE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566720)"><strong>KSP_NODE</strong></a></p></td>
<td><p>A buffer to hold the string name.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **NodeId** member of the KSP\_NODE structure specifies the node ID for which to return the string name.

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


[**KSP\_NODE**](https://msdn.microsoft.com/library/windows/hardware/ff566720)

 

 






