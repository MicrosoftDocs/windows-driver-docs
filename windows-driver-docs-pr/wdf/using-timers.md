---
title: Using Timers
description: Describes how to use the framework's built-in timer support. Applies to both KMDF drivers as well as UMDF drivers starting in version 2.
keywords:
- timers WDK KMDF
- framework objects WDK KMDF , timer objects
- timer objects WDK KMDF
- periodic timers WDK KMDF
- stopping timers WDK KMDF
- starting timers WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Timers


This topic describes how to use the framework's built-in timer support. It applies to both Kernel-Mode Driver Framework (KMDF) drivers as well as User-Mode Driver Framework (UMDF) drivers starting in version 2.

The framework provides a *timer object* that enables drivers to create timers. After a driver creates a timer object and starts the timer's clock, the framework calls a driver-supplied callback function after a specified amount of time has elapsed. Optionally, your driver can set up the timer so that the framework calls the callback function repeatedly, whenever a specified amount of time has elapsed.

To create a framework timer object, your driver must call the [**WdfTimerCreate**](/windows-hardware/drivers/ddi/wdftimer/nf-wdftimer-wdftimercreate) method. This method registers an [*EvtTimerFunc*](/windows-hardware/drivers/ddi/wdftimer/nc-wdftimer-evt_wdf_timer) callback function and a periodic time interval. If you want the framework to call the callback function only once, your driver specifies zero for the periodic time interval.

Typically, you will know the number of timers that your driver will need for each device. Therefore, the driver can create timer objects by calling [**WdfTimerCreate**](/windows-hardware/drivers/ddi/wdftimer/nf-wdftimer-wdftimercreate) in its [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function, and it can store timer object handles in a device or queue object's [context space](framework-object-context-space.md).

To start the timer, your driver calls [**WdfTimerStart**](/windows-hardware/drivers/ddi/wdftimer/nf-wdftimer-wdftimerstart), passing a "due time". The framework starts the timer's clock and calls the [*EvtTimerFunc*](/windows-hardware/drivers/ddi/wdftimer/nc-wdftimer-evt_wdf_timer) callback function when the specified amount of time has elapsed.

If the driver supplied a periodic time interval when it called [**WdfTimerCreate**](/windows-hardware/drivers/ddi/wdftimer/nf-wdftimer-wdftimercreate), the timer is referred to as a *periodic timer*. A periodic timer's clock continues to run after the initial "due time" has elapsed, and the framework calls the driver's callback function repeatedly, whenever the periodic time interval has elapsed. Periodic timers do not start automatically. Like non-periodic timers, the driver must still call [**WdfTimerStart**](/windows-hardware/drivers/ddi/wdftimer/nf-wdftimer-wdftimerstart) after creating the timer to start it the first time.

A driver might call [**WdfTimerStart**](/windows-hardware/drivers/ddi/wdftimer/nf-wdftimer-wdftimerstart) from its [*EvtTimerFunc*](/windows-hardware/drivers/ddi/wdftimer/nc-wdftimer-evt_wdf_timer) callback function in order to restart a non-periodic timer after it expires.

To stop a timer, the driver can call [**WdfTimerStop**](/windows-hardware/drivers/ddi/wdftimer/nf-wdftimer-wdftimerstop). Your driver can reuse timers by starting and stopping them repeatedly.

When your driver creates a timer object, it must specify a parent object. The framework stops the timer and deletes the timer object when the parent is deleted. To obtain a timer object's parent object, your driver can call [**WdfTimerGetParentObject**](/windows-hardware/drivers/ddi/wdftimer/nf-wdftimer-wdftimergetparentobject).

In KMDF versions prior to version 1.9, you cannot easily use timer objects if you want all of your driver's callback functions to run at IRQL = PASSIVE\_LEVEL. The framework implements the timer object's [*EvtTimerFunc*](/windows-hardware/drivers/ddi/wdftimer/nc-wdftimer-evt_wdf_timer) callback function as a deferred procedure call (DPC) that is called at IRQL = DISPATCH\_LEVEL. Therefore, if you want your timer expiration code to run at PASSIVE\_LEVEL the *EvtTimerFunc* callback function must queue a [work item](using-framework-work-items.md) that runs at PASSIVE\_LEVEL.

In KMDF versions 1.9 and later, you can create *passive-level timers*, which are timers that run at PASSIVE\_LEVEL. To create a passive-level timer, specify the [**WdfExecutionLevelPassive**](/windows-hardware/drivers/ddi/wdfobject/ne-wdfobject-_wdf_execution_level) execution level when your driver calls [**WdfTimerCreate**](/windows-hardware/drivers/ddi/wdftimer/nf-wdftimer-wdftimercreate). As a result, the framework implements [*EvtTimerFunc*](/windows-hardware/drivers/ddi/wdftimer/nc-wdftimer-evt_wdf_timer) callback functions as work items that run at PASSIVE\_LEVEL. Note that passive-level timers cannot be periodic timers.

Starting in UMDF version 2.0, the framework implements the timer object's [*EvtTimerFunc*](/windows-hardware/drivers/ddi/wdftimer/nc-wdftimer-evt_wdf_timer) callback functions as worker threads from the user-mode thread pool. As a result, a UMDF driver's timer callback functions always run at PASSIVE\_LEVEL.

## No Wake Timers


System power efficiency is reduced by timers that repeatedly cause the system to resume from low-power states. One way to improve battery life is to delay non-critical periodic operations rather than waking the system. Starting in Windows 8.1, you can use *no wake timers* to perform such non-critical operations in either a KMDF or UMDF driver. A no wake timer does not wake the system if it expires while the system is in a low-power state. Instead, the framework calls the driver's [*EvtTimerFunc*](/windows-hardware/drivers/ddi/wdftimer/nc-wdftimer-evt_wdf_timer) callback function the next time the system is in its fully on, S0 state.

No wake timers are available starting with KMDF version 1.13 and UMDF version 2.0.

To create a no wake timer, set the **TolerableDelay** member of [**WDF\_TIMER\_CONFIG**](/windows-hardware/drivers/ddi/wdftimer/ns-wdftimer-_wdf_timer_config) to **TolerableDelayUnlimited**.

For more information about no wake timers, see [No-Wake Timers](../kernel/no-wake-timers.md).

## High Resolution Timers


Standard framework timers have an accuracy that matches the system clock tick interval, which is by default 15.6 milliseconds. Starting in Windows 8.1, you can create *high resolution timers*. A high resolution timer has an accuracy of one millisecond. You might use a high resolution timer for a critical operation that requires a precise, predictable expiration time. As a result of the frequent servicing that it requires, a high resolution timer may result in decreased battery life.

High resolution timers are available only to KMDF drivers, starting with KMDF version 1.13.

To create a high resolution timer, set the **UseHighResolutionTimer** member of [**WDF\_TIMER\_CONFIG**](/windows-hardware/drivers/ddi/wdftimer/ns-wdftimer-_wdf_timer_config) to **WdfTrue**, and then adjust the **Period** value to the desired resolution.

The following table shows examples of timer behavior based on different values that the driver provides for **Period**. These examples assume that the system clock tick interval is 15 milliseconds.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Period, in ms</th>
<th align="left">Standard Timer</th>
<th align="left">High Resolution Timer</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>10</p></td>
<td align="left"><p>The timer expires between 0 milliseconds and 25 milliseconds.</p></td>
<td align="left"><p>The timer expires as soon after 10 milliseconds as possible.</p></td>
</tr>
<tr class="even">
<td align="left"><p>16</p></td>
<td align="left"><p>The timer expires between 15 milliseconds and 30 milliseconds.</p></td>
<td align="left"><p>The timer expires as soon after 16 milliseconds as possible.</p></td>
</tr>
</tbody>
</table>

 

For more information about high resolution timers, see [High-Resolution Timers](../kernel/high-resolution-timers.md).

For more information about how timer accuracy is related to the granularity of the system clock, see [Timer Accuracy](../kernel/timer-accuracy.md).

 

