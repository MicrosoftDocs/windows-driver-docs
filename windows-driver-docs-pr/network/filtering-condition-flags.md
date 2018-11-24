---
title: Filtering condition flags
description: This section describes filtering condition flags.
ms.assetid: a2493fc5-614f-47df-a818-cdec06dc9f4a
keywords:
- Filtering condition flags network drivers
ms.date: 11/08/2017
ms.localizationpriority: medium
---

# Filtering condition flags

The filtering condition flags are each represented by a bit field. These flags are defined as follows:

<table>
<tr>
<th>Filtering condition flag</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>FWP_CONDITION_FLAG_IS_LOOPBACK</p>
<p>0x00000001</p>
</td>
<td>
<p>Indicates that the network traffic is loopback traffic.</p>
<p>This flag is applicable at the following filtering layers:<dl>
<dd>FWPM_LAYER_INBOUND_IPPACKET_V4</dd>
<dd>FWPM_LAYER_INBOUND_IPPACKET_V6</dd>
<dd>FWPM_LAYER_INBOUND_IPPACKET_V4_DISCARD</dd>
<dd>FWPM_LAYER_INBOUND_IPPACKET_V6_DISCARD</dd>
<dd>FWPM_LAYER_OUTBOUND_IPPACKET_V4</dd>
<dd>FWPM_LAYER_OUTBOUND_IPPACKET_V6</dd>
<dd>FWPM_LAYER_OUTBOUND_IPPACKET_V4_DISCARD</dd>
<dd>FWPM_LAYER_OUTBOUND_IPPACKET_V6_DISCARD</dd>
<dd>FWPM_LAYER_INBOUND_TRANSPORT_V4</dd>
<dd>FWPM_LAYER_INBOUND_TRANSPORT_V6</dd>
<dd>FWPM_LAYER_INBOUND_TRANSPORT_V4_DISCARD</dd>
<dd>FWPM_LAYER_INBOUND_TRANSPORT_V6_DISCARD</dd>
<dd>FWPM_LAYER_OUTBOUND_TRANSPORT_V4</dd>
<dd>FWPM_LAYER_OUTBOUND_TRANSPORT_V6</dd>
<dd>FWPM_LAYER_OUTBOUND_TRANSPORT_V4_DISCARD</dd>
<dd>FWPM_LAYER_OUTBOUND_TRANSPORT_V6_DISCARD</dd>
<dd>FWPM_LAYER_DATAGRAM_DATA_V4</dd>
<dd>FWPM_LAYER_DATAGRAM_DATA_V6</dd>
<dd>FWPM_LAYER_DATAGRAM_DATA_V4_DISCARD</dd>
<dd>FWPM_LAYER_DATAGRAM_DATA_V6_DISCARD</dd>
<dd>FWPM_LAYER_INBOUND_ICMP_ERROR_V4</dd>
<dd>FWPM_LAYER_INBOUND_ICMP_ERROR_V6</dd>
<dd>FWPM_LAYER_INBOUND_ICMP_ERROR_V4_DISCARD</dd>
<dd>FWPM_LAYER_INBOUND_ICMP_ERROR_V6_DISCARD</dd>
<dd>FWPM_LAYER_OUTBOUND_ICMP_ERROR_V4</dd>
<dd>FWPM_LAYER_OUTBOUND_ICMP_ERROR_V6</dd>
<dd>FWPM_LAYER_OUTBOUND_ICMP_ERROR_V4_DISCARD</dd>
<dd>FWPM_LAYER_OUTBOUND_ICMP_ERROR_V6_DISCARD</dd>
<dd>FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V4</dd>
<dd>FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V6</dd>
<dd>FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V4_DISCARD</dd>
<dd>FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V6_DISCARD</dd>
<dd>FWPM_LAYER_ALE_FLOW_ESTABLISHED_V4</dd>
<dd>FWPM_LAYER_ALE_FLOW_ESTABLISHED_V6</dd>
<dd>FWPM_LAYER_ALE_FLOW_ESTABLISHED_V4_DISCARD</dd>
<dd>FWPM_LAYER_ALE_FLOW_ESTABLISHED_V6_DISCARD</dd>
</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_FLAG_IS_IPSEC_SECURED</p>
<p>0x00000002</p>
</td>
<td>
<p>Indicates that the network traffic is protected by IPsec.</p>
<p>This flag is applicable at the following filtering layers:<dl>
<dd>FWPM_LAYER_INBOUND_TRANSPORT_V4</dd>
<dd>FWPM_LAYER_INBOUND_TRANSPORT_V6</dd>
<dd>FWPM_LAYER_INBOUND_TRANSPORT_V4_DISCARD</dd>
<dd>FWPM_LAYER_INBOUND_TRANSPORT_V6_DISCARD</dd>
<dd>FWPM_LAYER_ALE_FLOW_ESTABLISHED_V4</dd>
<dd>FWPM_LAYER_ALE_FLOW_ESTABLISHED_V6</dd>
<dd>FWPM_LAYER_ALE_FLOW_ESTABLISHED_V4_DISCARD</dd>
<dd>FWPM_LAYER_ALE_FLOW_ESTABLISHED_V6_DISCARD</dd>
</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_FLAG_IS_REAUTHORIZE</p>
<p>0x00000004</p>
</td>
<td>
<p>Indicates a policy change (as opposed to a new connection).</p>
<p>This flag is applicable at the following filtering layers:<dl>
<dd>FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V4</dd>
<dd>FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V6</dd>
<dd>FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V4_DISCARD</dd>
<dd>FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V6_DISCARD</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V4</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V6</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V4_DISCARD</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V6_DISCARD</dd>
</dl>
</p>
<p>This flag is also applicable at the following filtering layers in Windows Server 2008 R2, Windows 7, and later versions of Windows:<dl>
<dd>FWPM_LAYER_ALE_BIND_REDIRECT_V4</dd>
<dd>FWPM_LAYER_ALE_BIND_REDIRECT_V6</dd>
</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_FLAG_IS_WILDCARD_BIND</p>
<p>0x00000008</p>
</td>
<td>
<p>Indicates that the application specified a wildcard address when binding to a local network address.</p>
<p>This flag is applicable at the following filtering layers:<dl>
<dd>FWPM_LAYER_ALE_RESOURCE_ASSIGNMENT_V4</dd>
<dd>FWPM_LAYER_ALE_RESOURCE_ASSIGNMENT_V6</dd>
<dd>FWPM_LAYER_ALE_RESOURCE_ASSIGNMENT_V4_DISCARD</dd>
<dd>FWPM_LAYER_ALE_RESOURCE_ASSIGNMENT_V6_DISCARD</dd>
</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_FLAG_IS_RAW_ENDPOINT</p>
<p>0x00000010</p>
</td>
<td>
<p>Indicates that the local endpoint that is sending and receiving traffic is a raw endpoint.</p>
<p>This flag is applicable at the following filtering layers:<dl>
<dd>FWPM_LAYER_INBOUND_TRANSPORT_V4</dd>
<dd>FWPM_LAYER_INBOUND_TRANSPORT_V6</dd>
<dd>FWPM_LAYER_INBOUND_TRANSPORT_V4_DISCARD</dd>
<dd>FWPM_LAYER_INBOUND_TRANSPORT_V6_DISCARD</dd>
<dd>FWPM_LAYER_OUTBOUND_TRANSPORT_V4</dd>
<dd>FWPM_LAYER_OUTBOUND_TRANSPORT_V6</dd>
<dd>FWPM_LAYER_OUTBOUND_TRANSPORT_V4_DISCARD</dd>
<dd>FWPM_LAYER_OUTBOUND_TRANSPORT_V6_DISCARD</dd>
<dd>FWPM_LAYER_DATAGRAM_DATA_V4</dd>
<dd>FWPM_LAYER_DATAGRAM_DATA_V6</dd>
<dd>FWPM_LAYER_DATAGRAM_DATA_V4_DISCARD</dd>
<dd>FWPM_LAYER_DATAGRAM_DATA_V6_DISCARD</dd>
<dd>FWPM_LAYER_INBOUND_ICMP_ERROR_V4</dd>
<dd>FWPM_LAYER_INBOUND_ICMP_ERROR_V6</dd>
<dd>FWPM_LAYER_INBOUND_ICMP_ERROR_V4_DISCARD</dd>
<dd>FWPM_LAYER_INBOUND_ICMP_ERROR_V6_DISCARD</dd>
<dd>FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V4</dd>
<dd>FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V6</dd>
<dd>FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V4_DISCARD</dd>
<dd>FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V6_DISCARD</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V4</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V6</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V4_DISCARD</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V6_DISCARD</dd>
</dl>
</p>
<p>This flag is applicable at the following filtering layers in Windows Server 2008 R2, Windows 7, and later versions of Windows:<dl>
<dd>FWPM_LAYER_ALE_CONNECT_REDIRECT_V4</dd>
<dd>FWPM_LAYER_ALE_CONNECT_REDIRECT_V6</dd>
<dd>FWPM_LAYER_ALE_BIND_REDIRECT_V4</dd>
<dd>FWPM_LAYER_ALE_BIND_REDIRECT_V6</dd>
</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_FLAG_IS_FRAGMENT</p>
<p>0x00000020</p>
</td>
<td>
<p>Indicates that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388"><b>NET_BUFFER_LIST</b></a> structure passed to a callout driver is an IP packet fragment.</p>
<p>This flag is applicable at the following filtering layers:<dl>
<dd>FWPM_LAYER_INBOUND_IPPACKET_V4</dd>
<dd>FWPM_LAYER_INBOUND_IPPACKET_V6</dd>
<dd>FWPM_LAYER_INBOUND_IPPACKET_V4_DISCARD</dd>
<dd>FWPM_LAYER_INBOUND_IPPACKET_V6_DISCARD</dd>
</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_FLAG_IS_FRAGMENT_GROUP</p>
<p>0x00000040</p>
</td>
<td>
<p>Indicates that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388"><b>NET_BUFFER_LIST</b></a> structure passed to a callout driver describes a linked list of packet
       fragments.</p>
<p>This flag is applicable at the following filtering layers:<dl>
<dd>FWPM_LAYER_INBOUND_IPPACKET_V4</dd>
<dd>FWPM_LAYER_INBOUND_IPPACKET_V6</dd>
<dd>FWPM_LAYER_INBOUND_IPPACKET_V4_DISCARD</dd>
<dd>FWPM_LAYER_INBOUND_IPPACKET_V6_DISCARD</dd>
</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_FLAG_IS_IPSEC_NATT_RECLASSIFY</p>
<p>0x00000080</p>
</td>
<td>
<p>This flag is set when an NAT Traversal (UDP port 4500) packet is indicated.  Once the decapsulation occurs, the flag is set for the reclassify using the information from the encapsulated packet.</p>
<p>This flag is applicable at the following filtering layers:<dl>
<dd>FWPM_LAYER_INBOUND_TRANSPORT_V4</dd>
<dd>FWPM_LAYER_INBOUND_TRANSPORT_V6</dd>
<dd>FWPM_LAYER_INBOUND_TRANSPORT_V4_DISCARD</dd>
<dd>FWPM_LAYER_INBOUND_TRANSPORT_V6_DISCARD</dd>
<dd>FWPM_LAYER_OUTBOUND_TRANSPORT_V4</dd>
<dd>FWPM_LAYER_OUTBOUND_TRANSPORT_V6</dd>
<dd>FWPM_LAYER_OUTBOUND_TRANSPORT_V4_DISCARD</dd>
<dd>FWPM_LAYER_OUTBOUND_TRANSPORT_V6_DISCARD</dd>
</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_FLAG_REQUIRES_ALE_CLASSIFY</p>
<p>0x00000100</p>
</td>
<td>
<p>Indicates that the packet has not yet reached the ALE receive/accept layer (FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V4 or FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V6), where its connection state will be tracked.</p>
<p>This flag is applicable at the following filtering layers:<dl>
<dd>FWPM_LAYER_INBOUND_TRANSPORT_V4</dd>
<dd>FWPM_LAYER_INBOUND_TRANSPORT_V6</dd>
<dd>FWPM_LAYER_INBOUND_TRANSPORT_V4_DISCARD</dd>
<dd>FWPM_LAYER_INBOUND_TRANSPORT_V6_DISCARD</dd>
</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_FLAG_IS_IMPLICIT_BIND</p>
<p>0x00000200</p>
</td>
<td>
<p>Indicates that the socket was not explicitly bound. If the sender  calls send without first calling bind, Windows Sockets performs an implicit bind.<div class="alert"><b>Note</b>  This flag is supported only in Windows Server 2008 and Windows Vista. It is deprecated in later Windows versions.</div>
<div> </div>
</p>
<p>This flag is applicable at the following filtering layers:<dl>
<dd>FWPM_LAYER_ALE_RESOURCE_ASSIGNMENT_V4</dd>
<dd>FWPM_LAYER_ALE_RESOURCE_ASSIGNMENT_V6</dd>
<dd>FWPM_LAYER_ALE_RESOURCE_ASSIGNMENT_V4_DISCARD</dd>
<dd>FWPM_LAYER_ALE_RESOURCE_ASSIGNMENT_V6_DISCARD</dd>
</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_FLAG_IS_REASSEMBLED</p>
<p>0x00000400</p>
</td>
<td>
<p>Indicates that the packet has been reassembled from a group of fragments.</p>
<p>This flag is applicable at the following filtering layers in Windows Server 2008, Windows Vista with Service Pack 1 (SP1), and later versions of Windows:<dl>
<dd>FWPM_LAYER_INBOUND_IPPACKET_V4</dd>
<dd>FWPM_LAYER_INBOUND_IPPACKET_V6</dd>
<dd>FWPM_LAYER_INBOUND_IPPACKET_V4_DISCARD</dd>
<dd>FWPM_LAYER_INBOUND_IPPACKET_V6_DISCARD</dd>
</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_FLAG_IS_NAME_APP_SPECIFIED</p>
<p>0x00004000</p>
</td>
<td>
<p>Indicates that the name of the peer machine that the application is expecting to connect to has been obtained by calling a function such as <a href="https://msdn.microsoft.com/library/windows/hardware/bb394822"><b>WSASetSocketPeerTargetName</b></a> and not by using the caching heuristics.</p>
<p>This flag is applicable at the following filtering layers in Windows Server 2008 R2, Windows 7, and later versions of Windows:<dl>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V4</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V6</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V4_DISCARD</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V6_DISCARD</dd>
</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_FLAG_IS_PROMISCUOUS</p>
<p>0x00008000</p>
</td>
<td>
<p>Reserved for future use.</p>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_FLAG_IS_AUTH_FW</p>
<p>0x00010000</p>
</td>
<td>
<p>Indicates that a packet matches authenticated firewall policies. Only connections matching the &quot;Allow the connection if it is secure&quot; firewall rule option will have this flag set. For more information, see <a href="http://technet.microsoft.com/library/cc753463">How to Enable Authenticated Firewall Bypass</a>.</p>
<p>This flag is also applicable at the following filtering layers in Windows Server 2008, Windows Vista with SP1, and later versions of Windows:<dl>
<dd>FWPM_LAYER_ALE_FLOW_ESTABLISHED_V4</dd>
<dd>FWPM_LAYER_ALE_FLOW_ESTABLISHED_V6</dd>
<dd>FWPM_LAYER_ALE_FLOW_ESTABLISHED_V4_DISCARD</dd>
<dd>FWPM_LAYER_ALE_FLOW_ESTABLISHED_V6_DISCARD</dd>
</dl>
</p>
<p>This flag is also applicable at the following filtering layers in Windows Server 2008 R2, Windows 7, and later versions of Windows:<dl>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V4</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V6</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V4_DISCARD</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V6_DISCARD</dd>
<dd>FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V4</dd>
<dd>FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V6</dd>
<dd>FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V4_DISCARD</dd>
<dd>FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V6_DISCARD</dd>
</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_FLAG_IS_RECLASSIFY</p>
<p>0x00020000</p>
</td>
<td>
<p>This flag is set when the <a href="https://msdn.microsoft.com/library/windows/hardware/aa832668">IPV6_PROTECTION_LEVEL</a> socket option is set on a previously authorized socket.</p>
<p>This flag is applicable at the following filtering layers:<dl>
<dd>FWPM_LAYER_ALE_RESOURCE_ASSIGNMENT_V6</dd>
<dd>FWPM_LAYER_ALE_RESOURCE_ASSIGNMENT_V6_DISCARD</dd>
<dd>FWPM_LAYER_ALE_AUTH_LISTEN_V6</dd>
<dd>FWPM_LAYER_ALE_AUTH_LISTEN_V6_DISCARD</dd>
</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_FLAG_IS_OUTBOUND_PASS_THRU</p>
<p>0x00040000</p>
</td>
<td>
<p>Indicates that the packet is weak-host sent, which means that it isn&#39;t leaving this network interface and therefore must be forwarded to another interface.</p>
<p>This flag is applicable at the following filtering layers in Windows Server 2008 R2, Windows 7, and later versions of Windows:<dl>
<dd>FWPM_LAYER_IPFORWARD_V4</dd>
<dd>FWPM_LAYER_IPFORWARD_V6</dd>
<dd>FWPM_LAYER_IPFORWARD_V4_DISCARD</dd>
<dd>FWPM_LAYER_IPFORWARD_V6_DISCARD</dd>
</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_FLAG_IS_INBOUND_PASS_THRU</p>
<p>0x00080000</p>
</td>
<td>
<p>Indicates that the packet is weak-host received, which means that it isn&#39;t destined for the receiving network interface and therefore must be forwarded to another interface.</p>
<p>This flag is applicable at the following filtering layers in Windows Server 2008 R2, Windows 7, and later versions of Windows:<dl>
<dd>FWPM_LAYER_IPFORWARD_V4</dd>
<dd>FWPM_LAYER_IPFORWARD_V6</dd>
<dd>FWPM_LAYER_IPFORWARD_V4_DISCARD</dd>
<dd>FWPM_LAYER_IPFORWARD_V6_DISCARD</dd>
</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_FLAG_IS_CONNECTION_REDIRECTED</p>
<p>0x00100000</p>
</td>
<td>
<p>Indicates that the connection was redirected by an ALE_CONNECT_REDIRECT callout function.</p>
<p>This flag is applicable at the following filtering layers in Windows Server 2008 R2, Windows 7, and later versions of Windows:<dl>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V4</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V6</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V4_DISCARD</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V6_DISCARD</dd>
</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_FLAG_IS_PROXY_CONNECTION</p>
<p>0x00200000</p>
</td>
<td>
<p>Indicates that the connection has been proxied, and therefore previous redirect records exist.</p>
<p>This flag is applicable at the following filtering layers in Windows Server 2012, Windows 8, and later versions of Windows:<dl>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V4</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V6</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V4_DISCARD</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V6_DISCARD</dd>
<dd>FWPM_LAYER_ALE_FLOW_ESTABLISHED_V4</dd>
<dd>FWPM_LAYER_ALE_FLOW_ESTABLISHED_V6</dd>
<dd>FWPM_LAYER_ALE_FLOW_ESTABLISHED_V4_DISCARD</dd>
<dd>FWPM_LAYER_ALE_FLOW_ESTABLISHED_V6_DISCARD</dd>
<dd>FWPM_LAYER_ALE_CONNECT_REDIRECT_V4</dd>
<dd>FWPM_LAYER_ALE_CONNECT_REDIRECT_V6</dd>
</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_FLAG_IS_APPCONTAINER_LOOPBACK</p>
<p>0x00400000</p>
</td>
<td>
<p>Indicates that the traffic is going to and from an AppContainer that is using loopback.</p>
<p>This flag is applicable at the following filtering layers in Windows Server 2012, Windows 8, and later versions of Windows:<dl>
<dd>FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V4</dd>
<dd>FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V6</dd>
<dd>FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V4_DISCARD</dd>
<dd>FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V6_DISCARD</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V4</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V6</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V4_DISCARD</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V6_DISCARD</dd>
</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_FLAG_IS_NON_APPCONTAINER_LOOPBACK</p>
<p>0x00800000</p>
</td>
<td>
<p>Indicates that the traffic is going to and from a standard app (not an AppContainer) that is using loopback.</p>
<p>This flag is applicable at the following filtering layers in Windows Server 2012, Windows 8, and later versions of Windows:<dl>
<dd>FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V4</dd>
<dd>FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V6</dd>
<dd>FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V4_DISCARD</dd>
<dd>FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V6_DISCARD</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V4</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V6</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V4_DISCARD</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V6_DISCARD</dd>
</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_FLAG_IS_RESERVED</p>
<p>0x01000000</p>
</td>
<td>
<p>Reserved for future use.</p>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_FLAG_IS_HONORING_POLICY_AUTHORIZE</p>
<p>0x02000000</p>
</td>
<td>
<p>Indicates that the current classification is being performed to honor the intention of a redirected Universal Windows app to connect to a specified host. Such a classification will contain the same classifiable field values as if the app were never redirected. The flag also indicates that a future classification will be invoked to match the effective redirected destination. If the app is redirected to a proxy service for inspection, it also means a future classification will be invoked on the proxy connection. Callout drivers should generally allow this classification.</p>
<p>This flag is applicable at the following filtering layers in Windows Server 2012, Windows 8, and later versions of Windows:<dl>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V4</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V6</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V4_DISCARD</dd>
<dd>FWPM_LAYER_ALE_AUTH_CONNECT_V6_DISCARD</dd>
</dl>
</p>
</td>
</tr>
</table>

