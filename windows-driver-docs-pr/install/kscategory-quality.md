---
title: KSCATEGORY_QUALITY
description: KSCATEGORY_QUALITY
ms.assetid: fc23e069-b514-41a3-b3c2-c65b35b2e431
keywords: ["KSCATEGORY_QUALITY Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_QUALITY
api_location:
- Ks.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# KSCATEGORY_QUALITY


The KSCATEGORY_QUALITY [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for the [kernel streaming](https://msdn.microsoft.com/library/windows/hardware/ff568277) (KS) functional category for quality management.

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
<td align="left"><p>KSCATEGORY_QUALITY</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{97EBAACB-95BD-11D0-A3EA-00A0C9223196}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers for KS devices register instances of KSCATEGORY_QUALITY to indicate to the operating system that the devices support the KSCATEGORY_QUALITY functional category.

For more information, see [Quality Management](https://msdn.microsoft.com/library/windows/hardware/ff568124).

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
<td align="left">Ks.h (include Ks.h)</td>
</tr>
</tbody>
</table>

 

 





