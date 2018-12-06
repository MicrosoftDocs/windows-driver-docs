---
title: Offload State Objects
description: Offload State Objects
ms.assetid: 39d0fb00-db07-4918-87a8-fd90d31107c8
keywords:
- offload state WDK TCP chimney offload , objects
- neighbor state WDK TCP chimney offload
- path state WDK TCP chimney offload
- TCP state object WDK TCP chimney offload
- constant variables WDK TCP chimney offload
- cached variables WDK TCP chimney offload
- delegated variables WDK TCP chimney offload
- variables WDK TCP chimney offload state
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Offload State Objects


\[The TCP chimney offload feature is deprecated and should not be used.\]




A *state object* is one instance of all the state variables of a particular layer of offload state. For example, a TCP connection state object contains all the constant, cached, and delegated variables of the TCP layer.

When offloading state from the host stack, an offload target stores the state for each state object in a context area that is specific to that state object. For more information about storing offloaded state, see [Storing and Referencing Offloaded State](storing-and-referencing-offloaded-state.md).

### Neighbor State Object

A neighbor state object contains the following constant, cached, and delegated variables.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Constant variable</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><em>DlSourceAddress</em></p></td>
<td align="left"><p>A 32-byte source medium access control (MAC) address. If the offload target supports software-configurable MAC addresses and <em>DISourceAddress</em> is non-<strong>NULL</strong>, the offload target must set the source MAC address of all packets that it sends on the offloaded connection to the value of <em>DlSourceAddress</em>. If the offload target does not support software-configurable MAC addresses and <em>DISourceAddress</em> is non-<strong>NULL</strong>, the offload target must fail an attempt to offload the neighbor constant state.</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>VlanId</em></p></td>
<td align="left"><p>An unsigned 12-bit binary number that identifies the virtual LAN (VLAN) to which a packet belongs. This VLAN identifier pertains only to packets that are sent or received by using the neighbor state object. When <em>VlanId</em> is <strong>NULL</strong>, it is not significant.</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Cached variable</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><em>DestinationAddress</em></p></td>
<td align="left"><p>The MAC address of the next hop (neighbor).</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>HostReachabilityDelta</em></p></td>
<td align="left"><p>The host stack&#39;s current time minus the value of <em>HostReachabilityDelta</em>, in units of clock ticks, is the last time that the host stack confirmed neighbor reachability (see forward reachability in RFC 2461). For more information about how the offload target uses this variable, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563619" data-raw-source="[&lt;strong&gt;NdisMOffloadEventIndicate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563619)"><strong>NdisMOffloadEventIndicate</strong></a>.</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Delegated variable</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><em>NicReachabilityDelta</em></p></td>
<td align="left"><p>The NIC&#39;s current time minus the value of <em>NicReachabilityDelta</em>, in units of clock ticks, is the last time that the offload target confirmed neighbor reachability (see forward reachability in RFC 2461). For more information about how the offload target uses this variable, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563619" data-raw-source="[&lt;strong&gt;NdisMOffloadEventIndicate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563619)"><strong>NdisMOffloadEventIndicate</strong></a>.</p></td>
</tr>
</tbody>
</table>

 

### Path State Object

A path state object contains the following constant, cached, and delegated variables.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Constant variable</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><em><em>SourceAddress</em></p></td>
<td align="left"><p>A pointer to the source IP address of a TCP connection. If the TCP connection is over IPv4, the address is a 4-byte IPv4 address. If the TCP connection is over IPv6, the address is a 16-byte IPv6 address. The source address bytes are always in network byte order.</p></td>
</tr>
<tr class="even">
<td align="left"><p><em></em>DestinationAddress</em></p></td>
<td align="left"><p>A pointer to the destination IP address of a TCP connection. If the TCP connection is over IPv4, the address is a 4-byte IPv4 address. If the TCP connection is over IPv6, the address is a 16-byte IPv6 address. The destination address bytes are always in network byte order.</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Cached variable</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><em>PathMtu</em></p></td>
<td align="left"><p>The maximum transmission unit (MTU) for the path (see RFC 1191 for IPv4 and RFC 1981 for IPv6).</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Delegated variable</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>None</p></td>
<td align="left"><p>Currently there is no delegated path state.</p></td>
</tr>
</tbody>
</table>

 

### TCP State Object

A TCP state connection object contains the following constant, cached, and delegated variables.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Constant variable</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><em>Flags</em></p></td>
<td align="left"><p>A bitwise OR of the following flags:</p>
<p>TCP_FLAG_TIMESTAMP_ENABLED (see RFC 1323)</p>
<p>TCP_FLAG_SACK_ENABLED (see RFC 2018)</p>
<p>TCP_FLAG_WINDOW_SCALING_ENABLED (see RFCs 2883 and 3517)</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>RemotePort</em></p></td>
<td align="left"><p>The destination port number (see RFC 793)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>LocalPort</em></p></td>
<td align="left"><p>The source port number (see RFC 793)</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>SndWindScale</em></p></td>
<td align="left"><p>The send window scale factor (see RFC 1323)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>RcvWindScale</em></p></td>
<td align="left"><p>The receive window scale factor (see RFC 1323)</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>RemoteMss</em></p></td>
<td align="left"><p>The initial maximum segment size (MSS) that is advertised by the remote endpoint during TCP connection setup (RFC 2581)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>HashValue</em></p></td>
<td align="left"><p>A 32-bit hash value that the offload target uses for <a href="ndis-receive-side-scaling2.md" data-raw-source="[Receive Side Scaling](ndis-receive-side-scaling2.md)">Receive Side Scaling</a> processing if the offload target supports RSS</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Cached variable</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><em>Flags</em></p></td>
<td align="left"><p>A bitwise OR of the following flags:</p>
<p>TCP_FLAG_KEEP_ALIVE_ENABLED (see RFC 1122)</p>
<p>TCP_FLAG_NAGLING_ENABLED (see RFC 896)</p>
<p>TCP_FLAG_KEEP_ALIVE_RESTART</p>
<p>TCP_FLAG_MAX_RT_RESTART</p>
<p>TCP_FLAG_UPDATE_RCV_WND</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>InitialRcvWnd</em></p></td>
<td align="left"><p>The default receive window (from socket option SO_RCVBUF)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>RcvIndicationSize</em></p></td>
<td align="left"><p>The optimum number of data bytes that the offload target should supply in a single call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564606" data-raw-source="[&lt;strong&gt;NdisTcpOffloadReceiveHandler&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564606)"><strong>NdisTcpOffloadReceiveHandler</strong></a> function</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>KaProbeCount</em></p></td>
<td align="left"><p>The number of keepalive probes that the offload target should send to determine whether a TCP connection is intact (see RFC 1122).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>KaTimeout</em></p></td>
<td align="left"><p>The time-out interval, in clock ticks, for inactivity before sending a keepalive probe (see RFC 1122).</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>KaInterval</em></p></td>
<td align="left"><p>The timeout, in clock ticks, after which to retransmit a keepalive frame if no response is received to a keepalive probe (see RFC 1122).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>MaxRT</em></p></td>
<td align="left"><p>The maximum time, in clock ticks, that the offload target should spend retransmitting a segment.</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>FlowLabel</em></p></td>
<td align="left"><p>A value that marks host-labeled packets for special handling by intervening routers (for example, nondefault quality of service (QoS) or &quot;real-time&quot; service (see RFC 2460)). This variable is set through a socket option and can vary during the lifetime of the TCP connection. This variable is meaningful only if the TCP connection is over IPv6.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>TtlOrHopLimit</p></td>
<td align="left"><p>If the TCP connection is over IPv4, this variable is the time to live (see RFC 791). If the TCP connection is over IPv6, this variable is the number of routers that the packet can pass through (see RFC 2460).</p></td>
</tr>
<tr class="even">
<td align="left"><p>TosOrTrafficClass</p></td>
<td align="left"><p>If the TCP connection is over IPv4, this variable is the type of service for routing a packet (see RFC 2474). If the TCP connection is over IPv6, this variable prioritizes values for packets according to traffic types, indicating how willing the sender is to have the packets discarded (see RFC 2460).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>UserPriority</p></td>
<td align="left"><p>A 3-bit 802.1p priority value.</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Delegated variable</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><em>State</em></p></td>
<td align="left"><p>The current state of the TCP connection (see RFC 793).</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>Flags</em></p></td>
<td align="left"><p>Reserved for system use.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>RcvNxt</em></p></td>
<td align="left"><p>The sequence number for the next receive segment (RCV.NEXT in RFC 793).</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>RcvWnd</em></p></td>
<td align="left"><p>The receive window size (RCV.WND in RFC 793).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>SndUna</em></p></td>
<td align="left"><p>The sequence number for the first byte of unacknowledged data (SND.UNA in RFC 793). For more information, see <a href="send-data-that-contains-data-to-be-retransmitted.md" data-raw-source="[Send Data That Contains Data to Be Retransmitted](send-data-that-contains-data-to-be-retransmitted.md)">Send Data That Contains Data to Be Retransmitted</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>SndNxt</em></p></td>
<td align="left"><p>The sequence number for the next byte to send on the connection (SND.NXT in RFC 793). For more information, see <a href="send-data-that-contains-data-to-be-retransmitted.md" data-raw-source="[Send Data That Contains Data to Be Retransmitted](send-data-that-contains-data-to-be-retransmitted.md)">Send Data That Contains Data to Be Retransmitted</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>SndMax</em></p></td>
<td align="left"><p>The maximum sequence number that has been sent on the connection. For more information, see <a href="send-data-that-contains-data-to-be-retransmitted.md" data-raw-source="[Send Data That Contains Data to Be Retransmitted](send-data-that-contains-data-to-be-retransmitted.md)">Send Data That Contains Data to Be Retransmitted</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>SndWnd</em></p></td>
<td align="left"><p>The send window size (SND.WND in RFC 793).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>MaxSndWnd</em></p></td>
<td align="left"><p>The maximum send window size (see RFC 813).</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>SndWL1</em></p></td>
<td align="left"><p>The segment sequence number that was used for the last window update (SND.WL1 in RFC 793).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>CWnd</em></p></td>
<td align="left"><p>The congestion window (cwnd in RFC 2581).</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>SsThresh</em></p></td>
<td align="left"><p>The slow start threshold (ssthresh in RFC 2581).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>SRtt</em></p></td>
<td align="left"><p>The smoothed round-trip time, in clock ticks (SRTT in RFCs 793 and 2988). This variable is maintained on a per-connection basis because it takes into account path, host, and perhaps application behavior. This variable is passed to an offload target at 8 times its value and must be passed back from an offload target as 8 times its value.</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>RttVar</em></p></td>
<td align="left"><p>The roundtrip time variation, in clock ticks (RTTVAR in RFC 2988). This variable is passed to an offload target as 4 times its value and must be passed back from an offload target as 4 times its value.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>TsRecent</em></p></td>
<td align="left"><p>The timestamp value to send in the next acknowledgment (ACK ). (TS.Recent in RFC 1323).</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>TsRecentAge</em></p></td>
<td align="left"><p>The amount of time, in clock ticks, since the most recent timestamp was received (see RFC 1323).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>TsTime</em></p></td>
<td align="left"><p>The current value of the adjusted timestamp.</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>TotalRT</em></p></td>
<td align="left"><p>The total time, in clock ticks, that has been spent transmitting the current TCP segment.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>DupAckCount</em></p></td>
<td align="left"><p>The number of ACKs that have been accepted for the same sequence number (see RFC 1323).</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>SndWndProbeCount</em></p></td>
<td align="left"><p>The current send window probe round. For a description of the send window probe round, see <a href="persist-timer.md" data-raw-source="[Persist Timer](persist-timer.md)">Persist Timer</a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>Keepalive ProbeCount</em></p></td>
<td align="left"><p>The number of keepalive probes that have been sent that have not received a response (see RFC 1122).</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>Keepalive TimeoutDelta</em></p></td>
<td align="left"><p>The time, in clock ticks, that remains until the next keepalive time-out (see RFC 1122).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>Retransmit Count</em></p></td>
<td align="left"><p>The number of retransmits that have been sent (see RFC 2581).</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>Retransmit TimeoutDelta</em></p></td>
<td align="left"><p>The time that remains until the next retransmit time-out (see RFC 2581).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>SendDataHead</em></p></td>
<td align="left"><p>A pointer to the first <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388" data-raw-source="[&lt;strong&gt;NET_BUFFER_LIST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568388)"><strong>NET_BUFFER_LIST</strong></a> structure whose <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376" data-raw-source="[&lt;strong&gt;NET_BUFFER&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568376)"><strong>NET_BUFFER</strong></a> structure has send data associated with it. This variable is used only in an initiate offload or terminate offload operation. For more information about handling such send data, see <a href="handling-outstanding-send-data-during-and-after-an-offload-operation.md" data-raw-source="[Handling Outstanding Send Data During and After an Offload Operation](handling-outstanding-send-data-during-and-after-an-offload-operation.md)">Handling Outstanding Send Data During and After an Offload Operation</a> and <a href="handling-outstanding-send-data-during-a-terminate-offload-operation.md" data-raw-source="[Handling Outstanding Send Data During a Terminate Offload Operation](handling-outstanding-send-data-during-a-terminate-offload-operation.md)">Handling Outstanding Send Data During a Terminate Offload Operation</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>SendDataTail</em></p></td>
<td align="left"><p>A pointer to the last NET_BUFFER_LIST structure whose NET_BUFFER structure has send data associated with it. This variable is used only in an initiate offload or terminate offload operation. For more information about handling such send data, see <a href="handling-outstanding-send-data-during-and-after-an-offload-operation.md" data-raw-source="[Handling Outstanding Send Data During and After an Offload Operation](handling-outstanding-send-data-during-and-after-an-offload-operation.md)">Handling Outstanding Send Data During and After an Offload Operation</a> and <a href="handling-outstanding-send-data-during-a-terminate-offload-operation.md" data-raw-source="[Handling Outstanding Send Data During a Terminate Offload Operation](handling-outstanding-send-data-during-a-terminate-offload-operation.md)">Handling Outstanding Send Data During a Terminate Offload Operation</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>SendBacklogSize</em></p></td>
<td align="left"><p>The optimum number of send data bytes that should be outstanding (that is, sent by the host stack and not yet completed by the offload target) at any given time. The offload target should specify a number that maximizes throughput while consuming the least possible amount of resources. The offload target returns a value for this variable in response to a query of delegated state.</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>BufferedData</em></p></td>
<td align="left"><p>A pointer to buffered receive data. The host stack can pass such data to the offload target when offloading a TCP connection. (For more information about handling such buffered receive data, see <a href="handling-buffered-receive-data-during-and-after-an-offload-operation.md" data-raw-source="[Handling Buffered Receive Data During and After an Offload Operation](handling-buffered-receive-data-during-and-after-an-offload-operation.md)">Handling Buffered Receive Data During and After an Offload Operation</a>.) The offload target can pass such data to the host stack when uploading a TCP connection. (For more information about handling such buffered receive data, see <a href="handling-buffered-receive-data-during-a-terminate-offload-operation.md" data-raw-source="[Handling Buffered Receive Data During a Terminate Offload Operation](handling-buffered-receive-data-during-a-terminate-offload-operation.md)">Handling Buffered Receive Data During a Terminate Offload Operation</a>.) This variable is used only in an initiate offload or terminate offload operation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>ReceiveBacklogSize</em></p></td>
<td align="left"><p>The number of receive data bytes that are buffered in the offload target for the offloaded TCP connection. The host stack uses this value to post one or more receive requests that are large enough to hold all of the buffered data. The offload target returns a value for this variable only in response to a query of delegated state.</p></td>
</tr>
</tbody>
</table>

 

 

 





