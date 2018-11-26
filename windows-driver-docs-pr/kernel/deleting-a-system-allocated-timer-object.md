---
title: Deleting a System-Allocated Timer Object
description: Starting with Windows 8.1, the ExDeleteTimer routine deletes a timer object that was created by the ExAllocateTimer routine.
ms.assetid: 7D119448-3890-4E8F-BC79-7FEB3213B693
keywords: ["ExXxxTimer routines", "ExAllocateTimer", "ExDeleteTimer", "ExSetTimer", "ExCancelTimer", "ExTimerCallback", "ExTimerDeleteCallback", "EX_TIMER"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Deleting a System-Allocated Timer Object


Starting with Windows 8.1, the [**ExDeleteTimer**](https://msdn.microsoft.com/library/windows/hardware/dn265181) routine deletes a timer object that was created by the [**ExAllocateTimer**](https://msdn.microsoft.com/library/windows/hardware/dn265179) routine. This timer object is a system-allocated [**EX\_TIMER**](https://msdn.microsoft.com/library/windows/hardware/dn265199) structure whose members are opaque to drivers. Before a timer object is deleted, **ExDeleteTimer** disables further timer operations on the object, and cancels or completes any pending operation on the object that might be in progress.

After a driver calls **ExDeleteTimer**, this routine takes several steps to ensure that it can safely delete the timer object. First, **ExDeleteTimer** marks the timer object as disabled to prevent the driver from starting a new timer operation that uses the object. After the timer object is disabled, a call to the [**ExSetTimer**](https://msdn.microsoft.com/library/windows/hardware/dn265188) or [**ExCancelTimer**](https://msdn.microsoft.com/library/windows/hardware/dn265180) routine immediately returns **FALSE** and performs no operation. Also, a second call to **ExDeleteTimer** returns **FALSE** and performs no operation.

Next, **ExDeleteTimer** checks whether a timer is still pending from a previous call to **ExDeleteTimer**. Disabling a timer object does not cancel a timer that was set before the object was disabled. In either of the following two cases, a timer that was previously set might expire after the timer object is disabled:

-   The timer is periodic.
-   The timer is one-shot (or nonperiodic) and has not yet expired.

A periodic timer can never expire more than once after the timer object is disabled.

If your driver implements an [*ExTimerCallback*](https://msdn.microsoft.com/library/windows/hardware/dn265190) callback routine, the *Timer* parameter to this routine is guaranteed to always be a valid pointer to the timer object (an **EX\_TIMER** structure), even if the timer expires after the timer object is disabled.

If no timer is pending, **ExDeleteTimer** deletes the timer object and returns without waiting.

If a timer is pending when **ExDeleteTimer** is called, the *Cancel* and *Wait* parameter values that your driver supplies to this routine control the routine's behavior. The *Cancel* parameter tells **ExDeleteTimer** whether to try to cancel a pending timer. The *Wait* parameter tells **ExDeleteTimer** whether to wait to return until the timer object is deleted.

If *Cancel* is **FALSE** (in which case, *Wait* must be **FALSE**) and a timer is pending, **ExDeleteTimer** lets the timer expire before the timer object is deleted. In this case, **ExDeleteTimer** marks the timer object to indicate that it is to be deleted after the pending timer expires (and any last callback to the *ExTimerCallback* routine finishes). Then **ExDeleteTimer** returns without waiting either for the timer to finish expiring or for the object to be deleted.

If *Cancel* is **TRUE**, **ExDeleteTimer** tries to cancel a pending timer before it expires. **ExDeleteTimer** returns **TRUE** if it successfully cancels the timer. **ExDeleteTimer** returns **FALSE** if it cannot cancel the timer, which is the case for a one-shot timer that has already expired or is in the process of expiring. **ExDeleteTimer** also returns **FALSE** if the (one-shot or periodic) timer was canceled before the **ExDeleteTimer** call or if the timer was never set.

If *Cancel* is **TRUE** and *Wait* is **FALSE**, **ExDeleteTimer** never blocks the calling thread. If the timer object cannot be immediately deleted, **ExDeleteTimer** marks the timer object to indicate that it is to be deleted after the pending timer finishes expiring, and returns immediately without waiting either for the timer to expire or for the object to be deleted.

If *Cancel* and *Wait* are both **TRUE**, **ExDeleteTimer** blocks the calling thread if the timer object cannot be immediately deleted. **ExDeleteTimer** waits, if necessary, for the timer to finish expiring and for any callback to a driver-implemented *ExTimerCallback* routine to finish. Next, **ExDeleteTimer** deletes the timer object and calls the [*ExTimerDeleteCallback*](https://msdn.microsoft.com/library/windows/hardware/dn265192) routine, if the driver implements this routine. Finally, **ExDeleteTimer** returns.

A driver can call **ExDeleteTimer** from the driver's *ExTimerCallback* routine, which runs at IRQL = DISPATCH\_LEVEL, but the driver must set the *Wait* parameter in this call to **FALSE**.

As an option, a driver can implement an *ExTimerDeleteCallback* callback routine that runs after a timer object is deleted. Typically, an *ExTimerDeleteCallback* routine frees any system resources that the driver allocated to use with the timer object.

**ExDeleteTimer** schedules a driver-implemented *ExTimerDeleteCallback* routine to run after the timer object is deleted, at which time the pointer to this object is no longer valid. If the *Wait* parameter is **TRUE** in the **ExDeleteTimer** call, the callback to the *ExTimerDeleteCallback* routine finishes before **ExDeleteTimer** returns. If *Wait* is **FALSE**, the *ExTimerDeleteCallback* routine might run before or after **ExDeleteTimer** returns.

For more information, see [Ex*Xxx*Timer Routines and EX\_TIMER Objects](exxxxtimer-routines-and-ex-timer-objects.md).

 

 




