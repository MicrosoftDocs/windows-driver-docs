---
title: 802.11 MAC Configuration
description: 802.11 MAC Configuration
ms.assetid: 718d6231-31f3-4730-bc12-275b8f3c7900
keywords: ["MAC configuration WDK Native 802.11", "configurations WDK Native 802.11 , MAC configuration"]
---

# 802.11 MAC Configuration


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The IEEE media access control (MAC) sublayer of the Native 802.11 station is configured through a set of object identifiers (OIDs), which are based on 802.11 management information base (MIB) objects. For more information about the 802.11 MIB objects, refer to Annex D of the IEEE 802.11 standards listed in [Background Reading on 802.11](background-reading-on-802-11.md).

The following OIDs set or query the configuration of the MAC sublayer:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Name</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[OID_DOT11_BEACON_PERIOD](https://msdn.microsoft.com/library/windows/hardware/ff569109)</p></td>
<td align="left"><p>Sets or queries the time interval used by the 802.11 station for scheduling the transmission of 802.11 Beacon frames. This OID can only be set or queried when the 802.11 station is configured for operations within an independent basic service set (IBSS) network.</p>
<div class="alert">
<strong>Note</strong>  IBSS (Ad hoc) and SoftAP are deprecated. Starting with Windows 8.1 and Windows Server 2012 R2, use [Wi-Fi Direct](wi-fi-direct-miniport-initialization-and-configuration.md).
</div>
<div>
 
</div></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_CF_POLLABLE](https://msdn.microsoft.com/library/windows/hardware/ff569116)</p></td>
<td align="left"><p>Queries whether the 802.11 station supports the contention free (CF) access method and CF-poll frames.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_FRAGMENTATION_THRESHOLD](https://msdn.microsoft.com/library/windows/hardware/ff569368)</p></td>
<td align="left"><p>Sets or queries the maximum size, in bytes, of the MAC protocol data unit (MPDU) frame that the PHY can transmit.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_LONG_RETRY_LIMIT](https://msdn.microsoft.com/library/windows/hardware/ff569380)</p></td>
<td align="left"><p>Queries the maximum number of retransmission attempts made by the 802.11 station for MAC service data unit (MSDU) packets with lengths greater than the request to send (RTS) threshold.</p>
<p>For more information about the RTS threshold, see [OID_DOT11_RTS_THRESHOLD](https://msdn.microsoft.com/library/windows/hardware/ff569411).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_MAC_ADDRESS](https://msdn.microsoft.com/library/windows/hardware/ff569381)</p></td>
<td align="left"><p>Queries the MAC address that the 802.11 station is currently using. This MAC address could either be the NIC's permanent address, which is queried through [OID_DOT11_PERMANENT_ADDRESS](https://msdn.microsoft.com/library/windows/hardware/ff569399), or a locally administered address.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_MAX_RECEIVE_LIFETIME](https://msdn.microsoft.com/library/windows/hardware/ff569384)</p></td>
<td align="left"><p>Queries the maximum elapsed time, after the initial reception of a management protocol data unit (MPDU) fragment that the 802.11 station can wait, to receive all remaining fragments of the MSDU packet.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_MAX_TRANSMIT_MSDU_LIFETIME](https://msdn.microsoft.com/library/windows/hardware/ff569385)</p></td>
<td align="left"><p>Queries the maximum time that the 802.11 station can spend transmitting all MPDU fragments for an MSDU packet.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_OPERATIONAL_RATE_SET](https://msdn.microsoft.com/library/windows/hardware/ff569395)</p></td>
<td align="left"><p>Sets or queries the rates at which the station can transmit data.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_RTS_THRESHOLD](https://msdn.microsoft.com/library/windows/hardware/ff569411)</p></td>
<td align="left"><p>Sets or queries the maximum length that an MPDU frame can have before the 802.11 station initiates the 802.11 request to send (RTS)/clear to send (CTS) handshake.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_SHORT_RETRY_LIMIT](https://msdn.microsoft.com/library/windows/hardware/ff569415)</p></td>
<td align="left"><p>Queries the maximum number of retransmission attempts made by the 802.11 station for MSDU packets with lengths less than or equal to the RTS threshold.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_STATION_ID](https://msdn.microsoft.com/library/windows/hardware/ff569419)</p></td>
<td align="left"><p>Queries the identifier (ID) value that uniquely identifies the 802.11 station to a remote management platform.</p></td>
</tr>
</tbody>
</table>

 

If the miniport driver is operating in Extensible Station (ExtSTA) mode, it can optionally support the automatic MAC configuration mode. For more information about this, see [Automatic MAC Configuration](automatic-mac-configuration.md).

 

 





