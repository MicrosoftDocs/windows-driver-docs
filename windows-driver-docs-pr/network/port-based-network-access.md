---
title: Port-Based Network Access
description: Port-Based Network Access
ms.assetid: f98f02de-861e-44b4-b7e5-78a5adcd0440
keywords:
- network operations WDK Native 802.11 , port-based network access
- port-based network access WDK Native 802.11
- ports WDK Native 802.11
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Port-Based Network Access


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

If an authentication algorithm, such as the Wi-Fi Protected Access ([WPA](wpa.md)) or Robust Security Network Association ([RSNA](rsna.md)) algorithms, is based on the IEEE 802.1X protocol, a port must be created and authorized before the 802.11 station can send or receive media access control (MAC) service data unit (MSDU) packets. For more information about ports and port access, refer to Clause 6 of the IEEE 802.1X-2001 standard.

The following topics describe the procedures involved in port management:

[Port Creation](port-creation.md)

[Port Deletion](port-deletion.md)

 

 





