---
title: Guidelines for 802.11 Promiscuous Receive Operations
description: Guidelines for 802.11 Promiscuous Receive Operations
ms.assetid: 4d7b9178-3e3f-49d9-88ff-3194bf5b14c7
keywords: ["promiscuous receive operations WDK Native 802.11"]
---

# Guidelines for 802.11 Promiscuous Receive Operations


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The 802.11 station operates in a promiscuous mode if the current packet filter has any of the following filter settings.

<a href="" id="ndis-packet-type-promiscuous"></a>NDIS\_PACKET\_TYPE\_PROMISCUOUS  
Enables promiscuous reception of media access control (MAC) service data unit (MSDU) packets, as well as all MAC protocol data unit (MPDU) fragments associated with the MSDU packet.

<a href="" id="ndis-packet-type-802-11-promiscuous-mgmt"></a>NDIS\_PACKET\_TYPE\_802\_11\_PROMISCUOUS\_MGMT  
Enables promiscuous reception of MAC management PDU (MMPDU) packets, as well as all MPDU fragments associated with the MMPDU packet.

<a href="" id="ndis-packet-type-802-11-promiscuous-ctrl"></a>NDIS\_PACKET\_TYPE\_802\_11\_PROMISCUOUS\_CTRL  
Enable promiscuous reception of 802.11 Control frames.

For more information about these filter settings, see [OID\_GEN\_CURRENT\_PACKET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569575).

**Note**  It is only valid for the miniport driver to enable the NDIS\_PACKET\_TYPE\_PROMISCUOUS, NDIS\_PACKET\_TYPE\_802\_11\_PROMISCUOUS\_MGMT, or NDIS\_PACKET\_TYPE\_802\_11\_PROMISCUOUS\_CTRL packet filters if the driver is operating in Network Monitor (NetMon) or Extensible Access Point (AP) modes. For more information about these modes, see [Network Monitor Operation Mode](network-monitor-operation-mode.md) and [Extensible Access Point Operation Mode](extensible-access-point-operation-mode.md).

 

If the 802.11 station is enabled for promiscuous receive operations, the station and miniport driver must follow these guidelines.

-   When configured for promiscuous receive operations, the 802.11 station must be configured to receive 802.11 packets with any destination address (DA) within the 802.11 MAC header.

-   If the 802.11 station has a matching cipher key for the 802.11 packet, the station must attempt to decrypt and reassemble all MPDU fragments for the 802.11 packet.
    **Note**  If the TKIP cipher algorithm is enabled and the received packet fails during the message integrity code (MIC) verification, the miniport driver must not make an [NDIS\_STATUS\_DOT11\_TKIPMIC\_FAILURE](https://msdn.microsoft.com/library/windows/hardware/ff567368) indication unless the packet was received by the 802.11 station in a nonpromiscuous mode.

     

-   If the 802.11 station is connected to a basic service set (BSS) network, the miniport driver must indicate receive packets through calls to [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598) based on the following conditions:
    -   The miniport driver must indicate 802.11 data packets only if the BSS Identifier (BSSID) address matches the BSSID of the network.
    -   The miniport driver must indicate 802.11 control and management packets for any BSSID address.
-   If the 802.11 station is not connected to a BSS network, the miniport driver must indicate 802.11 packets for any DA or BSSID address in the 802.11 MAC header.

-   When the miniport driver is in the ExtAP INIT state, the NIC must turn off Address 1 matching and must not perform BSSID matching. BSSID matching is not applicable because the NIC has not joined or started a BSS.

 

 





