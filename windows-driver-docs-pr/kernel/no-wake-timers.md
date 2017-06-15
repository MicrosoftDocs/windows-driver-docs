---
title: No-Wake Timers
author: windows-driver-content
description: Starting with Windows 8.1, drivers can use no-wake timers to avoid unnecessarily waking a processor from a low-power state.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 04CD107B-F196-4FF8-A423-C43CAA9A7EBD
keywords: ["No-wake timers", "ExXxxTimer routines", "EX_TIMER_NO_WAKE", "EX_TIMER_UNLIMITED_TOLERANCE", "coalescable timers", "timer coalescing", "KeSetCoalescableTimer"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20No-Wake%20Timers%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


