---
title: ".create (Create Process)"
description: "The .create command creates a new target application."
keywords: [".create (Create Process) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .create (Create Process)
api_type:
- NA
---

# .create (Create Process)


The **.create** command creates a new target application.

```dbgsyntax
.create [-premote RemoteOptions] [-f] CommandLine 
```

## <span id="ddk_meta_create_process_dbg"></span><span id="DDK_META_CREATE_PROCESS_DBG"></span>Parameters


<span id="_______RemoteOptions______"></span><span id="_______remoteoptions______"></span><span id="_______REMOTEOPTIONS______"></span> *RemoteOptions*   
Specifies a process server to which to attach. The options are the same as those for the command line **-premote** option. See [**Activating a Smart Client**](../debugger/activating-a-smart-client.md) for syntax details.

<span id="_______-f______"></span><span id="_______-F______"></span> **-f**   
Freezes all threads in all target applications, except in the new target being created. These threads will remain frozen until an exception occurs in the newly-created process. Note that an initial breakpoint qualifies as an exception. Individual threads can be unfrozen by using the [**~u (Unfreeze Thread)**](-u--unfreeze-thread-.md) command.

<span id="_______CommandLine______"></span><span id="_______commandline______"></span><span id="_______COMMANDLINE______"></span> *CommandLine*   
Specifies the complete command line for the new process. *CommandLine* may contain spaces, and must not be surrounded with quotes. All text after the **.create** command is taken as part of *CommandLine*; this command cannot be followed with a semicolon and additional debugger commands.

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes | user mode only |
|Targets | live debugging only |
|Platforms | all  |
 

## Remarks

This command can be used when CDB is dormant, or if it is already debugging one or more processes. It cannot be used when WinDbg is dormant.

If this command is successful, the debugger will create the specified process the next time the debugger issues an execution command. If this command is used several times in a row, execution will have to be requested as many times as this command was used.

Multiple target processes will always be executed together, unless some of their threads are frozen or suspended.

If you wish to create a new process and freeze all your existing targets, use the -f option.

If the **-premote** option is used, the new process will be part of a new system. For details, see [Debugging Multiple Targets](../debugger/debugging-multiple-targets.md).

