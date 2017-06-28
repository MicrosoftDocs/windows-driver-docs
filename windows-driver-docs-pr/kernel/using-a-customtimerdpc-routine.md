---
title: Using a CustomTimerDpc Routine
author: windows-driver-content
description: Using a CustomTimerDpc Routine
ms.assetid: e95d01a2-4d13-40d2-aeb0-44c45e4a49f5
keywords: ["timer objects WDK kernel , CustomTimerDpc routines", "CustomTimerDpc", "disabling timer objects", "timer objects WDK kernel , disabling", "periodic timers WDK kernel", "queuing timer objects", "timer objects WDK kernel , expirations", "timer expirations WDK kernel", "expired timers WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using a CustomTimerDpc Routine


## <a href="" id="ddk-using-a-customtimerdpc-routine-kg"></a>


To disable a previously set timer object, a driver calls [**KeCancelTimer**](https://msdn.microsoft.com/library/windows/hardware/ff551970). This routine removes the timer object from the system's timer queue. Generally, the timer object is not set to the signaled state and the *CustomTimerDpc* routine is not queued for execution. However, if the timer is about to expire when **KeCancelTimer** is called, expiration might occur before **KeCancelTimer** has a chance to access the time queue, in which case signaling and DPC queuing will occur.

Recalling [**KeSetTimer**](https://msdn.microsoft.com/library/windows/hardware/ff553286) or [**KeSetTimerEx**](https://msdn.microsoft.com/library/windows/hardware/ff553292), with previously specified *Timer* and *Dpc* pointers, before the previously specified interval expires, has the following effects:

-   The kernel removes the timer object from the timer queue, without setting the object to the signaled state or queuing the *CustomTimerDpc* routine.

-   The kernel reinserts the timer object in the timer queue, using the new *DueTime* value.

Using the same timer object for different purposes can cause race conditions or serious driver errors. For example, assume that a driver specifies a single timer object both to set up a call to a *CustomTimerDpc* routine and to set up waits in a driver-dedicated thread. Whenever the driver-dedicated thread calls **KeSetTimer**, **KeSetTimerEx**, or **KeCancelTimer** for the common timer object, the thread would cancel calls to the *CustomTimerDpc* routine, if the timer object was already queued for a *CustomTimerDpc* call.

If a driver has *CustomTimerDpc* routines, and also waits on timer objects in a nonarbitrary thread context, it should:

-   Never use a thread-context-sensitive timer object in a nonarbitrary thread context, or vice versa.

-   Allocate a separate timer object for each *CustomTimerDpc* routine. Each set of driver threads or driver routines that are called in a nonarbitrary thread context should have its own set of "waitable" timer objects.

If you use a *CustomTimerDpc* routine, choose carefully the interval the driver passes in calls to **KeSetTimer** or **KeSetTimerEx**. In addition, consider all possible effects of a call to **KeCancelTimer** with the same timer object from any driver routine that makes this call, particularly on SMP platforms.

Keep in mind the following fact about *CustomTimerDpc* routines:

Only one instantiation of a DPC object representing a particular DPC routine can be queued for execution at any given moment.

If a second driver routine calls **KeSetTimer** or **KeSetTimerEx** to run the same *CustomTimerDpc* routine before the interval specified by the first caller expires, the *CustomTimerDpc* routine is run only after the interval specified by the second caller expires. In these circumstances, the *CustomTimerDpc* does none of the work for which the first routine called **KeSetTimer** or **KeSetTimerEx**.

For drivers that have *CustomTimerDpc* routines and use periodic timers:

A driver cannot deallocate a periodic timer from a DPC routine. Drivers can deallocate only nonperiodic timers from a DPC routine.

Consider the following a design guideline for drivers that have both *CustomDpc* and *CustomTimerDpc* routines:

To prevent race conditions, never pass the same *Dpc* pointer to **KeSetTimer** or **KeSetTimerEx** and [**KeInsertQueueDpc**](https://msdn.microsoft.com/library/windows/hardware/ff552185).

In other words, suppose a driver's *StartIo* routine calls **KeSetTimer** or **KeSetTimerEx** to queue a *CustomTimerDpc* routine, and the driver's ISR calls **KeInsertQueueDpc** simultaneously from another processor with the same *Dpc* pointer. That DPC routine will be run when IRQL on a processor falls below DISPATCH\_LEVEL or the timer interval expires, whichever comes first. Whichever does come first, some essential work for the *StartIo* or ISR would simply be dropped by the DPC routine.

In addition, a DPC used by two standard driver routines with very different functionality would have poorer performance characteristics than separate *CustomTimerDpc* and *CustomDpc* routines. The DPC would have to determine which operations to carry out, depending on the conditions that caused the *StartIo* routine or ISR to queue it. Testing for these conditions in the DPC would use additional CPU cycles.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20a%20CustomTimerDpc%20Routine%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


