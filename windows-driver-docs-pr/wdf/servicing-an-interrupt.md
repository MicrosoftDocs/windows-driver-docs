---
title: Servicing an Interrupt
description: Learn how to service a DIRQL interrupt. Servicing an interrupt can consist of two, or sometimes three steps.
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

When a device generates a hardware interrupt, the framework calls the driver's interrupt service routine (ISR), which framework-based drivers implement as an [*EvtInterruptIsr*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_isr) callback function.

The [*EvtInterruptIsr*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_isr) callback function, which runs at the device's DIRQL, must quickly save interrupt information, such as register contents, that will be lost if another interrupt occurs.

Typically, the [*EvtInterruptIsr*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_isr) callback function schedules a deferred procedure call (DPC) to process the saved information later at a lower IRQL (DISPATCH\_LEVEL). Framework-based drivers implement DPC routines as [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) or [*EvtDpcFunc*](/windows-hardware/drivers/ddi/wdfdpc/nc-wdfdpc-evt_wdf_dpc) callback functions.

Most drivers use a single [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) callback function for each type of interrupt. To schedule execution of an *EvtInterruptDpc* callback function, a driver must call [**WdfInterruptQueueDpcForIsr**](/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdfinterruptqueuedpcforisr) from within the [*EvtInterruptIsr*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_isr) callback function.

If your driver creates multiple [framework queue objects](framework-queue-objects.md) for each device, you might consider using a separate [DPC object](/windows-hardware/drivers/ddi/wdfdpc/) and [*EvtDpcFunc*](/windows-hardware/drivers/ddi/wdfdpc/nc-wdfdpc-evt_wdf_dpc) callback function for each queue. To schedule execution of an *EvtDpcFunc* callback function, the driver must first create one or more DPC objects by calling [**WdfDpcCreate**](/windows-hardware/drivers/ddi/wdfdpc/nf-wdfdpc-wdfdpccreate), typically in the driver's [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function. Then the driver's [*EvtInterruptIsr*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_isr) callback function can call [**WdfDpcEnqueue**](/windows-hardware/drivers/ddi/wdfdpc/nf-wdfdpc-wdfdpcenqueue).

Drivers typically [complete I/O requests](completing-i-o-requests.md) in their [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) or [*EvtDpcFunc*](/windows-hardware/drivers/ddi/wdfdpc/nc-wdfdpc-evt_wdf_dpc) callback functions.

Sometimes a driver must perform some interrupt-servicing operations at IRQL = PASSIVE\_LEVEL. In such cases the driver's [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) or [*EvtDpcFunc*](/windows-hardware/drivers/ddi/wdfdpc/nc-wdfdpc-evt_wdf_dpc) callback function, executing at IRQL = DISPATCH\_LEVEL, can schedule execution of one or more [framework work items](using-framework-work-items.md), which run at IRQL = PASSIVE\_LEVEL.

For an example of a driver that uses work items while servicing device interrupts, see the [PCIDRV](sample-kmdf-drivers.md) sample driver.

 

