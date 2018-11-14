---
title: Packet Injection Functions
description: Packet Injection Functions
ms.assetid: ebbcafb6-7fbf-40e6-8806-0131aa1d4df5
keywords:
- packet injection functions WDK Windows Filtering Platform
- injection functions WDK Windows Filtering Platform
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Packet Injection Functions


A callout driver can call the following WFP functions to inject pended or modified packet data into the TCP/IP stack. The applicable layers from which data can be injected, together with possible destinations, are listed in the following table.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Injection function</th>
<th align="left">Applicable layer</th>
<th align="left">Destination</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551177" data-raw-source="[&lt;strong&gt;FwpsInjectForwardAsync0&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551177)"><strong>FwpsInjectForwardAsync0</strong></a></p></td>
<td align="left"><p>network layer</p></td>
<td align="left"><p>the forwarding data path</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551183" data-raw-source="[&lt;strong&gt;FwpsInjectNetworkReceiveAsync0&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551183)"><strong>FwpsInjectNetworkReceiveAsync0</strong></a></p></td>
<td align="left"><p>network layer</p></td>
<td align="left"><p>the receive data path</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551185" data-raw-source="[&lt;strong&gt;FwpsInjectNetworkSendAsync0&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551185)"><strong>FwpsInjectNetworkSendAsync0</strong></a></p></td>
<td align="left"><p>network layer</p></td>
<td align="left"><p>the send data path</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551186" data-raw-source="[&lt;strong&gt;FwpsInjectTransportReceiveAsync0&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551186)"><strong>FwpsInjectTransportReceiveAsync0</strong></a></p></td>
<td align="left"><p>packet data from the transport, datagram data, ICMP error, or ALE layers</p></td>
<td align="left"><p>the receive data path</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551188" data-raw-source="[&lt;strong&gt;FwpsInjectTransportSendAsync0&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551188)"><strong>FwpsInjectTransportSendAsync0</strong></a></p></td>
<td align="left"><p>packet data from the transport, datagram data, ICMP error, or ALE layers</p></td>
<td align="left"><p>the send data path</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551213" data-raw-source="[&lt;strong&gt;FwpsStreamInjectAsync0&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551213)"><strong>FwpsStreamInjectAsync0</strong></a></p></td>
<td align="left"><p>TCP data segments</p></td>
<td align="left"><p>a data stream</p></td>
</tr>
</tbody>
</table>

 

In addition, the [**FwpsQueryPacketInjectionState0**](https://msdn.microsoft.com/library/windows/hardware/ff551202) function is used to inspect the injection history of packet data.

Cross-layer injection is enabled if the callout can supply all needed information that is required by the injection function, and the net buffer list has the format expected by the injection function. For example, a callout can capture a packet at the forward path, modify its destination address to that of the local computer, and call **FwpsInjectTransportReceiveAsync0** to redirect the packet into the local computer's TCP/IP stack.

Except for the stream (TCP data) injection, injected incoming packets reenter from the "bottom" of the stack and WFP layers, while injected outgoing packets reenter from the "top" of the stack and WFP layers. For example, a UDP packet injected from the incoming datagram data layer will reenter the stack and traverse the network layer, the transport layer, the ALE receive or accept layer (optional), and back into the datagram data layer. Another UDP packet injected from the outgoing network layer will reenter the stack and traverse the ALE (optional), datagram data, and transport layers, and back to the network layer.

**FwpsInjectTransportReceiveAsync0** automatically bypasses IPsec processing for the reinjected packet because it had previously gone through IPsec verification.

A packet injected by a WFP callout driver will be re-indicated to the callout except in the cases in which modification to the packet causes it to miss the original filter conditions. WFP provides the **FwpsQueryPacketInjectionState0** function for callouts to query whether the packet was injected (or injected earlier) by the callout. To prevent infinite looping, callouts should permit self-injected packets.

Callouts must adjust the IP or transport layer checksum, or both, after they modify an IP packet. A callout can set the checksum to 0 for UDP over IPv4 packets. To be compatible with transport layer checksum offload, and to adjust the full checksum versus pseudo checksum calculations accordingly, a callout can use the following logic:

```cpp
NDIS_TCP_IP_CHECKSUM_PACKET_INFO ChecksumInfo;
 ChecksumInfo.Value = 
 (ULONG) (ULONG_PTR)NET_BUFFER_LIST_INFO(
 NetBufferList,TcpIpChecksumNetBufferListInfo);
```

If ChecksumInfo.Transmit.NdisPacketTcpChecksum is **TRUE**, the TCP send operation will be offloaded. If ChecksumInfo.Transmit.NdisPacketUdpChecksum is **TRUE**, the UDP send operation will be offloaded.

In Windows Vista with Service Pack 1 (SP1) and Windows Server 2008, if inMetaValues-&gt;headerIncludeHeaderLength is greater than 0, the outgoing packet is a RAW send reinjection that includes an IP header. To perform RAW send reinjections that include an IP header for Windows Vista with SP1 and Windows Server 2008, you must retreat the cloned packet by the amount in inMetaValues-&gt;headerIncludeHeaderLength and copy the inMetaValues-&gt;headerIncludeHeader over the newly extended space. Then, use FwpsInjectTransportSendAsync0 with the net buffer list for the packet and leave the FWPS\_TRANSPORT\_SEND\_PARAMS0 parameter set to **NULL**. For more information about retreat operations for net buffer lists, see [Retreat and Advance Operations](retreat-and-advance-operations.md).

**Note**  For raw send operations, the net buffer list must contain only a single net buffer. If your net buffer list contains more than one net buffer, you have to convert your net buffer list to a series of net buffer lists, and each in the series must contain a single net buffer. For more information about net buffer list management, see [NET\_BUFFER Architecture](net-buffer-architecture.md).

 

 

 





