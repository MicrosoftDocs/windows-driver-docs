---
title: Disable paging of kernel stacks
description: Disable paging of kernel stacks
ms.assetid: 3bf0ae20-4569-41de-9d7c-dd6a2790dac6
keywords: ["Disable paging of kernel stacks (global flag)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Disable paging of kernel stacks


## <span id="ddk_disable_paging_of_kernel_stacks_dtools"></span><span id="DDK_DISABLE_PAGING_OF_KERNEL_STACKS_DTOOLS"></span>


The **Disable paging of kernel stacks** flag prevents paging of the kernel-mode stacks of inactive threads.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Abbreviation</strong></p></td>
<td align="left"><p>dps</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hexadecimal value</strong></p></td>
<td align="left"><p>0x80000</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Symbolic Name</strong></p></td>
<td align="left"><p>FLG_DISABLE_PAGE_KERNEL_STACKS</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Destination</strong></p></td>
<td align="left"><p>System-wide registry entry</p></td>
</tr>
</tbody>
</table>

 

### <span id="comments"></span><span id="COMMENTS"></span>Comments

Generally, the kernel-mode stack cannot be paged; it is guaranteed to be resident in memory. However, Windows occasionally pages the kernel stacks of inactive threads. This flag prevents these occurrences.

The kernel debugger can provide information about a thread only when its stack is in physical memory. This flag is particularly important when debugging deadlocks and in other cases when every thread must be tracked.

 

 





