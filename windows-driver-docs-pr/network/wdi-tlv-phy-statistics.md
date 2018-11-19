---
title: WDI_TLV_PHY_STATISTICS
description: WDI_TLV_PHY_STATISTICS is a TLV that contains per-PHY statistics for OID_WDI_GET_STATISTICS.
ms.assetid: 2F27FF4E-54AC-4518-AEB0-3518FBC8BE0F
ms.date: 07/18/2017
keywords:
 - WDI_TLV_PHY_STATISTICS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_PHY\_STATISTICS


WDI\_TLV\_PHY\_STATISTICS is a TLV that contains per-PHY statistics for [OID\_WDI\_GET\_STATISTICS](https://msdn.microsoft.com/library/windows/hardware/dn925850).

## TLV Type


0xA7

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn926105" data-raw-source="[&lt;strong&gt;WDI_PHY_TYPE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn926105)"><strong>WDI_PHY_TYPE</strong></a></td>
<td>The type for this PHY.</td>
</tr>
<tr class="even">
<td>UINT64</td>
<td>The number of MSDU packets and MMPDU frames that the IEEE PHY layer of the 802.11 station has successfully transmitted.</td>
</tr>
<tr class="odd">
<td>UINT64</td>
<td>The number of multicast or broadcast MSDU packets and MMPDU frames that the IEEE PHY layer of the 802.11 station has successfully transmitted.</td>
</tr>
<tr class="even">
<td>UINT64</td>
<td>The number of MSDU packets and MMPDU frames that the 802.11 station failed to transmit after exceeding the retry limits defined by the 802.11 IEEE dot11ShortRetryLimit or dot11LongRetryLimit MIB counters.</td>
</tr>
<tr class="odd">
<td>UINT64</td>
<td>The number of MSDU packets and MMPDU frames that the 802.11 station successfully transmitted after one or more attempts.</td>
</tr>
<tr class="even">
<td>UINT64</td>
<td>The number of MSDU packets and MMPDU frames that the 802.11 station successfully transmitted after more than one retransmission attempts.
<p>For MSDU packets, the port must increment this counter for each packet that was transmitted successfully after one or more of its MPDU fragments required retransmission.</p></td>
</tr>
<tr class="odd">
<td>UINT64</td>
<td>The number of MSDU packets and MMPDU frames that the 802.11 station failed to transmit because of a timeout as defined by the IEEE 802.11 dot11MaxTransmitMSDULifetime MIB object.</td>
</tr>
<tr class="even">
<td>UINT64</td>
<td>The number of MPDU frames that the 802.11 station transmitted and acknowledged through a received 802.11 ACK frame.</td>
</tr>
<tr class="odd">
<td>UINT64</td>
<td>The number of times that the 802.11 station received a Clear To Send (CTS) frame in response to a Request To Send (RTS) frame. If this cannot be maintained per port, it can be maintained per channel.</td>
</tr>
<tr class="even">
<td>UINT64</td>
<td>The number of times that the 802.11 station did not receive a CTS frame in response to an RTS frame. If this cannot be maintained per port, it can be maintained per channel.</td>
</tr>
<tr class="odd">
<td>UINT64</td>
<td>The number of times that the 802.11 station expected and did not receive an Acknowledgment (ACK) frame. If this cannot be maintained per port, it can be maintained per channel.</td>
</tr>
<tr class="even">
<td>UINT64</td>
<td>The number of MSDU packets and MMPDU frames that the 802.11 station has successfully received.
<p>For MSDU packets, the port must increment this counter for each packet whose MPDU fragments were received and passed frame check sequence (FCS) verification and replay detection. The port must increment this member regardless of whether the received MSDU packet or MPDU fragment fail MAC-layer cipher decryption.</p></td>
</tr>
<tr class="odd">
<td>UINT64</td>
<td>The number of multicast or broadcast MSDU packets and MMPDU frames that the 802.11 station has successfully received.
<p>For MSDU packets, the port must increment this counter for each packet whose MPDU fragments were received and passed FCS verification and replay detection. The port must increment this member regardless of whether the received MSDU packet or MPDU fragment fail MAC-layer cipher decryption.</p></td>
</tr>
<tr class="even">
<td>UINT64</td>
<td>The number of MSDU packets or MMPDU frames received by the 802.11 station when a promiscuous packet filter is enabled. If this cannot be maintained per port, it can be maintained per channel.</td>
</tr>
<tr class="odd">
<td>UINT64</td>
<td>The number if MSDU packets and MMPDU frames that the 802.11 station discarded because of a timeout as defined by the IEEE 802.11 dot11MaxReceiveLifetime MIB object. If this cannot be maintained per port, it can be maintained per channel.</td>
</tr>
<tr class="even">
<td>UINT64</td>
<td>The number of duplicate MPDU frames that the 802.11 station received. The 802.11 station determines duplicate frames through the Sequence Control field of the 802.11 MAC header. If this cannot be maintained per port, it can be maintained per channel.</td>
</tr>
<tr class="odd">
<td>UINT64</td>
<td>The number of MPDU frames received by the 802.11 station for MSDU packets or MMPDU frames.</td>
</tr>
<tr class="even">
<td>UINT64</td>
<td>The number of MPDU frames received by the 802.11 station for MSDU packets or MMPDU frames when a promiscuous packet filter was enabled.</td>
</tr>
<tr class="odd">
<td>UINT64</td>
<td>The number of MPDU frames that the 802.11 station received with FCS errors. If this cannot be maintained per port, it can be maintained per channel.</td>
</tr>
</tbody>
</table>

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Wditypes.hpp</td>
</tr>
</tbody>
</table>

 

 




