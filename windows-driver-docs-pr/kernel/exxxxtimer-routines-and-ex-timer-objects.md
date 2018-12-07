---
title: ExXxxTimer Routines and EX_TIMER Objects
description: Starting with Windows 8.1, a comprehensive set of ExXxxTimer routines is available to manage timers.
ms.assetid: 5F2622F5-4D1A-48F4-9FF5-27DEC6109266
keywords: ["timers WDK kernel", "timer objects WDK kernel", "timer objects WDK kernel , about timer objects", "kernel dispatcher objects WDK , timer objects", "dispatcher objects WDK kernel , timer objects", "high-resolution timers WDK kernel", "no-wake timers WDK kernel", "EX_TIMER", "ExXxxTimer routines", "ExAllocateTimer", "ExDeleteTimer", "ExSetTimer", "ExCancelTimer", "ExTimerCallback"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# ExXxxTimer Routines and EX\_TIMER Objects


Starting with Windows 8.1, a comprehensive set of **Ex*Xxx*Timer** routines is available to manage timers. These routines use timer objects that are based on the [**EX\_TIMER**](https://msdn.microsoft.com/library/windows/hardware/dn265199) structure. The **Ex*Xxx*Timer** routines are replacements for the **Ke*Xxx*Timer** routines, which are available starting with Windows 2000. Drivers intended to run only on Windows 8.1 and later versions of Windows can use the **Ex*Xxx*Timer** routines instead of the **Ke*Xxx*Timer** routines. Windows 8.1 and later versions of Windows continue to support the **Ke*Xxx*Timer** routines.

The **Ex*Xxx*Timer** routines have all the important capabilities that are provided by the **Ke*Xxx*Timer** routines. In addition, the **Ex*Xxx*Timer** routines support two timer types, *high-resolution timers* and *no-wake timers*, that are not supported by the **Ke*Xxx*Timer** routines. High-resolution timers are timers whose expiration times can be specified with higher accuracy than those of timers whose accuracy is limited by the default resolution of the system clock. No-wake timers are timers that avoid unnecessarily waking processors from low-power states. For more information, see the following topics:

[High-Resolution Timers](high-resolution-timers.md)
[No-Wake Timers](no-wake-timers.md)
Starting with Windows 8.1, the following **Ex*Xxx*Timer** routines are available:

[**ExAllocateTimer**](https://msdn.microsoft.com/library/windows/hardware/dn265179)
[**ExSetTimer**](https://msdn.microsoft.com/library/windows/hardware/dn265188)
[**ExCancelTimer**](https://msdn.microsoft.com/library/windows/hardware/dn265180)
[**ExDeleteTimer**](https://msdn.microsoft.com/library/windows/hardware/dn265181)
The **ExSetTimer** routine can be used instead of the [**KeSetTimer**](https://msdn.microsoft.com/library/windows/hardware/ff553286) or [**KeSetTimerEx**](https://msdn.microsoft.com/library/windows/hardware/ff553292) routine. The **ExCancelTimer** routine can be used instead of the [**KeCancelTimer**](https://msdn.microsoft.com/library/windows/hardware/ff551970) routine.

The **ExAllocateTimer** and **ExDeleteTimer** routines have no direct **Ke*Xxx*Timer** counterparts. These two routines allocate and free a timer object. This timer object is a system-allocated [**EX\_TIMER**](https://msdn.microsoft.com/library/windows/hardware/dn265199) structure whose members are opaque to drivers. In contrast, the timer object used by the **Ke*Xxx*Timer** routines is a driver-allocated [**KTIMER**](https://msdn.microsoft.com/library/windows/hardware/ff554250) structure. The driver calls the [**KeInitializeTimer**](https://msdn.microsoft.com/library/windows/hardware/ff552168) or [**KeInitializeTimerEx**](https://msdn.microsoft.com/library/windows/hardware/ff552173) routine to initialize this object. **ExAllocateTimer** initializes the timer objects that it allocates. For more information about **ExDeleteTimer**, see [Deleting a System-Allocated Timer Object](deleting-a-system-allocated-timer-object.md).

**EX\_TIMER** and **KTIMER** structures are waitable objects. After a driver calls **ExSetTimer**, **KeSetTimer**, or **KeSetTimerEx** to set a timer, the driver can call a routine such as [**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350) or [**KeWaitForMultipleObjects**](https://msdn.microsoft.com/library/windows/hardware/ff553324) to wait for the timer to expire. The timer object is signaled when the timer expires. As an option, a driver can supply a pointer to a driver-implemented [*ExTimerCallback*](https://msdn.microsoft.com/library/windows/hardware/dn265190) or [*CustomTimerDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542983) callback routine that the operating system calls after the timer expires.

The **Ke*Xxx*Timer** routines have two capabilities that are not provided by the **Ex*Xxx*Timer** routines, but these capabilities are not needed by most drivers.

First, the **KTIMER** structure used as a timer object by the **Ke*Xxx*Timer** routines is driver-allocated. The driver can preallocate this object to ensure that the object is available even in circumstances in which resources are constrained and memory allocations can fail. In contrast, a call to **ExAllocateTimer** to allocate a timer object might fail in a resource-constrained environment. However, few drivers need to be designed to operate in environments in which memory allocations fail, and most drivers benefit from the convenience of an **ExAllocateTimer** routine that both allocates and initializes a timer object.

Second, there is no **Ex*Xxx*Timer** equivalent of the [**KeReadStateTimer**](https://msdn.microsoft.com/library/windows/hardware/ff553099) routine, which indicates whether a timer object is in the signaled state. However, this routine is rarely used. If necessary, a driver that uses the **Ex*Xxx*Timer** routines can check whether a timer object is in the signaled state by reading a Boolean value that is set by the *ExTimerCallback* callback routine that the driver supplies to the **ExAllocateTimer** routine.

 

 




