---
title: Network Profile Management
description: Network Profile Management
ms.assetid: 8f430502-e436-40c2-a993-c4f1e737076a
keywords:
- IHV Extensions DLL WDK Native 802.11 , network profiles
- network profiles WDK Native 802.11 IHV Extensions DLL
- Native 802.11 IHV Extensions DLL WDK , network profiles
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Network Profile Management


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

This section discusses the management and processing of network profiles by the IHV Extensions DLL. Network profiles define the attributes for the connection operation to a basic service (BSS) network.

The IHV Extensions DLL is responsible for verifying or creating proprietary extensions to a network profile. These extensions are XML data fragments, with each fragment declared within an **IHV** element of the Native 802.11 XML schema. The data within the &lt;IHV&gt; and &lt;/IHV&gt; tags of the **IHV** element is in a format defined by the IHV. For more information about the Native 802.11 XML schema, refer to the Microsoft Windows SDK documentation.

This section includes the following topics:

[Network Profile Overview](network-profile-overview.md)

[Creating Network Profile Extensions](creating-network-profile-extensions.md)

[Validating Network Profile Extensions](validating-network-profile-extensions.md)

 

 





