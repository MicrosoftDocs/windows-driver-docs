---
title: Enable heap tail checking
description: Enable heap tail checking
ms.assetid: d71b4567-55e7-49e6-a791-a292ad477c10
keywords: ["Enable heap tail checking (global flag)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Enable heap tail checking


## <span id="ddk_enable_heap_tail_checking_dtools"></span><span id="DDK_ENABLE_HEAP_TAIL_CHECKING_DTOOLS"></span>


The **Enable heap tail checking** flag checks for buffer overruns when the heap is freed.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Abbreviation</strong></p></td>
<td align="left"><p>htc</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hexadecimal value</strong></p></td>
<td align="left"><p>0x10</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Symbolic Name</strong></p></td>
<td align="left"><p>FLG_HEAP_ENABLE_TAIL_CHECK</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Destination</strong></p></td>
<td align="left"><p>System-wide registry entry, kernel flag, image file registry entry</p></td>
</tr>
</tbody>
</table>

 

### <span id="comments"></span><span id="COMMENTS"></span>Comments

This flag adds a short pattern to the end of each allocation. The Windows heap manager detects the pattern when the block is freed and, if the block was modified, the heap manager breaks into the debugger.

### <span id="see_also"></span><span id="SEE_ALSO"></span>See Also

[Enable heap free checking](enable-heap-free-checking.md), [Enable heap parameter checking](enable-heap-parameter-checking.md)

 

 





