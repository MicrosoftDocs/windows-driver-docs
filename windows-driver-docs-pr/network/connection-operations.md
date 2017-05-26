---
title: Connection Operations
description: Connection Operations
ms.assetid: 55bd72d6-6667-48e1-9907-c5ff516b4664
keywords:
- network operations WDK Native 802.11 , connection operations
- connections WDK Native 802.11 network operations
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Connection Operations


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The miniport driver performs the connection operation in order to:

-   Select a basic service set (BSS) network to connect to. The miniport driver selects the BSS network based on the intersection of the 802.11 station's network configuration, such as desired BSS type and desired SSID list, and the cache of BSS networks detected during the most recent scan operation.

-   If configured to operate in an infrastructure BSS network, determine an access point (AP) with which to associate. The miniport driver prepares a list of candidate APs to associate with from the BSS network candidate list. If the 802.11 station successfully associates with an AP, the miniport driver can successfully complete the connection operation.

-   If configured to operate in an independent BSS (IBSS) network, determine a cell of one or more peer stations with which to associate. The miniport driver prepares a list of candidate peer stations to associate with from the BSS network candidate list. After the 802.11 station successfully associates with at least one peer station, the miniport driver can successfully complete the connection operation.

    When performing the connection operation, the miniport driver can be configured to start a new IBSS network if it cannot detect an existing IBSS network.

The miniport driver initiates the connection operation following a set request of [OID\_DOT11\_CONNECT\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569122). The miniport driver must be in the initialization (INIT) state of the Extensible Station (ExtSTA) operation mode when the set request is made. During the set request, the miniport driver transitions to the operational (OP) state. For more information about these states, see [Extensible Station Operating States](extensible-station-operating-states.md).

The following topics describe the connection operation in more detail:

[General Connection Operation Guidelines](general-connection-operation-guidelines.md)

[Connection Operation Guidelines for Infrastructure BSS Networks](connection-operation-guidelines-for-infrastructure-bss-networks.md)

[Connection Operation Guidelines for Independent BSS Networks](connection-operation-guidelines-for-independent-bss-networks.md)

 

 





