---
title: Metadata field identifiers
description: This section describes metadata field identifiers for Windows Filtering Platform callout drivers.
ms.assetid: 2157bace-9fae-41e8-a435-c4a412873ee1
keywords:
- Metadata field identifiers network drivers
ms.date: 11/09/2017
ms.localizationpriority: medium
---

# Metadata field identifiers

The metadata field identifiers are each represented by a bit-field. These identifiers are defined as follows:

<table>
<tr>
<th>
       Metadata field identifier
       
      </th>
<th>
       Description 
       
      </th>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_ALE_CLASSIFY_REQUIRED</p>
</td>
<td>
<p>The inbound packet will also be indicated to the FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V4 and
       FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V6 filtering layers.</p>
<p>
<div class="alert"><b>Note</b>  Supported in Windows Server 2008, Windows Vista with Service Pack 1 (SP1), and later.</div>
<div> </div>
</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_COMPARTMENT_ID</p>
</td>
<td>
<p>The identifier of the routing compartment in which the packet was received or is being sent.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_COMPLETION_HANDLE</p>
</td>
<td>
<p>The completion handle used to pend the current filtering operation.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_DESTINATION_INTERFACE_INDEX</p>
</td>
<td>
<p>The index of the network interface where the outgoing packet is to be sent.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_DESTINATION_PREFIX</p>
</td>
<td>
<p>The destination IPV4 or IPV6 address and subnet mask for the outgoing packets.</p>
<div class="alert"><b>Note</b>  Supported starting with Windows 7.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_DISCARD_REASON</p>
</td>
<td>
<p>The reason that the data was discarded.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_ETHER_FRAME_LENGTH</p>
</td>
<td>
<p>This metadata field identifier is not currently supported.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_FLOW_HANDLE</p>
</td>
<td>
<p>The handle for the data flow.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_FORWARD_LAYER_INBOUND_PASS_THRU</p>
</td>
<td>
<p>The packet that traverses the FWPM_LAYER_IPFORWARD_V4 or FWPM_LAYER_IPFORWARD_V6 forward layer is
       locally destined (its destination matches an address that is assigned to an interface of the
       host).</p>
<p>
<div class="alert"><b>Note</b>  Supported in Windows Server 2008, Windows Vista with SP1, and later.</div>
<div> </div>
</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_FORWARD_LAYER_OUTBOUND_PASS_THRU</p>
</td>
<td>
<p>The packet that traverses the FWPM_LAYER_IPFORWARD_V4 or FWPM_LAYER_IPFORWARD_V6 forward layer
       originated locally.</p>
<p>
<div class="alert"><b>Note</b>  Supported in Windows Server 2008, Windows Vista with SP1, and later.</div>
<div> </div>
</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_FRAGMENT_DATA</p>
</td>
<td>
<p>The fragment data for a received packet fragment.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_ICMP_ID_AND_SEQUENCE</p>
</td>
<td>
<p>The Identifier and Sequence Number fields of an ICMP Echo Request or Echo Reply packet.</p>
<p>
<div class="alert"><b>Note</b>  Supported starting with Windows 7.</div>
<div> </div>
</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_IP_HEADER_SIZE</p>
</td>
<td>
<p>The size of the IP header.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_LOCAL_REDIRECT_TARGET_PID</p>
</td>
<td>
<p>The Process ID that a connection was redirected to.</p>
<p>
<div class="alert"><b>Note</b>  Supported starting with Windows 7.</div>
<div> </div>
</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_ORIGINAL_DESTINATION</p>
</td>
<td>
<p>A 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff570825"><b>SOCKADDR_STORAGE</b></a> structure that indicate
       the packet&#39;s original destination.</p>
<p>
<div class="alert"><b>Note</b>  Supported starting with Windows 7.</div>
<div> </div>
</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_PACKET_DIRECTION</p>
</td>
<td>
<p>The direction of network traffic (inbound or outbound).</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_PACKET_SYSTEM_CRITICAL</p>
</td>
<td>
<p>Reserved for system use. Do not use.</p>
<p>
<div class="alert"><b>Note</b>  Supported in Windows Server 2008, Windows Vista with SP1, and later.</div>
<div> </div>
</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_PARENT_ENDPOINT_HANDLE</p>
</td>
<td>
<p>The handle of the endpoint&#39;s parent socket.</p>
<p>
<div class="alert"><b>Note</b>  Supported starting with Windows 7.</div>
<div> </div>
</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_PATH_MTU</p>
</td>
<td>
<p>The path maximum transmission unit (path MTU) for an outgoing packet.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_PROCESS_ID</p>
</td>
<td>
<p>The process ID for the process that owns the endpoint.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_PROCESS_PATH</p>
</td>
<td>
<p>The full path to the process that owns the endpoint.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_REDIRECT_RECORD_HANDLE</p>
</td>
<td>
<p>The redirect records handle indicated to ALE_CONNECT_REDIRECT callout by the classify metadata.</p>
<p>
<div class="alert"><b>Note</b>  Supported starting with Windows 8.</div>
<div> </div>
</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_REMOTE_SCOPE_ID</p>
</td>
<td>
<p>The remote scope identifier to be used in outbound transport layer injection.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_RESERVED</p>
</td>
<td>
<p>Reserved for system use. Do not use.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_SOURCE_INTERFACE_INDEX</p>
</td>
<td>
<p>The index of the network interface where the incoming packet was received.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_SUB_PROCESS_TAG</p>
</td>
<td>
<p>Reserved for system use.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_SYSTEM_FLAGS</p>
</td>
<td>
<p>System flags that are used internally by the filter engine.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_TOKEN</p>
</td>
<td>
<p>The token used to validate the permissions for the user.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_TRANSPORT_CONTROL_DATA</p>
</td>
<td>
<p>An optional socket control data object.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_TRANSPORT_ENDPOINT_HANDLE</p>
</td>
<td>
<p>The handle for the end of the packet to be injected into the outbound transport layer.</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_TRANSPORT_HEADER_INCLUDE_HEADER</p>
</td>
<td>
<p>The IP header if the packet is sent from a raw socket.</p>
<p>
<div class="alert"><b>Note</b>  Supported in Windows Server 2008, Windows Vista with SP1, and later.</div>
<div> </div>
</p>
</td>
</tr>
<tr>
<td>
<p>FWPS_METADATA_FIELD_TRANSPORT_HEADER_SIZE</p>
</td>
<td>
<p>The size of the transport header.</p>
</td>
</tr>
</table>

