---
title: ".bpsync (Synchronize Threads at Breakpoint)"
description: "When a thread reaches a breakpoint, the .bpsync command freezes all other threads, until the thread to which the breakpoint applies has stepped through the breakpoint."
keywords: [".bpsync (Synchronize Threads at Breakpoint) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .bpsync (Synchronize Threads at Breakpoint)
api_type:
- NA
---

# .bpsync (Synchronize Threads at Breakpoint)


When a thread reaches a breakpoint, the **.bpsync** command freezes all other threads, until the thread to which the breakpoint applies has stepped through the breakpoint.

```dbgcmd
.bpsync 1
.bpsync 0
.bpsync 
```

## Parameters


<span id="_______1______"></span> **1**   
Causes all threads to freeze when one thread has reached a breakpoint. After the thread to which the breakpoint applies has stepped through the breakpoint, the other threads are unfrozen.

<span id="_______0______"></span> **0**   
Allows other threads to continue executing when one thread has reached a breakpoint. This is the default behavior.

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes|User mode only|
|Targets|Live, crash dump|
|Platforms|All|

 

## Remarks

With no parameters. the **.bpsync** command displays the current rule governing breakpoint synchronization behavior.

The **.bpsync** command applies both to software breakpoints (set with [**bp**](bp--bu--bm--set-breakpoint-.md), **bu**, or **bm**) and to processor breakpoints (set with [**ba**](ba--break-on-access-.md)).

If there is a possibility of multiple threads running through the same code, the **.bpsync 1** command can be useful for capturing all breakpoint occurrences. Without this command, a breakpoint occurrence could be missed because the first thread to reach the breakpoint always causes the debugger to temporarily remove the breakpoint. In the short period when the breakpoint is removed, other threads could reach the same place in the code and not trigger the breakpoint as intended.

The temporary removal of breakpoints is a normal aspect of debugger operation. When the target reaches a breakpoint and is resumed, the debugger has to remove the breakpoint temporarily so that the target can execute the real code. After the real instruction has been executed, the debugger reinserts the break. To do this, the debugger restores the code (or turns off data breaks), does a single-step, and then puts the break back.

Note that if you use **.bpsync 1**, there is a risk of deadlocks among the threads that have been frozen.

