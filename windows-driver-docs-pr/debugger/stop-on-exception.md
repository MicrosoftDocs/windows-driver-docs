---
title: Stop on exception
description: Stop on exception
ms.assetid: f459fa28-2fdf-4094-ba58-7e01a2309bb7
keywords: ["Stop on exception (global flag)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Stop on exception


## <span id="ddk_stop_on_exception_dtools"></span><span id="DDK_STOP_ON_EXCEPTION_DTOOLS"></span>


The **Stop on exception** flag causes the kernel to break into the kernel debugger whenever a kernel-mode exception occurs.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Abbreviation</strong></p></td>
<td align="left"><p>soe</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hexadecimal value</strong></p></td>
<td align="left"><p>0x1</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Symbolic Name</strong></p></td>
<td align="left"><p>FLG_STOP_ON_EXCEPTION</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Destination</strong></p></td>
<td align="left"><p>System-wide registry entry, kernel flag, image file registry entry</p></td>
</tr>
</tbody>
</table>

 

### <span id="comments"></span><span id="COMMENTS"></span>Comments

Windows passes all first chance exceptions (except for STATUS\_PORT\_DISCONNECT) with a severity of Warning or Error to the debugger before passing them to a local exception handler.

 

 





