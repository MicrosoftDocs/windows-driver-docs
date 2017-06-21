---
title: Windows Kernel-Mode Process and Thread Manager
author: windows-driver-content
description: Windows Kernel-Mode Process and Thread Manager
ms.assetid: 4053c73e-190d-4ffe-8db2-f531d120ba81
---

# Windows Kernel-Mode Process and Thread Manager


A *process* is a software program that is currently running in Windows. Every process has an ID, a number that identifies it. A *thread* is an object that identifies which part of the program is running. Each thread has an ID, a number that identifies it.

A process may have more than one thread. The purpose of a thread is to allocate processor time. On a machine with one processor, more than one thread can be allocated, but only one thread can run at a time. Each thread only runs a short time and then the execution is passed on to the next thread, giving the user the illusion that more than one thing is happening at once. On a machine with more than one processor, true multi-threading can take place. If an application has multiple threads, the threads can run simultaneously on different processors.

The Windows kernel-mode process and thread manager handles the execution of all threads in a process. Whether you have one processor or more, great care must be taken in driver programming to make sure that all threads of your process are designed so that no matter what order the threads are handled, your driver will operate properly.

If threads from different processes attempt to use the same resource at the same time, problems can occur. Windows provides several techniques to avoid this problem. The technique of making sure that threads from different processes do not touch the same resource is called *synchronization*. For more information about synchronization, see [Synchronization Techniques](synchronization-techniques.md).

Routines that provide a direct interface to the process and thread manager are usually prefixed with the letters "**Ps**"; for example, **PsCreateSystemThread**. For a list of process and thread manager routines, see [Process and Thread Manager Routines](https://msdn.microsoft.com/library/windows/hardware/ff559917). For a list of routines that relate to processes, threads, and synchronization, see [Synchronization](https://msdn.microsoft.com/library/windows/hardware/ff564517).

## Subsystem Processes


Starting in Windows 10, the Windows Subsystem for Linux (WSL) enables a user to run native Linux ELF64 binaries on Windows, alongside other Windows applications. For information about WSL architecture and the user-mode and kernel-mode components that are required to run the binaries, see the posts on the [Windows Subsystem for Linux](https://go.microsoft.com/fwlink/p/?linkid=838012) blog.

One of the components is a *subsystem process* that hosts the unmodified user-mode Linux binary, such as /bin/bash. Subsystem processes do not contain data structures associated with Win32 processes, such as Process Environment Block (PEB) and Thread Environment Block (TEB). For a subsystem process, system calls and user mode exceptions are dispatched to a paired driver.

Here are the changes to the [Process and Thread Manager Routines](https://msdn.microsoft.com/library/windows/hardware/ff559917) in order to support subsystem processes:

-   The WSL type is indicated by the **SubsystemInformationTypeWSL** value in the [**SUBSYSTEM\_INFORMATION\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/mt805892) enumeration. Drivers can call [**NtQueryInformationProcess**](https://msdn.microsoft.com/library/windows/desktop/ms684280) and [**NtQueryInformationThread**](https://msdn.microsoft.com/library/windows/desktop/ms684283) to determine the underlying subsystem. Those calls return **SubsystemInformationTypeWSL** for WSL.
-   Other kernel mode drivers can get notified about subsystem process creation/deletion by registering their callback routine through the [**PsSetCreateProcessNotifyRoutineEx2**](https://msdn.microsoft.com/library/windows/hardware/mt805891) call. To get notifications about thread creation/deletion, drivers can call [**PsSetCreateThreadNotifyRoutineEx**](https://msdn.microsoft.com/library/windows/hardware/dn957857), and specify **PsCreateThreadNotifySubsystems** as the type of notification.
-   The [**PS\_CREATE\_NOTIFY\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff559960) structure has been extended to include a **IsSubsystemProcess** member that indicates a subsystem other than Win32. Other members such as **FileObject**, **ImageFileName**, **CommandLine** indicate additional information about the subsystem process. For information about the behavior of those members, see [**SUBSYSTEM\_INFORMATION\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/mt805892).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Windows%20Kernel-Mode%20Process%20and%20Thread%20Manager%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


