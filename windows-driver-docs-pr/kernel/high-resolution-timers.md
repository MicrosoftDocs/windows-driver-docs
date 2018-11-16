---
title: High-Resolution Timers
description: Starting with Windows 8.1, drivers can use the ExXxxTimer routines to manage high-resolution timers.
ms.assetid: B8F2B28C-A02B-4015-B392-3D30BC0229B8
keywords: ["high-resolution timers", "timer accuracy", "timer resolution", "system clock granularity", "EX_TIMER_HIGH_RESOLUTION", "ExXxxTimer routines", "ExQueryTimerResolution", "ExSetTimerResolution"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# High-Resolution Timers


Starting with Windows 8.1, drivers can use the [**Ex*Xxx*Timer**](exxxxtimer-routines-and-ex-timer-objects.md) routines to manage high-resolution timers. The accuracy of a high-resolution timer is limited only by the maximum supported resolution of the system clock. In contrast, timers that are limited to the default system clock resolution are significantly less accurate.

However, high-resolution timers require system clock interrupts to—at least, temporarily—occur at a higher rate, which tends to increase power consumption. Thus, drivers should use high-resolution timers only when timer accuracy is essential, and use default-resolution timers in all other cases.

To create a high-resolution timer, a WDM driver calls the [**ExAllocateTimer**](https://msdn.microsoft.com/library/windows/hardware/dn265179) routine and sets the EX\_TIMER\_HIGH\_RESOLUTION flag in the *Attributes* parameter. When the driver calls the [**ExSetTimer**](https://msdn.microsoft.com/library/windows/hardware/dn265188) routine to set the high-resolution timer, the operating system increases the resolution of the system clock, as necessary, so that the times at which the timer expires more precisely correspond to the nominal expiration times specified in the *DueTime* and *Period* parameters.

A Kernel-Mode Driver Framework (KMDF) driver can call the [**WdfTimerCreate**](https://msdn.microsoft.com/library/windows/hardware/ff550050) method to create a high-resolution timer. In this call, the driver passes a pointer to a [**WDF\_TIMER\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552519) structure as a parameter. To create a high-resolution timer, the driver sets the **UseHighResolutionTimer** member of this structure to **TRUE**. This member is a part of the structure starting with Windows 8.1 and KMDF version 1.13.

## Controlling timer accuracy


For example, for Windows running on an x86 processor, the default interval between system clock ticks is typically about 15 milliseconds, and the minimum interval between system clock ticks is about 1 millisecond. Thus, the expiration time of a default-resolution timer (which **ExAllocateTimer** creates if the EX\_TIMER\_HIGH\_RESOLUTION flag is not set) can be controlled only to within about 15 milliseconds, but the expiration time of a high-resolution timer can be controlled to within a millisecond.

If a driver specifies a relative expiration time for a default-resolution timer, the timer can expire up to about 15 milliseconds earlier or later than the specified expiration time. If a driver specifies a relative expiration time for a high-resolution timer, the timer can expire as late as about a millisecond after the specified expiration time but it never expires early. For more information about the relationship between system clock resolution and timer accuracy, see [Timer Accuracy](timer-accuracy.md).

If no high-resolution timers are set, the operating system typically runs the system clock at its default rate. However, if one or more high-resolution timers are set, the operating system might need to run the system clock at its maximum rate for at least a part of the time before these timers expire.

To avoid unnecessarily increasing power consumption, the operating system runs the system clock at its maximum rate only when necessary to satisfy the timing requirements of high-resolution timers. For example, if a high-resolution timer is periodic, and its period spans several default system clock ticks, the operating system might run the system clock at its maximum rate only in the part of the timer period that immediately precedes each expiration. For the rest of the timer period, the system clock runs at its default rate.

To prevent excessive power consumption, drivers should avoid setting the period of a long-running high-resolution timer to a value that is less than the default interval between system clock ticks. Otherwise, the operating system is forced to continuously run the system clock at its maximum rate.

Starting with Windows 8, a driver can call the [**ExQueryTimerResolution**](https://msdn.microsoft.com/library/windows/hardware/dn275969) routine to get the range of timer resolutions that are supported by the system clock.

## Comparison to ExSetTimerResolution


Starting with Windows 2000, a driver can call the [**ExSetTimerResolution**](calling-exsettimerresolution-while-processing-a-power-irp.md) routine to change the time interval between successive system clock interrupts. For example, a driver can call this routine to change the system clock from its default rate to its maximum rate to improve timer accuracy. However, using **ExSetTimerResolution** has several disadvantages compared to using high-resolution timers created by **ExAllocateTimer**.

First, after calling **ExSetTimerResolution** to temporarily increase the system clock rate, a driver must call **ExSetTimerResolution** a second time to restore the system clock to its default rate. Otherwise, the system clock timer continuously generates interrupts at the maximum rate, which might cause excessive power consumption.

Second, a driver that uses the **ExSetTimerResolution** routine cannot optimize its temporary use of higher system clock rates as effectively as the operating system does for high-resolution timers. Thus, the system clock spends more time running at the maximum rate than is strictly necessary.

Third, if multiple drivers concurrently use **ExSetTimerResolution** to improve timer accuracy, the system clock might run at its maximum rate for long periods. In contrast, the operating system globally coordinates the operation of multiple high-resolution timers so that the system clock runs at the maximum rate only when necessary to meet the timing requirements of these timers.

Finally, using **ExSetTimerResolution** is inherently less accurate than using a high-resolution timer. After a driver calls **ExSetTimerResolution** to increase the system clock to its maximum rate, which is typically about a tick per millisecond, the driver might call a routine such as [**KeSetTimerEx**](https://msdn.microsoft.com/library/windows/hardware/ff553292) to set the timer. If, in this call, the driver specifies a relative expiration time, the timer can expire up to about a millisecond earlier than or later than the specified expiration time. However, if a relative expiration time is specified for a high-resolution timer, the timer can expire up to about a millisecond later than the specified expiration time but it never expires early.

 

 




