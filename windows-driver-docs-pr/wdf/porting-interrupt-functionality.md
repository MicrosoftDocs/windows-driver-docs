---
title: Porting Interrupts
description: Porting Interrupts
ms.assetid: E91B971D-044C-45A4-AD76-44AFB1213F8E
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Interrupts


The code for supporting and servicing interrupts is similar in WDF and WDM drivers. There is one primary difference:

-   A WDF driver creates the WDFINTERRUPT object and registers its interrupt service routine (ISR) callback by calling [**WdfInterruptCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfinterrupt/nf-wdfinterrupt-wdfinterruptcreate) from its [*EvtDriverDeviceAdd*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback.
-   A WDM driver creates a KINTERRUPT structure and connects it during [**IRP\_MN\_START\_DEVICE**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-start-device) processing.

The [*EvtInterruptIsr*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_isr) callback in a WDF driver performs the same tasks as the WDM driver’s [*InterruptService*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-kservice_routine) routine. The *EvtInterruptIsr* callback calls [**WdfInterruptQueueDpcForIsr**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfinterrupt/nf-wdfinterrupt-wdfinterruptqueuedpcforisr) to queue the [*EvtInterruptDpc*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) callback for later processing at DISPATCH\_LEVEL. In response, the framework adds a DPC object to the system queue that runs this callback.

For more information about framework interrupt objects, see [Handling Hardware Interrupts](handling-hardware-interrupts.md).

 

 





