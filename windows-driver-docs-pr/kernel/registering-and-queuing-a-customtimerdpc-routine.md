---
title: Registering and Queuing a CustomTimerDpc Routine
author: windows-driver-content
description: Registering and Queuing a CustomTimerDpc Routine
ms.assetid: 884bff8e-8437-44fb-acc0-f535d64ce900
keywords: ["timer objects WDK kernel , CustomTimerDpc routines", "CustomTimerDpc", "queuing timer objects", "registering timer objects", "KeSetTimer", "KeSetTimerEx", "KeInitializeTimer", "KeInitializeTimerEx", "invoking CustomTimerDpc routine repeatedly", "repeatedly invoke CustomTimerDpc routine", "DueTime values", "timer expirations WDK kernel", "expired timers WDK kernel", "timer objects WDK kernel , queuing", "timer objects WDK kernel , registering", "timer objects WDK kernel , expirations"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Registering and Queuing a CustomTimerDpc Routine


## <a href="" id="ddk-registering-and-queuing-a-customtimerdpc-routine-kg"></a>


A driver can register a [*CustomTimerDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542983) routine by calling the following routines, usually from its [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine:

1.  [**KeInitializeDpc**](https://msdn.microsoft.com/library/windows/hardware/ff552130) to register its routine

2.  [**KeInitializeTimer**](https://msdn.microsoft.com/library/windows/hardware/ff552168) or [**KeInitializeTimerEx**](https://msdn.microsoft.com/library/windows/hardware/ff552173) to set up a timer object

Subsequently, the driver can call [**KeSetTimer**](https://msdn.microsoft.com/library/windows/hardware/ff553286) or [**KeSetTimerEx**](https://msdn.microsoft.com/library/windows/hardware/ff553292) to specify an expiration time and to add the timer object to the system's timer queue. When the expiration time is reached, the system dequeues the timer object and calls the *CustomTimerDpc* routine. The following figure illustrates these calls.

![diagram illustrating using timer and dpc objects for a customtimerdpc routine](images/3ketmdpc.png)

As the previous figure shows, the driver must supply storage for both a DPC object and a timer object. Most drivers provide the storage for these objects in a [device extension](device-extensions.md) or in other driver-allocated, resident memory.

In the call to **KeSetTimer**, the driver passes pointers to the *Dpc* and *Timer* objects, along with a *DueTime* expressed in units of 100 nanoseconds, as shown in the previous figure. A positive value for *DueTime* specifies an *absolute expiration time* (since January 1, 1601) at which the *CustomTimerDpc* routine should be called. A negative value for *DueTime* specifies a *relative expiration time*.

Because an absolute timer expires at a specific system time, the wait duration of an absolute timer is not affected if the system time changes before the timer expires. On the other hand, a relative timer always expires after the specified number of time units elapses, regardless of changes to the absolute system time.

To invoke a *CustomTimerDpc* routine repeatedly, use **KeSetTimerEx** to set the timer and specify a recurring interval in the *Period* parameter. **KeSetTimerEx** is just like **KeSetTimer** except for this additional parameter.

As shown in the previous figure, the call to **KeSetTimer** or **KeSetTimerEx** queues the timer object for a specified interval as follows:

1.  When the *DueTime* expires, the timer object is dequeued and set to the Signaled state.

2.  If every processor in the machine is currently running code at an IRQL greater than or equal to DISPATCH\_LEVEL, the DPC object associated with the timer object is put in a DPC queue. Otherwise, the *CustomTimerDpc* routine is called.

3.  If the DPC object was already in the queue when the *DueTime* interval expired, the *CustomTimerDpc* routine is called as soon as the IRQL on any processor in the machine falls below DISPATCH\_LEVEL.

    **Note**  The *CustomTimerDpc* routine, like all DPC routines, is called at IRQL = DISPATCH\_LEVEL. While a DPC routine runs, all threads are prevented from running on the same processor. Driver developers should carefully design their *CustomTimerDpc* routines to run for as brief a time as possible.

     

The smallest time interval that can be specified to **KeSetTimer** and **KeSetTimerEx** is approximately ten milliseconds, so a driver can use a *CustomTimerDpc* routine when timing smaller intervals than an [*IoTimer*](https://msdn.microsoft.com/library/windows/hardware/ff550381) routine, which is run once per second, can handle.

Only one instantiation of a particular timer object can be queued at any moment. Calling **KeSetTimer** or **KeSetTimerEx** again with the same *Timer* object pointer cancels the queued timer object and resets it.

Setting up a [*CustomTimerDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542983) routine is exactly like setting up a [*CustomDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542972) routine, with an additional step to initialize the timer object. In fact, their prototypes are identical, but *CustomTimerDpc* routine cannot use the two *SystemArgument* pointers declared in its prototype.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Registering%20and%20Queuing%20a%20CustomTimerDpc%20Routine%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


