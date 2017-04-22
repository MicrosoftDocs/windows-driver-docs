---
title: Network Monitor Operating States
description: Network Monitor Operating States
ms.assetid: 1f9c73ed-6514-4d2d-97ca-5019b602b8d1
keywords:
- operating states WDK Native 802.11
- Network Monitor WDK Native 802.11
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Network Monitor Operating States


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

Unlike other Native 802.11 operation modes, the Network Monitor (NetMon) operation mode does not consist of a set of operating states.

After going into the NetMon operation mode following a set request of [OID\_DOT11\_CURRENT\_OPERATION\_MODE](https://msdn.microsoft.com/library/windows/hardware/ff569132), the miniport driver must configure itself and the 802.11 station to operate within the requirements defined in [Network Monitor Operation Mode](network-monitor-operation-mode.md).

 

 





