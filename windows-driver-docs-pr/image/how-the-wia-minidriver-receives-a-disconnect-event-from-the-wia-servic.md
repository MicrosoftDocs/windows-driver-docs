---
title: How WIA minidriver receives disconnect from WIA
author: windows-driver-content
description: How the WIA minidriver receives a disconnect event from the WIA service
ms.assetid: 6ae3c230-d026-469e-a699-860a295fba85
---

# How the WIA minidriver receives a disconnect event from the WIA service

When a device is surprise-disconnected from the computer, such as when the user disconnects the USB cable from the computer, the WIA service calls the [**IWiaMiniDrv::drvNotifyPnpEvent**](https://msdn.microsoft.com/library/windows/hardware/ff544998) method with a WIA\_EVENT\_DEVICE\_DISCONNECTED event. See [Adding Interrupt Event Support](adding-interrupt-event-support.md) for an example implementation of the **IWiaMiniDrv::drvNotifyPnpEvent** method.

The WIA minidriver should not attempt to communicate with the hardware during or after this event. This event indicates that the WIA service will unload the minidriver. The next device access allowed is when the WIA service reloads the minidriver. It is recommended that the minidriver set a flag preventing all [IWiaMiniDrv](iwiaminidrv-com-interface.md) interface calls from accessing the hardware until it is reconnected.

The WIA\_EVENT\_DEVICE\_DISCONNECTED event is not always sent to the WIA minidriver. When the computer is shutting down and the WIA service is unloading WIA drivers, it does not send this event. This event should be treated as a device hardware disabling action.

 

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20How%20the%20WIA%20Minidriver%20Receives%20a%20Disconnect%20Event%20from%20the%20WIA%20Service%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


