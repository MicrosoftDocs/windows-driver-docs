---
title: Extending the Properties for Wireless Network Profiles
description: Extending the Properties for Wireless Network Profiles
keywords:
- IHV UI Extensions DLL WDK Native 802.11 , network profile extensions
- network profiles WDK Native 802.11 IHV UI Extensions DLL
ms.date: 04/20/2017
---

# Extending the Properties for Wireless Network Profiles




 

The end user creates or edits a wireless network connection profile through the Native 802.11 Network Configuration user interface (UI). For more information about this UI, see [Native 802.11 Software Architecture](/previous-versions/windows/hardware/wireless/native-802-11-software-architecture).

The independent hardware vendor (IHV) can extend the Network Configuration UI to support proprietary connection and security profile settings through a Native 802.11 UI Extensions DLL. The DLL can extend the following tabs that are displayed in the Network Configuration UI.

<a href="" id="connection-tab"></a>**Connection tab**  
This tab displays the UI for the connection settings of a wireless LAN (WLAN) network.

The Native 802.11 IHV UI Extensions DLL can extend this UI by following the procedure described in [Extending Wireless Connection Property Pages](extending-wireless-connection-properties.md).

**Note**  For Windows Vista, the Native 802.11 UI Extensions DLL can only support one extension to the **Connection** tab.

 

<a href="" id="security-tab-------"></a>**Security tab**   
This tab displays the UI for the security settings of a wireless LAN (WLAN) network.

The Native 802.11 IHV UI Extensions DLL can extend this UI by adding display elements for proprietary security settings. For more information about this process, see [Extending Wireless Security Property Pages](extending-wireless-security-properties.md).

The Native 802.11 IHV UI Extensions DLL can also extend the Microsoft 802.1X settings on the **Security** tab. For more information about this process, see [Extending Microsoft 802.1X Security Settings](extending-microsoft-802-1x-security-settings.md).

**Note**  For Windows Vista, the Native 802.11 IHV UI Extensions DLL can only extend the properties of connection and security profiles for infrastructure wireless networks.

 

 

 
