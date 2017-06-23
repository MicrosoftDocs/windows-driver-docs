---
title: Introduction to Thread Objects
author: windows-driver-content
description: Introduction to Thread Objects
ms.assetid: c41dd20e-07c1-432f-b012-ecc45fe44413
keywords: ["thread objects WDK kernel", "system-process threads WDK kernel", "device-dedicated threads WDK kernel", "system worker threads WDK kernel", "worker threads WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Introduction to Thread Objects


## <a href="" id="ddk-introduction-to-thread-objects-kg"></a>


A user-mode thread object represents a path of execution within the current process. Every user-mode thread object is implemented through the use of an embedded kernel-mode thread object.

A kernel-mode thread object is an instance of a kernel-defined dispatcher object type. The thread that it represents is the basic schedulable entity in the operating system.

A thread object:

-   Is dispatched for execution by the kernel.

-   Has the following properties at any given moment:

    -   [*dispatch state*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-dispatch-state)

    -   [*priority*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-priority)

    -   [*context*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-context)

    -   Execution mode (kernel or user)

    -   [*affinity*](https://msdn.microsoft.com/library/windows/hardware/ff556270#wdkgloss-affinity)

-   Is "owned by" a process object but can attach itself to another process's address space.

Usually, most drivers execute in the context of the currently running thread, that is, in an arbitrary thread context. While a file system driver can create an independent process for its own device-dedicated threads, file systems usually avoid setting up a driver-created process and threads in order to conserve system memory and to avoid the overhead of context switches.

FSs (and other drivers) can set up device-dedicated (system-process) threads and/or FSs can use system worker threads if they need a driver-specific thread context in which to execute. Drivers use the kernel-mode **Ps*Xxx*** routines to create processes and/or device-dedicated threads. FSs call **Ex*Xxx*** routines to use system worker threads.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Introduction%20to%20Thread%20Objects%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


