---
title: Introduction to Native 802.11
description: Introduction to Native 802.11
ms.assetid: 8a8f15fe-af9a-484f-80a1-39a60738215a
keywords:
- Native 802.11 WDK networking , about Native 802.11
- wireless LAN networks WDK , Native 802.11 overview
- WLAN networks WDK , Native 802.11 overview
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Introduction to Native 802.11


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

Native 802.11 is a software architecture for wireless LAN (WLAN) network topologies that is integrated into the Windows Vista and later operating systems. Native 802.11 provides a framework for an integrated and extensible set of services and drivers.

The Native 802.11 framework provides support for the following:

<a href="" id="fully-compliant-802-11-operations"></a>**Fully compliant 802.11 operations**  
The Native 802.11 miniport driver manages an 802.11 NIC that operates over the WLAN media. All packets sent or received through the miniport driver are formatted in the IEEE media access control (MAC) frame format, as specified in Clause 8 of the IEEE 802.11-2012 standard.

The interface between the Native 802.11 framework and underlying miniport driver has been enhanced to provide:

-   A complete set of object identifiers (OIDs) based on IEEE 802.11 management information base (MIB) objects. The Native 802.11 framework uses these OIDs to query or set media access control (MAC) or PHY attributes on the underlying miniport driver and 802.11 station.

    For more information about these OIDs, see [Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691).

-   An extensive set of media-specific status indications. The Native 802.11 miniport driver uses these indications to notify the Native 802.11 framework about a variety of events pertaining to changes in MAC/PHY configuration or basic service set (BSS) network connectivity.

    For more information about these status indications, see [Native 802.11 Wireless LAN Status Indications](https://msdn.microsoft.com/library/windows/hardware/ff560692)

<a href="" id="standard-802-11-authentication-algorithms"></a>**Standard 802.11 authentication algorithms**  
802.11 authentication algorithms based on the IEEE 802.11 standards and Wi-Fi Alliance specifications are supported by the Native 802.11 framework. These standard authentication algorithms include Wi-Fi Protected Access ([WPA](wpa.md)) and Robust Security Network Association ([RSNA](rsna.md)).

The Native 802.11 miniport driver can be configured for any supported authentication algorithm and uses that configuration to determine the algorithms to enable when connecting to a basic service set (BSS) network.

After a standard authentication algorithm is enabled, the Native 802.11 framework processes all security packets for the algorithm and is responsible for deriving cipher keys through the authentication algorithm. All cipher keys are then downloaded to the Native 802.11 miniport driver through set requests of Native 802.11 OIDs.

<a href="" id="standard-802-11-cipher"></a>**Standard 802.11 cipher**  
Standard 802.11 cipher algorithms based on the IEEE 802.11 standards and Wi-Fi Alliance specifications are supported by the Native 802.11 framework. These standard cipher algorithms include Temporal Key Integrity Protocol ( [TKIP](tkip.md)) and [AES-CCMP](aes-ccmp.md).

The Native 802.11 miniport driver and underlying 802.11 station are responsible for the encryption and decryption operations for the cipher algorithms enabled on a BSS network connection.

The independent hardware vendor (IHV) can extend the functionality of the Native 802.11 framework by providing support for the following:

<a href="" id="proprietary-authentication-algorithms"></a>**Proprietary authentication algorithms**  
The IHV can develop authentication algorithms that are not supported by the Native 802.11 framework. The IHV can also develop its own version of standard authentication algorithms for use in place of those algorithms supported by the Native 802.11 framework.

<a href="" id="proprietary-cipher-algorithms"></a>**Proprietary cipher algorithms**  
The IHV can develop cipher algorithms that are not supported by the Native 802.11 framework. The IHV can also develop its own version of standard cipher algorithms for use in place of those algorithms supported by the Native 802.11 framework.

<a href="" id="proprietary-phy-configurations"></a>**Proprietary PHY configurations**  
The IHV can extend the Native 802.11 framework to support proprietary PHY types or configurations. For example, the IHV can develop a Native 802.11 miniport driver that supports a proprietary PHY or multiple supported or proprietary PHY types.

For more information about how the IHV can extend the Native 802.11 functionality, see [Native 802.11 IHV Extensions](native-802-11-ihv-extensions.md).

 

 





