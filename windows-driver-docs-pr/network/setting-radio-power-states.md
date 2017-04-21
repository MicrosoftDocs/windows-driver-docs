---
title: Setting Radio Power States
description: Setting Radio Power States
ms.assetid: 6a159c4a-855c-476e-8a0a-db203dd4d06f
keywords:
- radio power management WDK Native 802.11 miniport
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting Radio Power States


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

Only the software setting for the NIC's radio power state can be modified. The hardware setting for the NIC's radio power state is a read-only attribute of the radio power switch (if present) on the 802.11 NIC.

The miniport driver must follow these guidelines regarding the software setting for the radio power state:

-   The software setting can only be modified through a set request of the [OID\_DOT11\_NIC\_POWER\_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569392) object identifier (OID).

-   The software setting must persist through the reset operations described in [Native 802.11 Reset, Halt and Shutdown Operations](native-802-11-reset--halt-and-shutdown-operations.md).

-   If the miniport driver is operating in ExtSTA mode, the driver changes the software setting for the current PHY identifier (ID) when [OID\_DOT11\_NIC\_POWER\_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569392) is set. The operating system sets or queries the current PHY ID through [OID\_DOT11\_CURRENT\_PHY\_ID](https://msdn.microsoft.com/library/windows/hardware/ff569135). For more information about the method used to reference PHYs within the ExtSTA operation mode, see [802.11 PHY Configuration](802-11-phy-configuration.md).

-   If the 802.11 NIC supports multiple PHYs that share a common radio on the NIC, the miniport driver cannot turn off the radio until all PHYs have been turned off through sets of [OID\_DOT11\_NIC\_POWER\_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569392).

 

 





