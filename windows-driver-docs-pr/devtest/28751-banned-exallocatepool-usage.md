---
title: C28751
description: Warning C28751 Banned usage of ExAllocatePool and its variants.
ms.assetid: A2FBEDA8-FA5D-42A5-B298-FF0A32B1662C
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28751


warning C28751: Banned usage of ExAllocatePool and its variants

This warning indicates that a function is being used that has been banned, and has a more robust and secure replacement.

The kernel memory allocation functions ExAllocatePool and ExAllocatePoolWithQuota do not provide tags to assist in later debugging. There are replacements for these functions that you can use, which make debugging easier.

Replacement

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">API</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="ExAllocatePool"></span><span id="exallocatepool"></span><span id="EXALLOCATEPOOL"></span>ExAllocatePool</p></td>
<td align="left"><p>Secure replacement: <a href="https://msdn.microsoft.com/library/windows/hardware/ff544520" data-raw-source="[&lt;strong&gt;ExAllocatePoolWithTag&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544520)"><strong>ExAllocatePoolWithTag</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="ExAllocatePoolWithQuota"></span><span id="exallocatepoolwithquota"></span><span id="EXALLOCATEPOOLWITHQUOTA"></span>ExAllocatePoolWithQuota</p></td>
<td align="left"><p>Secure replacement: <a href="https://msdn.microsoft.com/library/windows/hardware/ff544513" data-raw-source="[&lt;strong&gt;ExAllocatePoolWithQuotaTag&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544513)"><strong>ExAllocatePoolWithQuotaTag</strong></a> routine</p></td>
</tr>
</tbody>
</table>

 

 

 





