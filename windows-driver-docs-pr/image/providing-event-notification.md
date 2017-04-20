---
title: Providing Event Notification
author: windows-driver-content
description: Providing Event Notification
ms.assetid: 53ca7ef0-fa8b-4ae1-9b5e-b145c2d02db2
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Providing Event Notification


## <a href="" id="ddk-providing-event-notification-si"></a>


The WIA service notifies a WIA minidriver of a supported device event by calling the [**IWiaMiniDrv::drvNotifyPnpEvent**](https://msdn.microsoft.com/library/windows/hardware/ff544998) method. In this method, the minidriver implements the device-specific functionality needed to respond to the event. The WIA service calls the **IWiaMiniDrv::drvNotifyPnpEvent** method only for an event the minidriver has indicated the device can support in the [**IWiaMiniDrv::drvGetCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff543977) method.

The minidriver initiates an event either through the STI event mechanism, or by using [**wiasQueueEvent**](https://msdn.microsoft.com/library/windows/hardware/ff549296) to add an event notification from this device to the event queue.

### Asynchronous Behavior: Power Management and I/O Cancellation

In most cases, the WIA service ensures that only one call is made down to the driver at a time. However, some methods are inherently asynchronous and reentrant in nature. A good example of this is the [**IWiaMiniDrv::drvNotifyPnpEvent**](https://msdn.microsoft.com/library/windows/hardware/ff544998) method.

The WIA service uses this method to notify the driver of events that may require immediate action. For example, when the WIA service receives a Plug and Play event indicating that the device has been removed, it informs the driver immediately. Other examples include power management events and I/O cancellation requests from applications.

For a sample implementation of the [**IWiaMiniDrv::drvNotifyPnpEvent**](https://msdn.microsoft.com/library/windows/hardware/ff544998) method, illustrating how it should respond to various kinds of events, see [Adding Interrupt Event Support](adding-interrupt-event-support.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Providing%20Event%20Notification%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


