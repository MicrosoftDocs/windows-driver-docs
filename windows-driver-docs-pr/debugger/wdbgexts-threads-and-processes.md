---
title: WdbgExts Threads and Processes
description: WdbgExts Threads and Processes
ms.assetid: fa513435-ea91-4dc5-9488-85087d585f96
keywords: ["WdbgExts extensions, threads", "WdbgExts extensions, processes"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# WdbgExts Threads and Processes


This topic provides a brief overview of how threads and processes can be manipulated using the WdbgExts API. For an overview of threads and processes in the [debugger engine](introduction.md#debugger-engine), see [Threads and Processes](threads-and-processes.md) in the [Debugger Engine Overview](debugger-engine-overview.md) section of this documentation.

### <span id="threads"></span><span id="THREADS"></span>Threads

To get the address of the thread environment block (TEB) that describes the current thread, use the method [**GetTebAddress**](https://msdn.microsoft.com/library/windows/hardware/ff549267). In kernel-mode debugging, the KTHREAD structure is also available to describe a thread. This structure is returned by [**GetCurrentThreadAddr**](https://msdn.microsoft.com/library/windows/hardware/ff545889) (in user-mode debugging, **GetCurrentThreadAddr** returns the address of the TEB).

The [thread context](scopes-and-symbol-groups.md#thread-context) is the state preserved by Windows when switching threads; it is represented by the CONTEXT structure. This structure varies with the operating system and platform and care should be taken when using the CONTEXT structure. The thread context is returned by the [**GetContext**](https://msdn.microsoft.com/library/windows/hardware/ff545736) function and can be set using the [**SetContext**](https://msdn.microsoft.com/library/windows/hardware/ff556644) function.

To examine the stack trace for the current thread, use the [**StackTrace**](https://msdn.microsoft.com/library/windows/hardware/ff558794) function. To temporarily change the thread used for examining the stack trace, use the [**SetThreadForOperation**](https://msdn.microsoft.com/library/windows/hardware/ff556830) or [**SetThreadForOperation64**](https://msdn.microsoft.com/library/windows/hardware/ff556832) functions. See [Examining the Stack Trace](examining-the-stack-trace.md) in the [Using the Debugger Engine API](using-the-debugger-engine-api.md) section of this documentation for additional methods for examining the stack.

To get information about an operating system thread in the target, use the [**Ioctl**](https://msdn.microsoft.com/library/windows/hardware/ff551084) operation [**IG\_GET\_THREAD\_OS\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff550924).

### <span id="processes"></span><span id="PROCESSES"></span>Processes

To get the address of the process environment block (PEB) that describes the current process use the method [**GetPebAddress**](https://msdn.microsoft.com/library/windows/hardware/ff548122). In kernel-mode debugging, the KPROCESS structure is also available to describe a process. This structure is returned by [**GetCurrentProcessAddr**](https://msdn.microsoft.com/library/windows/hardware/ff545779) (in user-mode debugging, **GetCurrentProcessAddr** returns the address of the PEB).

The method [**GetCurrentProcessHandle**](https://msdn.microsoft.com/library/windows/hardware/ff545816) returns the system handle for the current process.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For a more powerful thread manipulation and process manipulation API, see [Controlling Threads and Processes](controlling-threads-and-processes.md) in the [Using the Debugger Engine API](using-the-debugger-engine-api.md) section of this documentation.

 

 





