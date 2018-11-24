---
title: Creating an Interrupt Object
description: Creating an Interrupt Object
ms.assetid: D281F2E8-3ADA-4F4E-B345-CE72FA3C69EC
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating an Interrupt Object


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

A UMDF driver that handles a device's hardware interrupts must create a framework interrupt object for each interrupt that each device can support.

Typically, a driver creates framework interrupt objects in [**IDriverEntry::OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896). However, you can also create interrupt objects in [**IPnpCallbackHardware2::OnPrepareHardware**](https://msdn.microsoft.com/library/windows/hardware/hh439734).

To create a framework interrupt object, your driver must initialize a [**WUDF\_INTERRUPT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/hh464084) structure and pass it to the [**IWDFDevice3::CreateInterrupt**](https://msdn.microsoft.com/library/windows/hardware/hh451208) method. This method registers the following driver-supplied event callback functions:

<a href="" id="oninterruptenable"></a>[*OnInterruptEnable*](https://msdn.microsoft.com/library/windows/hardware/hh463899)  
Enables a hardware interrupt.

<a href="" id="oninterruptdisable"></a>[*OnInterruptDisable*](https://msdn.microsoft.com/library/windows/hardware/hh463895)  
Disables a hardware interrupt.

<a href="" id="oninterruptisr"></a>[*OnInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/hh463902)  
The interrupt service routine (ISR) for the interrupt.

<a href="" id="oninterruptworkitem"></a>[*OnInterruptWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh463905)  
The worker routine for the interrupt.

Optionally, the driver can call [**IWDFInterrupt::SetPolicy**](https://msdn.microsoft.com/library/windows/hardware/hh451328) or [**IWDFInterrupt::SetExtendedPolicy**](https://msdn.microsoft.com/library/windows/hardware/hh451324) to specify additional interrupt parameters.

The framework calls the driver's [**IDriverEntry::OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896) callback function before the Plug and Play (PnP) manager has assigned system resources, such as interrupt vectors, to the device. After the PnP manager assigns resources, the framework stores interrupt resources in the device's interrupt object. (Drivers that don't support Plug and Play cannot use interrupt objects.)

Message-signaled interrupts (MSIs) are supported in Windows Vista and later versions of the operating system. To enable the operating system to support MSIs for your device, your driver's INF file must set some values in the registry. For information about how to set these values, see [Enabling Message-Signaled Interrupts in the Registry](https://msdn.microsoft.com/library/windows/hardware/ff544246).

If a device can support a certain number of MSI messages, the PnP manager will try to assign that number of messages to the device. If the PnP manager cannot assign all of the messages that the device can support, it will assign only one message to the device.

Your driver should create a framework interrupt object for each interrupt vector or MSI message that the device can support. If the PnP manager doesn't grant the device all of the interrupt resources that the device can support, the extra interrupt objects won't be used, and their callback functions won't be called.

 

 





