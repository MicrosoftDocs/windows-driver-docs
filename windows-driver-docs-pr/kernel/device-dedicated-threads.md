---
title: Device-Dedicated Threads
description: Device-Dedicated Threads
keywords: ["thread objects WDK kernel", "device-dedicated threads WDK kernel", "run-time priority inversions WDK kernel", "PsCreateSystemThread", "KeSetBasePriorityThread"]
ms.date: 10/10/2025
ms.topic: concept-article
---

# Device-dedicated threads

The driver for a slow device or a device that you seldom use (like a CD/DVD drive) can solve many "waiting" problems by creating a device-dedicated system thread. Additionally, most file system drivers use system worker threads and supply worker-thread callback routines.

If a device driver has its own thread context or runs in a system-thread context, it can use synchronization objects for coordination. The device-dedicated thread or highest-level driver's worker-thread callback routine can synchronize operations on a dispatcher object, such as an [event object](event-objects.md) or [semaphore object](semaphore-objects.md), in a shared communication region of the driver's device extension. For example, a device-dedicated thread can wait for a shared dispatcher object, while the thread's device isn't in use, by calling [**KeWaitForSingleObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kewaitforsingleobject) for a semaphore. Until the device driver is called to carry out an I/O operation, its waiting thread uses no CPU time. When the driver is called, it sets the semaphore to the Signaled state.

A driver can call [**PsCreateSystemThread**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pscreatesystemthread) to create a driver- or device-dedicated thread, and then call [**KeSetBasePriorityThread**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-kesetbaseprioritythread) to set the thread's base priority. The driver should specify a priority value that avoids *run-time priority inversions* in SMP machines. That is, setting the base priority of a driver-created thread too high can create delays in the execution of lower priority threads that submit I/O requests for that driver.

Because thread objects are themselves a type of dispatcher object, a thread can wait for another thread to complete. To obtain the thread object pointer associated with a thread, a driver can call [**ObReferenceObjectByHandle**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obreferenceobjectbyhandle), passing in the thread handle received from **PsCreateSystemThread**.

A thread can call [**KeDelayExecutionThread**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kedelayexecutionthread) to wait for an interval that could be a full time slice or longer. The granularity of a **KeDelayExecutionThread** interval is around 10 milliseconds. Because **KeDelayExecutionThread** is a timer-driven routine, the granularity of its interval is slightly faster or slower than 10 milliseconds, depending on the platform.
