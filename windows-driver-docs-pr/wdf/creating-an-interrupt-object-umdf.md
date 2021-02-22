---
title: Creating an Interrupt Object (UMDF 1)
description: Creating an Interrupt Object
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating an Interrupt Object (UMDF 1)


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

A UMDF driver that handles a device's hardware interrupts must create a framework interrupt object for each interrupt that each device can support.

Typically, a driver creates framework interrupt objects in [**IDriverEntry::OnDeviceAdd**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-idriverentry-ondeviceadd). However, you can also create interrupt objects in [**IPnpCallbackHardware2::OnPrepareHardware**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallbackhardware2-onpreparehardware).

To create a framework interrupt object, your driver must initialize a [**WUDF\_INTERRUPT\_CONFIG**](/windows-hardware/drivers/ddi/wudfinterrupt/ns-wudfinterrupt-_wudf_interrupt_config) structure and pass it to the [**IWDFDevice3::CreateInterrupt**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice3-createinterrupt) method. This method registers the following driver-supplied event callback functions:

<a href="" id="oninterruptenable"></a>[*OnInterruptEnable*](/windows-hardware/drivers/ddi/wudfinterrupt/nc-wudfinterrupt-wudf_interrupt_enable)  
Enables a hardware interrupt.

<a href="" id="oninterruptdisable"></a>[*OnInterruptDisable*](/windows-hardware/drivers/ddi/wudfinterrupt/nc-wudfinterrupt-wudf_interrupt_disable)  
Disables a hardware interrupt.

<a href="" id="oninterruptisr"></a>[*OnInterruptIsr*](/windows-hardware/drivers/ddi/wudfinterrupt/nc-wudfinterrupt-wudf_interrupt_isr)  
The interrupt service routine (ISR) for the interrupt.

<a href="" id="oninterruptworkitem"></a>[*OnInterruptWorkItem*](/windows-hardware/drivers/ddi/wudfinterrupt/nc-wudfinterrupt-wudf_interrupt_workitem)  
The worker routine for the interrupt.

Optionally, the driver can call [**IWDFInterrupt::SetPolicy**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfinterrupt-setpolicy) or [**IWDFInterrupt::SetExtendedPolicy**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfinterrupt-setextendedpolicy) to specify additional interrupt parameters.

The framework calls the driver's [**IDriverEntry::OnDeviceAdd**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-idriverentry-ondeviceadd) callback function before the Plug and Play (PnP) manager has assigned system resources, such as interrupt vectors, to the device. After the PnP manager assigns resources, the framework stores interrupt resources in the device's interrupt object. (Drivers that don't support Plug and Play cannot use interrupt objects.)

Message-signaled interrupts (MSIs) are supported in Windows Vista and later versions of the operating system. To enable the operating system to support MSIs for your device, your driver's INF file must set some values in the registry. For information about how to set these values, see [Enabling Message-Signaled Interrupts in the Registry](../kernel/enabling-message-signaled-interrupts-in-the-registry.md).

If a device can support a certain number of MSI messages, the PnP manager will try to assign that number of messages to the device. If the PnP manager cannot assign all of the messages that the device can support, it will assign only one message to the device.

Your driver should create a framework interrupt object for each interrupt vector or MSI message that the device can support. If the PnP manager doesn't grant the device all of the interrupt resources that the device can support, the extra interrupt objects won't be used, and their callback functions won't be called.

 

