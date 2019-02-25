---
title: KSPROPERTY\_BDA\_TABLE\_SECTION
description: Clients use KSPROPERTY\_BDA\_TABLE\_SECTION to inform nodes about the table section to use when delivering data on the node's output.
ms.assetid: 58e6cc37-b6f1-49d6-a832-46f1edabf740
keywords: ["KSPROPERTY_BDA_TABLE_SECTION Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_TABLE_SECTION
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_BDA\_TABLE\_SECTION


Clients use KSPROPERTY\_BDA\_TABLE\_SECTION to inform nodes about the table section to use when delivering data on the node's output.

## <span id="ddk_ksproperty_bda_table_section_ks"></span><span id="DDK_KSPROPERTY_BDA_TABLE_SECTION_KS"></span>


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
<th>Property descriptor type</th>
<th>Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Filter</p></td>
<td><p>KSP_NODE</p></td>
<td><p>BDA_TABLE_SECTION</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **NodeId** member of KSP\_NODE specifies the LNB amplifier node.

The BDA\_TABLE\_SECTION structure describes the table section.

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

## See also


[**BDA\_TABLE\_SECTION**](https://msdn.microsoft.com/library/windows/hardware/ff556553)

[**KSP\_NODE**](https://msdn.microsoft.com/library/windows/hardware/ff566720)

 

 






