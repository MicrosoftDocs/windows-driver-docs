---
title: Native 802.11 Miniport Driver Registration
description: Native 802.11 Miniport Driver Registration
ms.assetid: bb05b936-0344-4e1d-93b6-83a893a8b99d
keywords:
- Native 802.11 miniport drivers WDK networking , registration
- miniport drivers WDK Native 802.11 , registration
- registering miniport drivers
- registering Native 802.11 miniport drivers
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Native 802.11 Miniport Driver Registration


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

After the miniport driver returns from its [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function, the operating system will register the miniport driver as a Native 802.11 device by completing the following steps:

-   A query request of [OID\_GEN\_MEDIA\_SUPPORTED](https://msdn.microsoft.com/library/windows/hardware/ff569609) is made to determine the network media that is supported by the miniport driver. If the driver does not return a value of **NdisMediumNative802\_11**, the operating system will not register the driver as a Native 802.11 device.

-   A set request of [OID\_DOT11\_CURRENT\_OPERATION\_MODE](https://msdn.microsoft.com/library/windows/hardware/ff569132) is made to initialize the driver's operation mode.

-   A method request of [OID\_DOT11\_RESET\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409) is made to reset the 802.11 station's media access control (MAC) and PHY layers, as well as initialize the cipher and authentication algorithms. At this stage, the 802.11 station is in a known state, and the operating system will configure the station further based on the parameters from a network profile selected by the user.

If any of these steps fail, the operating system will not register the miniport driver as a Native 802.11 device and will not issue requests to the driver for Native 802.11 operations.

 

 





