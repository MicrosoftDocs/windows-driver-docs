---
title: Native 802.11 DriverEntry Requirements
description: Native 802.11 DriverEntry Requirements
ms.assetid: 94638ca5-a4ca-480f-afee-7573877c7db9
keywords:
- DriverEntry WDK Native 802.11
- initializing Native 802.11 miniport drivers
- initializing miniport drivers
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Native 802.11 DriverEntry Requirements


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

When calling the [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654) function from its [*DriverEntry*](https://msdn.microsoft.com/library/windows/hardware/ff544113) function, the Native 802.11 driver must follow the guidelines described in [Initializing a Miniport Driver](initializing-a-miniport-driver.md). For more information about the *DriverEntry* function, see [**DriverEntry of NDIS Miniport Drivers**](https://msdn.microsoft.com/library/windows/hardware/ff548818). DriverEntry Requirements

## Related topics


[Native 802.11 DriverEntry Requirements](driverentry-requirements.md)

[Native 802.11 Miniport Driver Initialization](native-802-11-miniport-driver-initialization.md)

[Native 802.11 MiniportInitializeEx Requirements](miniportinitializeex-requirements.md)

 

 






