---
title: BSS Network Candidate List
description: BSS Network Candidate List
ms.assetid: a2190195-48aa-4414-8985-c19c245e6bd8
keywords: ["network operations WDK Native 802.11 , BSS network candidate list", "BSS network candidate list WDK Native 802.11", "network candidate list WDK Native 802.11"]
---

# BSS Network Candidate List


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

Many network operations, such as the connection and roaming operations, require a list of candidate basic service set (BSS) networks with which to perform the operation. The 802.11 station creates this list from the intersection of the following:

-   The cache of BSS networks detected during the most recent scan operation. For more information about this operation, see [Native 802.11 Scan Operations](native-802-11-scan-operations.md).

-   The 802.11 station's network configuration. Entries within the BSS network candidate list must match the network configuration of the 802.11 station as described in [Configuration Requirements for Network Operations](configuration-requirements-for-network-operations.md). For example, each entry in the candidate list must have an SSID that matches an entry in the desired SSID list and a BSSID that matches an entry in the desired BSSID list. For more information about the desired SSID list, see [OID\_DOT11\_DESIRED\_SSID\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569145). For more information about the desired BSSID list, see [OID\_DOT11\_DESIRED\_BSSID\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569141).

When creating the BSS network candidate list, the 802.11 station must follow these guidelines:

-   If the desired service set identifier (SSID) list contains a wildcard SSID, the 802.11 station can add entries to the BSS network candidate list for any SSID. If the desired SSID list contains zero entries, then the BSS network candidate list must also contain zero entries.

    For more information about the desired SSID list, see [OID\_DOT11\_DESIRED\_SSID\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569145).

    **Note**  If the 802.11 station is creating a BSS network candidate list for a roaming operation, it must only add entries to the list that matches the SSID of the network to which it is currently connected.

     

-   If the desired BSS identifier (BSSID) list contains a wildcard BSSID, the 802.11 station can add entries to the BSS network candidate list for any BSSID. If the desired BSSID list contains zero entries, then the BSS network candidate list must also contain zero entries.

    For more information about the desired BSSID list, see [OID\_DOT11\_DESIRED\_BSSID\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569141).

-   If the 802.11 station supports multiple regulatory domains as defined through the IEEE 802.11d-2001 standard, the 802.11 can add entries to the BSS network candidate list if one of the following are true:

    -   The Extensible Station (ExtSTA) **msDot11DesiredCountryorRegionString** management information base (MIB) object is set to a country or region string of all zeros. For more information about the **msDot11DesiredCountryorRegionString** MIB object, see [OID\_DOT11\_DESIRED\_COUNTRY\_OR\_REGION\_STRING](https://msdn.microsoft.com/library/windows/hardware/ff569143).
    -   The candidate access point (AP) or peer station is operating on a channel that is valid for the regulatory domain that is specified by the **msDot11DesiredCountryorRegionString** MIB object.
    -   The 802.11 Beacon or Probe Response frames sent by the candidate AP or peer station include a Country information element (IE) and the value of the Country or Region String subfield equals the **msDot11DesiredCountryorRegionString** MIB object.
    -   The 802.11 Beacon or Probe Response frames sent by the candidate AP or peer station do not contain a Country IE.

    The miniport driver specifies whether the 802.11 station supports multiple regulatory domains through a query request of [OID\_DOT11\_MULTI\_DOMAIN\_CAPABILITY\_IMPLEMENTED](https://msdn.microsoft.com/library/windows/hardware/ff569391).

-   Entries in the BSS network candidate list must be for BSS networks detected on a PHY that is defined in the desired PHY list. It might be possible for a scan request initiated through [OID\_DOT11\_SCAN\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569413) to include PHY types that are not in the desired PHY list.

    If the desired PHY list contains the wildcard PHY identifier, the 802.11 station can add entries to the BSS network candidate list for a BSS network detected on any supported PHY.

    For more information about the desired PHY list, see [OID\_DOT11\_DESIRED\_PHY\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569144).

If none of the entries in the BSS network cache have an SSID that matches an entry in the desired SSID list, the 802.11 station must attempt to detect a BSS using 802.11 Probe Request frames for each SSID in the desired SSID list. The station must do this in the situation where an access point (AP) or peer station is transmitting 802.11 Beacon frames with a zero-length SSID field. For more information about this procedure, see [Scanning for Non-Broadcast SSIDs](scanning-for-non-broadcast-ssids.md).

 

 





