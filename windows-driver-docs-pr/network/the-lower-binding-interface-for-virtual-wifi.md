---
title: The Lower Binding Interface for Virtual WiFi
description: The Lower Binding Interface for Virtual WiFi
ms.assetid: cf01a80e-07d7-496e-b36f-f8a8b29778cf
keywords:
- Virtual WiFi in kernel mode WDK networking , lower binding interface
- Virtual WiFi in kernel mode WDK networking , vwifi lower binding interface
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# The Lower Binding Interface for Virtual WiFi


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

Virtual WiFi introduces a new lower binding interface called "vwifi". An 802.11 miniport driver that supports Virtual WiFi must use this value in the **LowerRange** entry of its **Ndi\\Interfaces** key.

The following is an example of the changes that would be made in the INF file to support the Virtual WiFi lower binding interface.

``` syntax
[sample.reg]
HKR, Ndi\Interfaces, LowerRange, 0, "wlan,ethernet,vwifi"
```

For more information about the Ndi key, see [Creating the Ndi Key](add-registry-sections-in-a-network-inf-file.md#ddk-creating-the-ndi-key-ng).

For more information about binding interfaces for network INF files, see [Specifying Binding Interfaces](specifying-binding-interfaces.md).

For more information about the structure of a network INF file, see [Sections in a Network INF File](sections-in-a-network-inf-file.md).

 

 





