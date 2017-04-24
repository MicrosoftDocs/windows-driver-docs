---
title: Implicit Disassociation Operations
description: Implicit Disassociation Operations
ms.assetid: 73872583-f419-48b5-9953-84b4324d8378
keywords:
- disassociation operations WDK Native 802.11
- implicit disassociation operations WDK Native 802.11
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Implicit Disassociation Operations


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The miniport driver performs an implicit disassociation operation after the 802.11 station has successfully connected to a BSS network and one of the following occurs:

-   The miniport driver performs an association operation by reassociating with the same AP or peer station.

-   The miniport driver performs an association operation with another AP during a roaming operation.

    For more information about the roaming operation, see [Roaming Operations](roaming-operations.md).

In all situations, the operating system assumes that the 802.11 station is implicitly disassociated from the AP or peer station when the miniport driver makes the [NDIS\_STATUS\_DOT11\_ASSOCIATION\_START](https://msdn.microsoft.com/library/windows/hardware/ff567321) indication during the start of the association operation. For more information about the association operation, see [Association Operations](association-operations.md).

Whenever the 802.11 station implicitly disassociates from an AP or peer station, the miniport driver must not make the [NDIS\_STATUS\_DOT11\_DISASSOCIATION](https://msdn.microsoft.com/library/windows/hardware/ff567334) indication.

If the authentication algorithm that was used on the association requires port authorization for network access, the operating system deletes the port used for network access following the implicit disassociation. For more information about this process, see [Port-Based Network Access](port-based-network-access.md).

 

 





