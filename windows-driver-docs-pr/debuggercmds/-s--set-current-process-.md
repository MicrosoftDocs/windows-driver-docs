---
title: "|s (Set Current Process)"
description: "The |s command sets or displays the current process number."
keywords: ["|s (Set Current Process) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- s (Set Current Process)
api_type:
- NA
---

# |s (Set Current Process)

The **|s** command sets or displays the current process number.

Do not confuse this command with the [**s (Search Memory)**](s--search-memory-.md), [**~s (Change Current Processor)**](-s--change-current-processor-.md), [**~s (Set Current Thread)**](-s--set-current-thread-.md), or [**||s (Set Current System)**](--s--set-current-system-.md) command.

```dbgcmd
|Process s 
|s 
```

## Parameters

<span id="_______Process______"></span><span id="_______process______"></span><span id="_______PROCESS______"></span> *Process*   
Specifies the process to set or display. For more information about the syntax, see [Process Syntax](process-syntax.md).

## Environment

| Item      | Description      |
|-----------|------------------|
| Modes     | User mode only   |
| Targets   | Live, crash dump |
| Platforms | All              |

## Additional Information

For more information about other methods of displaying or controlling processes and threads, see [Controlling Processes and Threads](../debugger/controlling-processes-and-threads.md).

## Remarks

You can specify processes only in user mode.

If you use the **|s** syntax, the debugger displays information about the current process.

This command also disassembles the current instruction for the current system, process, and thread.
