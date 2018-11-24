---
title: Windows Kernel-Mode Process and Thread Manager
description: Windows Kernel-Mode Process and Thread Manager
ms.assetid: 4053c73e-190d-4ffe-8db2-f531d120ba81
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Windows Kernel-Mode Process and Thread Manager


A *process* is a software program that is currently running in Windows. Every process has an ID, a number that identifies it. A *thread* is an object that identifies which part of the program is running. Each thread has an ID, a number that identifies it.

A process may have more than one thread. The purpose of a thread is to allocate processor time. On a machine with one processor, more than one thread can be allocated, but only one thread can run at a time. Each thread only runs a short time and then the execution is passed on to the next thread, giving the user the illusion that more than one thing is happening at once. On a machine with more than one processor, true multi-threading can take place. If an application has multiple threads, the threads can run simultaneously on different processors.

The Windows kernel-mode process and thread manager handles the execution of all threads in a process. Whether you have one processor or more, great care must be taken in driver programming to make sure that all threads of your process are designed so that no matter what order the threads are handled, your driver will operate properly.

If threads from different processes attempt to use the same resource at the same time, problems can occur. Windows provides several techniques to avoid this problem. The technique of making sure that threads from different processes do not touch the same resource is called *synchronization*. For more information about synchronization, see [Synchronization Techniques](synchronization-techniques.md).

Routines that provide a direct interface to the process and thread manager are usually prefixed with the letters "**Ps**"; for example, **PsCreateSystemThread**. For a list of kernel DDIs, see [Windows kernel](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_kernel/).

This set of guidelines applies to these callback routines:

[_PCREATE_PROCESS_NOTIFY_ROUTINE_](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nc-ntddk-pcreate_process_notify_routine)

[_PCREATE_PROCESS_NOTIFY_ROUTINE_EX_](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nc-ntddk-pcreate_process_notify_routine_ex)

[_PCREATE_THREAD_NOTIFY_ROUTINE_](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nc-ntddk-pcreate_thread_notify_routine)

[_PLOAD_IMAGE_NOTIFY_ROUTINE_](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nc-ntddk-pload_image_notify_routine)

-    Keep notify routines short and simple.
-    Do not make calls into a user mode service to validate the process, thread, or image. 
-    Do not make registry calls. 
-    Do not make blocking and/or Interprocess Communication (IPC) function calls. 
-    Do not synchronize with other threads because it can lead to reentrancy deadlocks. 
-    Use [System Worker Threads](https://docs.microsoft.com/windows-hardware/drivers/kernel/system-worker-threads) to queue work especially work involving: 
        -    Slow API’s or API’s that call into other process.
        -    Any blocking behavior which could interrupt threads in core services. 
-    Be considerate of best practices for kernel mode stack usage. For examples, see [How do I keep my driver from running out of kernel-mode stack?](https://docs.microsoft.com/previous-versions/windows/hardware/design/dn613940(v=vs.85)) and [Key Driver Concepts and Tips](https://docs.microsoft.com/previous-versions/windows/hardware/design/dn614604(v%3dvs.85)).


## Subsystem Processes


Starting in Windows 10, the Windows Subsystem for Linux (WSL) enables a user to run native Linux ELF64 binaries on Windows, alongside other Windows applications. For information about WSL architecture and the user-mode and kernel-mode components that are required to run the binaries, see the posts on the [Windows Subsystem for Linux](https://go.microsoft.com/fwlink/p/?linkid=838012) blog.

One of the components is a *subsystem process* that hosts the unmodified user-mode Linux binary, such as /bin/bash. Subsystem processes do not contain data structures associated with Win32 processes, such as Process Environment Block (PEB) and Thread Environment Block (TEB). For a subsystem process, system calls and user mode exceptions are dispatched to a paired driver.

Here are the changes to the [Process and Thread Manager Routines](https://msdn.microsoft.com/library/windows/hardware/ff559917) in order to support subsystem processes:

-   The WSL type is indicated by the **SubsystemInformationTypeWSL** value in the [**SUBSYSTEM\_INFORMATION\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/mt805892) enumeration. Drivers can call [**NtQueryInformationProcess**](https://msdn.microsoft.com/library/windows/desktop/ms684280) and [**NtQueryInformationThread**](https://msdn.microsoft.com/library/windows/desktop/ms684283) to determine the underlying subsystem. Those calls return **SubsystemInformationTypeWSL** for WSL.
-   Other kernel mode drivers can get notified about subsystem process creation/deletion by registering their callback routine through the [**PsSetCreateProcessNotifyRoutineEx2**](https://msdn.microsoft.com/library/windows/hardware/mt805891) call. To get notifications about thread creation/deletion, drivers can call [**PsSetCreateThreadNotifyRoutineEx**](https://msdn.microsoft.com/library/windows/hardware/dn957857), and specify **PsCreateThreadNotifySubsystems** as the type of notification.
-   The [**PS\_CREATE\_NOTIFY\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff559960) structure has been extended to include a **IsSubsystemProcess** member that indicates a subsystem other than Win32. Other members such as **FileObject**, **ImageFileName**, **CommandLine** indicate additional information about the subsystem process. For information about the behavior of those members, see [**SUBSYSTEM\_INFORMATION\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/mt805892).

 

 




