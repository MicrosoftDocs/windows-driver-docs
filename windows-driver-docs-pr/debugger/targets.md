---
title: Targets
description: Targets
ms.assetid: 103d9b0a-2d51-404e-b8b9-513465427f7b
keywords: ["Debugger Engine, targets"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Targets


The [debugger engine](introduction.md#debugger-engine) supports debugging different types of targets, [user-mode](#live--user-mode-targets) and [kernel-mode](#live--kernel-mode-targets) targets, live targets and crash dump files, and local and remote targets. There are different methods for connecting the engine to these different types of targets.

### <span id="crash_dump_files"></span><span id="CRASH_DUMP_FILES"></span>Crash Dump Files

Both user-mode, and kernel-mode crash-dump files are opened with [**OpenDumpFile**](https://msdn.microsoft.com/library/windows/hardware/ff552322). The engine is also able to create dump files from a target with [**WriteDumpFile2**](https://msdn.microsoft.com/library/windows/hardware/ff561382).

### <span id="live--user-mode-targets"></span><span id="LIVE--USER-MODE-TARGETS"></span>Live, User-Mode Targets

The debugger engine can both create and attach to user-mode processes.

Creating a process is done by providing a command line, and optionally an initial directory and environment, for the new process. The engine can then connect to the new process, or keep the new process suspended while it connects to another process. For example, when debugging an application that consists of both a client and server, it is possible to create a client in a suspended state and attach to an already running server, allowing server breakpoints to be set before the client runs and provokes server operations.

When detaching from a process, the engine can optionally leave the process running normally, kill the process, or abandon the process (leaving it suspended until another debugger attaches to it or it is killed).

The engine can be queried for information about all of the user-mode processes that are running on the computer, including the process ID and name of the executable image that is used to start the process. This information can be used to help locate a process to debug.

### <span id="live--kernel-mode-targets"></span><span id="LIVE--KERNEL-MODE-TARGETS"></span>Live, Kernel-Mode Targets

The method [**AttachKernel**](https://msdn.microsoft.com/library/windows/hardware/ff538145) connects the debugger engine to a Windows kernel.

### <span id="remote-targets"></span><span id="REMOTE-TARGETS"></span>Remote Targets

When using the debugger engine to debug remotely, there are potentially two extra steps:

1.  Connect to the host engine. If the host engine is not the local engine instance, use [**DebugConnect**](https://msdn.microsoft.com/library/windows/hardware/ff540465) to create a client object that is connected to the host engine.

2.  Connect the host engine to the process server or kernel connection server. If the host engine does not connect directly to the target, it must connect to a process server or kernel connection server that does.

Now the client can tell the host engine to acquire a target through the process server or kernel connection server.

### <span id="acquiring_targets"></span><span id="ACQUIRING_TARGETS"></span>Acquiring Targets

When acquiring a target, the acquisition of the target is not complete until the target generates an event. Typically, this means first calling a method to attach the debugger to the target, then calling [**WaitForEvent**](https://msdn.microsoft.com/library/windows/hardware/ff561229) to let the target generate an event. This still holds true when the target is a crash dump file, as these always store an event-typically the event that caused the dump file to be created.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For details about attaching to targets, see [Connecting to Targets](connecting-to-targets.md).

 

 





