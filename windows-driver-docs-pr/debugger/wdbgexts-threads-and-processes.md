---
title: WdbgExts Threads and Processes
description: WdbgExts Threads and Processes
keywords: ["WdbgExts extensions, threads", "WdbgExts extensions, processes"]
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# WdbgExts Threads and Processes


This topic provides a brief overview of how threads and processes can be manipulated using the WdbgExts API. For an overview of threads and processes in the [debugger engine](introduction.md#debugger-engine), see [Threads and Processes](threads-and-processes.md) in the [Debugger Engine Overview](debugger-engine-overview.md) section of this documentation.

### <span id="threads"></span><span id="THREADS"></span>Threads

To get the address of the thread environment block (TEB) that describes the current thread, use the method [**GetTebAddress**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-gettebaddress). In kernel-mode debugging, the KTHREAD structure is also available to describe a thread. This structure is returned by [**GetCurrentThreadAddr**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-getcurrentthreadaddr) (in user-mode debugging, **GetCurrentThreadAddr** returns the address of the TEB).

The [thread context](scopes-and-symbol-groups.md#thread-context) is the state preserved by Windows when switching threads; it is represented by the CONTEXT structure. This structure varies with the operating system and platform and care should be taken when using the CONTEXT structure. The thread context is returned by the [**GetContext**](/previous-versions/windows/hardware/previsioning-framework/ff545736(v=vs.85)) function and can be set using the [**SetContext**](/previous-versions/windows/hardware/previsioning-framework/ff556644(v=vs.85)) function.

To examine the stack trace for the current thread, use the [**StackTrace**](/windows-hardware/drivers/ddi/wdbgexts/nc-wdbgexts-pwindbg_stacktrace_routine) function. To temporarily change the thread used for examining the stack trace, use the [**SetThreadForOperation**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-setthreadforoperation) or [**SetThreadForOperation64**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-setthreadforoperation64) functions. See [Examining the Stack Trace](examining-the-stack-trace.md) in the [Using the Debugger Engine API](using-the-debugger-engine-api.md) section of this documentation for additional methods for examining the stack.

To get information about an operating system thread in the target, use the [**Ioctl**](/windows-hardware/drivers/ddi/wdbgexts/nc-wdbgexts-pwindbg_ioctl_routine) operation [**IG\_GET\_THREAD\_OS\_INFO**](/windows-hardware/drivers/ddi/wdbgexts/ns-wdbgexts-_wdbgexts_thread_os_info).

### <span id="processes"></span><span id="PROCESSES"></span>Processes

To get the address of the process environment block (PEB) that describes the current process use the method [**GetPebAddress**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-getpebaddress). In kernel-mode debugging, the KPROCESS structure is also available to describe a process. This structure is returned by [**GetCurrentProcessAddr**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-getcurrentprocessaddr) (in user-mode debugging, **GetCurrentProcessAddr** returns the address of the PEB).

The method [**GetCurrentProcessHandle**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects-getcurrentprocesshandle) returns the system handle for the current process.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For a more powerful thread manipulation and process manipulation API, see [Controlling Threads and Processes](controlling-threads-and-processes.md) in the [Using the Debugger Engine API](using-the-debugger-engine-api.md) section of this documentation.

 

