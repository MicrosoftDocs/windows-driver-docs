---
title: Association Operations
description: Association Operations
ms.assetid: 04e97ea1-fe4b-471e-a7be-b5aa3ee88edc
keywords:
- network operations WDK Native 802.11 , association operations
- association operations WDK Native 802.11
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Association Operations


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The miniport driver performs an association operation when the following conditions occur:

-   The miniport driver is performing a connection operation. For more information about the connection operation, see [Connection Operations](connection-operations.md).

-   The miniport driver is performing a roaming operation. For more information about the roaming operation, see [Roaming Operations](roaming-operations.md).

-   The miniport driver is connected to an independent basic service set (IBSS) network and the 802.11 station detects a new peer station that is joining the IBSS.

    **Note**  IBSS (Ad hoc) and SoftAP are deprecated. Starting with Windows 8.1 and Windows Server 2012 R2, use [Wi-Fi Direct](wi-fi-direct-miniport-initialization-and-configuration.md).

     

The following topics describe the association operation in more detail:

[General Association Operation Guidelines](general-association-operation-guidelines.md)

[Association Operation Guidelines for Infrastructure BSS Networks](association-operation-guidelines-for-infrastructure-bss-networks.md)

[Association Operation Guidelines for Independent BSS Networks](association-operation-guidelines-for-independent-bss-networks.md)

[Association Operation Guidelines for Extensible Access Point (ExtAP) Mode](association-operation-guidelines-for-extensible-access-point--extap--m.md)

 

 





