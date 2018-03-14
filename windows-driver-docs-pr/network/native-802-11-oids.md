---
title: Native 802.11 OIDs
description: This section describes Native 802.11 OIDs and their characteristics.
keywords: ["Native 802.11 OIDs", "Native 802.11 WLAN OIDs", "WDK Native 802.11 IDs", "Native 802.11 object identifiers"]
ms.assetid: A0B31D4B-E7E1-44B1-BE00-26B2070FE58A
ms.author: windowsdriverdev
ms.date: 04/24/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Native 802.11 OIDs

>[!IMPORTANT]
> The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

The Native 802.11 wireless LAN (WLAN) object identifiers (OIDs) are supported by versions 6.0 and later of the Network Driver Interface Specification (NDIS). Miniport drivers that support the Native 802.11 interface for IEEE 802.11 network interface cards (NICs) must support all mandatory Native 802.11 OIDs. For some OIDs, support is optional.

In addition, miniport drivers that support the Native 802.11 interface must also support the mandatory NDIS general OIDS. For more information about these OIDs, see [General OIDs](https://msdn.microsoft.com/library/windows/hardware/ff552468).

Native 802.11 OIDs are issued by the Windows operating system. Third-party drivers cannot issue them.

A user-mode application or script can query the Native 802.11 OIDs indirectly by calling Microsoft Windows Management Instrumentation (WMI) methods. For more information, see [WMI Tasks: Networking](http://msdn.microsoft.com/library/windows/desktop/aa394595). Native 802.11 OIDs cannot be set in this way.

The Native 802.11 OIDs are defined in Windot11.h. When building a driver that supports these OIDs, include Ndis.h.

The Native 802.11 OIDs are described in the following sections:

- [Native 802.11 Extensible AP OIDs](native-802-11-extensible-ap-oids.md)
- [Native 802.11 Extensible Station OIDs](native-802-11-extensible-station-oids.md)
- [Native 802.11 Network Monitor OIDs](native-802-11-network-monitor-oids.md)
- [Native 802.11 Operational OIDs](native-802-11-operational-oids.md)
- [Native 802.11 MIB OIDs](native-802-11-mib-oids.md)
- [Native 802.11 Virtual WiFi OIDs](native-802-11-virtual-wifi-oids.md)

For an overview of the terms and naming conventions used throughout this section, see [Native 802.11 OID terminology](native-802-11-oid-terminology.md).


