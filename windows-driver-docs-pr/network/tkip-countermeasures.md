---
title: TKIP Countermeasures
description: TKIP Countermeasures
ms.assetid: 9ed848eb-54b3-4bb3-a8bd-ff249c6bac29
keywords: ["decryption WDK Native 802.11", "TKIP countermeasures WDK Native 802.11", "countermeasures WDK Native 802.11"]
---

# TKIP Countermeasures


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

TKIP countermeasures are defined in the Wi-Fi Protected Access (WPA) specification and Clause 8.3.2.4 of the IEEE 802.11i-2004 standard. TKIP countermeasures are invoked following message integrity code (MIC) verification failures on received packets.

When the MIC verification fails, the miniport driver and the 802.11 station must follow these guidelines:

-   The miniport driver must make a Native 802.11 media-specific [NDIS\_STATUS\_DOT11\_TKIPMIC\_FAILURE](https://msdn.microsoft.com/library/windows/hardware/ff567368) indication.

-   If port-based authentication is managed by the operating system, the 802.11 station must not perform the TKIP countermeasures. Instead, the operating system will perform the countermeasures after the miniport driver makes two [NDIS\_STATUS\_DOT11\_TKIPMIC\_FAILURE](https://msdn.microsoft.com/library/windows/hardware/ff567368) indications within a 60-second period.

    When performing the countermeasures, the operating system issues a set request of [OID\_DOT11\_EXCLUDED\_MAC\_ADDRESS\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569364) to the miniport driver. The excluded media access control (MAC) address list will contain the MAC address of the access point (AP) with which the 802.11 station is currently associated.

    After OID\_DOT11\_EXCLUDED\_MAC\_ADDRESS\_LIST is set, the 802.11 station disassociates from the AP and does not reassociate until the operating system issues another set request of this OID to remove the AP's MAC address from the excluded MAC address list. The operating system does not remove the AP's MAC address from the excluded list for at least 60 seconds.

    **Note**  If port-based authentication is managed by the operating system, TKIP is only supported for infrastructure basic service set (BSS) networks.

     

-   If port-based authentication is managed by a service developed by the independent hardware vendor (IHV), either the IHV service or 802.11 station must perform the TKIP countermeasures. The method used for performing the countermeasures is specific to the IHV implementation.

    **Note**  If port-based authentication is managed by an IHV service, TKIP can be supported for infrastructure and independent BSS networks.

     

 

 





