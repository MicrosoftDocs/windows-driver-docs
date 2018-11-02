---
title: KSCATEGORY_NETWORK
description: KSCATEGORY_NETWORK
ms.assetid: 8112f828-e215-433a-9749-1ba965a97700
keywords: ["KSCATEGORY_NETWORK Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_NETWORK
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# KSCATEGORY_NETWORK


The KSCATEGORY_NETWORK [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for the [kernel streaming](https://msdn.microsoft.com/library/windows/hardware/ff568277) (KS) functional category for a network device.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Attribute</th>
<th align="left">Setting</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Identifier</p></td>
<td align="left"><p>KSCATEGORY_NETWORK</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{67C9CC3C-69C4-11D2-8759-00A0C9223196}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers for KS devices register instances of KSCATEGORY_NETWORK to indicate to the operating system that the devices support the KSCATEGORY_NETWORK functional category.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

 

 





