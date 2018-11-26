---
title: How WIA minidriver receives disconnect from WIA
description: How the WIA minidriver receives a disconnect event from the WIA service
ms.assetid: 6ae3c230-d026-469e-a699-860a295fba85
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How the WIA minidriver receives a disconnect event from the WIA service

When a device is surprise-disconnected from the computer, such as when the user disconnects the USB cable from the computer, the WIA service calls the [**IWiaMiniDrv::drvNotifyPnpEvent**](https://msdn.microsoft.com/library/windows/hardware/ff544998) method with a WIA\_EVENT\_DEVICE\_DISCONNECTED event. See [Adding Interrupt Event Support](adding-interrupt-event-support.md) for an example implementation of the **IWiaMiniDrv::drvNotifyPnpEvent** method.

The WIA minidriver should not attempt to communicate with the hardware during or after this event. This event indicates that the WIA service will unload the minidriver. The next device access allowed is when the WIA service reloads the minidriver. It is recommended that the minidriver set a flag preventing all [IWiaMiniDrv](iwiaminidrv-com-interface.md) interface calls from accessing the hardware until it is reconnected.

The WIA\_EVENT\_DEVICE\_DISCONNECTED event is not always sent to the WIA minidriver. When the computer is shutting down and the WIA service is unloading WIA drivers, it does not send this event. This event should be treated as a device hardware disabling action.

 



