---
title: Creating Network Profile Extensions
description: Creating Network Profile Extensions
ms.assetid: b5f7a057-28bc-4df9-99da-58d39b81fb60
keywords:
- network profiles WDK Native 802.11 IHV Extensions DLL , creating extensions
- scan operation WDK Native 802.11
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Creating Network Profile Extensions


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

After the underlying wireless LAN (WLAN) adapter completes a scan operation, it returns a list of the detected basic service set (BSS) network to the operating system. The operating system calls the [*Dot11ExtIhvCreateDiscoveryProfiles*](https://msdn.microsoft.com/library/windows/hardware/ff547445) function for every BSS network for which the user has not created a network profile. When this function is called, the IHV Extensions DLL can return temporary connectivity and security profile fragments that could be used to connect to the BSS network.

For more information about the scan operation, see [Native 802.11 Scan Operations](native-802-11-scan-operations.md).

When [*Dot11ExtIhvCreateDiscoveryProfiles*](https://msdn.microsoft.com/library/windows/hardware/ff547445) is called, the IHV Extensions DLL must follow these guidelines.

-   The operating system passes to the *pConnectableBssid* parameter a list of IEEE 802.11 Beacon and Probe Response frames received during the last scan operation. This list is formatted as a DOT11\_BSS\_ENTRY structure. Each Beacon or Probe response within the list was sent by an access point (AP) with the same service set identifier (SSID).

    **Note**  For Windows Vista, the IHV Extensions DLL supports only infrastructure basic service set (BSS) networks.

     

    The IHV Extensions DLL must parse each of the fixed-length fields and variable-length information elements (IEs) in order to create the appropriate profile fragments.

-   The connectivity and security profile fragment must contain valid settings that can be used to connect to each of the APs, whose BSS identifiers (BSSIDs) are referenced through the *pConnectableBssid* parameter.

-   Each connectivity and security profile fragment contains the XML data for the profile extensions defined by the IHV. The XML data within the profile fragment must be delimited by &lt;IHV&gt; and &lt;/IHV&gt; tags.

 

 





