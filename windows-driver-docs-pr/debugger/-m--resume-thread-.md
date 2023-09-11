---
title: ~m (Resume Thread)
description: The ~m command resumes execution of the specified thread.Do not confuse this command with the m (Move Memory) command.
keywords: ["~m (Resume Thread) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ~m (Resume Thread)
api_type:
- NA
---

# ~m (Resume Thread)


The **~m** command resumes execution of the specified thread.

Do not confuse this command with the [**m (Move Memory)**](m--move-memory-.md) command.

```dbgcmd
~Thread m 
```

## <span id="ddk_cmd_resume_thread_dbg"></span><span id="DDK_CMD_RESUME_THREAD_DBG"></span>Parameters


<span id="_______Thread______"></span><span id="_______thread______"></span><span id="_______THREAD______"></span> *Thread*   
Specifies the thread or threads to resume. For more information about the syntax, see [Thread Syntax](thread-syntax.md).

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes | user mode only |
|Targets | live debugging only |
|Platforms | all  |
 

### Additional Information

For more information about the suspend count and how suspended threads behave and for a list of other commands that control the suspending and freezing of threads, see [Controlling Processes and Threads](controlling-processes-and-threads.md).

## Remarks

You can specify threads only in user mode. In kernel mode, the tilde (~) refers to a processor.

Every time that you use the **~m** command, the thread's suspend count is decreased by one.

 

 





