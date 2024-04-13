---
title: Metadata field identifiers
description: This section describes metadata field identifiers for Windows Filtering Platform callout drivers.
keywords:
- Metadata field identifiers network drivers
ms.date: 11/09/2017
---

# Metadata field identifiers

The metadata field identifiers are each represented by a bit-field. These identifiers are defined as follows:

|Metadata field identifier|Description|
|--- |--- |
|FWPS_METADATA_FIELD_ALE_CLASSIFY_REQUIRED|The inbound packet will also be indicated to the FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V4 and FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V6 filtering layers. **Note:**  Supported in Windows Server 2008, Windows Vista with Service Pack 1 (SP1), and later.|
|FWPS_METADATA_FIELD_COMPARTMENT_ID|The identifier of the routing compartment in which the packet was received or is being sent.|
|FWPS_METADATA_FIELD_COMPLETION_HANDLE|The completion handle used to pend the current filtering operation.|
|FWPS_METADATA_FIELD_DESTINATION_INTERFACE_INDEX|The index of the network interface where the outgoing packet is to be sent.|
|FWPS_METADATA_FIELD_DESTINATION_PREFIX|The destination IPV4 or IPV6 address and subnet mask for the outgoing packets. **Note:**  Supported starting with Windows 7.|
|FWPS_METADATA_FIELD_DISCARD_REASON|The reason that the data was discarded.|
|FWPS_METADATA_FIELD_ETHER_FRAME_LENGTH|This metadata field identifier is not currently supported.|
|FWPS_METADATA_FIELD_FLOW_HANDLE|The handle for the data flow.|
|FWPS_METADATA_FIELD_FORWARD_LAYER_INBOUND_PASS_THRU|The packet that traverses the FWPM_LAYER_IPFORWARD_V4 or FWPM_LAYER_IPFORWARD_V6 forward layer is locally destined (its destination matches an address that is assigned to an interface of the host). **Note:**  Supported in Windows Server 2008, Windows Vista with SP1, and later.|
|FWPS_METADATA_FIELD_FORWARD_LAYER_OUTBOUND_PASS_THRU|The packet that traverses the FWPM_LAYER_IPFORWARD_V4 or FWPM_LAYER_IPFORWARD_V6 forward layer originated locally. **Note:**  Supported in Windows Server 2008, Windows Vista with SP1, and later.|
|FWPS_METADATA_FIELD_FRAGMENT_DATA|The fragment data for a received packet fragment.|
|FWPS_METADATA_FIELD_ICMP_ID_AND_SEQUENCE|The Identifier and Sequence Number fields of an ICMP Echo Request or Echo Reply packet. **Note:**  Supported starting with Windows 7.|
|FWPS_METADATA_FIELD_IP_HEADER_SIZE|The size of the IP header.|
|FWPS_METADATA_FIELD_LOCAL_REDIRECT_TARGET_PID|The Process ID that a connection was redirected to. **Note:**  Supported starting with Windows 7.|
|FWPS_METADATA_FIELD_ORIGINAL_DESTINATION|A [**SOCKADDR_STORAGE**](/previous-versions/windows/desktop/legacy/ms740504(v=vs.85)) structure that indicate the packet's original destination. **Note:**  Supported starting with Windows 7.|
|FWPS_METADATA_FIELD_PACKET_DIRECTION|The direction of network traffic (inbound or outbound).|
|FWPS_METADATA_FIELD_PACKET_SYSTEM_CRITICAL|Reserved for system use. Do not use. **Note:**  Supported in Windows Server 2008, Windows Vista with SP1, and later.|
|FWPS_METADATA_FIELD_PARENT_ENDPOINT_HANDLE|The handle of the endpoint's parent socket. **Note:**  Supported starting with Windows 7.|
|FWPS_METADATA_FIELD_PATH_MTU|The path maximum transmission unit (path MTU) for an outgoing packet.|
|FWPS_METADATA_FIELD_PROCESS_ID|The process ID for the process that owns the endpoint.|
|FWPS_METADATA_FIELD_PROCESS_PATH|The full path to the process that owns the endpoint.|
|FWPS_METADATA_FIELD_REDIRECT_RECORD_HANDLE|The redirect records handle indicated to ALE_CONNECT_REDIRECT callout by the classify metadata. **Note:**  Supported starting with Windows 8.|
|FWPS_METADATA_FIELD_REMOTE_SCOPE_ID|The remote scope identifier to be used in outbound transport layer injection.|
|FWPS_METADATA_FIELD_RESERVED|Reserved for system use. Do not use.|
|FWPS_METADATA_FIELD_SOURCE_INTERFACE_INDEX|The index of the network interface where the incoming packet was received.|
|FWPS_METADATA_FIELD_SUB_PROCESS_TAG|Reserved for system use.|
|FWPS_METADATA_FIELD_SYSTEM_FLAGS|System flags that are used internally by the filter engine.|
|FWPS_METADATA_FIELD_TOKEN|The token used to validate the permissions for the user.|
|FWPS_METADATA_FIELD_TRANSPORT_CONTROL_DATA|An optional socket control data object.|
|FWPS_METADATA_FIELD_TRANSPORT_ENDPOINT_HANDLE|The handle for the end of the packet to be injected into the outbound transport layer.|
|FWPS_METADATA_FIELD_TRANSPORT_HEADER_INCLUDE_HEADER|The IP header if the packet is sent from a raw socket. **Note:**  Supported in Windows Server 2008, Windows Vista with SP1, and later.|
|FWPS_METADATA_FIELD_TRANSPORT_HEADER_SIZE|The size of the transport header.|
