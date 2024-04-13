---
title: Data field identifiers
description: This section describes Data field identifiers for Windows Filtering Platform callout drivers.
keywords:
- Data field identifiers network drivers
ms.date: 11/28/2017
---

# Data field identifiers

The run-time filtering layers are associated with data field identifiers. These identifiers represent a set of constant values that are declared as FWPS_FIELDS_XXX enumerations in Fwpsk.h.

The following table lists the run-time filtering layers and the associated data field enumerations.

<table>
<tr>
<th>
        Run-time filtering layer
      </th>
<th>
        Data field enumeration
      </th>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_INBOUND_IPPACKET_V4
        FWPS_LAYER_INBOUND_IPPACKET_V4_DISCARD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_inbound_ippacket_v4_"><b>
        FWPS_FIELDS_INBOUND_IPPACKET_V4</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_INBOUND_IPPACKET_V6
        FWPS_LAYER_INBOUND_IPPACKET_V6_DISCARD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_inbound_ippacket_v6_"><b>
        FWPS_FIELDS_INBOUND_IPPACKET_V6</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_OUTBOUND_IPPACKET_V4
        FWPS_LAYER_OUTBOUND_IPPACKET_V4_DISCARD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_outbound_ippacket_v4_"><b>
        FWPS_FIELDS_OUTBOUND_IPPACKET_V4</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_OUTBOUND_IPPACKET_V6
        FWPS_LAYER_OUTBOUND_IPPACKET_V6_DISCARD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_outbound_ippacket_v6_"><b>
        FWPS_FIELDS_OUTBOUND_IPPACKET_V6</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_IPFORWARD_V4
        FWPS_LAYER_IPFORWARD_V4_DISCARD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ipforward_v4_"><b>FWPS_FIELDS_IPFORWARD_V4</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_IPFORWARD_V6
        FWPS_LAYER_IPFORWARD_V6_DISCARD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ipforward_v6_"><b>FWPS_FIELDS_IPFORWARD_V6</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_INBOUND_TRANSPORT_V4
        FWPS_LAYER_INBOUND_TRANSPORT_V4_DISCARD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_inbound_transport_v4_"><b>
        FWPS_FIELDS_INBOUND_TRANSPORT_V4</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_INBOUND_TRANSPORT_V6
        FWPS_LAYER_INBOUND_TRANSPORT_V6_DISCARD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_inbound_transport_v6_"><b>
        FWPS_FIELDS_INBOUND_TRANSPORT_V6</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_OUTBOUND_TRANSPORT_V4
        FWPS_LAYER_OUTBOUND_TRANSPORT_V4_DISCARD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_outbound_transport_v4_"><b>
        FWPS_FIELDS_OUTBOUND_TRANSPORT_V4</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_OUTBOUND_TRANSPORT_V6
        FWPS_LAYER_OUTBOUND_TRANSPORT_V6_DISCARD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_outbound_transport_v6_"><b>
        FWPS_FIELDS_OUTBOUND_TRANSPORT_V6</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_STREAM_V4
        FWPS_LAYER_STREAM_V4_DISCARD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_stream_v4_"><b>FWPS_FIELDS_STREAM_V4</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_STREAM_V6
        FWPS_LAYER_STREAM_V6_DISCARD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_stream_v6_"><b>FWPS_FIELDS_STREAM_V6</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_DATAGRAM_DATA_V4
        FWPS_LAYER_DATAGRAM_DATA_V4_DISCARD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_datagram_data_v4_"><b>FWPS_FIELDS_DATAGRAM_DATA_V4</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_DATAGRAM_DATA_V6
        FWPS_LAYER_DATAGRAM_DATA_V6_DISCARD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_datagram_data_v6_"><b>FWPS_FIELDS_DATAGRAM_DATA_V6</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_STREAM_PACKET_V4</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_stream_packet_v4_"><b>FWPS_FIELDS_STREAM_PACKET_V4</b></a></p>
<div class="alert"><b>Note</b>  Supported in Windows 7 and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_STREAM_PACKET_V6</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_stream_packet_v6_"><b>FWPS_FIELDS_STREAM_PACKET_V6</b></a></p>
<div class="alert"><b>Note</b>  Supported in Windows 7 and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_INBOUND_ICMP_ERROR_V4
        FWPS_LAYER_INBOUND_ICMP_ERROR_V4_DISCARD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_inbound_icmp_error_v4_"><b>
        FWPS_FIELDS_INBOUND_ICMP_ERROR_V4</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_INBOUND_ICMP_ERROR_V6
        FWPS_LAYER_INBOUND_ICMP_ERROR_V6_DISCARD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_inbound_icmp_error_v6_"><b>
        FWPS_FIELDS_INBOUND_ICMP_ERROR_V6</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_OUTBOUND_ICMP_ERROR_V4
        FWPS_LAYER_OUTBOUND_ICMP_ERROR_V4_DISCARD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_outbound_icmp_error_v4_"><b>
        FWPS_FIELDS_OUTBOUND_ICMP_ERROR_V4</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_OUTBOUND_ICMP_ERROR_V6
        FWPS_LAYER_OUTBOUND_ICMP_ERROR_V6_DISCARD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_outbound_icmp_error_v6_"><b>
        FWPS_FIELDS_OUTBOUND_ICMP_ERROR_V6</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_ALE_RESOURCE_ASSIGNMENT_V4
        FWPS_LAYER_ALE_RESOURCE_ASSIGNMENT_V4_DISCARD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ale_resource_assignment_v4_"><b>
        FWPS_FIELDS_ALE_RESOURCE_ASSIGNMENT_V4</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_ALE_RESOURCE_ASSIGNMENT_V6
        FWPS_LAYER_ALE_RESOURCE_ASSIGNMENT_V6_DISCARD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ale_resource_assignment_v6_"><b>
        FWPS_FIELDS_ALE_RESOURCE_ASSIGNMENT_V6</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_ALE_RESOURCE_RELEASE_V4</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ale_resource_release_v4_"><b>
        FWPS_FIELDS_ALE_RESOURCE_RELEASE_V4</b></a></p>
<div class="alert"><b>Note</b>  Supported in Windows 7 and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_ALE_RESOURCE_RELEASE_V6</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ale_resource_release_v6_"><b>
        FWPS_FIELDS_ALE_RESOURCE_RELEASE_V6</b></a></p>
<div class="alert"><b>Note</b>  Supported in Windows 7 and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_ALE_ENDPOINT_CLOSURE_V4</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ale_endpoint_closure_v4_"><b>
        FWPS_FIELDS_ALE_ENDPOINT_CLOSURE_V4</b></a></p>
<div class="alert"><b>Note</b>  Supported in Windows 7 and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_ALE_ENDPOINT_CLOSURE_V6</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ale_endpoint_closure_v6_"><b>
        FWPS_FIELDS_ALE_ENDPOINT_CLOSURE_V6</b></a></p>
<div class="alert"><b>Note</b>  Supported in Windows 7 and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_ALE_AUTH_LISTEN_V4
        FWPS_LAYER_ALE_AUTH_LISTEN_V4_DISCARD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ale_auth_listen_v4_"><b>
        FWPS_FIELDS_ALE_AUTH_LISTEN_V4</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_ALE_AUTH_LISTEN_V6
        FWPS_LAYER_ALE_AUTH_LISTEN_V6_DISCARD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ale_auth_listen_v6_"><b>
        FWPS_FIELDS_ALE_AUTH_LISTEN_V6</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_ALE_AUTH_RECV_ACCEPT_V4
        FWPS_LAYER_ALE_AUTH_RECV_ACCEPT_V4_DISCARD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ale_auth_recv_accept_v4_"><b>
        FWPS_FIELDS_ALE_AUTH_RECV_ACCEPT_V4</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_ALE_AUTH_RECV_ACCEPT_V6
        FWPS_LAYER_ALE_AUTH_RECV_ACCEPT_V6_DISCARD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ale_auth_recv_accept_v6_"><b>
        FWPS_FIELDS_ALE_AUTH_RECV_ACCEPT_V6</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_ALE_BIND_REDIRECT_V4</p>
</td>
<td>
<p>
<dl>
<dt><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ale_bind_redirect_v4_"><b>
        FWPS_FIELDS_ALE_BIND_REDIRECT_V4</b></a></dt>
<dt>
<div class="alert"><b>Note</b>  Supported in Windows 7 and later versions of Windows.</div>
<div> </div>
</dt>
</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_ALE_BIND_REDIRECT_V6</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ale_bind_redirect_v6_"><b>
        FWPS_FIELDS_ALE_BIND_REDIRECT_V6</b></a></p>
<div class="alert"><b>Note</b>  Supported in Windows 7 and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_ALE_CONNECT_REDIRECT_V4</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ale_connect_redirect_v4_"><b>
        FWPS_FIELDS_ALE_CONNECT_REDIRECT_V4</b></a></p>
<div class="alert"><b>Note</b>  Supported in Windows 7 and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_ALE_CONNECT_REDIRECT_V6</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ale_connect_redirect_v6_"><b>
        FWPS_FIELDS_ALE_CONNECT_REDIRECT_V6</b></a></p>
<div class="alert"><b>Note</b>  Supported in Windows 7 and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_ALE_AUTH_CONNECT_V4
        FWPS_LAYER_ALE_AUTH_CONNECT_V4_DISCARD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ale_auth_connect_v4_"><b>
        FWPS_FIELDS_ALE_AUTH_CONNECT_V4</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_ALE_AUTH_CONNECT_V6
        FWPS_LAYER_ALE_AUTH_CONNECT_V6_DISCARD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ale_auth_connect_v6_"><b>
        FWPS_FIELDS_ALE_AUTH_CONNECT_V6</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_ALE_FLOW_ESTABLISHED_V4
        FWPS_LAYER_ALE_FLOW_ESTABLISHED_V4_DISCARD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ale_flow_established_v4_"><b>
        FWPS_FIELDS_ALE_FLOW_ESTABLISHED_V4</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_ALE_FLOW_ESTABLISHED_V6
        FWPS_LAYER_ALE_FLOW_ESTABLISHED_V6_DISCARD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ale_flow_established_v6_"><b>
        FWPS_FIELDS_ALE_FLOW_ESTABLISHED_V6</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_NAME_RESOLUTION_CACHE_V4</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_name_resolution_cache_v4_"><b>
        FWPS_FIELDS_NAME_RESOLUTION_CACHE_V4</b></a></p>
<div class="alert"><b>Note</b>  Supported in Windows 7 and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_NAME_RESOLUTION_CACHE_V6</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_name_resolution_cache_v6_"><b>
        FWPS_FIELDS_NAME_RESOLUTION_CACHE_V6</b></a></p>
<div class="alert"><b>Note</b>  Supported in Windows 7 and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_INBOUND_MAC_FRAME_ETHERNET</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_inbound_mac_frame_ethernet_"><b>
        FWPS_FIELDS_INBOUND_MAC_FRAME_ETHERNET</b></a></p>
<div class="alert"><b>Note</b>  Supported in <i>Windows 8</i> and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_OUTBOUND_MAC_FRAME_ETHERNET</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_outbound_mac_frame_ethernet_"><b>
        FWPS_FIELDS_OUTBOUND_MAC_FRAME_ETHERNET</b></a></p>
<div class="alert"><b>Note</b>  Supported in <i>Windows 8</i> and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>
        FWPM_LAYER_INBOUND_MAC_FRAME_NATIVE
       </p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_inbound_mac_frame_native_"><b>FWPS_FIELDS_INBOUND_MAC_FRAME_NATIVE</b></a></p>
<div class="alert"><b>Note</b>  Supported in <i>Windows 8</i> and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_LAYER_OUTBOUND_MAC_FRAME_NATIVE</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_outbound_mac_frame_native_"><b>FWPS_FIELDS_OUTBOUND_MAC_FRAME_NATIVE</b></a></p>
<div class="alert"><b>Note</b>  Supported in <i>Windows 8</i> and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_IPSEC_KM_DEMUX_V4</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ipsec_km_demux_v4_"><b>
        FWPS_FIELDS_IPSEC_KM_DEMUX_V4</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_IPSEC_KM_DEMUX_V6</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ipsec_km_demux_v6_"><b>
        FWPS_FIELDS_IPSEC_KM_DEMUX_V6</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_IPSEC_V4</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ipsec_v4_"><b>FWPS_FIELDS_IPSEC_V4</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_IPSEC_V6</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ipsec_v6_"><b>FWPS_FIELDS_IPSEC_V6</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_IKEEXT_V4</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ikeext_v4_"><b>FWPS_FIELDS_IKEEXT_V4</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_IKEEXT_V6</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ikeext_v6_"><b>FWPS_FIELDS_IKEEXT_V6</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_RPC_UM</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_rpc_um_"><b>FWPS_FIELDS_RPC_UM</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_RPC_EPMAP</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_rpc_epmap_"><b>FWPS_FIELDS_RPC_EPMAP</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_RPC_EP_ADD</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_rpc_ep_add_"><b>FWPS_FIELDS_RPC_EP_ADD</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_RPC_PROXY_CONN</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_rpc_proxy_conn_"><b>FWPS_FIELDS_RPC_PROXY_CONN</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_RPC_PROXY_IF</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_rpc_proxy_if_"><b>FWPS_FIELDS_RPC_PROXY_IF_IF</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_KM_AUTHORIZATION</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_km_authorization_"><b>FWPS_FIELDS_KM_AUTHORIZATION</b></a></p>
<div class="alert"><b>Note</b>  Supported in Windows 7 and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_INGRESS_VSWITCH_ETHERNET</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ingress_vswitch_ethernet_"><b>FWPS_FIELDS_INGRESS_VSWITCH_ETHERNET
</b></a></p>
<div class="alert"><b>Note</b>  Supported in <i>Windows 8</i> and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_EGRESS_VSWITCH_ETHERNET</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_egress_vswitch_ethernet_"><b>FWPS_FIELDS_EGRESS_VSWITCH_ETHERNET
</b></a></p>
<div class="alert"><b>Note</b>  Supported in <i>Windows 8</i> and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_INGRESS_VSWITCH_TRANSPORT_V4</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ingress_vswitch_transport_v4_"><b>FWPS_FIELDS_INGRESS_VSWITCH_TRANSPORT_V4
</b></a></p>
<div class="alert"><b>Note</b>  Supported in <i>Windows 8</i> and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>WPS_LAYER_INGRESS_VSWITCH_TRANSPORT_V6</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_ingress_vswitch_transport_v6_"><b>FWPS_FIELDS_INGRESS_VSWITCH_TRANSPORT_V6
</b></a></p>
<div class="alert"><b>Note</b>  Supported in <i>Windows 8</i> and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_EGRESS_VSWITCH_TRANSPORT_V4</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_egress_vswitch_transport_v4_"><b>FWPS_FIELDS_EGRESS_VSWITCH_TRANSPORT_V4
</b></a></p>
<div class="alert"><b>Note</b>  Supported in <i>Windows 8</i> and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_EGRESS_VSWITCH_TRANSPORT_V6</p>
</td>
<td>
<p><a href="/windows-hardware/drivers/ddi/fwpsk/ne-fwpsk-fwps_fields_egress_vswitch_transport_v6_"><b>FWPS_FIELDS_EGRESS_VSWITCH_TRANSPORT_V6
</b></a></p>
<div class="alert"><b>Note</b>  Supported in <i>Windows 8</i> and later versions of Windows.</div>
<div> </div>
</td>
</tr>
</table>
