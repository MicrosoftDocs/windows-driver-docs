---
title: KSPROPERTY\_BDA\_NODE\_DESCRIPTORS
description: Clients use KSPROPERTY\_BDA\_NODE\_DESCRIPTORS to retrieve a list of nodes.
ms.assetid: 53b297e6-7e31-4231-80ad-b114cf9343b4
keywords: ["KSPROPERTY_BDA_NODE_DESCRIPTORS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_NODE_DESCRIPTORS
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

# KSPROPERTY\_BDA\_NODE\_DESCRIPTORS


Clients use KSPROPERTY\_BDA\_NODE\_DESCRIPTORS to retrieve a list of nodes.

## <span id="ddk_ksproperty_bda_node_descriptors_ks"></span><span id="DDK_KSPROPERTY_BDA_NODE_DESCRIPTORS_KS"></span>


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
<td><p>List of GUIDs</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The list of nodes is an array of GUIDs for available nodes.

For a list of BDA nodes that are available to create in a template topology, see [BDA Node Category GUIDs](bda-node-category-guids.md).

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


[**BdaPropertyNodeDescriptors**](https://msdn.microsoft.com/library/windows/hardware/ff556484)

[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

 

 






