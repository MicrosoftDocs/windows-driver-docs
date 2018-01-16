---
title: Threads and Processes
description: Threads and Processes
ms.assetid: 7ba8226c-3fb3-4ed6-8f87-69a7999e34ad
keywords: ["Debugger Engine, threads and processes"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Threads and Processes


### <span id="terminology"></span><span id="TERMINOLOGY"></span>Terminology

Thread and a process concepts are different between user-mode debugging and kernel-mode debugging.

-   In *user-mode debugging*, a *process* is an operating system process and a *thread* is an operating system thread.

-   In *kernel-mode debugging*, the [debugger engine](introduction.md#debugger-engine) creates a *virtual process* for each target; this process represents the kernel and does not correspond to any operating system process. For each physical processor in the target computer, the debugger creates a *virtual thread*; these threads represent the processors and do not correspond to any operating system threads.

When an event occurs, the engine sets the *event process* and *event thread* to the process and thread (operating system or virtual) in which the event occurred.

The *current thread* is the thread (operating system or virtual) that the engine is currently controlling. The *current process* is the process (operating system or virtual) that the engine is currently controlling. When an event occurs, the current thread and process are initially set to the event thread and process; but, they can be changed using the clients while the session is accessible.

In kernel mode, the debugger keeps track of an implicit process and implicit thread. The *implicit process* is the operating system process that determines the translation from virtual to physical memory addresses.

The *implicit thread* is the operating system thread that determines the target's registers, including call stack, stack frame, and instruction offset.

When an event occurs, the implicit thread and implicit process are initially set to the event thread and process; they can be changed while the session is accessible.

### <span id="thread_and_process_data"></span><span id="THREAD_AND_PROCESS_DATA"></span>Thread and Process Data

The engine maintains several pieces of information about each thread and process. This includes the system thread and process ID and system handles, and the process environment (PEB), the thread environment block (TEB), and their locations in target's memory.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For details about using thread and processes, see [Controlling Threads and Processes](controlling-threads-and-processes.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Threads%20and%20Processes%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




