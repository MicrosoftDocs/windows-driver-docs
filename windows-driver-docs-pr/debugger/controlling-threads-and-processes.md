---
title: Controlling Threads and Processes
description: Controlling Threads and Processes
keywords: ["Debugger Engine API, threads and processes"]
ms.date: 05/23/2017
---

# Controlling Threads and Processes


## <span id="ddk_threads_and_processes_dbx"></span><span id="DDK_THREADS_AND_PROCESSES_DBX"></span>


For an overview of threads and processes in the debugger engine, see [Threads and Processes](threads-and-processes.md).

When an event occurs, the event thread and event process are set to the thread and process (operating system or virtual) in which the event occurred. They can be found using [**GetEventThread**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects4-geteventthread) and [**GetEventProcess**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects4-geteventprocess), respectively.

### <span id="implicit_threads_and_processes"></span><span id="IMPLICIT_THREADS_AND_PROCESSES"></span>Implicit Threads and Processes

In kernel-mode debugging the debugger engine will use the *implicit process* to determine which virtual address space to use when performing virtual to physical address translation -- for example, in the methods [**VirtualToPhysical**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-virtualtophysical) and [**ReadVirtual**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-readvirtual). When an event occurs, the implicit process is set to the current process.

The implicit process may be changed by using [**SetImplicitProcessDataOffset**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects4-setimplicitprocessdataoffset). To determine the implicit process use [**GetImplicitProcessDataOffset**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects4-getimplicitprocessdataoffset).

**Note**   When setting [breakpoints](../debuggercmds/multiprocessor-syntax.md#breakpoints) during a live kernel debugging session, the debugger engine will pass the virtual address of the breakpoint to the target, and the target will set the breakpoint. In this case, only the process context of the target is used when handling the breakpoint; the value of the implicit process is irrelevant.

 

In kernel-mode debugging, the debugger engine will use the *implicit thread* to determine some of the target's [registers](x86-architecture.md#registers). This includes the processor stack (see [**GetStackOffset**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugregisters2-getstackoffset)), the frame offset (see [**GetFrameOffset**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugregisters2-getframeoffset)), and the instruction offset (see [**GetInstructionOffset**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugregisters2-getinstructionoffset)). When an event occurs, the implicit thread is set to the current thread.

The implicit thread may be changed by using [**SetImplicitThreadDataOffset**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects4-setimplicitthreaddataoffset). To determine the implicit thread, use [**GetImplicitThreadDataOffset**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects4-getimplicitthreaddataoffset).

Not all registers are determined by the implicit thread. Some registers will remain the same when the implicit thread is changed.

**Warning**   The implicit process and implicit thread are independent. If the implicit thread does not belong to the implicit process, then user and session state for the implicit thread will be in the wrong virtual address space and attempts to access this information will cause errors or provide incorrect results. This problem does not occur when accessing kernel memory, since kernel memory addresses are constant across all virtual address spaces. Thus information for the implicit thread located in kernel memory may be accessed independent of the implicit process.

 

### <span id="threads"></span><span id="THREADS"></span>Threads

The *engine thread ID* is used by the debugger engine to identify each operating system thread and each virtual thread for a target.

While a target is stopped, each thread also has an index relative to the process to which it belongs. For any process, the index of the first thread in the process is zero, and the index of the last thread is the number of threads in the process minus one. The number of threads in the current process can be found by using [**GetNumberThreads**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects4-getnumberthreads). The total number of threads in all processes in the current target can be found by using [**GetTotalNumberThreads**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects4-gettotalnumberthreads).

The engine thread ID and system thread ID for one or more threads in the current process can be found from their index by using [**GetThreadIdsByIndex**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects4-getthreadidsbyindex).

The engine maintains several pieces of information about each thread. This information may be queried for the current thread, and may be used to find the engine thread ID for a thread.

<span id="system_thread_ID__user-mode_debugging_only_"></span><span id="system_thread_id__user-mode_debugging_only_"></span><span id="SYSTEM_THREAD_ID__USER-MODE_DEBUGGING_ONLY_"></span>system thread ID (user-mode debugging only)  
The system thread ID of the current thread can be found by using [**GetCurrentThreadSystemId**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects4-getcurrentthreadsystemid). For a given system thread ID, the corresponding engine thread ID may be found by using [**GetThreadIdBySystemId**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects4-getthreadidbysystemid).

<span id="thread_environment_block__TEB_"></span><span id="thread_environment_block__teb_"></span><span id="THREAD_ENVIRONMENT_BLOCK__TEB_"></span>thread environment block (TEB)  
The address of the TEB for the current thread can be found by using [**GetCurrentThreadTeb**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects4-getcurrentthreadteb). For a given TEB address, the corresponding engine thread ID may be found by using [**GetThreadIdByTeb**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects4-getthreadidbyteb). In kernel-mode debugging, the TEB of a (virtual) thread is the TEB of the system thread that was running on the corresponding processor when the last event occurred.

<span id="data_offset"></span><span id="DATA_OFFSET"></span>data offset  
In user-mode debugging, the data offset of a (system) thread is the location of the TEB for that thread. In kernel-mode debugging the data offset of a (virtual) thread is the KTHREAD structure for the system thread that was running on the corresponding processor when the last event occurred. The data offset of the current thread can be found by using [**GetCurrentThreadDataOffset**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects4-getcurrentthreaddataoffset). For a given data offset, the corresponding engine thread ID may be found by using [**GetThreadIdByDataOffset**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects4-getthreadidbydataoffset).

<span id="system_handle"></span><span id="SYSTEM_HANDLE"></span>system handle  
The system handle of the current thread can be found by using [**GetCurrentThreadHandle**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects4-getcurrentthreadhandle). For a given system handle, the corresponding engine thread ID may be found by using [**GetThreadIdByHandle**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects4-getthreadidbyhandle). In kernel-mode debugging, an artificial handle is created for each (virtual) process. This handle can only be used with debugger engine API queries.

### <span id="processes"></span><span id="PROCESSES"></span>Processes

The *engine process ID* is used by the debugger engine to identify each operating system process and each virtual process for a target.

While a target is stopped, each process has an index relative to the target. The index of the first process in the target is zero, and the index of the last process is the number of processes in the target minus one. The number of processes in the current target can be found by using [**GetNumberProcesses**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects4-getnumberprocesses).

The engine process ID and system process ID for one or more threads in the current target can be found from their index by using [**GetProcessIdsByIndex**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects4-getprocessidsbyindex).

The engine maintains several pieces of information about each process. This information may be queried for the current process, and may be used to find the engine process ID for a process.

<span id="system_process_ID__user-mode_debugging_only_"></span><span id="system_process_id__user-mode_debugging_only_"></span><span id="SYSTEM_PROCESS_ID__USER-MODE_DEBUGGING_ONLY_"></span>system process ID (user-mode debugging only)  
The system process ID of the current process can be found by using [**GetCurrentProcessSystemId**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects4-getcurrentprocesssystemid). For a given system process ID, the corresponding engine process ID may be found by using [**GetProcessIdBySystemId**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects4-getprocessidbysystemid).

<span id="process_environment_block__PEB_"></span><span id="process_environment_block__peb_"></span><span id="PROCESS_ENVIRONMENT_BLOCK__PEB_"></span>process environment block (PEB)  
The address of the PEB for the current process can be found by using [**GetCurrentProcessPeb**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects4-getcurrentprocesspeb). For a given PEB address, the corresponding engine process ID may be found by using [**GetProcessIdByPeb**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects4-getprocessidbypeb). In kernel-mode debugging, the PEB of the (virtual) process is the PEB of the system process that was running when the last event occurred.

<span id="data_offset"></span><span id="DATA_OFFSET"></span>data offset  
In user-mode debugging, the data offset of a (system) process is the location of the PEB of that process. In kernel-mode debugging, the data offset of the (virtual) process is the KPROCESS structure for the system process that was running when the last event occurred. The data offset of the current process can be found by using [**GetCurrentProcessDataOffset**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects4-getcurrentprocessdataoffset). For a given data offset, the corresponding engine process ID may be found by using [**GetProcessIdByDataOffset**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects4-getprocessidbydataoffset).

<span id="system_handle"></span><span id="SYSTEM_HANDLE"></span>system handle  
The system handle of the current process can be found by using [**GetCurrentProcessHandle**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects4-getcurrentprocesshandle). For a given system handle, the corresponding engine process ID may be found by using [**GetProcessIdByHandle**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects4-getprocessidbyhandle). In kernel-mode debugging, an artificial handle is created for the (virtual) process. This handle can only be used with debugger engine queries.

### <span id="events"></span><span id="EVENTS"></span>Events

In live user-mode debugging, whenever a thread is created or exits in a target, the create-thread and exit-thread debugging events are generated. These events result in calls to the [**IDebugEventCallbacks::CreateThread**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugeventcallbacks-createthread) and [**IDebugEventCallbacks::ExitThread**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugeventcallbacks-exitthread) callback methods.

In live user-mode debugging, whenever a process is created or exits in a target, the create-process and exit-process debugging events are generated. These events result in calls to the [**IDebugEventCallbacks::CreateProcess**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugeventcallbacks-createprocess) and [**IDebugEventCallbacks::ExitProcess**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugeventcallbacks-exitprocess) callback methods.

For more information about events, see [Monitoring Events](monitoring-events.md).

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about threads and processes, including the TEB, KTHREAD, PEB, and KPROCESS structures, see *Microsoft Windows Internals* by David Solomon and Mark Russinovich.

 

