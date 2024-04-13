---
title: "~n (Suspend Thread)"
description: "The ~n command suspends execution of the specified thread.Do not confuse this command with the n (Set Number Base) command."
keywords: ["~n (Suspend Thread) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ~n (Suspend Thread)
api_type:
- NA
---

# ~n (Suspend Thread)


The **~n** command suspends execution of the specified thread.

Do not confuse this command with the [**n (Set Number Base)**](n--set-number-base-.md) command.

```dbgcmd
~Thread n 
```

## <span id="ddk_cmd_suspend_thread_dbg"></span><span id="DDK_CMD_SUSPEND_THREAD_DBG"></span>Parameters


<span id="_______Thread______"></span><span id="_______thread______"></span><span id="_______THREAD______"></span> *Thread*   
Specifies the thread or threads to suspend. For more information about the syntax, see [Thread Syntax](thread-syntax.md).

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes | user mode only |
|Targets | live debugging only |
|Platforms | all  |
 

## Additional Information

For more information about the suspend count and how suspended threads behave and for a list of other commands that control the suspending and freezing of threads, see [Controlling Processes and Threads](../debugger/controlling-processes-and-threads.md).

## Remarks

You can specify threads only in user mode. In kernel mode, the tilde (~) refers to a processor.

Every time that you use the **~n** command, the thread's suspend count is increased by one.

The thread's start address is displayed when you use this command.

