---
title: Encryption Guidelines
description: Encryption Guidelines
ms.assetid: 35ca791e-cbd8-4e87-a101-b091a0a3d57a
keywords:
- cipher operations WDK Native 802.11 , encryption
- encryption WDK Native 802.11
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Encryption Guidelines


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

When encrypting a media access control (MAC) service data unit (MSDU) packet before transmitting it, the 802.11 station follows these guidelines when selecting the cipher key:

-   For a unicast packet, the 802.11 station selects the key as follows:
    -   If the receiver's MAC address is found in the key-mapping key table, the 802.11 station must use the key-mapping key associated with the MAC address for the cipher algorithm.
    -   If the receiver's MAC address is not found in the key-mapping key table, the 802.11 station must use the key, indexed by the default key identifier (ID), from the default key table. For more information about the default key ID, see [OID\_DOT11\_CIPHER\_DEFAULT\_KEY\_ID](https://msdn.microsoft.com/library/windows/hardware/ff569120).
-   For a broadcast or multicast packet, the 802.11 station must use the key, indexed by the default key identifier (ID), from the default key table.

 

 





