---
title: Packet Decryption
description: Packet Decryption
ms.assetid: 20d5ce82-d43d-4836-8b60-7e8982213b0f
keywords: ["decryption WDK Native 802.11", "packet decryptions WDK Native 802.11"]
---

# Packet Decryption


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

When decrypting a received packet, the 802.11 station follows these guidelines when selecting the cipher key:

-   For a unicast packet, the 802.11 station selects the key as follows:
    -   If the transmitter's media access control (MAC) address is found in the key-mapping key table, the 802.11 station must select the key-mapping key associated with the MAC address.
    -   If the transmitter's MAC address is not found in the key-mapping key table, the 802.11 station must select the key, indexed by the value of the 802.11 Key Identifier (ID) subfield of the packet, from the default key table.
-   For a multicast or broadcast packet, the 802.11 station selects the key as follows:
    -   If the 802.11 station has connected to an independent basic service set (IBSS) network through the IEEE 802.11i Robust Security Network Association (RSNA) authentication algorithm, the station selects the key from the per-station (STA) default key table.

        **Note**  IBSS (Ad hoc) and SoftAP are deprecated. Starting with Windows 8.1 and Windows Server 2012 R2, use [Wi-Fi Direct](wi-fi-direct-miniport-initialization-and-configuration.md).

         

        The 802.11 selects the row in the per-STA default key table indexed by the transmitter's MAC address. If a row is found, the 802.11 station selects the key from the row indexed by the value of the 802.11 Key Identifier (ID) subfield of the packet. Otherwise, the 802.11 station must reject the packet.

    -   If the 802.11 station has connected to any other type of BSS network, it must select the key, indexed by the value of the 802.11 Key Identifier (ID) subfield of the packet, from the default key table.

The 802.11 station must reject the received packet under any of the following conditions:

-   The value of the 802.11 Key Identifier (ID) subfield of the packet is invalid.

-   The key, indexed by the value of the 802.11 Key Identifier (ID) subfield of the packet, is not active or has been deleted from the default key table.

-   The key, indexed by the value of the 802.11 Key Identifier (ID) subfield of the packet, is not active or has been deleted from the row, indexed by the by the transmitter's MAC address, in the per-STA default key table. This is only applicable for IBSS network connections through the IEEE 802.11i RSNA authentication algorithm.

-   The cipher algorithm fails to decrypt the packet successfully.

-   If TKIP is the cipher algorithm, the 802.11 station rejects the packet if any one of the following occur:
    -   The message integrity code (MIC) verification fails on the decrypted packet. For more information about how the miniport driver handles MIC failures, see [TKIP Countermeasures](tkip-countermeasures.md).
    -   The replay protection algorithm detects a duplicate TKIP sequence counter (TSC) value. For more information about the TKIP replay protection algorithm, refer to Clause 8.3.2.6 of the IEEE 802.11i-2004 standard.
-   If AES-CCMP is the cipher algorithm, the 802.11 station rejects the packet if the replay protection algorithm detects a duplicate packet number (PN) value. For more information about the AES-CCMP replay protection algorithm, refer to Clause 8.3.3.4.3 of the IEEE 802.11i-2004 standard.

-   The packet is rejected due to decryption exemptions. For more information about how the 802.11 station applies decryption exemptions to received packets, see [Decryption Exemptions](decryption-exemptions.md).

If the 802.11 station rejects the received packet, the miniport driver must do the following:

-   Increment the appropriate statistical counter in the DOT11\_STATISTICS structure. For example, if the MPDU frame failed decryption through the AES-CCMP cipher, the driver increments the value of the **ullCCMPDecryptErrors** member. For more information about these statistical counters, see [OID\_DOT11\_STATISTICS](https://msdn.microsoft.com/library/windows/hardware/ff569420).

-   If the miniport driver's current packet filter does not enable NDIS\_PACKET\_TYPE\_802\_11\_RAW\_DATA or NDIS\_PACKET\_TYPE\_802\_11\_RAW\_MGMT, the driver must discard the received packet and not indicate it through a call to [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598). For more information about these packet filter settings, see [OID\_GEN\_CURRENT\_PACKET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569575).

-   If the miniport driver's current packet filter enables NDIS\_PACKET\_TYPE\_802\_11\_RAW\_DATA, the driver must indicate the packet if it is an 802.11 data packet. Similarly, if the driver's current packet filter enables NDIS\_PACKET\_TYPE\_802\_11\_RAW\_MGMT, the driver must indicate the packet if it is an 802.11 management packet. In either case, the driver must indicate the unmodified packet data originally received by the 802.11 station.

    For more information about indicating raw packets, see [Indicating Raw 802.11 Packets](indicating-raw-802-11-packets.md).

 

 





