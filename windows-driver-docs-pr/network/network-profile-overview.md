---
title: Network Profile Overview
description: Network Profile Overview
keywords:
- network profiles WDK Native 802.11 IHV Extensions DLL , about network profiles
- XML fragments WDK Native 802.11 IHV Extensions DLL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Network Profile Overview




 

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

    For the WLAN adapter that is managed by the IHV Extensions DLL, the DLL is responsible for the security algorithms, such as the Robust Security Network Association ( [RSNA](/previous-versions/windows/hardware/wireless/rsna-overview)) authentication algorithm or the [AES-CCMP](/previous-versions/windows/hardware/wireless/aes-ccmp) cipher algorithm. The operating system is no longer responsible. In this situation, the IHV Extensions DLL can either process the algorithms or provide proprietary methods for offloading the processing to the WLAN adapter.

-   Proprietary security settings.

    The IHV Extensions DLL can provide support for security algorithms not supported by the operating system, such as non-standard or proprietary algorithms. The DLL is responsible for processing the algorithms or provide proprietary methods for offloading the processing to the WLAN adapter.

For more information about the Native 802.11 XML schema, refer to the Microsoft Windows SDK documentation.

 

 
