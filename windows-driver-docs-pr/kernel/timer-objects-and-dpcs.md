---
title: KeXxxTimer Routines, KTIMER Objects, and DPCs
description: Starting with Windows 2000, a set of KeXxxTimer routines is available to manage timers.
ms.assetid: b58487de-6e9e-45f4-acb8-9233c8718ee2
keywords: ["timers WDK kernel", "timer objects WDK kernel", "timer objects WDK kernel , about timer objects", "deferred procedure calls WDK kernel", "DPCs WDK kernel", "kernel dispatcher objects WDK , timer objects", "dispatcher objects WDK kernel , timer objects", "notification timers WDK kernel", "synchronization timers WDK kernel", "KTIMER", "KeXxxTimer routines", "KeInitializeTimer", "KeInitializeTimerEx", "KeSetTimer", "KeSetTimerEx", "CustomTimerDpc", "timeout intervals WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# KeXxxTimer Routines, KTIMER Objects, and DPCs


Starting with Windows 2000, a set of **Ke*Xxx*Timer** routines is available to manage timers. These routines use timer objects that are based on the [**KTIMER**](https://msdn.microsoft.com/library/windows/hardware/ff554250) structure. To create a timer object, a driver first allocates storage for a **KTIMER** structure. Then the driver calls a routine such as [**KeInitializeTimer**](https://msdn.microsoft.com/library/windows/hardware/ff552168) or [**KeInitializeTimerEx**](https://msdn.microsoft.com/library/windows/hardware/ff552173) to initialize this structure.




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
 

 




