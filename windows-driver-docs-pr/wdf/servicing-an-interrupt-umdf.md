---
title: Servicing an Interrupt (UMDF 1)
description: Servicing an Interrupt
ms.date: 04/20/2017
---

# Servicing an Interrupt (UMDF 1)


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

Servicing an interrupt consists of two steps:

1.  Saving volatile information (such as register contents) quickly, in an interrupt service routine.
2.  Processing the saved volatile information in a workitem routine.

When a device generates a hardware interrupt, the framework calls the driver's interrupt service routine (ISR), which framework-based drivers implement as an [*OnInterruptIsr*](/windows-hardware/drivers/ddi/wudfinterrupt/nc-wudfinterrupt-wudf_interrupt_isr) callback function.

The [*OnInterruptIsr*](/windows-hardware/drivers/ddi/wudfinterrupt/nc-wudfinterrupt-wudf_interrupt_isr) callback function, which runs at PASSIVE\_LEVEL, must quickly save interrupt information, such as register contents, queue a workitem to process the data further, and return from the ISR to allow servicing of other interrupts if the interrupt line is shared. Because the UMDF driver's ISR runs at PASSIVE\_LEVEL, handling PCI line-based interrupts is not recommended. These interrupts are typically shared between multiple devices, some of which might not accept ISR delays. However, you can handle PCI MSI interrupts in a UMDF driver. These interrupts have edge semantics and are not shared.

Typically, the [*OnInterruptIsr*](/windows-hardware/drivers/ddi/wudfinterrupt/nc-wudfinterrupt-wudf_interrupt_isr) callback function schedules a workitem to process the saved information later. Framework-based drivers implement workitem routines as [*OnInterruptWorkItem*](/windows-hardware/drivers/ddi/wudfinterrupt/nc-wudfinterrupt-wudf_interrupt_workitem) callback functions.

Most drivers use a single [*OnInterruptWorkItem*](/windows-hardware/drivers/ddi/wudfinterrupt/nc-wudfinterrupt-wudf_interrupt_workitem) callback function for each type of interrupt. To schedule execution of an *OnInterruptWorkItem* callback function, a driver must call [**IWDFInterrupt::QueueWorkItemForIsr**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfinterrupt-queueworkitemforisr) from within the [*OnInterruptIsr*](/windows-hardware/drivers/ddi/wudfinterrupt/nc-wudfinterrupt-wudf_interrupt_isr) callback function.

If your driver creates multiple framework queue objects for each device, you might consider using a separate workitem object and [*OnWorkItem*](/windows-hardware/drivers/ddi/wudfworkitem/nc-wudfworkitem-wudf_workitem_function) callback function for each queue. To schedule execution of an *OnWorkItem* callback function, the driver must first create one or more workitem objects by calling [**IWdfDevice3::CreateWorkItem**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice3-createworkitem), typically from the driver's [**IDriverEntry::OnDeviceAdd**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-idriverentry-ondeviceadd) callback function. Then the driver's [*OnInterruptIsr*](/windows-hardware/drivers/ddi/wudfinterrupt/nc-wudfinterrupt-wudf_interrupt_isr) callback function can call [**IWDFWorkItem::Enqueue**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfworkitem-enqueue).

Drivers typically complete I/O requests in their [*OnInterruptWorkItem*](/windows-hardware/drivers/ddi/wudfinterrupt/nc-wudfinterrupt-wudf_interrupt_workitem) or [*OnWorkItem*](/windows-hardware/drivers/ddi/wudfworkitem/nc-wudfworkitem-wudf_workitem_function) callback functions.

For an example of a UMDF driver that handles interrupts, see the [SpbAccelerometer](/samples/browse/) sample driver, available starting in the Windows 8 WDK.

