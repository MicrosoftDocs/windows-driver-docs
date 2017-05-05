---
title: Native 802.11 Operation Modes
description: Native 802.11 Operation Modes
ms.assetid: 68b188c1-740f-426c-8ee5-5a605dc77565
keywords:
- Native 802.11 miniport drivers WDK networking , operation modes
- miniport drivers WDK Native 802.11 , operation modes
- operation modes WDK Native 802.11
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Native 802.11 Operation Modes


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

A miniport driver can support any number of the Native 802.11 operation modes. The operating system queries the driver for the operation modes it supports through [OID\_DOT11\_OPERATION\_MODE\_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/ff569396). The operating system will never switch the NIC to an operation mode that the NIC does not support.

The operating system sets or queries the current operation mode on the miniport driver through [OID\_DOT11\_CURRENT\_OPERATION\_MODE](https://msdn.microsoft.com/library/windows/hardware/ff569132). When the NIC's 802.11 medium access controller (MAC) switches to a new operation mode, it must reload its factory default settings for the new operation mode.

In Windows Vista, a miniport driver can support only one 802.11 MAC. Beginning with Windows 7, if the miniport driver implements [Virtual WiFi](virtual-wifi-in-kernel-mode.md), it can support multiple 802.11 MACs. Each MAC can operate in a separate operation mode.

The following topics describe the Native 802.11 operation modes.

[Extensible Access Point (ExtAP) Operation Mode](extensible-access-point-operation-mode.md)

[Extensible Station (ExtSTA) Operation Mode](extensible-station-operation-mode.md)

[Network Monitor (NetMon) Operation Mode](network-monitor-operation-mode.md)

For information about the operating states for each of these operation modes, see [Native 802.11 Operating States](native-802-11-operating-states.md).

 

 





