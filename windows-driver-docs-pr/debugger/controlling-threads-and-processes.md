---
title: Controlling Threads and Processes
description: Controlling Threads and Processes
ms.assetid: 6182ca34-ee5e-47e9-82fe-29266397e3a8
keywords: ["Debugger Engine API, threads and processes"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Controlling Threads and Processes


## <span id="ddk_threads_and_processes_dbx"></span><span id="DDK_THREADS_AND_PROCESSES_DBX"></span>


For an overview of threads and processes in the debugger engine, see [Threads and Processes](threads-and-processes.md).

When an event occurs, the event thread and event process are set to the thread and process (operating system or virtual) in which the event occurred. They can be found using [**GetEventThread**](https://msdn.microsoft.com/library/windows/hardware/ff546646) and [**GetEventProcess**](https://msdn.microsoft.com/library/windows/hardware/ff546640), respectively.

### <span id="implicit_threads_and_processes"></span><span id="IMPLICIT_THREADS_AND_PROCESSES"></span>Implicit Threads and Processes

In kernel-mode debugging the debugger engine will use the *implicit process* to determine which virtual address space to use when performing virtual to physical address translation -- for example, in the methods [**VirtualToPhysical**](https://msdn.microsoft.com/library/windows/hardware/ff560335) and [**ReadVirtual**](https://msdn.microsoft.com/library/windows/hardware/ff554359). When an event occurs, the implicit process is set to the current process.

The implicit process may be changed by using [**SetImplicitProcessDataOffset**](https://msdn.microsoft.com/library/windows/hardware/ff556713). To determine the implicit process use [**GetImplicitProcessDataOffset**](https://msdn.microsoft.com/library/windows/hardware/ff546865).

**Note**   When setting [breakpoints](multiprocessor-syntax.md#breakpoints) during a live kernel debugging session, the debugger engine will pass the virtual address of the breakpoint to the target, and the target will set the breakpoint. In this case, only the process context of the target is used when handling the breakpoint; the value of the implicit process is irrelevant.

 

In kernel-mode debugging, the debugger engine will use the *implicit thread* to determine some of the target's [registers](x86-architecture.md#registers). This includes the processor stack (see [**GetStackOffset**](https://msdn.microsoft.com/library/windows/hardware/ff548403)), the frame offset (see [**GetFrameOffset**](https://msdn.microsoft.com/library/windows/hardware/ff546806)), and the instruction offset (see [**GetInstructionOffset**](https://msdn.microsoft.com/library/windows/hardware/ff546916)). When an event occurs, the implicit thread is set to the current thread.

The implicit thread may be changed by using [**SetImplicitThreadDataOffset**](https://msdn.microsoft.com/library/windows/hardware/ff556716). To determine the implicit thread, use [**GetImplicitThreadDataOffset**](https://msdn.microsoft.com/library/windows/hardware/ff546871).

Not all registers are determined by the implicit thread. Some registers will remain the same when the implicit thread is changed.

**Warning**   The implicit process and implicit thread are independent. If the implicit thread does not belong to the implicit process, then user and session state for the implicit thread will be in the wrong virtual address space and attempts to access this information will cause errors or provide incorrect results. This problem does not occur when accessing kernel memory, since kernel memory addresses are constant across all virtual address spaces. Thus information for the implicit thread located in kernel memory may be accessed independent of the implicit process.

 

### <span id="threads"></span><span id="THREADS"></span>Threads

The *engine thread ID* is used by the debugger engine to identify each operating system thread and each virtual thread for a target.

While a target is stopped, each thread also has an index relative to the process to which it belongs. For any process, the index of the first thread in the process is zero, and the index of the last thread is the number of threads in the process minus one. The number of threads in the current process can be found by using [**GetNumberThreads**](https://msdn.microsoft.com/library/windows/hardware/ff547992). The total number of threads in all processes in the current target can be found by using [**GetTotalNumberThreads**](https://msdn.microsoft.com/library/windows/hardware/ff549356).

The engine thread ID and system thread ID for one or more threads in the current process can be found from their index by using [**GetThreadIdsByIndex**](https://msdn.microsoft.com/library/windows/hardware/ff549339).

The engine maintains several pieces of information about each thread. This information may be queried for the current thread, and may be used to find the engine thread ID for a thread.

<span id="system_thread_ID__user-mode_debugging_only_"></span><span id="system_thread_id__user-mode_debugging_only_"></span><span id="SYSTEM_THREAD_ID__USER-MODE_DEBUGGING_ONLY_"></span>system thread ID (user-mode debugging only)  
The system thread ID of the current thread can be found by using [**GetCurrentThreadSystemId**](https://msdn.microsoft.com/library/windows/hardware/ff546544). For a given system thread ID, the corresponding engine thread ID may be found by using [**GetThreadIdBySystemId**](https://msdn.microsoft.com/library/windows/hardware/ff549329).

<span id="thread_environment_block__TEB_"></span><span id="thread_environment_block__teb_"></span><span id="THREAD_ENVIRONMENT_BLOCK__TEB_"></span>thread environment block (TEB)  
The address of the TEB for the current thread can be found by using [**GetCurrentThreadTeb**](https://msdn.microsoft.com/library/windows/hardware/ff546549). For a given TEB address, the corresponding engine thread ID may be found by using [**GetThreadIdByTeb**](https://msdn.microsoft.com/library/windows/hardware/ff549336). In kernel-mode debugging, the TEB of a (virtual) thread is the TEB of the system thread that was running on the corresponding processor when the last event occurred.

<span id="data_offset"></span><span id="DATA_OFFSET"></span>data offset  
In user-mode debugging, the data offset of a (system) thread is the location of the TEB for that thread. In kernel-mode debugging the data offset of a (virtual) thread is the KTHREAD structure for the system thread that was running on the corresponding processor when the last event occurred. The data offset of the current thread can be found by using [**GetCurrentThreadDataOffset**](https://msdn.microsoft.com/library/windows/hardware/ff545894). For a given data offset, the corresponding engine thread ID may be found by using [**GetThreadIdByDataOffset**](https://msdn.microsoft.com/library/windows/hardware/ff549302).

<span id="system_handle"></span><span id="SYSTEM_HANDLE"></span>system handle  
The system handle of the current thread can be found by using [**GetCurrentThreadHandle**](https://msdn.microsoft.com/library/windows/hardware/ff545904). For a given system handle, the corresponding engine thread ID may be found by using [**GetThreadIdByHandle**](https://msdn.microsoft.com/library/windows/hardware/ff549312). In kernel-mode debugging, an artificial handle is created for each (virtual) process. This handle can only be used with debugger engine API queries.

### <span id="processes"></span><span id="PROCESSES"></span>Processes

The *engine process ID* is used by the debugger engine to identify each operating system process and each virtual process for a target.

While a target is stopped, each process has an index relative to the target. The index of the first process in the target is zero, and the index of the last process is the number of processes in the target minus one. The number of processes in the current target can be found by using [**GetNumberProcesses**](https://msdn.microsoft.com/library/windows/hardware/ff547946).

The engine process ID and system process ID for one or more threads in the current target can be found from their index by using [**GetProcessIdsByIndex**](https://msdn.microsoft.com/library/windows/hardware/ff548160).

The engine maintains several pieces of information about each process. This information may be queried for the current process, and may be used to find the engine process ID for a process.

<span id="system_process_ID__user-mode_debugging_only_"></span><span id="system_process_id__user-mode_debugging_only_"></span><span id="SYSTEM_PROCESS_ID__USER-MODE_DEBUGGING_ONLY_"></span>system process ID (user-mode debugging only)  
The system process ID of the current process can be found by using [**GetCurrentProcessSystemId**](https://msdn.microsoft.com/library/windows/hardware/ff545850). For a given system process ID, the corresponding engine process ID may be found by using [**GetProcessIdBySystemId**](https://msdn.microsoft.com/library/windows/hardware/ff548155).

<span id="process_environment_block__PEB_"></span><span id="process_environment_block__peb_"></span><span id="PROCESS_ENVIRONMENT_BLOCK__PEB_"></span>process environment block (PEB)  
The address of the PEB for the current process can be found by using [**GetCurrentProcessPeb**](https://msdn.microsoft.com/library/windows/hardware/ff545839). For a given PEB address, the corresponding engine process ID may be found by using [**GetProcessIdByPeb**](https://msdn.microsoft.com/library/windows/hardware/ff548150). In kernel-mode debugging, the PEB of the (virtual) process is the PEB of the system process that was running when the last event occurred.

<span id="data_offset"></span><span id="DATA_OFFSET"></span>data offset  
In user-mode debugging, the data offset of a (system) process is the location of the PEB of that process. In kernel-mode debugging, the data offset of the (virtual) process is the KPROCESS structure for the system process that was running when the last event occurred. The data offset of the current process can be found by using [**GetCurrentProcessDataOffset**](https://msdn.microsoft.com/library/windows/hardware/ff545787). For a given data offset, the corresponding engine process ID may be found by using [**GetProcessIdByDataOffset**](https://msdn.microsoft.com/library/windows/hardware/ff548140).

<span id="system_handle"></span><span id="SYSTEM_HANDLE"></span>system handle  
The system handle of the current process can be found by using [**GetCurrentProcessHandle**](https://msdn.microsoft.com/library/windows/hardware/ff545829). For a given system handle, the corresponding engine process ID may be found by using [**GetProcessIdByHandle**](https://msdn.microsoft.com/library/windows/hardware/ff548147). In kernel-mode debugging, an artificial handle is created for the (virtual) process. This handle can only be used with debugger engine queries.

### <span id="events"></span><span id="EVENTS"></span>Events

In live user-mode debugging, whenever a thread is created or exits in a target, the create-thread and exit-thread debugging events are generated. These events result in calls to the [**IDebugEventCallbacks::CreateThread**](https://msdn.microsoft.com/library/windows/hardware/ff550713) and [**IDebugEventCallbacks::ExitThread**](https://msdn.microsoft.com/library/windows/hardware/ff550730) callback methods.

In live user-mode debugging, whenever a process is created or exits in a target, the create-process and exit-process debugging events are generated. These events result in calls to the [**IDebugEventCallbacks::CreateProcess**](https://msdn.microsoft.com/library/windows/hardware/ff550697) and [**IDebugEventCallbacks::ExitProcess**](https://msdn.microsoft.com/library/windows/hardware/ff550728) callback methods.

For more information about events, see [Monitoring Events](monitoring-events.md).

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about threads and processes, including the TEB, KTHREAD, PEB, and KPROCESS structures, see *Microsoft Windows Internals* by David Solomon and Mark Russinovich.

 

 





