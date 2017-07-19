---
title: WDI\_TLV\_PHY\_STATISTICS
author: windows-driver-content
description: WDI\_TLV\_PHY\_STATISTICS is a TLV that contains per-PHY statistics for OID\_WDI\_GET\_STATISTICS.
ms.assetid: 2F27FF4E-54AC-4518-AEB0-3518FBC8BE0F
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_PHY_STATISTICS Network Drivers Starting with Windows Vista
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
<td>[<strong>WDI_PHY_TYPE</strong>](https://msdn.microsoft.com/library/windows/hardware/dn926105)</td>
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_PHY_STATISTICS%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


