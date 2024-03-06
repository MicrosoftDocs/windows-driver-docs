---
title: ~s (Set Current Thread)
description: The ~s command sets or displays the current thread number.
keywords: ["~s (Set Current Thread) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ~s (Set Current Thread)
api_type:
- NA
---

# ~s (Set Current Thread)


The **~s** command sets or displays the current thread number in user mode.

Do not confuse this command with the [**~s (Change Current Processor)**](-s--change-current-processor-.md) command (which works only in kernel mode), the [**|s (Set Current Process)**](-s--set-current-process-.md) command, the [**||s (Set Current System)**](--s--set-current-system-.md) command, or the [**s (Search Memory)**](s--search-memory-.md) command.

```dbgcmd
~Thread s 
~ s 
```

## <span id="ddk_cmd_set_current_thread_dbg"></span><span id="DDK_CMD_SET_CURRENT_THREAD_DBG"></span>Parameters


<span id="_______Thread______"></span><span id="_______thread______"></span><span id="_______THREAD______"></span> *Thread*   
Specifies the thread to set or display. For more information about the syntax, see [Thread Syntax](thread-syntax.md).

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes|User mode only|
|Targets|Live, crash dump|
|Platforms|All|

 

### Additional Information

For more information and other methods of displaying or controlling processes and threads, see [Controlling Processes and Threads](../debugger/controlling-processes-and-threads.md).

## Remarks

You can specify threads only in user mode. In kernel mode, the tilde (~) refers to a processor.

If you use the **~s** syntax, the debugger displays information about the current thread.

This command also disassembles the current instruction for the current system, process, and thread.

 

 





