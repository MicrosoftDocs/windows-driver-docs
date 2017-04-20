---
title: Shared Key Authentication
description: Shared Key Authentication
ms.assetid: 7db377df-aff3-4a4a-8d31-4faff642820f
keywords:
- authentication WDK Native 802.11 , shared key
- shared key authentication WDK Native 802.11
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Shared Key Authentication


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The Shared Key authentication algorithm is specified in Clause 11.2.3.3 of the IEEE 802.11-2012 standard. Because this authentication algorithm makes use of the WEP cipher algorithm, it is required for both infrastructure and independent basic service set (BSS) network types only if the 802.11 station supports WEP.

When configured for Shared Key authentication, the 802.11 station must authenticate with an access point (AP) in an infrastructure BSS or peer station in an independent BSS (IBSS) by using the protocol defined for the Shared Key authentication algorithm.

**Note**  IBSS (Ad hoc) and SoftAP are deprecated. Starting with Windows 8.1 and Windows Server 2012 R2, use [Wi-Fi Direct](wi-fi-direct-miniport-initialization-and-configuration.md).

 

If the miniport driver is operating in Extensible Station (ExtSTA) mode, it must be configured in the following way in order to use the Shared Key authentication algorithm:

-   The Shared Key authentication algorithm must be enabled through a set of [OID\_DOT11\_ENABLED\_AUTHENTICATION\_ALGORITHM](https://msdn.microsoft.com/library/windows/hardware/ff569356).

-   The WEP cipher algorithm must be enabled through a set of [OID\_DOT11\_ENABLED\_UNICAST\_CIPHER\_ALGORITHM](https://msdn.microsoft.com/library/windows/hardware/ff569358).

-   A cipher key, used by the WEP cipher for some of the frames exchanged during this sequence, must be configured through a set of [OID\_DOT11\_CIPHER\_DEFAULT\_KEY](https://msdn.microsoft.com/library/windows/hardware/ff569119) and [OID\_DOT11\_CIPHER\_DEFAULT\_KEY\_ID](https://msdn.microsoft.com/library/windows/hardware/ff569120).

 

 





