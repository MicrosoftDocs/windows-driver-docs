---
title: Key-Mapping Keys
description: Key-Mapping Keys
ms.assetid: eed9effd-5c63-44ac-ab02-446f767feaea
keywords:
- cipher operations WDK Native 802.11 , cipher keys
- cipher keys WDK Native 802.11
- key-mapping keys WDK Native 802.11
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Key-Mapping Keys


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The 802.11 station uses a key-mapping key for cipher operations on all sent or received packets for which a mapping exists for the receiver's media access control (MAC) address (RA) or the transmitter's MAC address (TA). For received packets, the 802.11 station uses the TA as the index within the key-mapping key table. For transmitted packets, the station uses the RA as the index. The 802.11 station uses a single key for each RA/TA mapping.

It is recommended that the 802.11 station support a key mapping table that stores a minimum of 32 keys. If the miniport driver supports the Extensible Station (ExtSTA) mode, the 802.11 station can support a key-mapping table size of 32 or greater.

The miniport driver, when operating in ExtSTA mode, reports the size of the 802.11 station's key-mapping key table when [OID\_DOT11\_EXTSTA\_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/ff569366) is queried.

For more information about the usage of key-mapping keys, refer to Clause 11.2.2.3 of the IEEE 802.11-2012 standard.

 

 





