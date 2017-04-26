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


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")