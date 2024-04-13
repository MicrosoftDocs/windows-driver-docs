---
title: DEBUG_PROCESS_XXX
description: The process options are a bit set that control how the debugger engine treats user-modeprocesses. Some of these process options are global; others are specific to a process.
ms.date: 12/07/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- DEBUG_PROCESS_DETACH_ON_EXIT
- DEBUG_PROCESS_ONLY_THIS_PROCESS
api_location:
- DbgEng.h
api_type:
- HeaderDef
---

# DEBUG\_PROCESS\_XXX


The process options are a bit set that control how the [debugger engine](./introduction.md#debugger-engine) treats user-mode[processes](./controlling-threads-and-processes.md#processes). Some of these process options are global; others are specific to a process.

The process options only apply to live user-mode debugging.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Bit-flag</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><span id="DEBUG_PROCESS_DETACH_ON_EXIT"></span><span id="debug_process_detach_on_exit"></span>
<strong>DEBUG_PROCESS_DETACH_ON_EXIT</strong></td>
<td align="left"><p>The debugger automatically detaches itself from the target process when the debugger exits. This is a global setting.</p></td>
</tr>
<tr class="even">
<td align="left"><span id="DEBUG_PROCESS_ONLY_THIS_PROCESS"></span><span id="debug_process_only_this_process"></span>
<strong>DEBUG_PROCESS_ONLY_THIS_PROCESS</strong></td>
<td align="left"><p>The debugger will not debug child processes that are created by this process.</p></td>
</tr>
</tbody>
</table>

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">DbgEng.h (include DbgEng.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**.childdbg**](../debuggercmds/../debuggercmds/-childdbg--debug-child-processes-.md)

 

