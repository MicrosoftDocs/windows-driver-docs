---
title: No-Wake Timers
description: Starting with Windows 8.1, drivers can use no-wake timers to avoid unnecessarily waking a processor from a low-power state.
ms.assetid: 04CD107B-F196-4FF8-A423-C43CAA9A7EBD
keywords: ["No-wake timers", "ExXxxTimer routines", "EX_TIMER_NO_WAKE", "EX_TIMER_UNLIMITED_TOLERANCE", "coalescable timers", "timer coalescing", "KeSetCoalescableTimer"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# No-Wake Timers


Starting with Windows 8.1, drivers can use no-wake timers to avoid unnecessarily waking a processor from a low-power state. By keeping the processor in a low-power state, a no-wake timer reduces power consumption and extends the time that a tablet or other mobile computer can run on a battery charge.

A timer can expire only when the processor is in an active, running state. If a timer reaches its expiration time when the processor is in a low-power state, and the timer needs to expire immediately, the timer must wake the processor. However, when a no-wake timer reaches its expiration time and the processor is in a low-power state, this timer waits to expire until the processor wakes for some reason other than the timer. As an option, a driver can specify a maximum delay tolerance for a no-wake timer so that if the processor does not wake (for some other reason) within the maximum delay tolerance after the timer's expiration time, the timer wakes the processor.

A driver can use a no-wake timer to initiate noncritical operations that need to be performed only when the processor is in an active state. For example, a driver might use a no-wake timer to periodically flush accumulated status information from a memory buffer to a file. This status information describes processing work that the driver performs only when the processor is active. When the processor is in a low-power state, no status information is generated, and there is no need to wake the processor.

To create a no-wake timer, a WDM driver calls the [**ExAllocateTimer**](https://msdn.microsoft.com/library/windows/hardware/dn265179) routine. In this call, the driver sets the EX\_TIMER\_NO\_WAKE flag bit in the *Attributes* parameter.

To set a no-wake timer to expire at some due time, the driver calls the [**ExSetTimer**](https://msdn.microsoft.com/library/windows/hardware/dn265188) routine. In this call, the driver can specify how long the no-wake timer should wait after it reaches its expiration time before the timer wakes the processor. The driver writes this tolerable-delay time to the **NoWakeTolerance** member in the [**EXT\_SET\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn265196) structure that the driver passes as an input parameter to the **ExSetTimer** routine. If the driver sets the **NoWakeTolerance** member to the special value EX\_TIMER\_UNLIMITED\_TOLERANCE, the timer never wakes the processor and, thus, cannot expire until the processor wakes for some other reason.

A Kernel-Mode Driver Framework (KMDF) driver or User-Mode Driver Framework (UMDF) driver can call the [**WdfTimerCreate**](https://msdn.microsoft.com/library/windows/hardware/ff550050) method to create a no-wake timer. In this call, the driver passes a pointer to a [**WDF\_TIMER\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552519) structure as a parameter. To create a no-wake timer that never wakes the processor, the driver sets the **TolerableDelay** member of this structure to the **TolerableDelayUnlimited** constant. This constant is supported starting with Windows 8.1 and KMDF version 1.13 or UMDF 2.0.

## Comparison to coalescable timers


The [**KeSetCoalescableTimer**](https://msdn.microsoft.com/library/windows/hardware/ff553249) routine was introduced in Windows 7. This routine enables a driver to specify how much tolerance to allow in the expiration time of a timer. Frequently, the operating system can use this information to coalesce two or more timer interrupts into a single interrupt. If the expiration times of multiple timers are close enough to each other that their tolerance windows overlap, a single timer interrupt in the region of overlap can satisfy the timing requirements of all of these timers.

The chief benefit of timer coalescing is that it extends the time that the processor can stay in a low-power state between timer expirations. Thus, drivers use timer coalescing and no-wake timers for similar purposes.

However, coalesceable timers behave differently from no-wake timers. In particular, the tolerable delay specified for a no-wake timer applies only when the processor is in a low-power state, whereas the tolerance specified for the expiration of a coalescable timer applies regardless of whether the processor is in a low-power state. For a coalescable timer, a driver can increase the amount of tolerance in the expiration time to reduce the likelihood that the timer wakes the processor, but increasing the tolerance has the side effect of decreasing the accuracy of the timer when the processor is active. In contrast, the tolerable delay specified for a no-wake timer does not affect the accuracy of the timer when the processor is active. For many drivers, no-wake timers might be a better way to reduce power consumption.

 

 




