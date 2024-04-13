---
title: Creating Network Profile Extensions
description: Creating Network Profile Extensions
keywords:
- network profiles WDK Native 802.11 IHV Extensions DLL , creating extensions
- scan operation WDK Native 802.11
ms.date: 04/20/2017
---

# Creating Network Profile Extensions




 

After the underlying wireless LAN (WLAN) adapter completes a scan operation, it returns a list of the detected basic service set (BSS) network to the operating system. The operating system calls the [*Dot11ExtIhvCreateDiscoveryProfiles*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_create_discovery_profiles) function for every BSS network for which the user has not created a network profile. When this function is called, the IHV Extensions DLL can return temporary connectivity and security profile fragments that could be used to connect to the BSS network.

For more information about the scan operation, see [Native 802.11 Scan Operations](/previous-versions/windows/hardware/wireless/native-802-11-scan-operations).

When [*Dot11ExtIhvCreateDiscoveryProfiles*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_create_discovery_profiles) is called, the IHV Extensions DLL must follow these guidelines.

-   The operating system passes to the *pConnectableBssid* parameter a list of IEEE 802.11 Beacon and Probe Response frames received during the last scan operation. This list is formatted as a DOT11\_BSS\_ENTRY structure. Each Beacon or Probe response within the list was sent by an access point (AP) with the same service set identifier (SSID).

    **Note**  For Windows Vista, the IHV Extensions DLL supports only infrastructure basic service set (BSS) networks.

     

    The IHV Extensions DLL must parse each of the fixed-length fields and variable-length information elements (IEs) in order to create the appropriate profile fragments.

-   The connectivity and security profile fragment must contain valid settings that can be used to connect to each of the APs, whose BSS identifiers (BSSIDs) are referenced through the *pConnectableBssid* parameter.

-   Each connectivity and security profile fragment contains the XML data for the profile extensions defined by the IHV. The XML data within the profile fragment must be delimited by &lt;IHV&gt; and &lt;/IHV&gt; tags.

 

 
