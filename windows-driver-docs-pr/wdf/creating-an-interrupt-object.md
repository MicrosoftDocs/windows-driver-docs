---
title: Creating an Interrupt Object
description: Learn about creating an interrupt object. Drivers can create interrupt objects from 'EvtDriverDeviceAdd' and 'EvtDevicePrepareHardware' callback functions.
keywords:
- hardware interrupts WDK KMDF , object creation
- interrupts WDK KMDF , object creation
- message-signaled interrupts WDK KMDF
- MSIs WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating an Interrupt Object


A Windows Driver Frameworks (WDF) driver that handles a device's hardware interrupts must create a framework interrupt object for each interrupt that each device can support. In framework versions 1.11 and later running on Windows 8 or later versions of the operating system, Kernel-Mode Driver Framework (KMDF) and User-Mode Driver Framework (UMDF) drivers can create interrupt objects requiring [passive-level handling](supporting-passive-level-interrupts.md). Unless you are writing a driver for a System on a Chip (SoC) platform, however, your driver should use DIRQL interrupt objects.

A driver typically creates framework interrupt objects in its [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function. A driver can also create interrupt objects from its [*EvtDevicePrepareHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) callback function.

The framework calls the driver's [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function before the Plug and Play (PnP) manager has assigned system resources, such as interrupt vectors, to the device. After the PnP manager assigns resources, the framework stores interrupt resources in the device's interrupt object. (Drivers that [do not support Plug and Play](using-kernel-mode-driver-framework-with-non-pnp-drivers.md) cannot use interrupt objects.)

To create a framework interrupt object, your driver must initialize a [**WDF\_INTERRUPT\_CONFIG**](/windows-hardware/drivers/ddi/wdfinterrupt/ns-wdfinterrupt-_wdf_interrupt_config) structure and pass it to the [**WdfInterruptCreate**](/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdfinterruptcreate) method.

UMDF supports the following types of interrupts:

-   Level-triggered (shared or exclusive)
-   Edge-triggered (exclusive only)
-   MSI (exclusive by definition)

**Note**  UMDF does not support *shared* edge-triggered interrupts.

 

Starting in UMDF version 2.15, UMDF supports interrupts for simple devices like hardware push-buttons, usually backed by GPIO pins, that you cannot enable or disable explicitly using hardware registers. To support such devices, a UMDF driver must use exclusive edge-triggered interrupts.

Starting in KMDF version 1.15, KMDF also supports interrupts for such devices, without the workaround described in [Handling Active-Both Interrupts](handling-active-both-interrupts.md).

Also in [**WDF\_INTERRUPT\_CONFIG**](/windows-hardware/drivers/ddi/wdfinterrupt/ns-wdfinterrupt-_wdf_interrupt_config), your driver supplies pointers to the following driver-supplied event callback functions:

<a href="" id="---------evtinterruptenable--------"></a>[*EvtInterruptEnable*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_enable)  
Enables a hardware interrupt.

<a href="" id="---------evtinterruptdisable--------"></a>[*EvtInterruptDisable*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_disable)  
Disables a hardware interrupt.

<a href="" id="---------evtinterruptisr--------"></a>[*EvtInterruptIsr*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_isr)  
Interrupt service routine (ISR) for the interrupt.

<a href="" id="---------evtinterruptdpc--------"></a>[*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc)  
Deferred procedure call (DPC) for the interrupt.

<a href="" id="evtinterruptworkitem"></a>[*EvtInterruptWorkItem*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_workitem)  
Work item for a [passive-level interrupt](supporting-passive-level-interrupts.md).

For drivers using framework version 1.11 or later on Windows 8 or later versions of the operating system, the driver can explicitly set the parent of a framework interrupt object (DIRQL or passive) to either a framework device object or a framework queue object. If the driver specifies a parent, the driver must set the **AutomaticSerialization** member of the interrupt object's [**WDF\_INTERRUPT\_CONFIG**](/windows-hardware/drivers/ddi/wdfinterrupt/ns-wdfinterrupt-_wdf_interrupt_config) structure to TRUE. (Recall that if **AutomaticSerialization** is TRUE, the framework synchronizes execution of the interrupt object's [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) or [*EvtInterruptWorkItem*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_workitem) callback function with callback functions from other objects that are underneath the interrupt's parent object.)

As an example, a driver might specify a queue as parent of an interrupt to synchronize the queue's callbacks with either the interrupt's [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) or [*EvtInterruptWorkItem*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_workitem) callback. In this configuration, the framework deletes the queue object when it deletes the device object.

After calling [**WdfInterruptCreate**](/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdfinterruptcreate), the driver can optionally call [**WdfInterruptSetPolicy**](/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdfinterruptsetpolicy) or [**WdfInterruptSetExtendedPolicy**](/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdfinterruptsetextendedpolicy) to specify additional interrupt parameters. Typically the driver calls these methods from its [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function.

The framework automatically deletes the interrupt before deleting the interrupt's parent. Optionally, a driver can call [**WdfObjectDelete**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete) to delete the interrupt at an earlier time.

## Supporting Message-signaled Interrupts


Message-signaled interrupts (MSIs) are supported starting with Windows Vista. To enable the operating system to support MSIs for your device, your driver's INF file must set some values in the registry. For information about how to set these values, see [Enabling Message-Signaled Interrupts in the Registry](../kernel/enabling-message-signaled-interrupts-in-the-registry.md).

Your driver should create a framework interrupt object for each interrupt vector or MSI message that the device can support. If the PnP manager does not grant the device all of the interrupt resources that the device can support, the extra interrupt objects will not be used and their callback functions will not be called.

In Windows 7, the operating system does not support resource requests for more than 910 interrupt messages per device function. In Windows 8, the operating system does not support resource requests for more than 2048 interrupts per device function.

If the device driver exceeds this limit, the device might fail to start. To operate in a computer that contains many logical processors, the driver should not request more than one interrupt per processor.

A driver must tolerate, without failures, system rebalancing of interrupt resources in which the PnP manager assigns to the device any set of alternative interrupt resources from the resource requirements list. For example, the device might be assigned a smaller number of message interrupts than the driver requested. In the worst case, the driver must be prepared to operate the device with just one line-based interrupt.

 

