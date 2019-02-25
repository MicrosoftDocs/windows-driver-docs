---
title: Servicing an Interrupt
description: Servicing an Interrupt
ms.assetid: b6306d2c-a7be-4fc3-8123-4d2b5c60c988
keywords:
- hardware interrupts WDK KMDF , servicing
- interrupts WDK KMDF , servicing
- servicing interrupts WDK KMDF
- interrupt service routines WDK KMDF
- ISRs WDK KMDF
- deferred procedure calls WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Servicing an Interrupt


This topic describes how to service a DIRQL interrupt. For information about servicing a passive-level interrupt, see [Supporting Passive Level Interrupts](supporting-passive-level-interrupts.md#servicing).

Servicing an interrupt consists of two, and sometimes three, steps:

1.  Saving volatile information (such as register contents) quickly, in an interrupt service routine that runs at IRQL = DIRQL.

2.  Processing the saved volatile information in a deferred procedure call (DPC) that runs at IRQL = DISPATCH\_LEVEL.

3.  Performing additional work at IRQL = PASSIVE\_LEVEL, if necessary.

When a device generates a hardware interrupt, the framework calls the driver's interrupt service routine (ISR), which framework-based drivers implement as an [*EvtInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/ff541735) callback function.

The [*EvtInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/ff541735) callback function, which runs at the device's DIRQL, must quickly save interrupt information, such as register contents, that will be lost if another interrupt occurs.

Typically, the [*EvtInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/ff541735) callback function schedules a deferred procedure call (DPC) to process the saved information later at a lower IRQL (DISPATCH\_LEVEL). Framework-based drivers implement DPC routines as [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) or [*EvtDpcFunc*](https://msdn.microsoft.com/library/windows/hardware/ff541683) callback functions.

Most drivers use a single [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) callback function for each type of interrupt. To schedule execution of an *EvtInterruptDpc* callback function, a driver must call [**WdfInterruptQueueDpcForIsr**](https://msdn.microsoft.com/library/windows/hardware/ff547371) from within the [*EvtInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/ff541735) callback function.

If your driver creates multiple [framework queue objects](framework-queue-objects.md) for each device, you might consider using a separate [DPC object](https://msdn.microsoft.com/library/windows/hardware/dn265635) and [*EvtDpcFunc*](https://msdn.microsoft.com/library/windows/hardware/ff541683) callback function for each queue. To schedule execution of an *EvtDpcFunc* callback function, the driver must first create one or more DPC objects by calling [**WdfDpcCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547140), typically in the driver's [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function. Then the driver's [*EvtInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/ff541735) callback function can call [**WdfDpcEnqueue**](https://msdn.microsoft.com/library/windows/hardware/ff547148).

Drivers typically [complete I/O requests](completing-i-o-requests.md) in their [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) or [*EvtDpcFunc*](https://msdn.microsoft.com/library/windows/hardware/ff541683) callback functions.

Sometimes a driver must perform some interrupt-servicing operations at IRQL = PASSIVE\_LEVEL. In such cases the driver's [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) or [*EvtDpcFunc*](https://msdn.microsoft.com/library/windows/hardware/ff541683) callback function, executing at IRQL = DISPATCH\_LEVEL, can schedule execution of one or more [framework work items](using-framework-work-items.md), which run at IRQL = PASSIVE\_LEVEL.

For an example of a driver that uses work items while servicing device interrupts, see the [PCIDRV](sample-kmdf-drivers.md) sample driver.

 

 





