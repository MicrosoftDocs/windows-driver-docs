---
title: Scanning for Non-Broadcast SSIDs
description: Scanning for Non-Broadcast SSIDs
ms.assetid: ad4fd978-1e18-48c6-907b-1139fe7832d3
keywords:
- scan operations WDK Native 802.11 , non-broadcast SSIDs
- non-broadcast SSIDs WDK Native 802.11
- SSIDs WDK Native 802.11
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Scanning for Non-Broadcast SSIDs


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

An access point (AP) or peer station can be configured to exclude the service set identifier (SSID) in the SSID information element (IE) of any broadcast 802.11 Beacon or Probe Response frames. For example, an AP could exclude its SSID by either setting the Length or SSID fields of the SSID IE to zero.

When the 802.11 station receives an 802.11 Beacon or Probe Response with an excluded SSID, the station must follow these guidelines:

-   If the 802.11 station is performing an explicit scan operation through a set of [OID\_DOT11\_SCAN\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569413), the station must resolve excluded SSIDs as part of the scan operation. In this situation, the 802.11 station resolves an excluded SSID from the list of SSIDs specified through the **udot11SSIDsOffset** member of the [**DOT11\_SCAN\_REQUEST\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff548767) structure.

-   If the 802.11 station is performing an implicit scan operation, the station can optionally resolve excluded SSIDs. If the 802.11 station attempts to resolve excluded SSIDs, it must follow these guidelines:
    -   When [OID\_DOT11\_SCAN\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569413) is set, the 802.11 station must cache the list of SSIDs specified through the **udot11SSIDsOffset** member.
    -   When performing the implicit scan operation, the 802.11 station must only resolve excluded SSIDs from the cached list of SSIDs.

**Note**  If the **uNumOfdot11SSIDs** member of the [**DOT11\_SCAN\_REQUEST\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff548767) structure has a value of zero, the 802.11 station must not attempt to resolve excluded SSIDs when performing a scan operation.

 

The 802.11 station resolves the excluded SSID by sending an 802.11 Probe Request frame with the SSID IE set to the value of an SSID specified through the **udot11SSIDsOffset** member. The 802.11 station can either:

-   Send the Probe Request frame directly to the AP or peer station from which the station received the Beacon or Probe Response frame with the excluded SSID.

-   Broadcast the Probe Request frame to the BSS network from which the station received the Beacon or Probe Response frame with the excluded SSID.

 

 





