---
title: Porting Interrupts
description: Porting Interrupts
ms.date: 04/20/2017
---

# Porting Interrupts


The code for supporting and servicing interrupts is similar in WDF and WDM drivers. There is one primary difference:

-   A WDF driver creates the WDFINTERRUPT object and registers its interrupt service routine (ISR) callback by calling [**WdfInterruptCreate**](/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdfinterruptcreate) from its [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback.
-   A WDM driver creates a KINTERRUPT structure and connects it during [**IRP\_MN\_START\_DEVICE**](../kernel/irp-mn-start-device.md) processing.

The [*EvtInterruptIsr*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_isr) callback in a WDF driver performs the same tasks as the WDM driver’s [*InterruptService*](/windows-hardware/drivers/ddi/wdm/nc-wdm-kservice_routine) routine. The *EvtInterruptIsr* callback calls [**WdfInterruptQueueDpcForIsr**](/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdfinterruptqueuedpcforisr) to queue the [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) callback for later processing at DISPATCH\_LEVEL. In response, the framework adds a DPC object to the system queue that runs this callback.

For more information about framework interrupt objects, see [Handling Hardware Interrupts](creating-an-interrupt-object.md).

 

