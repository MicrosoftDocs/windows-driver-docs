---
title: Live User-Mode Targets
description: Live User-Mode Targets
ms.assetid: 2709dd01-6486-471d-afa1-a8441665da8d
keywords: ["Debugger Engine API, targets, user-mode", "Debugger Engine API, disconnecting from a process", "Debugger Engine API, process options"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Live User-Mode Targets


## <span id="ddk_live_user_mode_targets_dbx"></span><span id="DDK_LIVE_USER_MODE_TARGETS_DBX"></span>


The methods for creating and attaching to processes that are listed in this topic can be used for the local computer and for a remote computer running a process server.

A user-mode process can be created using [**Create Process**](https://msdn.microsoft.com/library/windows/hardware/ff539321) or [**CreateProcess2**](https://msdn.microsoft.com/library/windows/hardware/ff539323), which execute a given command to create a process. The method [**AttachProcess**](https://msdn.microsoft.com/library/windows/hardware/ff538150) can be used to attach the [debugger engine](introduction.md#debugger-engine) to an existing user-mode process. [**CreateProcessAndAttach**](https://msdn.microsoft.com/library/windows/hardware/ff540048) and [**CreateProcessAndAttach2**](https://msdn.microsoft.com/library/windows/hardware/ff540055) create a new user-mode process and attach to it or another user-mode process on the same computer. The [**Request**](https://msdn.microsoft.com/library/windows/hardware/ff554564) operations [**DEBUG\_REQUEST\_GET\_ADDITIONAL\_CREATE\_OPTIONS**](https://msdn.microsoft.com/library/windows/hardware/ff541553), [**DEBUG\_REQUEST\_SET\_ADDITIONAL\_CREATE\_OPTIONS**](https://msdn.microsoft.com/library/windows/hardware/ff541586), and [**DEBUG\_REQUEST\_SET\_LOCAL\_IMPLICIT\_COMMAND\_LINE**](https://msdn.microsoft.com/library/windows/hardware/ff541592) can be used to set some of the default options for creating processes.

**Note**   The engine doesn't completely attach to the process until the [**WaitForEvent**](https://msdn.microsoft.com/library/windows/hardware/ff561229) method has been called. Only after the process has generated an event -- for example, the process creation event -- does it become available in the debugger session. See [Debugging Session and Execution Model](debugging-session-and-execution-model.md) for more details.

 

The method [**GetRunningProcessSystemIds**](https://msdn.microsoft.com/library/windows/hardware/ff548265) will return the process IDs of all the running processes on the computer. The process ID of a particular program can be found using [**GetRunningProcessSystemIdByExecutableName**](https://msdn.microsoft.com/library/windows/hardware/ff548254). Given a process ID, a description of the process is returned by [**GetRunningProcessDescription**](https://msdn.microsoft.com/library/windows/hardware/ff548243).

### <span id="Process_Options"></span><span id="process_options"></span><span id="PROCESS_OPTIONS"></span>Process Options

The process options determine part of the engine's behavior when attached to a user-mode process, including whether or not the debugger engine will automatically attach to child processes created by the target process and what the engine does with the target processes when it exits. See [**DEBUG\_PROCESS\_XXX**](https://msdn.microsoft.com/library/windows/hardware/ff541534) for a description of the process options.

The process options can be queried using [**GetProcessOptions**](https://msdn.microsoft.com/library/windows/hardware/ff548163). They can be changed using [**AddProcessOptions**](https://msdn.microsoft.com/library/windows/hardware/ff537917), [**RemoveProcessOptions**](https://msdn.microsoft.com/library/windows/hardware/ff554505), and [**SetProcessOptions**](https://msdn.microsoft.com/library/windows/hardware/ff556765).

### <span id="Disconnecting_from_Processes"></span><span id="disconnecting_from_processes"></span><span id="DISCONNECTING_FROM_PROCESSES"></span>Disconnecting from Processes

There are three different ways for the engine to disconnect from a process.

1.  *Detach*. Resume all the threads in the process so that it will continue running, no longer being debugged. [**DetachCurrentProcess**](https://msdn.microsoft.com/library/windows/hardware/ff541846) will detach the engine from the current process and [**DetachProcesses**](https://msdn.microsoft.com/library/windows/hardware/ff541851) will detach the engine from all processes. Not all targets support detaching. The [**Request**](https://msdn.microsoft.com/library/windows/hardware/ff554564) operation [**DEBUG\_REQUEST\_TARGET\_CAN\_DETACH**](https://msdn.microsoft.com/library/windows/hardware/ff541602) can be used to check if the target supports detaching.

2.  *Terminate*. Attempt to kill the process. [**TerminateCurrentProcess**](https://msdn.microsoft.com/library/windows/hardware/ff558866) will terminate the current process and [**TerminateProcesses**](https://msdn.microsoft.com/library/windows/hardware/ff558867) will terminate all processes in the debugger session.

3.  *Abandon*. Remove the process from the list of processes being debugged. The operating system will still consider the process as being debugged and it will remain suspended until another debugger attaches to it or it is killed. [**AbandonCurrentProcess**](https://msdn.microsoft.com/library/windows/hardware/ff537786) will abandon the current process.

 

 





