---
title: Guidelines for Native 802.11 ExtSTA receive operations
description: Guidelines for Native 802.11 Extensible Station Receive Operations
ms.assetid: 08cc06c7-822d-4d1b-b4a3-e43f424425e8
keywords:
- Extensible Station receive operations WDK Native 802.11
- ExtSTA receive operations WDK Native 802.11
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Guidelines for Native 802.11 Extensible Station Receive Operations


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

This section describes the guidelines for receive operations performed by a Native 802.11 miniport driver operating in Extensible Station (ExtSTA) mode. For more information about this operation mode, see [Extensible Station Operation Mode](extensible-station-operation-mode.md).

When performing a receive operation, the 802.11 station and miniport driver must follow these guidelines.

-   If the 802.11 station supports and enables multiple PHYs for the current basic service set (BSS) network connection, the station must detect and discard duplicate media access control (MAC) protocol data unit (MPDU) fragments received by more than one PHY.

-   If the 802.11 station supports IEEE 802.1p packet prioritization or 802.1Q virtual LAN (VLAN), the station must remove the 802.1Q/p tag header after the 802.11 MAC and IEEE LLC/SNAP headers. The miniport driver returns its support for 802.1Q/p when queried by [OID\_GEN\_MAC\_OPTIONS](https://msdn.microsoft.com/library/windows/hardware/ff569597).

    The miniport driver must return the 802.1Q/p tag header through the [**NDIS\_NET\_BUFFER\_LIST\_8021Q\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff566565) structure associated with the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure used for the received packet. The miniport driver accesses the NDIS\_NET\_BUFFER\_LIST\_8021Q\_INFO structure by calling the [**NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff568401) macro with the **Ieee8021QNetBufferListInfo** identifier.

    For more information about the 802.1Q/p tag header, refer to Clause 9 of the IEEE 802.1Q-1998 standard.

-   If the 802.11 station supports wireless Quality of Service (QoS) extensions not supported by the operating system, the station must remove any QoS extensions from the MAC header and payload data. The miniport driver must return the appropriate IEEE 802.1D priority value through the [**NDIS\_NET\_BUFFER\_LIST\_8021Q\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff566565) structure that is associated with the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure used for the received packet.

    **Note**  The Windows Vista operating system does not support the wireless QoS extensions defined in either the IEEE 802.11e-2005 standard or Wireless Multimedia (WMM) specification (IEEE Document 802.11-03-504r7). However, the operating system will process the QoS Control field in the IEEE MAC header. In this situation, the miniport driver can either retain or remove the QoS Control field before indicating the received packet. The driver must still return the appropriate 802.1D priority value through the [**NDIS\_NET\_BUFFER\_LIST\_8021Q\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff566565) structure. For more information about QoS support, see [IEEE 802.11e/WMM Support](ieee-802-11e-wmm-support.md).

     

-   The 802.11 station must receive 802.11 packets that match the following conditions:
    -   The destination address (DA) in the 802.11 MAC header matches either the 802.11 station's MAC address or an entry within the station's multicast address table. For more information about the multicast address table, see [OID\_DOT11\_MULTICAST\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569388).
    -   If connected to a BSS network, the BSS Identifier (BSSID) address in the 802.11 MAC header matches the BSSID of the network. If not connected to a BSS network, the 802.11 station must receive 802.11 packets with any BSSID address.
-   The 802.11 station must not filter received packets based on the From DS or To DS subfields of the Frame Control field within the 802.11 MAC header. For more information about these subfields, refer to Clause 8.2.4.1 of the IEEE 802.11-2012 standard.

-   If the packet is received with a DA that matches either the 802.11 station's MAC address or an entry within the station's multicast address table, the 802.11 station must do the following:
    -   If the packet is received with an encrypted payload, the 802.11 station must discard the packet if any of the following are true:
        -   A cipher key is not available to decrypt the packet.
        -   The packet payload data fails to decrypt successfully.
        -   The packet payload data fails the message integrity code (MIC) verification. If the TKIP cipher algorithm is enabled, the miniport driver must perform the actions defined in [TKIP Countermeasures](tkip-countermeasures.md).
        -   The packet fails the replay mechanism defined for the cipher algorithm.
        -   A privacy exemption is defined for the packet's EtherType that specifies an action of DOT11\_EXEMPT\_ALWAYS. For more information about privacy exemptions, see [Privacy Exemption Lists](privacy-exemption-lists.md).
    -   If the packet is received with an unencrypted payload, the 802.11 station must discard the packet if any of the following are true:
        -   A cipher key is available to decrypt the packet and a privacy exemption is defined for the packet's EtherType that specifies an action of DOT11\_EXEMPT\_ON\_KEY\_UNAVAILABLE. For more information about privacy exemptions, see [Privacy Exemption Lists](privacy-exemption-lists.md).
        -   The IEEE 802.11 **dot11ExcludeUnencrypted** management information base (MIB) object is set to **TRUE**. For more information about this MIB object, see [OID\_DOT11\_EXCLUDE\_UNENCRYPTED](https://msdn.microsoft.com/library/windows/hardware/ff569365).
-   The miniport driver must increment the appropriate MAC and PHY statistical counters for all MPDU fragments and MSDU/MPPDU packets either received successfully or discarded by the 802.11 station. For more information about these statistical counters, see [OID\_DOT11\_STATISTICS](https://msdn.microsoft.com/library/windows/hardware/ff569420).

 

 





