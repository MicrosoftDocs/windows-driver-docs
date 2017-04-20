---
title: Requesting Explicit Scan Operations
description: Requesting Explicit Scan Operations
ms.assetid: 036c5a7a-c3f3-4f51-bc82-cee7619d0ee0
keywords:
- explicit scan operations WDK Native 802.11
- requesting explicit scan operations WDK Native 802.11
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Requesting Explicit Scan Operations


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The 802.11 station performs an explicit scan operation when the [OID\_DOT11\_SCAN\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569413) object identifier (OID) is set. When set, this OID invokes the station's media access control (MAC) layer management entity (MLME) MLME-SCAN.request service primitive (defined in Clause 6.3.3 of the IEEE 802.11-2012 standard).

The data type that accompanies the set request of [OID\_DOT11\_SCAN\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569413) is the [**DOT11\_SCAN\_REQUEST\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff548767) structure. Some of the members of this structure directly correspond to the parameters of the MLME-SCAN.request service primitive as defined by the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Service primitive parameter</th>
<th align="left">DOT11_SCAN_REQUEST_V2 member</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>BSSType</p></td>
<td align="left"><p><strong>dot11BSSType</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>BSSID</p></td>
<td align="left"><p><strong>dot11BSSID</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>ScanType</p></td>
<td align="left"><p><strong>dot11ScanType</strong></p></td>
</tr>
</tbody>
</table>

 

Other members of the [**DOT11\_SCAN\_REQUEST\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff548767) structure indirectly correspond to the rest of the parameters of the MLME-SCAN.request service primitive, as described below:

<a href="" id="ssid-parameter------"></a>**SSID parameter**   
Instead of requesting a scan on a single service set identifier (SSID), the [**DOT11\_SCAN\_REQUEST\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff548767) structure allows an explicit scan operation to be performed on one or more SSIDs. The list of SSIDs are defined though the **udot11SSIDsOffset** and **uNumOfdot11SSIDs** members of this structure.

The 802.11 station performs the scan operation using the zero-length broadcast SSID if any of the following are true:

-   An entry in the list of SSIDs defines the broadcast SSID.

-   The **uNumOfdot11SSIDs** member has a value of zero.

<a href="" id="probedelay--minchanneltime--and-maxchanneltime-parameters------"></a>**ProbeDelay, MinChannelTime, and MaxChannelTime parameters**   
The [**DOT11\_SCAN\_REQUEST\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff548767) structure allows an explicit scan operation to be performed on one or more PHYs supported by the 802.11 NIC. Each PHY is configured for the scan operation through the [**DOT11\_PHY\_TYPE\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff548745) structure. The following table defines the relationship between the members of this structure and the parameters of the MLME-SCAN.request service primitive.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Service primitive parameter</th>
<th align="left">DOT11_PHY_TYPE_INFO member</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>ProbeDelay</p></td>
<td align="left"><p><strong>uProbeDelay</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>MinChannelTime</p></td>
<td align="left"><p><strong>uMinChannelTime</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>MaxChannelTime</p></td>
<td align="left"><p><strong>uMaxChannelTime</strong></p></td>
</tr>
</tbody>
</table>

 

If the miniport driver is operating in Extensible Station (ExtSTA) mode, the 802.11 station configures each PHY used in the scan operation with its own values for these parameters.

<a href="" id="channellist-parameter------"></a>**ChannelList parameter**   
The channel list is defined through the **uChannelListSize** and **ucChannelListBuffer** members of the [**DOT11\_PHY\_TYPE\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff548745) structure, allowing a separate channel list to be defined for each PHY used in the scan operation.

If the miniport driver is operating in Extensible Station (ExtSTA) mode, the operating system will not define the channel list. Instead, the 802.11 station scans all of the channels that are valid for the regulatory domain that the station is currently operating within.

The [**DOT11\_SCAN\_REQUEST\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff548767) structure extends the MLME-SCAN.request service primitive in the following ways:

-   The scan type, specified through the **dot11ScanType** member, can be either an active or passive scan or a combination of both methods.
    If the **dot11ScanType** member is set to **dot11\_scan\_type\_auto**, the following cases are possible:
    In Windows Vista, the 802.11 station can use any scanning method when it performs the scan operation.
    Beginning with Windows 7, if the miniport driver is not joined to or hosting a BSS or IBSS, the 802.11 station should perform an active scan when not restricted by regulatory requirements. In this case, the 802.11 station must complete a scan request within 4 seconds and must return the correct list of available WLAN networks.
-   If the **bUseRequestIE** member is set to **TRUE**, the 802.11 station must add the 802.11d Request information elements (IE) defined through the **bRequestIDsOffset** and **uNumOfRequestIDs** members to any Probe Request frames that the station sends when performing an active scan.
    **Note**  The miniport driver must ignore the **bUseRequestIE**, **bRequestIDsOffset**, and **uNumOfRequestIDs** members if the IEEE 802.11d **dot11MultiDomainCapabilityEnabled** management information base (MIB) object is set to **FALSE** or the station is performing a passive scan. For more information about the **dot11MultiDomainCapabilityEnabled** MIB object, see [OID\_DOT11\_MULTI\_DOMAIN\_CAPABILITY\_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569390).

     

Beginning with Windows 7, the miniport driver should attempt to maintain a stable connection. To do this, the driver should scan a few channels at a time and move back to its active channel when it needs to send and receive data. When the driver has an infrastructure association with an AP, it can also set the power save (PS) bit in a null data packet. By doing this, the driver requests the AP to buffer packets until it can return to its active channel.

 

 





