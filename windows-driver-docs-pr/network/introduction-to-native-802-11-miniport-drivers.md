---
title: Introduction to Native 802.11 Miniport Drivers
description: Introduction to Native 802.11 Miniport Drivers
ms.assetid: 03cccb4e-fb83-4bbb-abf7-06acfe86e5b6
keywords:
- Native 802.11 miniport drivers WDK networking , about Native 802.11 miniport drivers
- miniport drivers WDK Native 802.11 , about Native 802.11 miniport drivers
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Introduction to Native 802.11 Miniport Drivers


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

Native 802.11 miniport drivers provide the access to IEEE 802.11 wireless LAN (WLAN) media and basic service set (BSS) networks. A Native 802.11 miniport driver is developed as an NDIS 6.0 or later miniport driver. Besides supporting the standard object identifiers (OIDs) required for NDIS 6.0 or later miniport drivers, the Native 802.11 miniport driver also supports a variety of OIDs specific to the Native 802.11 framework.

Native 802.11 miniport drivers provide support for the following:

<a href="" id="standard-ieee-802-11-media-access-control--mac--frame-formats"></a>**Standard IEEE 802.11 Media Access Control (MAC) frame formats**  
All data packets sent or received by Native 802.11 miniport drivers are compliant with the MAC frame formats defined in Clause 8 of the IEEE 802.11-2012 standard.

<a href="" id="standard-802-11-media-access-control--mac--services-and-protocols"></a>**Standard 802.11 Media Access Control (MAC) services and protocols**  
802.11 MAC services and protocols, based on the IEEE 802.11 standards, can be configured on the 802.11 station through the Native 802.11 miniport driver.

For miniport drivers operating in Extensible Station (ExtSTA) mode, most of the MAC services are provided by the 802.11 station and invoked by the operating system. For more information about this operating mode, see [Extensible Station Operation Mode](extensible-station-operation-mode.md).

<a href="" id="standard-802-11-authentication-algorithms"></a>**Standard 802.11 authentication algorithms**  
802.11 authentication algorithms, based on the IEEE 802.11 standards and Wi-Fi Alliance specifications, can be configured on the 802.11 station through the Native 802.11 miniport driver.

For miniport drivers operating in ExtSTA mode, the operating system processes the authentication algorithms that it supports. However, the ExtSTA operation mode provides an interface where the independent hardware vendor (IHV) can extend the set of authentication algorithms to include algorithms not supported by the operating system. For more information about this, see [Native 802.11 IHV Extensions](native-802-11-ihv-extensions.md).

<a href="" id="standard-802-11-cipher-algorithms"></a>**Standard 802.11 cipher algorithms**  
802.11 cipher algorithms, based on the IEEE 802.11 standards and Wi-Fi Alliance specifications, can be configured on the 802.11 station through the Native 802.11 miniport driver.

For miniport drivers operating in ExtSTA mode, the 802.11 station processes the cipher algorithms that it supports. The operating system does not process cipher algorithms that are not supported by the 802.11 station.

The ExtSTA operation also provides an interface where the IHV can extend the cipher algorithms to include algorithms not supported by the operating system. For more information about this, see [Native 802.11 IHV Extensions](native-802-11-ihv-extensions.md).

<a href="" id="802-11-mac-phy-configuration"></a>**802.11 MAC/PHY configuration**  
Native 802.11 specifies a set of NDIS object identifiers (OIDs) for MAC/PHY configuration through the miniport driver. These OIDs are based on the set of standard 802.11management information block (MIB) objects, which are defined in Annex D of the various IEEE 802.11 standards. For a list of these standards, see [Background Reading on 802.11](background-reading-on-802-11.md).

<a href="" id="802-11-network-connectivity-security-configuration"></a>**802.11 network connectivity/security configuration**  
In the ExtSTA operation mode, a miniport driver implements most of the 802.11 MAC protocols used to access basic service set (BSS) networks. Native 802.11 specifies a set of NDIS ExtSTA OIDs for BSS network configuration, including BSS type and service set identifiers (SSID). The operating system will use these OIDs when it configures the miniport driver with a network profile. For more information about this, see [Configuration through a Network Profile](configuration-through-a-network-profile.md).

For more information about the NDIS driver model, see [NDIS Miniport Drivers](ndis-miniport-drivers.md).

 

 





