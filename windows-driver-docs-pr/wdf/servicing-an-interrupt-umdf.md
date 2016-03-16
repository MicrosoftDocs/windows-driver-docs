---
title: Servicing an Interrupt
description: Servicing an Interrupt
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: 79BA75B3-E10F-4AC1-A2C5-A502BF821188
---

# Servicing an Interrupt


\[This topic applies to UMDF 1.*x*.\]

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Servicing%20an%20Interrupt%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




