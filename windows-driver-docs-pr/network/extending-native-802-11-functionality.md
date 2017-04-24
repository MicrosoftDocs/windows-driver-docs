---
title: Extending Native 802.11 Functionality
description: Extending Native 802.11 Functionality
ms.assetid: 6ef2a690-568c-4b39-b988-40a01b6f7298
keywords:
- Native 802.11 miniport drivers WDK networking , extending functionality
- miniport drivers WDK Native 802.11 , extending functionality
- extending functionality WDK Native 802.11
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Extending Native 802.11 Functionality


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The independent hardware vendor (IHV) can develop 802.11 extensions that are not supported by the operating system through the following components.

-   A Native 802.11 miniport driver that supports operation in the Extensible Station (ExtSTA) mode. For more information about the ExtSTA operation mode, see [Extensible Station Operation Mode](extensible-station-operation-mode.md).
-   An IHV Extensions DLL, through which the 802.11 extensions can be processed or downloaded to the Native 802.11 miniport driver for processing. For more information about the IHV Extensions DLL, see [Native 802.11 IHV Extensions DLL](https://msdn.microsoft.com/library/windows/hardware/ff560614).

For example, an IHV can do the following:

-   Replace or add 802.11 authentication algorithms.

    Through an IHV Extensions DLL, the IHV can replace an authentication algorithm that is supported by the operating system, such as Wi-Fi Protected Access ( [WPA](wpa.md)) or Robust Security Network Association ( [RSNA](rsna.md)).

    In addition, the IHV Extensions DLL can provide support for non-standard or proprietary 802.11 authentication algorithms. This DLL can then configure security settings for any authentication protocol that it supports. The operating system queries the DLL for security settings before configuring the miniport driver with the settings from a network profile.

    For more information, see [Extending Support for 802.11 Authentication Algorithms](extending-support-for-802-11-authentication-algorithms.md).

-   Add or activate 802.11 cipher algorithms.

    Through an IHV Extensions DLL, the IHV can extend the types and configurations for 802.11 cipher algorithms. These cipher algorithms can be standard 802.11 ciphers, such as [TKIP](tkip.md) or [AES-CCMP](aes-ccmp.md). The DLL can also provide support for proprietary or non-standard ciphers, as well as provide support for standard cipher algorithms over network configurations that are not supported by the operating system.

    The IHV Extensions DLL also manages keys for any standard or proprietary cipher algorithm that it activates on the 802.11 station.

    For more information, see [Extending Support for 802.11 Cipher Algorithms](extending-support-for-802-11-cipher-algorithms.md).

-   Add support for proprietary or non-standard PHY configurations.

    For more information, see [Extending Support for 802.11 PHY Configurations](extending-support-for-802-11-phy-configurations.md).

**Note**  For more information about extending the Native 802.11 functionality, see [Native 802.11 IHV Extensions](native-802-11-ihv-extensions.md).

 

 

 





