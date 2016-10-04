---
title: Privacy Exemption Lists
description: Privacy Exemption Lists
ms.assetid: 0a9c5eea-1559-4ba9-86cd-8c7692502b40
keywords: ["privacy exemptions WDK Native 802.11", "exemptions WDK Native 802.11"]
---

# Privacy Exemption Lists


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

If an operating system enables cipher operations on the 802.11 station, the operating system can download a list of privacy exemptions to the station through a set of [OID\_DOT11\_PRIVACY\_EXEMPTION\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569404).

A privacy exemption defines an action performed by the 802.11 station when decrypting received 802.11 packets. Privacy exemptions are specific to the EtherType and the address type (unicast and/or multicast) of the packet. The following exemption actions are defined:

<a href="" id="dot11-exempt-always"></a>DOT11\_EXEMPT\_ALWAYS  
The 802.11 station must discard the received packet if the Protected subfield of the Frame Control field in the 802.11 MAC header is set to one.

<a href="" id="dot11-exempt-on-key-unavailable"></a>DOT11\_EXEMPT\_ON\_KEY\_UNAVAILABLE  
The 802.11 station must discard the received packet if a cipher key (or key-mapping key for the source MAC address) is available and the Protected subfield of the Frame Control field in the 802.11 MAC header is set to zero.

**Note**  If the miniport driver is enabled for raw packet indications, the driver must still indicate every media access control (MAC) protocol data unit (MPDU) fragment of the exempted packet. For more information about raw packet indications, see [Indicating Raw 802.11 Packets](indicating-raw-802-11-packets.md).

 

**Note**  When operating in safe-mode, miniport drivers should not perform filtering based on the privacy exemption list.

 

 

 





