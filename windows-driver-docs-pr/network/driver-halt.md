---
title: Native 802.11 Miniport Driver Halt
description: Native 802.11 Miniport Driver Halt
ms.assetid: 74cac3e5-0219-4c5b-b1c0-5aab043ab329
keywords: ["Native 802.11 miniport drivers WDK networking , halt operations", "miniport drivers WDK Native 802.11 , halt operations", "halting miniport drivers WDK Native 802.11", "stopping Native 802.11 miniport drivers"]
---

# Native 802.11 Miniport Driver Halt


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

For the most part, Native 802.11 miniport drivers follow the same guidelines for [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) as other NDIS miniport drivers. For more information about these guidelines, see [Halting a Miniport Adapter](halting-a-miniport-adapter.md).

In addition, the 802.11 station must do the following when the driver's [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) function is called:

-   If the 802.11 station is connected to a basic service set (BSS) network, it is recommended that the 802.11 station disconnect from the BSS before the driver returns from [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388).

-   The 802.11 station must turn off all radios on the NIC.

    After the radios are turned off, the 802.11 station must not turn the radios on until the driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function is called.

## Related topics


[Adapter States of a Miniport Driver](adapter-states-of-a-miniport-driver.md)

[Miniport Adapter States and Operations](miniport-adapter-states-and-operations.md)

[Native 802.11 Reset, Halt, and Shutdown Operations](native-802-11-reset--halt-and-shutdown-operations.md)

 

 






