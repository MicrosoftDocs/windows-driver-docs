---
title: Overview of Scan Operations
description: Overview of Scan Operations
ms.assetid: 2cdd4f98-eaf9-40c2-a199-1d392fa288cb
keywords:
- scan operations WDK Native 802.11 , about scan operations
- passive scans WDK Native 802.11
- active scans WDK Native 802.11
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Overview of Scan Operations


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The 802.11 station periodically performs scan operations to detect basic service set (BSS) networks that are within radio range of the network interface card (NIC).

When scanning, the 802.11 station detects a BSS network by receiving 802.11 Beacon or Probe Response frames transmitted by an access point (AP) or peer station. The Beacon and Probe Response frames contain information elements (IEs), such as a service set identifier (SSID), which identify the BSS network. The 802.11 station will use these IEs when performing a connect or roaming operation. For more information about connection and roaming operations, see [Native 802.11 Network Operations](native-802-11-network-operations.md).

There are two types of scan operations:

<a href="" id="explicit-scan-operations"></a>**Explicit Scan Operations**  
The 802.11 station performs an explicit scan operation that follows a set request of [OID\_DOT11\_SCAN\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569413). When set, this object identifier (OID) defines the parameters for the scan operation, including a list of SSIDs that the 802.11 station must locate.

For more information about this scan operation, see [Explicit Scan Operations](explicit-scan-operations.md).

<a href="" id="implicit-scan-operations"></a>**Implicit Scan Operations**  
The 802.11 device performs an implicit scan operation on its own without a preceding set request of [OID\_DOT11\_SCAN\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569413). The 802.11 station must determine the parameters of the scan operation, including the SSIDs to locate or channels to scan. Implicit scan operations are also referred to as "background scan operations."

For more information about this scan operation, see [Implicit Scan Operations](implicit-scan-operations.md).

When performing scan operations, the 802.11 station uses the following scanning methods:

<a href="" id="active-scans"></a>**Active Scans**  
The 802.11 station broadcasts an 802.11 Probe Request frame on the channel for each SSID it is trying to locate. The 802.11 station sets the SSID IE of the Probe Request to the SSID that the station is trying to locate. If the station is scanning for all SSIDs, it sets the SSID IE to the zero-length broadcast SSID value.

<a href="" id="passive-scans"></a>**Passive Scans**  
The 802.11 station does not send an 802.11 Probe Request. Instead, it dwells on a channel for a short period in order to receive any 802.11 Probe Response or Beacon frames from the SSID it is trying to locate.

For both scanning methods, the 802.11 station must follow these guidelines:

-   For each channel it is scanning, the 802.11 station must dwell on the channel long enough to potentially receive any 802.11 Probe Response or Beacon frames from the SSID it is trying to locate.

    The dwell period is dependent on the independent hardware vendor's (IHV's) implementation, as well as the scanning method used. However, after a maximum dwell period is reached, the station must start a scan on another channel.

-   If the 802.11 station is actively scanning, it must only send 802.11 Probe Request frames on the channels that are valid for the regulatory domain that the station is currently operating within. However, the 802.11 station can passively scan on the other channels outside of the regulatory domain.

-   If the 802.11 station supports multiple regulatory domains and the IEEE 802.11 **dot11CurrentRegDomain** management information base (MIB) object is set to a value of DOT11\_REG\_DOMAIN\_OTHER, the station must only perform a passive scan until the regulatory domain is determined. For more information about this MIB object, see [OID\_DOT11\_CURRENT\_REG\_DOMAIN](https://msdn.microsoft.com/library/windows/hardware/ff569136).

    In general, when the **dot11CurrentRegDomain** MIB object is set to DOT11\_REG\_DOMAIN\_OTHER, the 802.11 station determines the regulatory domain through the connection operation to a BSS network. For more information about this operation, see [Connection Operations](connection-operations.md).

-   If the 802.11 station detects the presence of a BSS network that does not broadcast its service set identifier (SSID) within the 802.11 Beacon or Probe Request frames, the station must resolve the SSID by following the guidelines described in [Scanning for Non-Broadcast SSIDs](scanning-for-non-broadcast-ssids.md).

If the miniport driver is operating in Extensible Station (ExtSTA) mode, the 802.11 station must maintain a cache of detected BSS networks, which the station uses in the following ways:

-   After the scan operation completes, the 802.11 station will update its BSS network cache based on the 802.11 Probe Response or Beacon frames it received during the scan operation.

-   When performing a connect or roaming operation, the 802.11 station will determine the BSS identifier (BSSID) to connect or roam to based on the best candidate from the BSS network cache.

-   The miniport driver returns the entries from the BSS network cache when a method request of [OID\_DOT11\_ENUM\_BSS\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569360) is made.

-   The miniport driver must only clear the BSS network cache when [OID\_DOT11\_FLUSH\_BSS\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569367) is set.

 

 





