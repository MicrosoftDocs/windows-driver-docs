---
title: Default Keys
description: Default Keys
ms.assetid: 33475691-f608-445a-8bef-f4d191c4655a
keywords: ["cipher operations WDK Native 802.11 , cipher keys", "cipher keys WDK Native 802.11", "default cipher keys"]
---

# Default Keys


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The 802.11 station uses default keys for cipher operations on received multicast or broadcast packets. The station also uses default keys for cipher operations on sent or received unicast packets whenever a key mapping does not exist between the receiver's media access control (MAC) address and the transmitter's MAC address.

The 802.11 station must support a default key table that stores a minimum of four keys. If the miniport driver supports the Extensible Station (ExtSTA) mode, the 802.11 station can support a default key table size of four or greater.

The miniport driver, when operating in ExtSTA mode, reports the size of the 802.11 station's default key table when [OID\_DOT11\_EXTSTA\_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/ff569366) is queried.

For more information about the usage of default keys, refer to Clause 11.2.2.3 of the IEEE 802.11-2012 standard.

 

 





