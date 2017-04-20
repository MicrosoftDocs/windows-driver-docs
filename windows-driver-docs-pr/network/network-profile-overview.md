---
title: Network Profile Overview
description: Network Profile Overview
ms.assetid: b7d902db-4918-4e9f-a7e0-3bb6c5ed1dfb
keywords:
- network profiles WDK Native 802.11 IHV Extensions DLL , about network profiles
- XML fragments WDK Native 802.11 IHV Extensions DLL
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Network Profile Overview


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

A network profile defines the attributes for a connection to a basic service set (BSS) network. Network profiles consist of XML data fragments. For Windows Vista, a network profile contains the following XML fragments.

<a href="" id="profile-name--required-"></a>**Profile Name (required)**  
The name of the network profile, which is the service set identifier (SSID) of the BSS network.

<a href="" id="standard-802-11-connectivity-settings--required-"></a>**Standard 802.11 Connectivity Settings (required)**  
This XML fragment consists of standard 802.11 settings for network connectivity, such as the BSS network type (infrastructure or independent) or type of wireless LAN (WLAN) security. The operating system processes the standard connectivity settings and configures the wireless WLAN adapter with them.

<a href="" id="ihv-connectivity-extensions--optional-"></a>**IHV Connectivity Extensions (optional)**  
This XML fragment consists of the extensions to network connectivity as defined by the IHV. The operating system passes the connectivity extensions to the IHV Extensions DLL for processing. The DLL is responsible for configuring the WLAN adapter with the proprietary extensions.

<a href="" id="standard-802-11-security-settings--optional-"></a>**Standard 802.11 Security Settings (optional)**  
This XML fragment consists of the standard 802.11 authentication and cipher settings, such as the type of authentication and cipher algorithm to use on the BSS network connection. The operating system processes the standard security settings and configures the WLAN adapter with them.

<a href="" id="ihv-security-extensions--optional-"></a>**IHV Security Extensions (optional)**  
This XML fragment consists of the extensions to network security as defined by the IHV. The IHV extensions can specify either of the following:

-   Standard security settings.

    For the WLAN adapter that is managed by the IHV Extensions DLL, the DLL is responsible for the security algorithms, such as the Robust Security Network Association ( [RSNA](rsna.md)) authentication algorithm or the [AES-CCMP](aes-ccmp.md) cipher algorithm. The operating system is no longer responsible. In this situation, the IHV Extensions DLL can either process the algorithms or provide proprietary methods for offloading the processing to the WLAN adapter.

-   Proprietary security settings.

    The IHV Extensions DLL can provide support for security algorithms not supported by the operating system, such as non-standard or proprietary algorithms. The DLL is responsible for processing the algorithms or provide proprietary methods for offloading the processing to the WLAN adapter.

For more information about the Native 802.11 XML schema, refer to the Microsoft Windows SDK documentation.

 

 





