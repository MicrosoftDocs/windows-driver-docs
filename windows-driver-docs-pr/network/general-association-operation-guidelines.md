---
title: General Association Operation Guidelines
description: General Association Operation Guidelines
ms.assetid: 1b5cc8ef-6273-4442-b19c-6718e7929dfb
keywords:
- association operations WDK Native 802.11
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# General Association Operation Guidelines


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

Before performing the association operation, the 802.11 station must select a candidate access point (AP) (if operating in an infrastructure basic service set (BSS) network) or peer station (if operating in an independent BSS (IBSS) network) from the BSS network candidate list. If the 802.11 station has connected to an IBSS network, it can associate with a peer station that is joining the network if it matches the criteria described in [BSS Network Candidate List](bss-network-candidate-list.md).

**Note**  IBSS (Ad hoc) and SoftAP are deprecated. Starting with Windows 8.1 and Windows Server 2012 R2, use [Wi-Fi Direct](wi-fi-direct-miniport-initialization-and-configuration.md).

 

When performing the association operation, the miniport driver and 802.11 station must follow these guidelines regardless of the type of BSS network the station is configured for:

1.  The miniport driver must ensure that it has the resources available in order to make the media-specific indications required for the association operation. The miniport driver makes the following indications during the association operation:
    -   [NDIS\_STATUS\_DOT11\_ASSOCIATION\_START](https://msdn.microsoft.com/library/windows/hardware/ff567321)
    -   [NDIS\_STATUS\_DOT11\_ASSOCIATION\_COMPLETION](https://msdn.microsoft.com/library/windows/hardware/ff567319)

2.  Before the 802.11 station attempts to associate with either an AP or a peer station, the miniport driver make an [NDIS\_STATUS\_DOT11\_ASSOCIATION\_START](https://msdn.microsoft.com/library/windows/hardware/ff567321) indication. When it makes this indication, the miniport driver provides information about the AP or peer station it is attempting to associate with, such as the media access control (MAC) address of the AP or peer station.

3.  After the miniport driver makes the [NDIS\_STATUS\_DOT11\_ASSOCIATION\_START](https://msdn.microsoft.com/library/windows/hardware/ff567321) indication, the 802.11 station performs the association operation with the AP or peer station. The association operation can be, but is not limited to, the 802.11 authentication services (as specified in Clause 11.2 of the IEEE 802.11-2012 standard and Clause 8 of the 802.11i-2004 standard) and 802.11 association procedures (as specified in Clause 10.3 of the IEEE 802.11-2012 standard).

    **Note**  The method that is used by the 802.11 station for associating to peer stations within an IBSS network is specific to the implementation by the IHV.

     

    **Note**  IBSS (Ad hoc) and SoftAP are deprecated. Starting with Windows 8.1 and Windows Server 2012 R2, use [Wi-Fi Direct](wi-fi-direct-miniport-initialization-and-configuration.md).

     

4.  If configured for operations within an infrastructure network, the miniport driver must perform the association operation by following the guidelines described in [Association Operation Guidelines for Infrastructure BSS Networks](association-operation-guidelines-for-infrastructure-bss-networks.md).

    If configured for operations within an IBSS network, the miniport driver must perform the association operation by following the guidelines described in [Association Operation Guidelines for Independent BSS Networks](association-operation-guidelines-for-independent-bss-networks.md).

    **Note**  IBSS (Ad hoc) and SoftAP are deprecated. Starting with Windows 8.1 and Windows Server 2012 R2, use [Wi-Fi Direct](wi-fi-direct-miniport-initialization-and-configuration.md).

     

5.  After the association operation is completed, the miniport driver make an [NDIS\_STATUS\_DOT11\_ASSOCIATION\_COMPLETION](https://msdn.microsoft.com/library/windows/hardware/ff567319) indication. The miniport driver provides information about the results of the association operation through this indication, such as:
    -   The status of the association operation.
    -   802.11 Association Request and Association Response frames sent or received during the operation.
    -   The last 802.11 Beacon frame received from the AP or peer station with which the 802.11 station associated.
    -   The authentication and cipher algorithms to be used on the BSS network as negotiated through the association operation.

The miniport driver successfully completes the association operation whenever any of the following happens:

-   The 802.11 station has successfully associated with an AP in an infrastructure BSS network.

-   The 802.11 station has successfully associated with at least one peer station in an IBSS network.

    **Note**  IBSS (Ad hoc) and SoftAP are deprecated. Starting with Windows 8.1 and Windows Server 2012 R2, use [Wi-Fi Direct](wi-fi-direct-miniport-initialization-and-configuration.md).

     

**Note**  If the 802.11 station successfully associates with an AP or peer station, the miniport driver must not make a status indication of NDIS\_STATUS\_MEDIA\_CONNECT.

 

The miniport driver fails the association operation whenever any of the following happens:

-   The 802.11 station has failed to associate with the AP or peer station.

-   All of the PHYs on the 802.11 station have been turned off during the association operation. For example, a PHY can be turned off through a set request of [OID\_DOT11\_NIC\_POWER\_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569392).

-   The operating system makes a method request of [OID\_DOT11\_RESET\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409) or a set request of [OID\_DOT11\_NIC\_POWER\_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569392).

If the authentication algorithm that is used on the association requires port authorization for network access, the operating system creates and authorizes a port after the association operation has completed successfully. For more information about this process, see [Port-Based Network Access](port-based-network-access.md).

Beginning with Windows 7, if the 802.11 station discovers an AP that matches the configured wireless network profile, the station must complete association with the AP and report association success to the operating system within 10 seconds. If the station does not complete the association within 10 seconds, the operating system will reset the miniport driver and will attempt to connect to the next [wireless network profile](network-profile-overview.md), if available.

 

 





