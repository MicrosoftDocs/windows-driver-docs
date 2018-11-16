---
title: Providing Event Notification
description: Providing Event Notification
ms.assetid: 53ca7ef0-fa8b-4ae1-9b5e-b145c2d02db2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Providing Event Notification





The WIA service notifies a WIA minidriver of a supported device event by calling the [**IWiaMiniDrv::drvNotifyPnpEvent**](https://msdn.microsoft.com/library/windows/hardware/ff544998) method. In this method, the minidriver implements the device-specific functionality needed to respond to the event. The WIA service calls the **IWiaMiniDrv::drvNotifyPnpEvent** method only for an event the minidriver has indicated the device can support in the [**IWiaMiniDrv::drvGetCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff543977) method.

The minidriver initiates an event either through the STI event mechanism, or by using [**wiasQueueEvent**](https://msdn.microsoft.com/library/windows/hardware/ff549296) to add an event notification from this device to the event queue.

### Asynchronous Behavior: Power Management and I/O Cancellation

In most cases, the WIA service ensures that only one call is made down to the driver at a time. However, some methods are inherently asynchronous and reentrant in nature. A good example of this is the [**IWiaMiniDrv::drvNotifyPnpEvent**](https://msdn.microsoft.com/library/windows/hardware/ff544998) method.

The WIA service uses this method to notify the driver of events that may require immediate action. For example, when the WIA service receives a Plug and Play event indicating that the device has been removed, it informs the driver immediately. Other examples include power management events and I/O cancellation requests from applications.

For a sample implementation of the [**IWiaMiniDrv::drvNotifyPnpEvent**](https://msdn.microsoft.com/library/windows/hardware/ff544998) method, illustrating how it should respond to various kinds of events, see [Adding Interrupt Event Support](adding-interrupt-event-support.md).

 

 




