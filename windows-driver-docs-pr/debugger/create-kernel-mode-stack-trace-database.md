---
title: Create kernel mode stack trace database
description: Create kernel mode stack trace database
keywords: ["Create kernel mode stack trace database (global flag)"]
ms.date: 05/23/2017
---

# Create kernel mode stack trace database


## <span id="ddk_create_kernel_mode_stack_trace_database_dtools"></span><span id="DDK_CREATE_KERNEL_MODE_STACK_TRACE_DATABASE_DTOOLS"></span>


The **Create kernel mode stack trace database** flag creates a run-time stack trace database of kernel operations, such as resource objects and object management operations, and works only when using the checked build of Windows. Checked builds were available on older versions of Windows before Windows 10, version 1803.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Abbreviation</strong></p></td>
<td align="left"><p>kst</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hexadecimal value</strong></p></td>
<td align="left"><p>0x2000</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Symbolic Name</strong></p></td>
<td align="left"><p>FLG_KERNEL_STACK_TRACE_DB</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Destination</strong></p></td>
<td align="left"><p>System-wide registry entry</p></td>
</tr>
</tbody>
</table>

 

### <span id="comments"></span><span id="COMMENTS"></span>Comments

GFlags displays this flag as a kernel flag setting, but it is not effective at run time, because the kernel is already started.

 

 