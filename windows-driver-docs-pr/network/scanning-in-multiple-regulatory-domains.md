---
title: Scanning in Multiple Regulatory Domains
description: Scanning in Multiple Regulatory Domains
ms.assetid: 329ca1df-3368-4dae-a1ce-3a2f3e46ba92
keywords: ["scan operations WDK Native 802.11 , multiple regulatory domains", "multiple regulatory domains WDK Native 802.11", "regulatory domain WDK Native 802.11"]
---

# Scanning in Multiple Regulatory Domains


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

If the 802.11 station supports multiple regulatory domains, the 802.11 station must follow these guidelines when performing the scan operation:

-   If the value of the IEEE 802.11 **dot11CurrentRegDomain** management information base (MIB) object is set to a value of DOT11\_REG\_DOMAIN\_OTHER, the 802.11 station determines the regulatory domain it is operating in through the IEEE 802.11d Country information element (IE) of the received 802.11 Beacon and Probe Response frames when it connects to the basic service set (BSS) network.

    While the 802.11 station is connected to the BSS network, the 802.11 station can perform an active scan on the channels that are valid for the regulatory domain used within the BSS network.

    If the 802.11 station performs a disconnection operation from the BSS network or performs a disassociation operation with an access point (AP), the 802.11 must only perform a passive scan on any channel supported by the PHY. For more information about these operations, see [Native 802.11 Network Operations](native-802-11-network-operations.md).

-   If the value of the **dot11CurrentRegDomain** MIB object is not set to a value of DOT11\_REG\_DOMAIN\_OTHER, the 802.11 station is operating within its default regulatory domain. In this situation, the 802.11 station can perform an active scan on all channels that are valid for the regulatory domain specified by the **dot11CurrentRegDomain** MIB object.

For more information about the **dot11CurrentRegDomain** MIB object, see [OID\_DOT11\_CURRENT\_REG\_DOMAIN](https://msdn.microsoft.com/library/windows/hardware/ff569136).

 

 





