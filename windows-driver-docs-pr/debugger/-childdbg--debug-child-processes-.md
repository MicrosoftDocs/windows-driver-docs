---
title: .childdbg (Debug Child Processes)
description: The .childdbg command controls the debugging of child processes.
keywords: [".childdbg (Debug Child Processes) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .childdbg (Debug Child Processes)
api_type:
- NA
ms.localizationpriority: medium
---

# .childdbg (Debug Child Processes)


The **.childdbg** command controls the debugging of child processes.

```dbgsyntax
.childdbg 0 
.childdbg 1 
.childdbg 
```

## <span id="ddk_meta_debug_child_processes_dbg"></span><span id="DDK_META_DEBUG_CHILD_PROCESSES_DBG"></span>Parameters


<span id="_______0______"></span> **0**   
Prevents the debugger from debugging child processes.

<span id="_______1______"></span> **1**   
Causes the debugger to debug child processes.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

This command is only supported in Windows XP and later versions of Windows.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>x86 and x64</p></td>
</tr>
</tbody>
</table>

 

## Remarks

**Child processes** are additional processes launched by the original target application.

With no parameters, **.childdbg** will display the current status of child-process debugging.

 

 





