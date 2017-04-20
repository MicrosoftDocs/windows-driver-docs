---
title: WIA Minidriver Interfaces
author: windows-driver-content
description: WIA Minidriver Interfaces
ms.assetid: 6d069584-f9e1-4312-b8f2-1ef3d518faeb
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WIA Minidriver Interfaces


## <a href="" id="ddk-wia-minidriver-interfaces-si"></a>


The WIA minidriver is a COM object that implements the standard **IUnknown** COM interface (which is described in the Microsoft Windows SDK documentation) and two additional WIA-specific interfaces: [IStiUSD](istiusd-com-interface.md) and [IWiaMiniDrv](https://msdn.microsoft.com/library/windows/hardware/ff545027).

### IStiUSD Interface

The **IStiUSD** interface, which is defined in *Stiusd.h*, performs the following actions:

-   Initializes the driver when the WIA service first loads it.

-   Returns the driver's capabilities to the WIA service, reporting whether the device supports asynchronous device notifications.

-   Locks and unlocks the device for exclusive use.

### IWiaMiniDrv Interface

The **IWiaMiniDrv** interface, which is defined in *Wiamindr.h*, exposes most of the WIA minidriver's functionality. This interface performs the following actions:

-   Defines the still image device's default and current settings.

-   Defines the still image device's supported commands and events.

-   Transfers data from the device to the WIA service (which ultimately passes it on to the calling application).

For more information about these interfaces, see [Developing a WIA Driver: Basic Concepts](developing-a-wia-driver--basic-concepts.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Minidriver%20Interfaces%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


