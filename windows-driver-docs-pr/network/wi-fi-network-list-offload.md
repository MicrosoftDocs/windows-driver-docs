---
title: Wi-Fi Network List Offload
description: This section describes Native 802.11 WLAN Wi-Fi Network List Offload (NLO)
ms.assetid: 528838AA-4002-4923-A71B-37ADEE9B8D07
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Wi-Fi Network List Offload


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

Wi-Fi Network List Offload (NLO) is a feature where certain Wi-Fi profile information is offloaded to the NIC firmware to allow the Wi-Fi NIC to perform logic that optimizes the power efficiency and connectivity of a given system. The WLAN Service will use the system states and various connection hints to determine when NLO should be activated and the profiles that should be offloaded. The WLAN Service will only offload broadcast profiles to the Wi-Fi NIC. The profile information that will be offloaded to the Wi-Fi NIC are:

-   SSID
-   Encryption type
-   Authentication type
-   Channel number hints

The WLAN Service will be responsible for configuring NLO to the Wi-Fi NIC at different system conditions. The miniport driver should not have any assumption on the type of profiles and when the WLAN Service will provision NLO to the device. Therefore, the miniport driver will need to support NLO in both D0 and D3 device power states. The Wi-Fi device must be able to handle OS requested scan operations while NLO is active (configured) as well as when NLO is not active.

It is expected that the Wi-Fi NIC maintain the NLO list in device firmware rather than in the miniport driver in order to reduce the number of interrupts to Windows.

Here are some examples of how WLAN Service and NLO operate for various different scenarios:

**Wi-Fi Connected to Wi-Fi Network**

If the currently connected Wi-Fi profile has the “Connect to a more preferred network if available” option selected, the WLAN Service will configure NLO to the device. The NLO will contain all the profiles that are more preferred than the currently connected Wi-Fi profile. If the currently connected Wi-Fi profile is already the most preferred profile, then the WLAN Service will not configure NLO.

**Connected to non Wi-Fi media**

The WLAN Service will configure only Wi-Fi profiles that is more preferred that the current media type. For example, if currently connected to a Mobile Broadband (MB) connection, the WLAN Service will configure NLO for Wi-Fi profiles. Once connected to any Wi-Fi profile, Mobile Broadband connection might be disconnected.

**Not Connected**

The WLAN Service will configure NLO.

## Related topics


[Wi-Fi Network List Offload Reference](https://msdn.microsoft.com/library/windows/hardware/hh440296)

 

 






