---
title: Timer Accuracy
author: windows-driver-content
description: A system timer routine typically enables the caller to specify either an absolute or a relative expiration time for a timer.
ms.assetid: CA29DC02-1AEA-4A13-B2D6-8C8052E21EDB
---

# Timer Accuracy


A system timer routine typically enables the caller to specify either an absolute or a relative expiration time for a timer. For example, see [**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350), [**KeSetTimer**](https://msdn.microsoft.com/library/windows/hardware/ff553286), or [**KeDelayExecutionThread**](https://msdn.microsoft.com/library/windows/hardware/ff551986). The accuracy with which the operating system can measure expiration times is limited by the granularity of the system clock.

The system time is updated on every tick of the system clock, and is accurate only to the latest tick. If the caller specifies an absolute expiration time, the expiration of the timer is detected during processing of the first system clock tick that occurs after the specified time. Thus, the timer can expire as much as one system clock period later than the specified absolute expiration time. If a timer interval, or relative expiration time, is instead specified, the expiration can occur up to a period earlier than or a period later than the specified time, depending on where exactly the start and end times of this interval fall between system clock ticks. Regardless of whether an absolute or a relative time is specified, the timer expiration might not be detected until even later if interrupt processing for the system clock is delayed by interrupt processing for other devices.

When the caller specifies a relative expiration time, the timer routine adds the current system clock time to the specified relative expiration time to calculate the absolute expiration time to use for the timer. Because the system time is accurate only to the latest tick of the system clock, the calculated expiration time can be up to a system clock period earlier than the expiration time expected by the caller. If a specified relative expiration time is close to or smaller than the system clock period, the timer might expire immediately, with no delay.

A possible way to more accurately support shorter expiration times is to decrease the time between system clock ticks, but doing so is likely to increase power consumption. In addition, reducing the system clock period might not reliably achieve a finer system clock granularity unless interrupt processing for the other devices in the platform can be guaranteed not to delay the processing of system clock interrupts.

Starting with Windows 8, [**KeDelayExecutionThread**](https://msdn.microsoft.com/library/windows/hardware/ff551986) uses a more precise technique to calculate the absolute expiration time from a caller-specified relative expiration time. First, to obtain a more precise estimate of the current system time, the routine uses the system performance counter to measure the time elapsed since the last system clock tick. Next, the routine adds this more precise estimate of the system time to the relative expiration time to calculate the absolute expiration time. The absolute expiration time calculated by this technique is accurate to within a microsecond. As a result, the timer will not expire before the specified relative expiration time elapses. The timer can still expire up to a system clock period later than the specified time, and might expire even later if processing of the system clock interrupt is delayed by interrupt processing for other devices.

If the system time changes before a timer expires, a relative timer is not affected but the system adjusts each absolute timer. A relative timer always expires after the specified number of time units elapse, regardless of the absolute system time. An absolute timer expires at a specific system time, so a change in the system time changes the wait duration of an absolute timer.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Timer%20Accuracy%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


