---
title: Creating an Interrupt Object
description: Creating an Interrupt Object
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: D281F2E8-3ADA-4F4E-B345-CE72FA3C69EC
---

# Creating an Interrupt Object


\[This topic applies to UMDF 1.*x*.\]

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Creating%20an%20Interrupt%20Object%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




