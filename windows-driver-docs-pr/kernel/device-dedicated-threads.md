---
title: Device-Dedicated Threads
author: windows-driver-content
description: Device-Dedicated Threads
MS-HAID:
- 'Synchro\_90b913c3-e635-4250-8378-79531f91879c.xml'
- 'kernel.device\_dedicated\_threads'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2e11e2c9-aefd-4b7b-8d80-7eb1da9f7cce
keywords: ["thread objects WDK kernel", "device-dedicated threads WDK kernel", "run-time priority inversions WDK kernel", "PsCreateSystemThread", "KeSetBasePriorityThread"]
---

# Device-Dedicated Threads


## <a href="" id="ddk-device-dedicated-threads-kg"></a>


The driver of a slow device or a device that is seldom used (like the floppy controller) can solve many "waiting" problems by creating a device-dedicated system thread. Additionally, most file system drivers use system worker threads and supply worker-thread callback routines.

If a device driver has its own thread context or is running in a system-thread context, the device-dedicated thread or highest-level driver's worker-thread callback routine can synchronize operations on a dispatcher object, such as an [event object](event-objects.md) or [semaphore object](semaphore-objects.md), in a shared communication region of the driver's device extension. For example, a device-dedicated thread can wait for a shared dispatcher object, while the thread's device is not in use, by calling [**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350) for a semaphore. Until the device driver is called to carry out an I/O operation (at which point it sets the semaphore to the Signaled state), its waiting thread uses no CPU time.

A driver can call [**PsCreateSystemThread**](https://msdn.microsoft.com/library/windows/hardware/ff559932) to create a driver- or device-dedicated thread, and then call [**KeSetBasePriorityThread**](https://msdn.microsoft.com/library/windows/hardware/ff553246) to set the thread's base priority. The driver should specify a priority value that avoids *run-time priority inversions* in SMP machines. That is, setting the base priority of a driver-created thread too high can create delays in the execution of lower priority threads that submit I/O requests for that driver.

Because thread objects are themselves a type of dispatcher object, a thread can wait for another thread to complete. To obtain the thread object pointer associated with a thread, a driver can call [**ObReferenceObjectByHandle**](https://msdn.microsoft.com/library/windows/hardware/ff558679), passing in the thread handle received from **PsCreateSystemThread**.

A thread can call [**KeDelayExecutionThread**](https://msdn.microsoft.com/library/windows/hardware/ff551986) to wait for an interval that could be a full time slice or longer. The granularity of a **KeDelayExecutionThread** interval is around 10 milliseconds. Because **KeDelayExecutionThread** is a timer-driven routine, the granularity of its interval is slightly faster or slower than 10 milliseconds, depending on the platform.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Device-Dedicated%20Threads%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


