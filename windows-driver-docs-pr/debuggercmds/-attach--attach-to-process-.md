---
title: ".attach (Attach to Process)"
description: "The .attach command attaches to a new target application."
keywords: ["Attach to Process (.attach) command", "process, Attach to Process (.attach) command", ".attach (Attach to Process) Windows Debugging"]
ms.date: 09/17/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- .attach (Attach to Process)
api_type:
- NA
---

# .attach (Attach to Process)


The **.attach** command attaches to a new target application.

```dbgcmd    
.attach [-premote RemoteOptions] AttachOptions PID
```

## <span id="ddk_meta_attach_to_process_dbg"></span><span id="DDK_META_ATTACH_TO_PROCESS_DBG"></span>Parameters


<span id="_______RemoteOptions______"></span><span id="_______remoteoptions______"></span><span id="_______REMOTEOPTIONS______"></span> *RemoteOptions*   
Specifies a process server to attach to. The options are the same as those for the command line **-premote** option. See [**Activating a Smart Client**](../debugger/activating-a-smart-client.md) for syntax details.

<span id="_______AttachOptions______"></span><span id="_______attachoptions______"></span><span id="_______ATTACHOPTIONS______"></span> *AttachOptions*   
Specifies how the attach is to be done. This can include any of the following options:

<span id="-b"></span><span id="-B"></span>**-b**  
Prevents the debugger from requesting an initial break-in when attaching to a target process. This can be useful if the application is already suspended, or if you want to avoid creating a break-in thread in the target.

<span id="-e"></span><span id="-E"></span>**-e**  
Allows the debugger to attach to a process that is already being debugged. See [Re-attaching to the Target Application](../debugger/reattaching-to-the-target-application.md) for details.

<span id="-k"></span><span id="-K"></span>**-k**  
Begins a local kernel debugging session. See [Performing Local Kernel Debugging](../debugger/performing-local-kernel-debugging.md) for details.

<span id="-f"></span><span id="-F"></span>**-f**  
Freezes all threads in all target applications, except in the new target being attached to. These threads will remain frozen until an exception occurs in the newly-attached process. Note that an initial breakpoint qualifies as an exception. Individual threads can be unfrozen by using the [**~u (Unfreeze Thread)**](-u--unfreeze-thread-.md) command.

<span id="-r"></span><span id="-R"></span>**-r**  

Causes the debugger to start the target process running when it attaches to it. This can be useful if the application is already suspended and you want it to resume execution.

<span id="-v"></span><span id="-V"></span>**-v**  
Causes the specified process to be debugged noninvasively.

<span id="_______PID______"></span><span id="_______pid______"></span> *PID*   
Specifies the process ID of the new target application.

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes | user mode only |
|Targets | live debugging only |
|Platforms | all  |
 

## Remarks

This command can be used when CDB is dormant, or if it is already debugging one or more processes. It cannot be used when WinDbg is dormant.

If this command is successful, the debugger will attach to the specified process the next time the debugger issues an execution command. If this command is used several times in a row, execution will have to be requested as many times as this command was used.

Because execution is not permitted during noninvasive debugging, the debugger is not able to noninvasively debug more than one process at a time. This also means that using the **.attach -v** command may render an already-existing invasive debugging session less useful.

Multiple target processes will always be executed together, unless some of their threads are frozen or suspended.

If you wish to attach to a new process and freeze all your existing targets, use the **-f** option. For example, you might be debugging a crash in a client application and want to attach to the server process without letting the client application continue running.

If the **-premote** option is used, the new process will be part of a new system. For details, see [Debugging Multiple Targets](../debugger/debugging-multiple-targets.md).

