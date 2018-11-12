---
title: ISCSI\_HEADER\_INTEGRITY\_TYPE\_QUALIFIERS
description: ISCSI\_HEADER\_INTEGRITY\_TYPE\_QUALIFIERS
ms.assetid: 32e72d48-b80a-4cfb-ad35-174219753c01
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# ISCSI\_HEADER\_INTEGRITY\_TYPE\_QUALIFIERS


## <span id="ddk_iscsi_header_integrity_type_qualifiers_kr"></span><span id="DDK_ISCSI_HEADER_INTEGRITY_TYPE_QUALIFIERS_KR"></span>


The ISCSI\_HEADER\_INTEGRITY\_TYPE\_QUALIFIERS WMI property qualifier corresponds to a group of values that indicate the technique for guaranteeing header integrity.

The following table describes the ISCSI\_HEADER\_INTEGRITY\_TYPE\_QUALIFIERS values.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Header integrity check value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>No data integrity check is done on the header.</p></td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"><p>A 32-bit cyclic redundancy check is performed on the header.</p></td>
</tr>
</tbody>
</table>

 

 

 





