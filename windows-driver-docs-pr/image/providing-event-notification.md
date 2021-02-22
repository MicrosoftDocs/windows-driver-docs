---
title: Providing Event Notification
description: Providing Event Notification
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Providing Event Notification





The WIA service notifies a WIA minidriver of a supported device event by calling the [**IWiaMiniDrv::drvNotifyPnpEvent**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvnotifypnpevent) method. In this method, the minidriver implements the device-specific functionality needed to respond to the event. The WIA service calls the **IWiaMiniDrv::drvNotifyPnpEvent** method only for an event the minidriver has indicated the device can support in the [**IWiaMiniDrv::drvGetCapabilities**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvgetcapabilities) method.

The minidriver initiates an event either through the STI event mechanism, or by using [**wiasQueueEvent**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasqueueevent) to add an event notification from this device to the event queue.

### Asynchronous Behavior: Power Management and I/O Cancellation

In most cases, the WIA service ensures that only one call is made down to the driver at a time. However, some methods are inherently asynchronous and reentrant in nature. A good example of this is the [**IWiaMiniDrv::drvNotifyPnpEvent**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvnotifypnpevent) method.

The WIA service uses this method to notify the driver of events that may require immediate action. For example, when the WIA service receives a Plug and Play event indicating that the device has been removed, it informs the driver immediately. Other examples include power management events and I/O cancellation requests from applications.

For a sample implementation of the [**IWiaMiniDrv::drvNotifyPnpEvent**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvnotifypnpevent) method, illustrating how it should respond to various kinds of events, see [Adding Interrupt Event Support](adding-interrupt-event-support.md).

 

