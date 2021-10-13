---
title: ExXxxTimer Routines and EX_TIMER Objects
description: Starting with Windows 8.1, a comprehensive set of ExXxxTimer routines is available to manage timers.
keywords: ["timers WDK kernel", "timer objects WDK kernel", "timer objects WDK kernel , about timer objects", "kernel dispatcher objects WDK , timer objects", "dispatcher objects WDK kernel , timer objects", "high-resolution timers WDK kernel", "no-wake timers WDK kernel", "EX_TIMER", "ExXxxTimer routines", "ExAllocateTimer", "ExDeleteTimer", "ExSetTimer", "ExCancelTimer", "ExTimerCallback"]
ms.date: 07/21/2021
ms.localizationpriority: medium
---

# ExXxxTimer Routines and EX_TIMER Objects

Starting with Windows 8.1, a comprehensive set of **Ex*Xxx*Timer** routines is available to manage timers. These routines use timer objects that are based on the [**EX_TIMER**](./eprocess.md) structure. The **Ex*Xxx*Timer** routines are replacements for the **Ke*Xxx*Timer** routines, which are available starting with Windows 2000. Drivers intended to run only on Windows 8.1 and later versions of Windows can use the **Ex*Xxx*Timer** routines instead of the **Ke*Xxx*Timer** routines. Windows 8.1 and later versions of Windows continue to support the **Ke*Xxx*Timer** routines.

The **Ex*Xxx*Timer** routines have all the important capabilities that are provided by the **Ke*Xxx*Timer** routines. In addition, the **Ex*Xxx*Timer** routines support two timer types, *high-resolution timers* and *no-wake timers*, that are not supported by the **Ke*Xxx*Timer** routines. High-resolution timers are timers whose expiration times can be specified with higher accuracy than those of timers whose accuracy is limited by the default resolution of the system clock. No-wake timers are timers that avoid unnecessarily waking processors from low-power states. For more information, see the following topics:

[High-Resolution Timers](high-resolution-timers.md)

[No-Wake Timers](no-wake-timers.md)

Starting with Windows 8.1, the following **Ex*Xxx*Timer** routines are available:

[**ExAllocateTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatetimer)

[**ExSetTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exsettimer)

[**ExCancelTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-excanceltimer)

[**ExDeleteTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exdeletetimer)

The **ExSetTimer** routine can be used instead of the [**KeSetTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesettimer) or [**KeSetTimerEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesettimerex) routine. The **ExCancelTimer** routine can be used instead of the [**KeCancelTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kecanceltimer) routine.

The **ExAllocateTimer** and **ExDeleteTimer** routines have no direct **Ke*Xxx*Timer** counterparts. These two routines allocate and free a timer object. This timer object is a system-allocated [**EX_TIMER**](./eprocess.md) structure whose members are opaque to drivers. In contrast, the timer object used by the **Ke*Xxx*Timer** routines is a driver-allocated [**KTIMER**](./eprocess.md) structure. The driver calls the [**KeInitializeTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializetimer) or [**KeInitializeTimerEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializetimerex) routine to initialize this object. **ExAllocateTimer** initializes the timer objects that it allocates. For more information about **ExDeleteTimer**, see [Deleting a System-Allocated Timer Object](deleting-a-system-allocated-timer-object.md).

**EX_TIMER** and **KTIMER** structures are waitable objects. After a driver calls **ExSetTimer**, **KeSetTimer**, or **KeSetTimerEx** to set a timer, the driver can call a routine such as [**KeWaitForSingleObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kewaitforsingleobject) or [**KeWaitForMultipleObjects**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kewaitformultipleobjects) to wait for the timer to expire. The timer object is signaled when the timer expires. As an option, a driver can supply a pointer to a driver-implemented [*ExTimerCallback*](/windows-hardware/drivers/ddi/wdm/nc-wdm-ext_callback) or [*CustomTimerDpc*](using-a-customtimerdpc-routine.md) callback routine that the operating system calls after the timer expires.

The **Ke*Xxx*Timer** routines have two capabilities that are not provided by the **Ex*Xxx*Timer** routines, but these capabilities are not needed by most drivers.

First, the **KTIMER** structure used as a timer object by the **Ke*Xxx*Timer** routines is driver-allocated. The driver can preallocate this object to ensure that the object is available even in circumstances in which resources are constrained and memory allocations can fail. In contrast, a call to **ExAllocateTimer** to allocate a timer object might fail in a resource-constrained environment. However, few drivers need to be designed to operate in environments in which memory allocations fail, and most drivers benefit from the convenience of an **ExAllocateTimer** routine that both allocates and initializes a timer object.

Second, there is no **Ex*Xxx*Timer** equivalent of the [**KeReadStateTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereadstatetimer) routine, which indicates whether a timer object is in the signaled state. However, this routine is rarely used. If necessary, a driver that uses the **Ex*Xxx*Timer** routines can check whether a timer object is in the signaled state by reading a Boolean value that is set by the *ExTimerCallback* callback routine that the driver supplies to the **ExAllocateTimer** routine.
