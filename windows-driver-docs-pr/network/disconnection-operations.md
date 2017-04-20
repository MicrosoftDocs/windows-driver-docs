---
title: Disconnection Operations
description: Disconnection Operations
ms.assetid: f0ccdd41-3470-4602-a26b-af166e7eac82
keywords:
- network operations WDK Native 802.11 , disconnection operations
- disconnections WDK Native 802.11
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Disconnection Operations


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The miniport driver performs the disconnection operation when the following are true:

-   The 802.11 station is connected to a basic service set (BSS) network.

-   The operating system makes either a set request of [OID\_DOT11\_DISCONNECT\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569147) or method request of [OID\_DOT11\_RESET\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409).

The miniport driver must do the following when performing this operation:

-   Cancel any roaming operations and must not start new ones. For more information about canceling and starting roaming operations, see [Roaming Operations](roaming-operations.md).

-   Perform a disassociation operation with the access point (AP) or, in the case of an independent BSS (IBSS) network connection, every peer station with which it is currently associated. For more information about this operation, see [Disassociation Operations](disassociation-operations.md).

-   Transition to the initialization (INIT) operating state. For more information about this state, see [Extensible Station Operating States](extensible-station-operating-states.md).

 

 





