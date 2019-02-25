---
title: WIA Minidriver Interfaces
description: WIA Minidriver Interfaces
ms.assetid: 6d069584-f9e1-4312-b8f2-1ef3d518faeb
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Minidriver Interfaces





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

 

 




