---
title: Extensible Station Requirements for Cipher Key Types
description: Extensible Station Requirements for Cipher Key Types
ms.assetid: 03e9f8fb-4852-4f87-85ea-32b9bb5dd0ab
keywords:
- cipher operations WDK Native 802.11 , cipher keys
- cipher keys WDK Native 802.11
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Extensible Station Requirements for Cipher Key Types


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

When the miniport driver is operating in Extensible Station (ExtSTA) mode, the 802.11 station must support four or more default cipher keys. For more information about this type of cipher key, see [Default Keys](default-keys.md).

It is recommended that the 802.11 station support the following cipher key types:

-   32 or more key-mapping keys. For more information about this type of cipher key, see [Key-Mapping Keys](key-mapping-keys.md).

-   32 or more per-station (STA) default keys. For more information about this type of cipher key, see [Per-Station Default Keys](per-station-default-keys.md).

For the TKIP and AES-CCMP cipher algorithms, each cipher key must have a length of 128 bits.

For the WEP cipher suite, the 802.11 station can support one or more of the following WEP algorithms (as defined through the [**DOT11\_CIPHER\_ALGORITHM**](https://msdn.microsoft.com/library/windows/hardware/ff547672) enumeration):

<a href="" id="dot11-cipher-algo-wep40"></a>**DOT11\_CIPHER\_ALGO\_WEP40**  
The WEP algorithm that uses a 40-bit cipher key.

<a href="" id="dot11-cipher-algo-wep104"></a>**DOT11\_CIPHER\_ALGO\_WEP104**  
The WEP algorithm that uses a 104-bit cipher key.

<a href="" id="dot11-cipher-algo-wep"></a>**DOT11\_CIPHER\_ALGO\_WEP**  
The WEP algorithm that uses a cipher key of any length.

When operating in ExtSTA mode, the miniport driver specifies the following when queried by [OID\_DOT11\_EXTSTA\_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/ff569366):

-   The maximum number of entries within the default key, key-mapping key, and per-STA default key tables.

-   The maximum length of WEP keys supported by the 802.11 station.

 

 





