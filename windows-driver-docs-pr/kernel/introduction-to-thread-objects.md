---
title: Introduction to Thread Objects
description: Introduction to Thread Objects
ms.assetid: c41dd20e-07c1-432f-b012-ecc45fe44413
keywords: ["thread objects WDK kernel", "system-process threads WDK kernel", "device-dedicated threads WDK kernel", "system worker threads WDK kernel", "worker threads WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Introduction to Thread Objects





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

 

 




