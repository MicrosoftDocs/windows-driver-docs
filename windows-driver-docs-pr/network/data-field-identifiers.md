---
title: Data field identifiers
description: This section describes Data field identifiers for Windows Filtering Platform callout drivers.
ms.assetid: 6e617ef4-807b-4564-8b95-b289edfee8d2
keywords:
- Data field identifiers network drivers
ms.date: 11/28/2017
ms.localizationpriority: medium
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551287(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551289(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551329(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551331(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551297(v=vs.85).aspx"><b>FWPS_FIELDS_IPFORWARD_V4</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_IPFORWARD_V6
        FWPS_LAYER_IPFORWARD_V6_DISCARD</p>
</td>
<td>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551299(v=vs.85).aspx"><b>FWPS_FIELDS_IPFORWARD_V6</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_INBOUND_TRANSPORT_V4
        FWPS_LAYER_INBOUND_TRANSPORT_V4_DISCARD</p>
</td>
<td>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551293(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551294(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551335(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551338(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552384(v=vs.85).aspx"><b>FWPS_FIELDS_STREAM_V4</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_STREAM_V6
        FWPS_LAYER_STREAM_V6_DISCARD</p>
</td>
<td>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552385(v=vs.85).aspx"><b>FWPS_FIELDS_STREAM_V6</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_DATAGRAM_DATA_V4
        FWPS_LAYER_DATAGRAM_DATA_V4_DISCARD</p>
</td>
<td>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551274(v=vs.85).aspx"><b>FWPS_FIELDS_DATAGRAM_DATA_V4</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_DATAGRAM_DATA_V6
        FWPS_LAYER_DATAGRAM_DATA_V6_DISCARD</p>
</td>
<td>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551276(v=vs.85).aspx"><b>FWPS_FIELDS_DATAGRAM_DATA_V6</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_STREAM_PACKET_V4</p>
</td>
<td>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552379(v=vs.85).aspx"><b>FWPS_FIELDS_STREAM_PACKET_V4</b></a></p>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552383(v=vs.85).aspx"><b>FWPS_FIELDS_STREAM_PACKET_V6</b></a></p>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551283(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551285(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551324(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551327(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551266(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551267(v=vs.85).aspx"><b>
        FWPS_FIELDS_ALE_RESOURCE_ASSIGNMENT_V6</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_ALE_RESOURCE_RELEASE_V4</p>
</td>
<td>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551269(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551272(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551256(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551258(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551240(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551242(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551245(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551246(v=vs.85).aspx"><b>
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
<dt><a href="https://msdn.microsoft.com/library/windows/hardware/ff551247(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551249(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551251(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551254(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551238(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551239(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551261(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551263(v=vs.85).aspx"><b>
        FWPS_FIELDS_ALE_FLOW_ESTABLISHED_V6</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_NAME_RESOLUTION_CACHE_V4</p>
</td>
<td>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551316(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551320(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551291(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551334(v=vs.85).aspx"><b>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/hh439728(v=vs.85).aspx"><b>FWPS_FIELDS_INBOUND_MAC_FRAME_NATIVE</b></a></p>
<div class="alert"><b>Note</b>  Supported in <i>Windows 8</i> and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPM_LAYER_OUTBOUND_MAC_FRAME_NATIVE</p>
</td>
<td>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/hh439757(v=vs.85).aspx"><b>FWPS_FIELDS_OUTBOUND_MAC_FRAME_NATIVE</b></a></p>
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551301(v=vs.85).aspx"><b>
        FWPS_FIELDS_IPSEC_KM_DEMUX_V4</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_IPSEC_KM_DEMUX_V6</p>
</td>
<td>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551304(v=vs.85).aspx"><b>
        FWPS_FIELDS_IPSEC_KM_DEMUX_V6</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_IPSEC_V4</p>
</td>
<td>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551305(v=vs.85).aspx"><b>FWPS_FIELDS_IPSEC_V4</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_IPSEC_V6</p>
</td>
<td>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551307(v=vs.85).aspx"><b>FWPS_FIELDS_IPSEC_V6</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_IKEEXT_V4</p>
</td>
<td>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551278(v=vs.85).aspx"><b>FWPS_FIELDS_IKEEXT_V4</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_IKEEXT_V6</p>
</td>
<td>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551281(v=vs.85).aspx"><b>FWPS_FIELDS_IKEEXT_V6</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_RPC_UM</p>
</td>
<td>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552376(v=vs.85).aspx"><b>FWPS_FIELDS_RPC_UM</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_RPC_EPMAP</p>
</td>
<td>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551339(v=vs.85).aspx"><b>FWPS_FIELDS_RPC_EPMAP</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_RPC_EP_ADD</p>
</td>
<td>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552370(v=vs.85).aspx"><b>FWPS_FIELDS_RPC_EP_ADD</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_RPC_PROXY_CONN</p>
</td>
<td>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552372(v=vs.85).aspx"><b>FWPS_FIELDS_RPC_PROXY_CONN</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_RPC_PROXY_IF</p>
</td>
<td>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552374(v=vs.85).aspx"><b>FWPS_FIELDS_RPC_PROXY_IF_IF</b></a></p>
</td>
</tr>
<tr>
<td>
<p>
        FWPS_LAYER_KM_AUTHORIZATION</p>
</td>
<td>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551312(v=vs.85).aspx"><b>FWPS_FIELDS_KM_AUTHORIZATION</b></a></p>
<div class="alert"><b>Note</b>  Supported in Windows 7 and later versions of Windows.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPS_LAYER_INGRESS_VSWITCH_ETHERNET</p>
</td>
<td>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/hh439733(v=vs.85).aspx"><b>FWPS_FIELDS_INGRESS_VSWITCH_ETHERNET
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/hh439709(v=vs.85).aspx"><b>FWPS_FIELDS_EGRESS_VSWITCH_ETHERNET
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/hh439738(v=vs.85).aspx"><b>FWPS_FIELDS_INGRESS_VSWITCH_TRANSPORT_V4
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/hh439745(v=vs.85).aspx"><b>FWPS_FIELDS_INGRESS_VSWITCH_TRANSPORT_V6
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/hh439715(v=vs.85).aspx"><b>FWPS_FIELDS_EGRESS_VSWITCH_TRANSPORT_V4
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
<p><a href="https://msdn.microsoft.com/library/windows/hardware/hh439721(v=vs.85).aspx"><b>FWPS_FIELDS_EGRESS_VSWITCH_TRANSPORT_V6
</b></a></p>
<div class="alert"><b>Note</b>  Supported in <i>Windows 8</i> and later versions of Windows.</div>
<div> </div>
</td>
</tr>
</table>

