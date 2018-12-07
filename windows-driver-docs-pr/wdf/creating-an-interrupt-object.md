---
title: Creating an Interrupt Object
description: Creating an Interrupt Object
ms.assetid: 8bea7498-9fee-4d84-9e6b-976102c54876
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

A driver typically creates framework interrupt objects in its [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function. A driver can also create interrupt objects from its [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880) callback function.

The framework calls the driver's [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function before the Plug and Play (PnP) manager has assigned system resources, such as interrupt vectors, to the device. After the PnP manager assigns resources, the framework stores interrupt resources in the device's interrupt object. (Drivers that [do not support Plug and Play](using-kernel-mode-driver-framework-with-non-pnp-drivers.md) cannot use interrupt objects.)

To create a framework interrupt object, your driver must initialize a [**WDF\_INTERRUPT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552347) structure and pass it to the [**WdfInterruptCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547345) method.

UMDF supports the following types of interrupts:

-   Level-triggered (shared or exclusive)
-   Edge-triggered (exclusive only)
-   MSI (exclusive by definition)

**Note**  UMDF does not support *shared* edge-triggered interrupts.

 

Starting in UMDF version 2.15, UMDF supports interrupts for simple devices like hardware push-buttons, usually backed by GPIO pins, that you cannot enable or disable explicitly using hardware registers. To support such devices, a UMDF driver must use exclusive edge-triggered interrupts.

Starting in KMDF version 1.15, KMDF also supports interrupts for such devices, without the workaround described in [Handling Active-Both Interrupts](handling-active-both-interrupts.md).

Also in [**WDF\_INTERRUPT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552347), your driver supplies pointers to the following driver-supplied event callback functions:

<a href="" id="---------evtinterruptenable--------"></a>[*EvtInterruptEnable*](https://msdn.microsoft.com/library/windows/hardware/ff541730)  
Enables a hardware interrupt.

<a href="" id="---------evtinterruptdisable--------"></a>[*EvtInterruptDisable*](https://msdn.microsoft.com/library/windows/hardware/ff541714)  
Disables a hardware interrupt.

<a href="" id="---------evtinterruptisr--------"></a>[*EvtInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/ff541735)  
Interrupt service routine (ISR) for the interrupt.

<a href="" id="---------evtinterruptdpc--------"></a>[*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721)  
Deferred procedure call (DPC) for the interrupt.

<a href="" id="evtinterruptworkitem"></a>[*EvtInterruptWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh406422)  
Work item for a [passive-level interrupt](supporting-passive-level-interrupts.md).

For drivers using framework version 1.11 or later on Windows 8 or later versions of the operating system, the driver can explicitly set the parent of a framework interrupt object (DIRQL or passive) to either a framework device object or a framework queue object. If the driver specifies a parent, the driver must set the **AutomaticSerialization** member of the interrupt object's [**WDF\_INTERRUPT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552347) structure to TRUE. (Recall that if **AutomaticSerialization** is TRUE, the framework synchronizes execution of the interrupt object's [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) or [*EvtInterruptWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh406422) callback function with callback functions from other objects that are underneath the interrupt's parent object.)

As an example, a driver might specify a queue as parent of an interrupt to synchronize the queue's callbacks with either the interrupt's [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) or [*EvtInterruptWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh406422) callback. In this configuration, the framework deletes the queue object when it deletes the device object.

After calling [**WdfInterruptCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547345), the driver can optionally call [**WdfInterruptSetPolicy**](https://msdn.microsoft.com/library/windows/hardware/ff547387) or [**WdfInterruptSetExtendedPolicy**](https://msdn.microsoft.com/library/windows/hardware/ff547381) to specify additional interrupt parameters. Typically the driver calls these methods from its [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function.

The framework automatically deletes the interrupt before deleting the interrupt's parent. Optionally, a driver can call [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734) to delete the interrupt at an earlier time.

## Supporting Message-signaled Interrupts


Message-signaled interrupts (MSIs) are supported starting with Windows Vista. To enable the operating system to support MSIs for your device, your driver's INF file must set some values in the registry. For information about how to set these values, see [Enabling Message-Signaled Interrupts in the Registry](https://msdn.microsoft.com/library/windows/hardware/ff544246).

Your driver should create a framework interrupt object for each interrupt vector or MSI message that the device can support. If the PnP manager does not grant the device all of the interrupt resources that the device can support, the extra interrupt objects will not be used and their callback functions will not be called.

In Windows 7, the operating system does not support resource requests for more than 910 interrupt messages per device function. In Windows 8, the operating system does not support resource requests for more than 2048 interrupts per device function.

If the device driver exceeds this limit, the device might fail to start. To operate in a computer that contains many logical processors, the driver should not request more than one interrupt per processor.

A driver must tolerate, without failures, system rebalancing of interrupt resources in which the PnP manager assigns to the device any set of alternative interrupt resources from the resource requirements list. For example, the device might be assigned a smaller number of message interrupts than the driver requested. In the worst case, the driver must be prepared to operate the device with just one line-based interrupt.

 

 





