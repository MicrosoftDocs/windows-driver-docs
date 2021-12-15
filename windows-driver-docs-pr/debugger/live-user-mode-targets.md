---
title: Live User-Mode Targets
description: Live User-Mode Targets
keywords: ["Debugger Engine API, targets, user-mode", "Debugger Engine API, disconnecting from a process", "Debugger Engine API, process options"]
ms.date: 05/23/2017
---

# Live User-Mode Targets


## <span id="ddk_live_user_mode_targets_dbx"></span><span id="DDK_LIVE_USER_MODE_TARGETS_DBX"></span>


The methods for creating and attaching to processes that are listed in this topic can be used for the local computer and for a remote computer running a process server.

A user-mode process can be created using [**Create Process**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-createprocess) or [**CreateProcess2**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-createprocess2), which execute a given command to create a process. The method [**AttachProcess**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-attachprocess) can be used to attach the [debugger engine](introduction.md#debugger-engine) to an existing user-mode process. [**CreateProcessAndAttach**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-createprocessandattach) and [**CreateProcessAndAttach2**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-createprocessandattach2) create a new user-mode process and attach to it or another user-mode process on the same computer. The [**Request**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugadvanced3-request) operations [**DEBUG\_REQUEST\_GET\_ADDITIONAL\_CREATE\_OPTIONS**](debug-request-get-additional-create-options.md), [**DEBUG\_REQUEST\_SET\_ADDITIONAL\_CREATE\_OPTIONS**](debug-request-set-additional-create-options.md), and [**DEBUG\_REQUEST\_SET\_LOCAL\_IMPLICIT\_COMMAND\_LINE**](debug-request-set-local-implicit-command-line.md) can be used to set some of the default options for creating processes.

**Note**   The engine doesn't completely attach to the process until the [**WaitForEvent**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-waitforevent) method has been called. Only after the process has generated an event -- for example, the process creation event -- does it become available in the debugger session. See [Debugging Session and Execution Model](debugging-session-and-execution-model.md) for more details.

 

The method [**GetRunningProcessSystemIds**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-getrunningprocesssystemids) will return the process IDs of all the running processes on the computer. The process ID of a particular program can be found using [**GetRunningProcessSystemIdByExecutableName**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-getrunningprocesssystemidbyexecutablename). Given a process ID, a description of the process is returned by [**GetRunningProcessDescription**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-getrunningprocessdescription).

### <span id="Process_Options"></span><span id="process_options"></span><span id="PROCESS_OPTIONS"></span>Process Options

The process options determine part of the engine's behavior when attached to a user-mode process, including whether or not the debugger engine will automatically attach to child processes created by the target process and what the engine does with the target processes when it exits. See [**DEBUG\_PROCESS\_XXX**](./debug-process-xxx.md) for a description of the process options.

The process options can be queried using [**GetProcessOptions**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-getprocessoptions). They can be changed using [**AddProcessOptions**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-addprocessoptions), [**RemoveProcessOptions**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-removeprocessoptions), and [**SetProcessOptions**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-setprocessoptions).

### <span id="Disconnecting_from_Processes"></span><span id="disconnecting_from_processes"></span><span id="DISCONNECTING_FROM_PROCESSES"></span>Disconnecting from Processes

There are three different ways for the engine to disconnect from a process.

1.  *Detach*. Resume all the threads in the process so that it will continue running, no longer being debugged. [**DetachCurrentProcess**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-detachcurrentprocess) will detach the engine from the current process and [**DetachProcesses**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-detachprocesses) will detach the engine from all processes. Not all targets support detaching. The [**Request**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugadvanced3-request) operation [**DEBUG\_REQUEST\_TARGET\_CAN\_DETACH**](./debug-request-target-can-detach.md) can be used to check if the target supports detaching.

2.  *Terminate*. Attempt to kill the process. [**TerminateCurrentProcess**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-terminatecurrentprocess) will terminate the current process and [**TerminateProcesses**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-terminateprocesses) will terminate all processes in the debugger session.

3.  *Abandon*. Remove the process from the list of processes being debugged. The operating system will still consider the process as being debugged and it will remain suspended until another debugger attaches to it or it is killed. [**AbandonCurrentProcess**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-abandoncurrentprocess) will abandon the current process.

 

