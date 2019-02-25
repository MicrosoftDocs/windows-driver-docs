---
title: Data offset positions
description: This section describes Data offset positions for Windows Filtering Platform callout drivers.
ms.assetid: cf4656cf-b978-4539-9fff-8f0aa5de1b5e
keywords:
- Data offset positions network drivers
ms.date: 11/09/2017
ms.localizationpriority: medium
---

# Data offset positions

When the filter engine calls a callout driver's [classifyFn](https://msdn.microsoft.com/library/windows/hardware/ff544890) callout function, it passes a pointer to a structure in the *layerData* parameter. For the layers that filter packet data, the pointer references a [NET_BUFFER_LIST](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure. Depending on the filtering layer at which the *classifyFn* callout function is called, the filter engine passes a pointer in the layerData* parameter to one of the following structures:

- For the stream layer, the *layerData* parameter contains a pointer to an [FWPS_STREAM_CALLOUT_IO_PACKET0](https://msdn.microsoft.com/library/windows/hardware/ff552417) structure. The streamData member of this structure contains a pointer to an [FWPS_STREAM_DATA0](https://msdn.microsoft.com/library/windows/hardware/ff552419) structure. 

    The **netBufferListChain** member of the [FWPS_STREAM_DATA0](https://msdn.microsoft.com/library/windows/hardware/ff552419) structure contains a pointer to a [NET_BUFFER_LIST](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure. 

- For all the other layers, the *layerData* parameter contains a pointer to a [NET_BUFFER_LIST](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

> [!NOTE]
> The *layerData* parameter might be NULL, depending on the layer being filtered and the conditions under which the driver's [classifyFn](https://msdn.microsoft.com/library/windows/hardware/ff544890) callout function is called.
 
The [NET_BUFFER_LIST](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure contains a linked list of [NET_BUFFER](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures. Within the [NET_BUFFER_DATA](https://msdn.microsoft.com/library/windows/hardware/ff568381) structure of each **NET_BUFFER** structure, the **DataOffset** member points to a specific position in the packet data. The position that the **DataOffset** member points to depends on the filtering layer at which the filter engine calls the callout driver's *classifyFn* callout function. 

For each filtering layer, the position in the packet data as specified by the **DataOffset** member is defined as follows:

<table>
<tr>
<th>Run-time filtering layer identifier (starting with Windows Vista)</th>
<th>Position in the packet data</th>
</tr>
<tr>
<td>
<p>FWPS_LAYER_INBOUND_IPPACKET_V4</p>
<p>FWPS_LAYER_INBOUND_IPPACKET_V6</p>
</td>
<td>
<p>The beginning of the transport header.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_INBOUND_IPPACKET_V4_DISCARD</p>
<p>FWPS_LAYER_INBOUND_IPPACKET_V6_DISCARD</p>
</td>
<td>
<p>The offset where the TCP/IP stack stopped processing.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_OUTBOUND_IPPACKET_V4</p>
<p>FWPS_LAYER_OUTBOUND_IPPACKET_V6</p>
</td>
<td>
<p>The beginning of the IP header.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_OUTBOUND_IPPACKET_V4_DISCARD</p>
<p>FWPS_LAYER_OUTBOUND_IPPACKET_V6_DISCARD</p>
</td>
<td>
<p>The offset where the TCP/IP stack stopped processing.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_IPFORWARD_V4</p>
<p>FWPS_LAYER_IPFORWARD_V6</p>
</td>
<td>
<p>The beginning of the IP header.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_IPFORWARD_V4_DISCARD</p>
<p>FWPS_LAYER_IPFORWARD_V6_DISCARD</p>
</td>
<td>
<p>The beginning of the IP header.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_INBOUND_TRANSPORT_V4</p>
<p>FWPS_LAYER_INBOUND_TRANSPORT_V6</p>
</td>
<td>
<p>The beginning of the data.</p>
<div class="alert"><b>Note</b>  For inbound packets received on the ICMP socket of the TCP/IP stack, the offset is the beginning of the ICMP header.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_INBOUND_TRANSPORT_V4_DISCARD</p>
<p>FWPS_LAYER_INBOUND_TRANSPORT_V6_DISCARD</p>
</td>
<td>
<p>The beginning of the data.</p>
<div class="alert"><b>Note</b>  For inbound packets received on the ICMP socket of the TCP/IP stack, the offset is the beginning of the ICMP header.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_OUTBOUND_TRANSPORT_V4</p>
<p>FWPS_LAYER_OUTBOUND_TRANSPORT_V6</p>
</td>
<td>
<p>The beginning of the transport header.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_OUTBOUND_TRANSPORT_V4_DISCARD</p>
<p>FWPS_LAYER_OUTBOUND_TRANSPORT_V6_DISCARD</p>
</td>
<td>
<p>The beginning of the transport header.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_STREAM_V4</p>
<p>FWPS_LAYER_STREAM_V6</p>
</td>
<td>
<p>The beginning of the data.</p>
<div class="alert"><b>Note</b>   The position in the packet data contains no IP, IPv6, and transport headers.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_STREAM_V4_DISCARD</p>
<p>FWPS_LAYER_STREAM_V6_DISCARD</p>
</td>
<td>
<p>The beginning of the data.</p>
<div class="alert"><b>Note</b>   The position in the packet data contains no IP, IPv6, or transport headers.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_DATAGRAM_DATA_V4</p>
<p>FWPS_LAYER_DATAGRAM_DATA_V6</p>
</td>
<td>
<p>For inbound datagrams: The beginning of the data.</p>
<div class="alert"><b>Note</b>  For inbound packets received on the ICMP socket of the TCP/IP stack, the offset is the beginning of the ICMP header.</div>
<div> </div>
<p>For outbound datagrams: The beginning of the transport header.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_DATAGRAM_DATA_V4_DISCARD</p>
<p>FWPS_LAYER_DATAGRAM_DATA_V6_DISCARD</p>
</td>
<td>
<p>For inbound datagrams: The beginning of the data.</p>
<div class="alert"><b>Note</b>  For inbound packets received on the ICMP socket of the TCP/IP stack, the offset is the beginning of the ICMP header.</div>
<div> </div>
<p>For outbound datagrams: The beginning of the transport header.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_INBOUND_ICMP_ERROR_V4</p>
<p>FWPS_LAYER_INBOUND_ICMP_ERROR_V6</p>
</td>
<td>
<p>The beginning of the inner IP header.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_INBOUND_ICMP_ERROR_V4_DISCARD</p>
<p>FWPS_LAYER_INBOUND_ICMP_ERROR_V6_DISCARD</p>
</td>
<td>
<p>The beginning of the inner IP header.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_OUTBOUND_ICMP_ERROR_V4</p>
<p>FWPS_LAYER_OUTBOUND_ICMP_ERROR_V6</p>
</td>
<td>
<p>The beginning of the ICMP header.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_OUTBOUND_ICMP_ERROR_V4_DISCARD</p>
<p>FWPS_LAYER_OUTBOUND_ICMP_ERROR_V6_DISCARD</p>
</td>
<td>
<p>The beginning of the ICMP header.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_ALE_RESOURCE_ASSIGNMENT_V4</p>
<p>FWPS_LAYER_ALE_RESOURCE_ASSIGNMENT_V6</p>
</td>
<td>
<p>Not applicable.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_ALE_RESOURCE_ASSIGNMENT_V4_DISCARD</p>
<p>FWPS_LAYER_ALE_RESOURCE_ASSIGNMENT_V6_DISCARD</p>
</td>
<td>
<p>Not applicable.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_ALE_AUTH_LISTEN_V4</p>
<p>FWPS_LAYER_ALE_AUTH_LISTEN_V6</p>
</td>
<td>
<p>Not applicable.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_ALE_AUTH_LISTEN_V4_DISCARD</p>
<p>FWPS_LAYER_ALE_AUTH_LISTEN_V6_DISCARD</p>
</td>
<td>
<p>Not applicable.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_ALE_AUTH_RECV_ACCEPT_V4</p>
<p>FWPS_LAYER_ALE_AUTH_RECV_ACCEPT_V6</p>
</td>
<td>
<p>For inbound packet direction: The beginning of the data.</p>
<div class="alert"><b>Note</b>  For inbound packets received on the ICMP socket of the TCP/IP stack, the offset is the beginning of the ICMP header.</div>
<div> </div>
<p>For outbound packet direction: The beginning of the transport header.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_ALE_AUTH_RECV_ACCEPT_V4_DISCARD</p>
<p>FWPS_LAYER_ALE_AUTH_RECV_ACCEPT_V6_DISCARD</p>
</td>
<td>
<p>For inbound packet direction: The beginning of the data.</p>
<div class="alert"><b>Note</b>  For inbound packets received on the ICMP socket of the TCP/IP stack, the offset is the beginning of the ICMP header.</div>
<div> </div>
<p>For outbound packet direction: The beginning of the transport header.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_ALE_AUTH_CONNECT_V4</p>
<p>FWPS_LAYER_ALE_AUTH_CONNECT_V6</p>
</td>
<td>
<p>For non-TCP traffic: The beginning of the transport header.</p>
<p>For TCP traffic: Not applicable.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_ALE_AUTH_CONNECT_V4_DISCARD</p>
<p>FWPS_LAYER_ALE_AUTH_CONNECT_V6_DISCARD</p>
</td>
<td>
<p>For non-TCP traffic: The beginning of the transport header.</p>
<p>For TCP traffic: Not applicable.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_ALE_FLOW_ESTABLISHED_V4</p>
<p>FWPS_LAYER_ALE_FLOW_ESTABLISHED_V6</p>
</td>
<td>
<p>For inbound packet direction: The beginning of the data.</p>
<div class="alert"><b>Note</b>  For inbound packets received on the ICMP socket of the TCP/IP stack, the offset is the beginning of the ICMP header.</div>
<div> </div>
<p>For outbound packet direction: The beginning of the transport header.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_ALE_FLOW_ESTABLISHED_V4_DISCARD</p>
<p>FWPS_LAYER_ALE_FLOW_ESTABLISHED_V6_DISCARD</p>
</td>
<td>
<p>For inbound packet direction: The beginning of the data.</p>
<div class="alert"><b>Note</b>  For inbound packets received on the ICMP socket of the TCP/IP stack, the offset is the beginning of the ICMP header.</div>
<div> </div>
<p>For outbound packet direction: The beginning of the transport header.
      </p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_IPSEC_KM_DEMUX_V4</p>
<p>FWPS_LAYER_IPSEC_KM_DEMUX_V6</p>
</td>
<td>
<p>Not applicable.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_IPSEC_V4</p>
<p>FWPS_LAYER_IPSEC_V6</p>
</td>
<td>
<p>Not applicable.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_IKEEXT_V4</p>
<p>FWPS_LAYER_IKEEXT_V6</p>
</td>
<td>
<p>Not applicable.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_RPC_UM</p>
</td>
<td>
<p>Not applicable.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_RPC_EPMAP</p>
</td>
<td>
<p>Not applicable.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_RPC_EP_ADD</p>
</td>
<td>
<p>Not applicable.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_RPC_PROXY_CONN</p>
</td>
<td>
<p>Not applicable.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_RPC_PROXY_IF</p>
</td>
<td>
<p>Not applicable.</p>
</td>
</tr>
<tr>
<th>Run-time filtering layer identifier (starting with Windows 7)</th>
<th>Position in the packet data</th>
</tr>
<tr>
<td>
<p>FWPS_LAYER_NAME_RESOLUTION_CACHE_V4</p>
<p>
FWPS_LAYER_NAME_RESOLUTION_CACHE_V6</p>
</td>
<td>
<p>Not applicable.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_ALE_RESOURCE_RELEASE_V4</p>
<p>FWPS_LAYER_ALE_RESOURCE_RELEASE_V6</p>
</td>
<td>
<p>Not applicable.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_ALE_ENDPOINT_CLOSURE_V4</p>
<p>FWPS_LAYER_ALE_ENDPOINT_CLOSURE_V6</p>
</td>
<td>
<p>Not applicable.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_ALE_CONNECT_REDIRECT_V4</p>
<p>FWPS_LAYER_ALE_CONNECT_REDIRECT_V6</p>
</td>
<td>
<p>Not applicable.</p>
<div class="alert"><b>Note</b>  For these filtering layers, the <i><em>layerData</em></i> parameter contains a pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551231"><b>FWPS_CONNECT_REQUEST0</b></a> structure. This structure does  not reference a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388"><b>NET_BUFFER_LIST</b></a> structure that describes packet data.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_ALE_BIND_REDIRECT_V4</p>
<p>FWPS_LAYER_ALE_BIND_REDIRECT_V6</p>
</td>
<td>
<p>Not applicable.</p>
<div class="alert"><b>Note</b>  For these filtering layers, the  <i><em>layerData</em></i> parameter contains a pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551221"><b>FWPS_BIND_REQUEST0</b></a> structure. This structure does  not reference a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388"><b>NET_BUFFER_LIST</b></a> structure that describes packet data.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_STREAM_PACKET_V4</p>
<p>FWPS_LAYER_STREAM_PACKET_V6</p>
</td>
<td>
<p>For inbound packet direction: The beginning of the data.</p>
<p>For outbound packet direction: The beginning of the transport header.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_KM_AUTHORIZATION</p>
</td>
<td>
<p>Not applicable.</p>
</td>
</tr>
<tr>
<th>Run-time filtering layer identifier (starting with Windows 8)</th>
<th>Position in the packet data</th>
</tr>
<tr>
<td>
<p>FWPS_LAYER_INBOUND_MAC_FRAME_ETHERNET</p>
</td>
<td>
<p>The beginning of the IP header.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_OUTBOUND_MAC_FRAME_ETHERNET</p>
</td>
<td>
<p>The beginning of the MAC header.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_INBOUND_MAC_FRAME_NATIVE</p>
</td>
<td>
<p>The beginning of the MAC header.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_OUTBOUND_MAC_FRAME_NATIVE</p>
</td>
<td>
<p>The beginning of the MAC header.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_INGRESS_VSWITCH_ETHERNET</p>
</td>
<td>
<p>The beginning of the ethernet header.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_EGRESS_VSWITCH_ETHERNET</p>
</td>
<td>
<p>The beginning of the ethernet header.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_INGRESS_VSWITCH_TRANSPORT_V4</p>
</td>
<td>
<p>The beginning of the IP header.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_INGRESS_VSWITCH_TRANSPORT_V6</p>
</td>
<td>
<p>The beginning of the IP header.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_EGRESS_VSWITCH_TRANSPORT_V4</p>
</td>
<td>
<p>The beginning of the IP header.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_EGRESS_VSWITCH_TRANSPORT_V6</p>
</td>
<td>
<p>The beginning of the IP header.</p>
</td>
</tr>
</table>

