---
title: Open System Authentication
description: Open System Authentication
ms.assetid: f07d2d77-ccaf-4599-b59e-6ea4ecf55e0f
keywords:
- Open System authentication WDK Native 802.11
- authentication WDK Native 802.11 , Open System
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Open System Authentication


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The Open System authentication algorithm is specified in Clause 11.2.3.2 of the IEEE 802.11-2012 standard. Open System authentication is required for both infrastructure and independent basic service set (BSS) network types.

When configured for Open System authentication, the 802.11 station must do the following:

-   If it is configured to operate in an infrastructure BSS network, authenticate with the access point (AP) using the protocol defined for the Open System authentication algorithm.

-   If it is configured to operate in an independent BSS (IBSS), authenticate with other peer stations using one of the following:
    -   The protocol defined for the Open System authentication algorithm.
    -   A proprietary protocol defined by the independent hardware vendor (IHV). For example, a common approach is to authenticate the peer station as soon as the first frame is received from the peer station.

    **Note**  IBSS (Ad hoc) and SoftAP are deprecated. Starting with Windows 8.1 and Windows Server 2012 R2, use [Wi-Fi Direct](wi-fi-direct-miniport-initialization-and-configuration.md).

     

When initialized or reset, the 802.11 station must default to Open System authentication. If configured for WPA or RSNA authentication, the 802.11 station must first authenticate to a BSS network using the Open System authentication algorithm.

 

 





