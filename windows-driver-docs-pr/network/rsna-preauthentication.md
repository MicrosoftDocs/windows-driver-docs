---
title: RSNA Preauthentication
description: RSNA Preauthentication
ms.assetid: d93ac119-6d46-4e94-943e-1b48ca5a5e0a
keywords:
- authentication WDK Native 802.11 , preauthentications
- Robust Security Network Association WDK Native 802.11
- RSNA WDK Native 802.11
- preauthentication WDK Native 802.11
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# RSNA Preauthentication


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The Robust Security Network (RSN) Association (RSNA) authentication algorithm defines a method through which the 802.1X supplicant can preauthenticate with one or more access points (APs) within an infrastructure basic service set (BSS). For more information about preauthentication, refer to Clause 8.4.6.1 of the IEEE 802.11i-2004 standard.

With preauthentication, the supplicant can optionally perform an RSNA authentication with other APs while the 802.11 station is still associated with its current AP. After the preauthentication completes with an AP, the supplicant has resolved a pairwise master key (PMK) that the 802.11 station uses if it needs to associate with the AP.

The 802.11 station can only preauthenticate with an AP that sets Bit 0 (preauthentication) within the RSN Capabilities subfield of the RSN information element (IE) in the IEEE Beacon and Probe Response frames that the AP transmits. For more information about the RSN IE, refer to Clause 7.3.2.25 of the IEEE 802.11i-2004 standard.

 

 





