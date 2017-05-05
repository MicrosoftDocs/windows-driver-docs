---
title: Roaming Operations
description: Roaming Operations
ms.assetid: b52e134e-4f26-4797-af57-dd7da177c193
keywords:
- network operations WDK Native 802.11 , roaming operations
- roaming operations WDK Native 802.11
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Roaming Operations


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The miniport driver performs a roaming operation after the 802.11 station has successfully connected to a basic service set (BSS) network and one of the following occurs:

-   If connected to an infrastructure basic service set (BSS) network, the 802.11 station has either disassociated with the access point (AP), no longer detects the AP within the BSS network, or detects an AP that provides a better network connection.

    For example, the 802.11 station might decide to roam to another AP due to its stronger signal strength.

-   If connected to an independent BSS (IBSS) network, the 802.11 station detects another IBSS network with the same service set identifier (SSID) but a different BSS identifier (BSSID). The algorithm used to determine when the 802.11 station roams within an IBSS network is specific to the implementation by the independent hardware vendor (IHV).

The following topics describe the roaming operation in more detail:

[General Roaming Operation Guidelines](general-roaming-operation-guidelines.md)

[Roaming Operation Guidelines for Infrastructure BSS Networks](roaming-operation-guidelines-for-infrastructure-bss-networks.md)

[Roaming Operation Guidelines for Independent BSS Networks](roaming-operation-guidelines-for-independent-bss-networks.md)

 

 





