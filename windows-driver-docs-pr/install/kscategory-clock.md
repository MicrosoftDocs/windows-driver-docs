---
title: KSCATEGORY_CLOCK
description: KSCATEGORY_CLOCK
ms.assetid: 1a5afadd-f76f-4184-a93e-af82769ecc1b
keywords: ["KSCATEGORY_CLOCK Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_CLOCK
api_location:
- Ks.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# KSCATEGORY_CLOCK


The KSCATEGORY_CLOCK [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for the [kernel streaming](https://msdn.microsoft.com/library/windows/hardware/ff568277) (KS) functional category for a clock device.

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
<td align="left"><p>KSCATEGORY_CLOCK</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{53172480-4791-11D0-A5D6-28DB04C10000}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers for KS devices register instances of KSCATEGORY_CLOCK to indicate to the operating system that the devices support the KSCATEGORY_CLOCK functional category.

For more information about kernel streaming clocks, see [KS Minidriver Architecture](https://msdn.microsoft.com/library/windows/hardware/ff567656), [KS Clocks](https://msdn.microsoft.com/library/windows/hardware/ff567307), and [AVStream Clocks](https://msdn.microsoft.com/library/windows/hardware/ff554208).

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

 

 





