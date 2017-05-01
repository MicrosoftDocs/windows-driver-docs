---
title: Specifying Virtual WiFi Bus Dependencies
description: Specifying Virtual WiFi Bus Dependencies
ms.assetid: e6768302-b8f0-4346-993c-54358dea9242
keywords:
- Virtual WiFi in kernel mode WDK networking , INF file dependencies
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Specifying Virtual WiFi Bus Dependencies


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The INF file for an 802.11 miniport driver that supports Virtual WiFi must declare its dependency on the Virtual WiFi Bus. To do this, the INF file must use the **Include** and **Needs** INF entries to import specifications for the Virtual WiFi Bus from *Netvwifibus.inf*. Starting with NDIS 6.20 (Windows 7), this INF file is included in the default installation of Windows.

Within the INF file for a 802.11 miniport driver, the **Include** and **Needs** INF entries must be specified in the Ndi keys of the INF file for all Plug and Play (PnP) identifiers that support Virtual WiFi.

The following is an example of how these INF entries would be specified within the INF file.

``` syntax
[model.ndi.NT$ARCH$]
Include=netvwifibus.inf
Needs=VWiFiBus.CopyFiles

[model.ndi.NT$ARCH$.Services]
Include=netvwifibus.inf
Needs=VWiFiBus.Services
 
[model.ndi.NT$ARCH$.HW]
Include=netvwifibus.inf
Needs=VWiFiBus.PnPFilterRegistration
```

For more information about the Ndi key, see [Creating the Ndi Key](add-registry-sections-in-a-network-inf-file.md#ddk-creating-the-ndi-key-ng).

For more information about the structure of a network INF file, see [Sections in a Network INF File](sections-in-a-network-inf-file.md).

 

 





