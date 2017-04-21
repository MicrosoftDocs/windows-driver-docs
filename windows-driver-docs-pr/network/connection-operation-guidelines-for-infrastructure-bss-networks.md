---
title: Connection Operation Guidelines for Infrastructure BSS Networks
description: Connection Operation Guidelines for Infrastructure BSS Networks
ms.assetid: e5fd785f-044e-4981-9843-c3b67109331d
keywords:
- infrastructure BSS networks WDK Native 802.11
- BSS networks WDK Native 802.11
- connections WDK Native 802.11 network operations
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Connection Operation Guidelines for Infrastructure BSS Networks


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

When connecting to an infrastructure basic service set (BSS) network, the miniport driver and 802.11 station must follow the general guidelines defined in [General Connection Operation Guidelines](general-connection-operation-guidelines.md).

In addition, the miniport driver and 802.11 station must follow these guidelines for connection operations to an infrastructure BSS network:

-   The miniport driver initiates an association operation with access points (APs) from the candidate list of BSS networks. For more information about the candidate list, see [BSS Network Candidate List](bss-network-candidate-list.md).

    The miniport driver must enclose the association operation between [NDIS\_STATUS\_DOT11\_ASSOCIATION\_START](https://msdn.microsoft.com/library/windows/hardware/ff567321) and [NDIS\_STATUS\_DOT11\_ASSOCIATION\_COMPLETION](https://msdn.microsoft.com/library/windows/hardware/ff567319) indications. For more information about the association operation, see [Association Operations](association-operations.md).

-   If the 802.11 station fails to associate with one AP, it must attempt to associate with the next AP within the candidate list. If the 802.11 station has run out of APs from the candidate list with which to associate, the miniport driver must fail the connection operation.

-   The 802.11 station must successfully associate with no more than one AP during the connection operation. The miniport driver must complete the connection operation after the 802.11 station successfully associates with an AP within the infrastructure BSS network.

The following figure shows the sequence of events when the 802.11 station attempts to successfully associate with an AP in an infrastructure network during the connection operation.

![diagram illustrating an 802.11 station attempting to associate with an ap in an infrastructure network during the connection operation](images/native-802-11-connect-ess.png)

 

 





