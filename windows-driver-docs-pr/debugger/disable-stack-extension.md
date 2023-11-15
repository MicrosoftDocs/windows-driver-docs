---
title: Disable stack extension
description: Disable stack extension
keywords: ["Disable stack extension (global flag)"]
ms.date: 05/23/2017
---

# Disable stack extension


## <span id="ddk_disable_stack_extension_dtools"></span><span id="DDK_DISABLE_STACK_EXTENSION_DTOOLS"></span>


The **Disable stack extension** flag prevents the kernel from extending the stacks of the threads in the process beyond the initial committed memory.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Abbreviation</strong></p></td>
<td align="left"><p>dse</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hexadecimal value</strong></p></td>
<td align="left"><p>0x10000</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Symbolic Name</strong></p></td>
<td align="left"><p>FLG_DISABLE_STACK_EXTENSION</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Destination</strong></p></td>
<td align="left"><p>Image file registry entry</p></td>
</tr>
</tbody>
</table>

 

### <span id="comments"></span><span id="COMMENTS"></span>Comments

This feature is used to simulate low memory conditions (where stack extensions fail) and to test the strategic system processes that are expected to run well even with low memory.

 

 