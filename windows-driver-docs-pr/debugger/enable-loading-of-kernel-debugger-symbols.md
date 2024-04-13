---
title: Enable Loading of Kernel Debugger Symbols
description: Enable loading of kernel debugger symbols
keywords: ["Enable loading of kernel debugger symbols (global flag)"]
ms.date: 05/23/2017
---

# Enable loading of kernel debugger symbols


## <span id="ddk_enable_loading_of_kernel_debugger_symbols_dtools"></span><span id="DDK_ENABLE_LOADING_OF_KERNEL_DEBUGGER_SYMBOLS_DTOOLS"></span>


The **Enable loading of kernel debugger symbols** flag loads kernel symbols into the kernel memory space the next time Windows starts.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Abbreviation</strong></p></td>
<td align="left"><p>ksl</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hexadecimal value</strong></p></td>
<td align="left"><p>0x40000</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Symbolic Name</strong></p></td>
<td align="left"><p>FLG_ENABLE_KDEBUG_SYMBOL_LOAD</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Destination</strong></p></td>
<td align="left"><p>System-wide registry entry, kernel flag</p></td>
</tr>
</tbody>
</table>

 

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The kernel symbols are used in kernel profiling and by advanced kernel debugging tools.

 

 