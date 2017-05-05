---
title: Supported Virtualization Configurations
description: Supported Virtualization Configurations
ms.assetid: d350de1e-433c-4b1d-ba48-762799ba2fe1
keywords:
- Virtual WiFi in kernel mode WDK networking , configurations
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supported Virtualization Configurations


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

In NDIS 6.30 (Windows 8) and later, the operating system supports the same virtualization configurations in Native 802.11 WiFi as those that are outlined in [Wi-Fi Direct Miniport Initialization and Configuration](wi-fi-direct-miniport-initialization-and-configuration.md).

In NDIS 6.20 (Windows 7), the operating system supports only the following virtualization configurations, even if the 802.11 miniport driver might be capable of supporting more configurations.

-   A maximum of three MAC entities can operate simultaneously on one wireless interface.

-   The combinations of MAC entities are limited to one of the following:
    Infrastructure Station and Software Access Point
    Infrastructure Station, Software Access Point, and Virtual Station
-   The operating system will not ask the miniport driver to be put into a [Network Monitor Operation Mode](network-monitor-operation-mode.md), a FIPS Mode, or an Adhoc connection while the miniport has a Software Access Point running. Similarly, the operating system will not attempt to start a Software Access Point while one of these incompatible connections is in progress.

    **Note**  IBSS (Ad hoc) and SoftAP are deprecated. Starting with Windows 8.1 and Windows Server 2012 R2, use [Wi-Fi Direct](wi-fi-direct-miniport-initialization-and-configuration.md).

     

-   In NDIS 6.20 (Windows 7), the default port (port 0) will not transition to the Extensible Access Point (ExtAP) or to the Virtual Station (VSTA) MAC.

 

 





