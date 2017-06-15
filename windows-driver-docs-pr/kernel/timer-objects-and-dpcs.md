---
title: KeXxxTimer Routines, KTIMER Objects, and DPCs
author: windows-driver-content
description: Starting with Windows 2000, a set of KeXxxTimer routines is available to manage timers.
MS-HAID:
- 'Synchro\_0965b486-7df0-4616-8a12-54329b6a15be.xml'
- 'kernel.timer\_objects\_and\_dpcs'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b58487de-6e9e-45f4-acb8-9233c8718ee2
keywords: ["timers WDK kernel", "timer objects WDK kernel", "timer objects WDK kernel , about timer objects", "deferred procedure calls WDK kernel", "DPCs WDK kernel", "kernel dispatcher objects WDK , timer objects", "dispatcher objects WDK kernel , timer objects", "notification timers WDK kernel", "synchronization timers WDK kernel", "KTIMER", "KeXxxTimer routines", "KeInitializeTimer", "KeInitializeTimerEx", "KeSetTimer", "KeSetTimerEx", "CustomTimerDpc", "timeout intervals WDK kernel"]
---

# KeXxxTimer Routines, KTIMER Objects, and DPCs


Starting with Windows 2000, a set of **Ke*Xxx*Timer** routines is available to manage timers. These routines use timer objects that are based on the [**KTIMER**](https://msdn.microsoft.com/library/windows/hardware/ff554250) structure. To create a timer object, a driver first allocates storage for a **KTIMER** structure. Then the driver calls a routine such as [**KeInitializeTimer**](https://msdn.microsoft.com/library/windows/hardware/ff552168) or [**KeInitializeTimerEx**](https://msdn.microsoft.com/library/windows/hardware/ff552173) to initialize this structure.

## <a href="" id="ddk-timer-objects-and-dpcs-kg"></a>


A timer can be set to expire just once, or to expire repeatedly after a given interval. [**KeSetTimer**](https://msdn.microsoft.com/library/windows/hardware/ff553286) always sets a timer that will expire just once. [**KeSetTimerEx**](https://msdn.microsoft.com/library/windows/hardware/ff553292) accepts an optional *Period* parameter, which specifies a recurring timer interval.

An optional [*CustomTimerDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542983) routine (a type of deferred procedure call) can be associated with either a notification timer or a synchronization timer. This routine executes when the specified time interval expires. For more information, see [Using Timer Objects](using-timer-objects.md).

A timer can be a *notification timer* or a *synchronization timer*.

-   When a notification timer is signaled, all waiting threads have their wait satisfied. The state of the timer remains signaled until it is explicitly reset.

-   When a synchronization timer expires, its state is set to Signaled until a single waiting thread is released. Then the timer is reset to the Not-Signaled state.

**KeInitializeTimer** always creates notification timers. **KeInitializeTimerEx** accepts a *Type* parameter, which can be **NotificationTimer** or **SynchronizationTimer**.

The following topics provide more information about timer objects and DPCs:

[Using Timer Objects](using-timer-objects.md)
[Timer Accuracy](timer-accuracy.md)
[Registering and Queuing a CustomTimerDpc Routine](registering-and-queuing-a-customtimerdpc-routine.md)
[Providing CustomTimerDpc Context Information](providing-customtimerdpc-context-information.md)
[Using a CustomTimerDpc Routine](using-a-customtimerdpc-routine.md)
 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20KeXxxTimer%20Routines,%20KTIMER%20Objects,%20and%20DPCs%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


