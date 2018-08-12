---
title: KSPROPERTY\_BDA\_NODE\_TYPES
description: Clients use KSPROPERTY\_BDA\_NODE\_TYPES to retrieve a list of node types.
ms.assetid: 8fe72434-3635-4c2c-a72a-1fd398e488d8
keywords: ["KSPROPERTY_BDA_NODE_TYPES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_NODE_TYPES
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# KSPROPERTY\_BDA\_NODE\_TYPES


Clients use KSPROPERTY\_BDA\_NODE\_TYPES to retrieve a list of node types.

## <span id="ddk_ksproperty_bda_node_types_ks"></span><span id="DDK_KSPROPERTY_BDA_NODE_TYPES_KS"></span>


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
<th>Property descriptor type</th>
<th>Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>No</p></td>
<td><p>Filter</p></td>
<td><p>KSPROPERTY</p></td>
<td><p>List of KSNODE_DESCRIPTORs</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

In a template topology each node type can only occur once, but it can occur multiple times in an actual topology. This list of node types is an array of KSNODE\_DESCRIPTOR structures. Typically, the index of each element in this array is used to identify each particular node type.

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
<td>Bdamedia.h (include Bdamedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**BdaPropertyNodeTypes**](https://msdn.microsoft.com/library/windows/hardware/ff556497)

[**KSNODE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff563473)

[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

 

 






