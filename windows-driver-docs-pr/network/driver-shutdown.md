---
title: Native 802.11 Miniport Driver Shutdown
description: Native 802.11 Miniport Driver Shutdown
ms.assetid: f64859aa-6f37-4759-b262-b5cbd0149085
keywords:
- Native 802.11 miniport drivers WDK networking , shutdown operations
- miniport drivers WDK Native 802.11 , shutdown operations
- shutdown WDK networking
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Native 802.11 Miniport Driver Shutdown


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

For the most part, Native 802.11 miniport drivers follow the same guidelines for [*MiniportShutdownEx*](https://msdn.microsoft.com/library/windows/hardware/ff559449) as other NDIS miniport drivers. For more information about these guidelines, see [Adapter Shutdown](miniport-adapter-shutdown.md).

In addition, the 802.11 station must turn off all radios on the NIC. After the radios are turned off, the 802.11 station must not turn the radios on following a system boot until the driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function is called.

## Related topics


[Adapter States of a Miniport Driver](adapter-states-of-a-miniport-driver.md)

[Miniport Adapter States and Operations](miniport-adapter-states-and-operations.md)

[Native 802.11 Reset, Halt, and Shutdown Operations](native-802-11-reset--halt-and-shutdown-operations.md)

 

 






