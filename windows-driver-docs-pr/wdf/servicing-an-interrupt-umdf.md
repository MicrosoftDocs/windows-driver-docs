---
title: Servicing an Interrupt
description: Servicing an Interrupt
ms.assetid: 79BA75B3-E10F-4AC1-A2C5-A502BF821188
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Servicing an Interrupt


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

Servicing an interrupt consists of two steps:

1.  Saving volatile information (such as register contents) quickly, in an interrupt service routine.
2.  Processing the saved volatile information in a workitem routine.

When a device generates a hardware interrupt, the framework calls the driver's interrupt service routine (ISR), which framework-based drivers implement as an [*OnInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/hh463902) callback function.

The [*OnInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/hh463902) callback function, which runs at PASSIVE\_LEVEL, must quickly save interrupt information, such as register contents, queue a workitem to process the data further, and return from the ISR to allow servicing of other interrupts if the interrupt line is shared. Because the UMDF driver's ISR runs at PASSIVE\_LEVEL, handling PCI line-based interrupts is not recommended. These interrupts are typically shared between multiple devices, some of which might not accept ISR delays. However, you can handle PCI MSI interrupts in a UMDF driver. These interrupts have edge semantics and are not shared.

Typically, the [*OnInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/hh463902) callback function schedules a workitem to process the saved information later. Framework-based drivers implement workitem routines as [*OnInterruptWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh463905) callback functions.

Most drivers use a single [*OnInterruptWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh463905) callback function for each type of interrupt. To schedule execution of an *OnInterruptWorkItem* callback function, a driver must call [**IWDFInterrupt::QueueWorkItemForIsr**](https://msdn.microsoft.com/library/windows/hardware/hh451314) from within the [*OnInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/hh463902) callback function.

If your driver creates multiple framework queue objects for each device, you might consider using a separate workitem object and [*OnWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh463909) callback function for each queue. To schedule execution of an *OnWorkItem* callback function, the driver must first create one or more workitem objects by calling [**IWdfDevice3::CreateWorkItem**](https://msdn.microsoft.com/library/windows/hardware/hh451213), typically from the driver's [**IDriverEntry::OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896) callback function. Then the driver's [*OnInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/hh463902) callback function can call [**IWDFWorkItem::Enqueue**](https://msdn.microsoft.com/library/windows/hardware/hh463883).

Drivers typically complete I/O requests in their [*OnInterruptWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh463905) or [*OnWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh463909) callback functions.

For an example of a UMDF driver that handles interrupts, see the [SpbAccelerometer](http://go.microsoft.com/fwlink/p/?linkid=256189) sample driver, available starting in the Windows 8 WDK.

 

 





