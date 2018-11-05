---
title: .bpsync (Synchronize Threads at Breakpoint)
description: When a thread reaches a breakpoint, the .bpsync command freezes all other threads, until the thread to which the breakpoint applies has stepped through the breakpoint.
ms.assetid: 3e97ea97-77b8-4a22-b49c-c99739b42d59
keywords: [".bpsync (Synchronize Threads at Breakpoint) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .bpsync (Synchronize Threads at Breakpoint)
api_type:
- NA
ms.localizationpriority: medium
---

# .bpsync (Synchronize Threads at Breakpoint)


When a thread reaches a breakpoint, the **.bpsync** command freezes all other threads, until the thread to which the breakpoint applies has stepped through the breakpoint.

```dbgcmd
.bpsync 1
.bpsync 0
.bpsync 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______1______"></span> **1**   
Causes all threads to freeze when one thread has reached a breakpoint. After the thread to which the breakpoint applies has stepped through the breakpoint, the other threads are unfrozen.

<span id="_______0______"></span> **0**   
Allows other threads to continue executing when one thread has reached a breakpoint. This is the default behavior.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

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
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

With no parameters. the **.bpsync** command displays the current rule governing breakpoint synchronization behavior.

The **.bpsync** command applies both to software breakpoints (set with [**bp**](bp--bu--bm--set-breakpoint-.md), **bu**, or **bm**) and to processor breakpoints (set with [**ba**](ba--break-on-access-.md)).

If there is a possibility of multiple threads running through the same code, the **.bpsync 1** command can be useful for capturing all breakpoint occurrences. Without this command, a breakpoint occurrence could be missed because the first thread to reach the breakpoint always causes the debugger to temporarily remove the breakpoint. In the short period when the breakpoint is removed, other threads could reach the same place in the code and not trigger the breakpoint as intended.

The temporary removal of breakpoints is a normal aspect of debugger operation. When the target reaches a breakpoint and is resumed, the debugger has to remove the breakpoint temporarily so that the target can execute the real code. After the real instruction has been executed, the debugger reinserts the break. To do this, the debugger restores the code (or turns off data breaks), does a single-step, and then puts the break back.

Note that if you use **.bpsync 1**, there is a risk of deadlocks among the threads that have been frozen.

 

 





