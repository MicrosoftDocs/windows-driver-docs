---
title: Filtering condition identifiers
description: This section describes filtering condition identifiers.
ms.assetid: 53321aea-6406-426a-a541-2626faad2232
keywords:
- Filtering condition identifiers network drivers
ms.date: 11/08/2017
ms.localizationpriority: medium
---

# Filtering condition identifiers

The filtering condition identifiers are each represented by a GUID. These identifiers are described in the following table.

<table>
<tr>
<th>Filtering condition identifier</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_ARRIVAL_INTERFACE_INDEX</p>
</td>
<td>
<p>The index of the arrival network interface, as enumerated by the network stack.</p>
<p>WFP uses the Arrival interface to match this condition. The Arrival Interface is the first interface the
       packet sees before entering the IP stack inbound from the network, before weak-host or forwarding are
       performed.</p>
<p>This condition is asymmetric for reauthorization purposes, as it is intrinsically an inbound condition. This
       means that WFP will use an empty value on this condition when reauthorizing an inbound connection on a response
       outbound packet.</p>
<p>To handle reauthorization a second filter must be used. This second filter can either permit or block the
       empty values, or use a different condition that will have a valid value for such circumstance. In the case of
       arrival interface conditions, the next hop class of interface conditions will have a valid interface on outbound
       packets.</p>
<div class="alert"><b>Note</b><br/>Available only in Windows Server 2008 R2, Windows 7, and later versions of
       Windows.
</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_ARRIVAL_INTERFACE_TYPE</p>
</td>
<td>
<p>The type of the arrival network interface, as defined by the Internet Assigned Numbers Authority (IANA). For
       more information, see 
       <a href="http://www.iana.org/assignments/ianaiftype-mib/ianaiftype-mib">IANAifType-MIB Definitions</a>.</p>
<p>WFP uses the Arrival interface to match this condition. The Arrival Interface is the first interface the
       packet sees before entering the IP stack inbound from the network, before weak-host or forwarding are
       performed.</p>
<p>This condition is asymmetric for reauthorization purposes, as it is intrinsically an inbound condition. This
       means that WFP will use an empty value on this condition when reauthorizing an inbound connection on a response
       outbound packet.</p>
<p>To handle reauthorization a second filter must be used. This second filter can either permit or block the
       empty values, or use a different condition that will have a valid value for such circumstance. In the case of
       arrival interface conditions, the next hop class of interface conditions will have a valid interface on outbound
       packets.</p>
<div class="alert"><b>Note</b><br/>Available only in Windows Server 2008 R2, Windows 7, and later versions of
       Windows.
</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_ARRIVAL_TUNNEL_TYPE</p>
</td>
<td>
<p>The encapsulation method used by a tunnel if the IfType member of the <a href="https://msdn.microsoft.com/library/windows/hardware/aa366058"><b>IP_ADAPTER_ADDRESSES</b></a> structure is
       IF_TYPE_TUNNEL. The tunnel type is defined by the IANA. For more information, see 
       <a href="http://www.iana.org/assignments/ianaiftype-mib/ianaiftype-mib">IANAifType-MIB Definitions</a>and the Windows
       SDK <a href="https://msdn.microsoft.com/library/windows/hardware/ff557015">IP Helper</a> documentation.</p>
<p>WFP uses the Arrival interface to match this condition. The Arrival Interface is the first interface the
       packet sees before entering the IP stack inbound from the network, before weak-host or forwarding are
       performed.</p>
<p>This condition is asymmetric for reauthorization purposes, as it is intrinsically an inbound condition. This
       means that WFP will use an empty value on this condition when reauthorizing an inbound connection on a response
       outbound packet.</p>
<p>To handle reauthorization a second filter must be used. This second filter can either permit or block the
       empty values, or use a different condition that will have a valid value for such circumstance. In the case of
       arrival interface conditions, the next hop class of interface conditions will have a valid interface on outbound
       packets.</p>
<div class="alert"><b>Note</b><br/>Available only in Windows Server 2008 R2, Windows 7, and later versions of
       Windows.
</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_IP_ARRIVAL_INTERFACE</p>
</td>
<td>
<p>The 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff557080"><b>LUID</b></a> for the network interface that is associated with the
       arrival IP address.</p>
<p>WFP uses the Arrival interface to match this condition. The Arrival Interface is the first interface the
       packet sees before entering the IP stack inbound from the network, before weak-host or forwarding are
       performed.</p>
<p>This condition is asymmetric for reauthorization purposes, as it is intrinsically an inbound condition. This
       means that WFP will use an empty value on this condition when reauthorizing an inbound connection on a response
       outbound packet.</p>
<p>To handle reauthorization a second filter must be used. This second filter can either permit or block the
       empty values, or use a different condition that will have a valid value for such circumstance. In the case of
       arrival interface conditions, the next hop class of interface conditions will have a valid interface on outbound
       packets.</p>
<div class="alert"><b>Note</b><br/>Available only in Windows Server 2008 R2, Windows 7, and later versions of
       Windows.
</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_NEXTHOP_INTERFACE_INDEX</p>
</td>
<td>
<p>The index of the arrival network interface, as enumerated by the network stack.</p>
<p>WFP uses the Next Hop interface to match this condition. The Next Hop Interface is the last interface the
       packet sees before leaving the IP stack outbound towards the network, after weak-host or forwarding are
       performed.</p>
<p>This condition is asymmetric for reauthorization purposes, as it is intrinsically an outbound condition. This
       means that WFP will use an empty value on this condition when reauthorizing an outbound connection on a response
       inbound packet.</p>
<p>To handle reauthorization a second filter must be used. This second filter can either permit or block the
       empty values, or use a different condition that will have a valid value for such circumstance. In the case of
       next hop interface conditions, the arrival class of interface conditions will have a valid interface on inbound
       packets.</p>
<div class="alert"><b>Note</b><br/>Available only in Windows Server 2008 R2, Windows 7, and later versions of
       Windows.
</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_NEXTHOP_INTERFACE_TYPE</p>
</td>
<td>
<p>The type of the arrival network interface, as defined by the Internet Assigned Numbers Authority (IANA). For
       more information, see 
       <a href="http://www.iana.org/assignments/ianaiftype-mib/ianaiftype-mib">IANAifType-MIB Definitions</a>.</p>
<p>WFP uses the Next Hop interface to match this condition. The Next Hop Interface is the last interface the
       packet sees before leaving the IP stack outbound towards the network, after weak-host or forwarding are
       performed.</p>
<p>This condition is asymmetric for reauthorization purposes, as it is intrinsically an outbound condition. This
       means that WFP will use an empty value on this condition when reauthorizing an outbound connection on a response
       inbound packet.</p>
<p>To handle reauthorization a second filter must be used. This second filter can either permit or block the
       empty values, or use a different condition that will have a valid value for such circumstance. In the case of
       next hop interface conditions, the arrival class of interface conditions will have a valid interface on inbound
       packets.</p>
<div class="alert"><b>Note</b><br/>Available only in Windows Server 2008 R2, Windows 7, and later versions of
       Windows.
</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_NEXTHOP_TUNNEL_TYPE</p>
</td>
<td>
<p>The encapsulation method used by a tunnel if the <b>IfType</b> member of the  <a href="https://msdn.microsoft.com/library/windows/hardware/aa366058"><b>IP_ADAPTER_ADDRESSES</b></a> structure is
       IF_TYPE_TUNNEL. The tunnel type is defined by the IANA. For more information, see 
       <a href="http://www.iana.org/assignments/ianaiftype-mib/ianaiftype-mib">IANAifType-MIB Definitions</a> and the Windows
       SDK <a href="https://msdn.microsoft.com/library/windows/hardware/ff557015">IP Helper</a> documentation.</p>
<p>WFP uses the Next Hop interface to match this condition. The Next Hop Interface is the last interface the
       packet sees before leaving the IP stack outbound towards the network, after weak-host or forwarding are
       performed.</p>
<p>This condition is asymmetric for reauthorization purposes, as it is intrinsically an outbound condition. This
       means that WFP will use an empty value on this condition when reauthorizing an outbound connection on a response
       inbound packet.</p>
<p>To handle reauthorization a second filter must be used. This second filter can either permit or block the
       empty values, or use a different condition that will have a valid value for such circumstance. In the case of
       next hop interface conditions, the arrival class of interface conditions will have a valid interface on inbound
       packets.</p>
<div class="alert"><b>Note</b><br/>Available only in Windows Server 2008 R2, Windows 7, and later versions of
       Windows.
</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_IP_NEXTHOP_INTERFACE</p>
</td>
<td>
<p>The 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff557080"><b>LUID</b></a>for the network interface that is associated with the
       arrival IP address.</p>
<p>WFP uses the Next Hop interface to match this condition. The Next Hop Interface is the last interface the
       packet sees before leaving the IP stack outbound towards the network, after weak-host or forwarding are
       performed.</p>
<p>This condition is asymmetric for reauthorization purposes, as it is intrinsically an outbound condition. This
       means that WFP will use an empty value on this condition when reauthorizing an outbound connection on a response
       inbound packet.</p>
<p>To handle reauthorization a second filter must be used. This second filter can either permit or block the
       empty values, or use a different condition that will have a valid value for such circumstance. In the case of
       next hop interface conditions, the arrival class of interface conditions will have a valid interface on inbound
       packets.</p>
<div class="alert"><b>Note</b><br/>Available only in Windows Server 2008 R2, Windows 7, and later versions of
       Windows.
</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_IP_LOCAL_ADDRESS</p>
</td>
<td>
<p>The local IP address.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_IP_REMOTE_ADDRESS</p>
</td>
<td>
<p>The remote IP address.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_IP_SOURCE_ADDRESS</p>
</td>
<td>
<p>The source IP address for forwarded packets.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_IP_DESTINATION_ADDRESS</p>
</td>
<td>
<p>The destination IP address for forwarded packets.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_IP_LOCAL_ADDRESS_TYPE</p>
</td>
<td>
<p>The local IP address type. The possible condition values are:</p>
<p>
<dl>
<dd>
NlatUnspecified

</dd>
<dd>
NlatUnicast

</dd>
<dd>
NlatAnycast

</dd>
<dd>
NlatMulticast

</dd>
<dd>
NlatBroadcast
</dd>
</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_IP_DESTINATION_ADDRESS_TYPE</p>
</td>
<td>
<p>The destination IP address type. The possible condition values are:</p>
<p>
<dl>
<dd>
NlatUnspecified

</dd>
<dd>
NlatUnicast

</dd>
<dd>
NlatAnycast

</dd>
<dd>
NlatMulticast

</dd>
<dd>
NlatBroadcast
</dd>
</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_IP_LOCAL_INTERFACE</p>
</td>
<td>
<p>The LUID for the network interface associated with the local IP address.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_IP_FORWARD_INTERFACE</p>
</td>
<td>
<p>The LUID for the network interface on which the packet being forwarded is to be sent out.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_IP_PROTOCOL</p>
</td>
<td>
<p>The IP protocol number, as specified in <a href="http://tools.ietf.org/html/rfc1700">RFC 1700</a>.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_IP_LOCAL_PORT</p>
</td>
<td>
<p>The local transport protocol port number.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_IP_REMOTE_PORT</p>
</td>
<td>
<p>The remote transport protocol port number.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_ICMP_TYPE</p>
</td>
<td>
<p>The ICMP type field, as specified in <a href="http://tools.ietf.org/html/rfc792">RFC 792</a>.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_ICMP_CODE</p>
</td>
<td>
<p>The ICMP code field, as specified in <a href="http://tools.ietf.org/html/rfc792">RFC 792</a>.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_EMBEDDED_LOCAL_ADDRESS_TYPE</p>
</td>
<td>
<p>The local IP address type that is embedded in the ICMP packet. The possible condition values are:</p>
<p>
<dl>
<dd>
NlatUnspecified

</dd>
<dd>
NlatUnicast

</dd>
<dd>
NlatAnycast

</dd>
<dd>
NlatMulticast

</dd>
<dd>
NlatBroadcast
</dd>
</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_EMBEDDED_REMOTE_ADDRESS</p>
</td>
<td>
<p>The remote IP address that is embedded in the ICMP packet.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_EMBEDDED_PROTOCOL</p>
</td>
<td>
<p>The IP protocol number that is embedded in the ICMP packet, as specified in <a href="http://tools.ietf.org/html/rfc1700">RFC 1700</a>.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_EMBEDDED_LOCAL_PORT</p>
</td>
<td>
<p>The local transport protocol port number that is embedded in the ICMP packet.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_EMBEDDED_REMOTE_PORT</p>
</td>
<td>
<p>The remote transport protocol port number that is embedded in the ICMP packet.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_FLAGS</p>
</td>
<td>
<p>A bitwise OR of a combination of filtering condition flags. For information about the possible flags, see 
       <a href="filtering-condition-flags.md">Filtering Condition Flags</a>.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_DIRECTION</p>
</td>
<td>
<p>The direction of the datagram traffic or data flow.</p>
<p>The possible condition values are:</p>
<p>
<dl>
<dd>
FWP_DIRECTION_INBOUND

</dd>
<dd>
FWP_DIRECTION_OUTBOUND
</dd>
</dl>
</p>
<p>In datagram data layers and stream packet layers, this condition specifies the direction of the packet.</p>
<p>In stream layers and ALE flow established layers, this condition specifies the direction of the connection
       (for example, when a local application initiates the connection, an inbound packet has FWPM_CONDITION_DIRECTION
       set to FWP_DIRECTION_OUTBOUND).</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_INTERFACE_INDEX</p>
</td>
<td>
<p>The index of the network interface, as enumerated by the network stack.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_INTERFACE_TYPE</p>
</td>
<td>
<p>The bus type of the network interface.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_SUB_INTERFACE_INDEX</p>
</td>
<td>
<p>The index of the logical network interface, as enumerated by the network stack.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_SOURCE_INTERFACE_INDEX</p>
</td>
<td>
<p>The index of the source network interface for forwarded packets, as enumerated by the network stack.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_SOURCE_SUB_INTERFACE_INDEX</p>
</td>
<td>
<p>The index of the source logical network interface for forwarded packets, as enumerated by the network
       stack.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_DESTINATION_INTERFACE_INDEX</p>
</td>
<td>
<p>The index of the destination network interface for forwarded packets, as enumerated by the network stack.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_DESTINATION_SUB_INTERFACE_INDEX</p>
</td>
<td>
<p>The index of the destination logical network interface for forwarded packets, as enumerated by the network
       stack.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_ALE_APP_ID</p>
</td>
<td>
<p>The full path of the application.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_ALE_USER_ID</p>
</td>
<td>
<p>The identification of the local user.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_ALE_REMOTE_USER_ID</p>
</td>
<td>
<p>The identification of the remote user.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_ALE_REMOTE_MACHINE_ID</p>
</td>
<td>
<p>The identification of the remote machine.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_ALE_PROMISCUOUS_MODE</p>
</td>
<td>
<p>The raw socket mode that is allowed or denied. The possible condition values are:</p>
<p>
<dl>
<dd>
SIO_RCVALL

</dd>
<dd>
SIO_RCVALL_IGMPMCAST

</dd>
<dd>
SIO_RCVALL_MCAST

</dd>
</dl>
</p>
<p>For a description of these raw socket modes, see <a href="https://msdn.microsoft.com/library/windows/hardware/ms741621"><b>WSAIoctl</b></a> in the Microsoft Windows SDK documentation.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_ALE_SIO_FIREWALL_SYSTEM_PORT</p>
</td>
<td>
<p>Reserved for internal use.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_ALE_NAP_CONTEXT</p>
</td>
<td>
<p>Reserved for internal use.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_REMOTE_USER_TOKEN</p>
</td>
<td>
<p>The identification of the remote user.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_RPC_IF_UUID</p>
</td>
<td>
<p>The UUID of the RPC interface.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_RPC_IF_VERSION</p>
</td>
<td>
<p>The version of the RPC interface.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_RCP_IF_FLAG</p>
</td>
<td>
<p>Reserved for internal use.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_DCOM_APP_ID</p>
</td>
<td>
<p>The identification of the COM application.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_IMAGE_NAME</p>
</td>
<td>
<p>The name of the application.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_RPC_PROTOCOL</p>
</td>
<td>
<p>The RPC protocol. The possible condition values are:</p>
<p>
<dl>
<dd>
RPC_PROTSEQ_TCP

</dd>
<dd>
RPC_PROTSEQ_HTTP

</dd>
<dd>
RPC_PROTSEQ_NMP
</dd>
</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_RPC_AUTH_TYPE</p>
</td>
<td>
<p>The authentication service type. For more information about authentication service types, see
       <a href="https://msdn.microsoft.com/library/windows/hardware/aa373556"><b>Authentication-Service Constants</b></a> in the RPC section of the Windows SDK documentation.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_RPC_AUTH_LEVEL</p>
</td>
<td>
<p>The authentication service level. For more information about authentication service levels, see
       <a href="https://msdn.microsoft.com/library/windows/hardware/aa373553"><b>Authentication-Level Constants</b></a> in the RPC section of the Windows SDK documentation.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_SEC_ENCRYPT_ALGORITHM</p>
</td>
<td>
<p>The certificate based security service provider interface (SSPI) encryption algorithm.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_SEC_KEY_SIZE</p>
</td>
<td>
<p>The certificate based security service provider interface (SSPI) encryption key size.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_IP_LOCAL_ADDRESS_V4</p>
</td>
<td>
<p>The local IPv4 address.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_IP_LOCAL_ADDRESS_V6</p>
</td>
<td>
<p>The local IPv6 address.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_PIPE</p>
</td>
<td>
<p>The name of the remote named pipe.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_IP_REMOTE_ADDRESS_V4</p>
</td>
<td>
<p>The remote IPv4 address.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_IP_REMOTE_ADDRESS_V6</p>
</td>
<td>
<p>The remote IPv6 address.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_PROCESS_WITH_RPC_IF_UUID</p>
</td>
<td>
<p>The UUID of the process with the RPC interface.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_RPC_EP_VALUE</p>
</td>
<td>
<p>Reserved for internal use.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_RPC_EP_FLAGS</p>
</td>
<td>
<p>Reserved for internal use.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_CLIENT_TOKEN</p>
</td>
<td>
<p>The identification of the client when using RpcProxy.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_RPC_SERVER_NAME</p>
</td>
<td>
<p>The name of the RPC server when using RpcProxy.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_RPC_SERVER_PORT</p>
</td>
<td>
<p>The port on the RPC server when using RpcProxy.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_RPC_PROXY_AUTH_TYPE</p>
</td>
<td>
<p>The RPC proxy authentication service type. For more information about authentication service types, see
       <a href="https://msdn.microsoft.com/library/windows/hardware/aa373556"><b>Authentication-Service Constants</b></a> in the RPC section of the Windows SDK documentation.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_TUNNEL_TYPE</p>
</td>
<td>
<p>The encapsulation method used by a tunnel.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_CLIENT_CERT_KEY_LENGTH</p>
</td>
<td>
<p>The secure socket layer (SSL) key length in the client certificate.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_CLIENT_CERT_OID</p>
</td>
<td>
<p>The object identifier (OID) in the client certificate.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_INTERFACE_MAC_ADDRESS
</p>
</td>
<td>
<p>The physical address of the sending or receiving network interface.</p>
<div class="alert"><b>Note</b>  Supported in Windows 8,  Windows Server 2012, and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_MAC_LOCAL_ADDRESS
</p>
</td>
<td>
<p>The physical address of the local network interface.
For inbound traffic this is the destination MAC address in the frame.
For outbound traffic this is the source MAC address of the frame.</p>
<div class="alert"><b>Note</b>  Supported in Windows 8,  Windows Server 2012, and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_MAC_REMOTE_ADDRESS</p>
</td>
<td>
<p>The physical address of the remote network interface.
For inbound traffic this is the source MAC address in the frame.
For outbound traffic this is the destination MAC address of the frame.</p>
<div class="alert"><b>Note</b>  Supported in Windows 8,  Windows Server 2012, and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_ETHER_TYPE</p>
</td>
<td>
<p>The type indicated in the MAC frame.
This value is 0x800 for   IPv4 traffic,  0x86DD for  IPv6 traffic or, 0x806 for  ARP traffic.
 All of the possible values are defined as  NDIS_ETH_TYPE_Xxx in ntddndis.h.</p>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_VLAN_ID</p>
</td>
<td>
<p>The identifier of the VLAN in the ETHERNET SNAP header.
If the frame is ETHERNET II, this value is 0.
</p>
<div class="alert"><b>Note</b>  Supported in Windows 8,  Windows Server 2012, and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_NDIS_PORT</p>
</td>
<td>
<p>The port number identifying a miniport adapter port. </p>
<div class="alert"><b>Note</b>  Supported in Windows 8,  Windows Server 2012, and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_NDIS_MEDIA_TYPE</p>
</td>
<td>
<p>The type of the NDIS medium specified as one of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565910"><b>NDIS_MEDIUM</b></a> enumeration values.</p>
<div class="alert"><b>Note</b>  Supported in Windows 8,  Windows Server 2012, and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_NDIS_PHYSICAL_MEDIA_TYPE</p>
</td>
<td>
<p>The type of the physical medium for the communicating interface specified as one of the
NDIS_PHYSICAL_MEDIUM enumeration values.</p>
<div class="alert"><b>Note</b>  Supported in Windows 8,  Windows Server 2012, and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_L2_FLAGS</p>
</td>
<td>
<p>A bitwise OR of a combination of filtering condition flags for the MAC layers. For information about the possible flags, see 
       <a href="filtering-condition-l2-flags.md">Filtering Condition L2 Flags</a>.</p>
<div class="alert"><b>Note</b>  Supported in Windows 8,  Windows Server 2012, and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_MAC_LOCAL_ADDRESS_TYPE</p>
</td>
<td>
<p>The Datalink type of the local MAC address. This is one of the values that are defined in the <a href="https://msdn.microsoft.com/library/windows/hardware/dd744934"><b>DL_ADDRESS_TYPE</b></a> enumeration in FwpmTypes.h.</p>
<div class="alert"><b>Note</b>  Supported in Windows 8,  Windows Server 2012, and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_MAC_REMOTE_ADDRESS_TYPE</p>
</td>
<td>
<p>The Datalink type of the remote MAC address. This is one of the values that are defined in the <a href="https://msdn.microsoft.com/library/windows/hardware/dd744934"><b>DL_ADDRESS_TYPE</b></a> enumeration in FwpmTypes.h.</p>
<div class="alert"><b>Note</b>  Supported in Windows 8,  Windows Server 2012, and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_INTERFACE</p>
</td>
<td>
<p>The LUID for the network interface that is associated with the local MAC address.</p>
<div class="alert"><b>Note</b>  Supported in Windows 8,  Windows Server 2012, and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_ALE_PACKAGE_ID</p>
</td>
<td>
<p>The security identifier (SID) of the AppContainer restricted package.</p>
<div class="alert"><b>Note</b>  Supported in Windows 8,  Windows Server 2012, and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_MAC_SOURCE_ADDRESS</p>
</td>
<td>
<p>The physical address of the network interface that created the MAC frame.</p>
<div class="alert"><b>Note</b>  Supported in Windows 8,  Windows Server 2012, and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_MAC_DESTINATION_ADDRESS</p>
</td>
<td>
<p>The physical address of the network interface to which the frame is destined.</p>
<div class="alert"><b>Note</b>  Supported in Windows 8,  Windows Server 2012, and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_MAC_SOURCE_ADDRESS_TYPE</p>
</td>
<td>
<p>The Datalink type of the MAC Address for the interface that created the frame. This is one of the values that are defined in the <a href="https://msdn.microsoft.com/library/windows/hardware/dd744934"><b>DL_ADDRESS_TYPE</b></a> enumeration in FwpmTypes.h.</p>
<div class="alert"><b>Note</b>  Supported in Windows 8,  Windows Server 2012, and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_MAC_DESTINATION_ADDRESS_TYPE</p>
</td>
<td>
<p>The Datalink type of the MAC Address for the interface to which the frame is destined. This is one of the values that are defined in the <a href="https://msdn.microsoft.com/library/windows/hardware/dd744934"><b>DL_ADDRESS_TYPE</b></a> enumeration in FwpmTypes.h.</p>
<div class="alert"><b>Note</b>  Supported in Windows 8,  Windows Server 2012, and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_IP_SOURCE_PORT</p>
</td>
<td>
<p>The transport protocol source port number.</p>
<div class="alert"><b>Note</b>  Supported in Windows 8,  Windows Server 2012, and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_IP_DESTINATION_PORT</p>
</td>
<td>
<p>The transport protocol destination port number.</p>
<div class="alert"><b>Note</b>  Supported in Windows 8,  Windows Server 2012, and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_VSWITCH_ID</p>
</td>
<td>
<p>The GUID of the virtual switch.</p>
<div class="alert"><b>Note</b>  Supported in Windows 8,  Windows Server 2012, and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_VSWITCH_NETWORK_TYPE</p>
</td>
<td>
<p>The type of network that is associated with the virtual switch. This is one of the values that are defined in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh447394"><b>FWP_VSWITCH_NETWORK_TYPE</b></a> enumeration in FwpTypes.h.</p>
<div class="alert"><b>Note</b>  Supported in <i>Windows 8</i> and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_VSWITCH_SOURCE_INTERFACE_ID</p>
</td>
<td>
<p>The GUID of the interface of the virtual switch that created the frame.</p>
<div class="alert"><b>Note</b>  Supported in Windows 8,  Windows Server 2012, and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_VSWITCH_DESTINATION_INTERFACE_ID</p>
</td>
<td>
<p>The GUID of the interface of the virtual switch to which the frame is destined.</p>
<div class="alert"><b>Note</b>  Supported in <i>Windows 8</i> and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_VSWITCH_SOURCE_INTERFACE_TYPE</p>
</td>
<td>
<p>The type of the virtual switch interface that created the frame. This is one of the values that are defined in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451589"><b>NDIS_NIC_SWITCH_TYPE</b></a> enumeration in Ntddndis.h.</p>
<div class="alert"><b>Note</b>  Supported in Windows 8,  Windows Server 2012, and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_VSWITCH_DESTINATION_INTERFACE_TYPE</p>
</td>
<td>
<p>The type of the virtual switch interface to which the frame is destined. This is one of the values that are defined in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451589"><b>NDIS_NIC_SWITCH_TYPE</b></a> enumeration in Ntddndis.h.</p>
<div class="alert"><b>Note</b>  Supported in Windows 8,  Windows Server 2012, and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_VSWITCH_SOURCE_VM_ID</p>
</td>
<td>
<p>Unique identifier of the vSwitch source virtual machine.</p>
<div class="alert"><b>Note</b>  Supported in Windows 8,  Windows Server 2012, and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_VSWITCH_DESTINATION_VM_ID</p>
</td>
<td>
<p>Unique identifier of the vSwitch destination virtual machine.</p>
<div class="alert"><b>Note</b>  Supported in Windows 8,  Windows Server 2012, and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_VSWITCH_TENANT_NETWORK_ID</p>
</td>
<td>
<p>Unique identifier for the vSwitch network. Cannot be used in conjunction with VLAN_IDs.</p>
<div class="alert"><b>Note</b>  Supported in Windows 8,  Windows Server 2012, and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_ALE_PACKAGE_ID</p>
</td>
<td>
<p>The security identifier (SID) of an app container.</p>
<div class="alert"><b>Note</b>  Supported in Windows 8,  Windows Server 2012, and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_ALE_ORIGINAL_APP_ID</p>
</td>
<td>
<p>The original full path of the application before alteration from proxying.  Note that if proxying is not involved, then this will be the same as the FWPM_CONDITION_ALE_APP_ID.</p>
<div class="alert"><b>Note</b>  Supported in Windows 8,  Windows Server 2012, and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_CONDITION_QM_MODE</p>
</td>
<td>
<p>The quick mode (QM) mode.</p>
<div class="alert"><b>Note</b>  Supported in Windows 8,  Windows Server 2012, and later versions of Windows.</div>
<div> </div>
</td>
</tr>
</table>

