---
title: Native 802.11 Operational MIB objects
description: This section describes Native 802.11 Operational MIB objects
keywords: ["Native 802.11 Operational MIB objects", "Native 802.11 WLAN Operational MIB objects", "WDK Native 802.11 Operational MIB objects"]
ms.assetid: 6757B4C4-FC4E-476D-9F9E-A654A5609283
ms.author: windowsdriverdev
ms.date: 04/25/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Native 802.11 Operational MIB objects

>[!IMPORTANT]
> The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

Some of the Native 802.11 Operational object identifiers (OIDs) are used to reference Native 802.11 Operational management information base (MIB) objects.

The following table lists the Native 802.11 Operational OID name and the corresponding Native 802.11 Operational MIB object name. For more information about a Native 802.11 Operational MIB object, refer to the topic for the specific Native 802.11 Operational OID.

| Native 802.11 Operational OID name | Native 802.11 Operational MIB object name |
| --- | --- |
| [OID_DOT11_NIC_POWER_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569392) | msDot11NICPowerState |
| [OID_DOT11_SUPPORTED_PHY_TYPES](https://msdn.microsoft.com/library/windows/hardware/ff569426) | msDot11SupportedPhyTypes |

Unless a Native 802.11 Operational MIB object defines a specific default value, the Native 802.11 miniport driver defines its own default value for the MIB object.

>[!NOTE]
> When the miniport driver receives an [OID_DOT11_RESET_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409) method request, the miniport driver must reset a Native 802.11 Operational MIB object to its default value under the following conditions:
   - When MIB values for the MAC and/or PHY are reset to their default values only if **bSetDefaultMIB** is set to **TRUE**. 
   - When MAC or PHY values are affected by the value of the **dot11ResetType** member. 
> For more information, refer to the topic for the specific Native 802.11 Operational OID.

