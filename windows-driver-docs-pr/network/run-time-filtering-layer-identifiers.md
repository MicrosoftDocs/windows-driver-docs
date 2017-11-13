---
title: Run-time filtering layer identifiers
author: windows-driver-content
description: This section describes run-time filtering layer identifiers.
ms.assetid: 21c466a3-cdfc-4e94-83d3-1c2c7a58a2ca
keywords:
- Run-time filtering layer identifiers network drivers
ms.author: windowsdriverdev
ms.date: 11/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Run-time filtering layer identifiers

The run-time filtering layer identifiers are used by kernel-mode callout drivers and are each represented by a locally unique identifier ([LUID](https://msdn.microsoft.com/library/windows/hardware/ff557080)), which is 64 bits in size. These identifiers are constant values in the FWPS_BUILTIN_LAYERS enumeration that is defined in Fwpsk.h. These identifiers are defined as follows:

> [!NOTE]
> The V4 and V6 suffixes at the end of the run-time layer identifiers indicate whether the layer is located in the IPv4 network stack or in the IPv6 network stack.

| Run-time filtering layer identifier | Filtering layer description |
| --- | --- |
| <p>FWPS_LAYER_INBOUND_IPPACKET_V4</p><p>FWPS_LAYER_INBOUND_IPPACKET_V6</p> | This filtering layer is located in the receive path just after the IP header of a received packet has been parsed but before any IP header processing takes place. No IPsec decryption or reassembly has occurred. |
| <p>FWPS_LAYER_INBOUND_IPPACKET_V4_DISCARD</p><p>FWPS_LAYER_INBOUND_IPPACKET_V6_DISCARD</p> | This filtering layer is located in the receive path for processing any received packets that have been discarded at the network layer. |
| <p>FWPS_LAYER_OUTBOUND_IPPACKET_V4</p><p>FWPS_LAYER_OUTBOUND_IPPACKET_V6</p> | This filtering layer is located in the send path just before the sent packet is evaluated for fragmentation. All IP header processing is complete and all extension headers are in place. Any IPsec authentication and encryption has already occurred. |
| <p>FWPS_LAYER_OUTBOUND_IPPACKET_V4_DISCARD</p><p>FWPS_LAYER_OUTBOUND_IPPACKET_V6_DISCARD</p> | This filtering layer is located in the send path for processing any sent packets that have been discarded at the network layer. |
| <p>FWPS_LAYER_IPFORWARD_V4</p><p>FWPS_LAYER_IPFORWARD_V6</p> | This filtering layer is located in the forwarding path at the point where a received packet is forwarded. |
| <p>FWPS_LAYER_IPFORWARD_V4_DISCARD</p><p>FWPS_LAYER_IPFORWARD_V6_DISCARD</p> | This filtering layer is located in the forwarding path for processing any forwarded packets that have been discarded at the forward layer. |
| <p>FWPS_LAYER_INBOUND_TRANSPORT_V4</p><p>FWPS_LAYER_INBOUND_TRANSPORT_V6</p> | This filtering layer is located in the receive path just after a received packet's header has been parsed by the network stack at the transport layer, but before any transport layer processing takes place. |
| <p>FWPS_LAYER_INBOUND_TRANSPORT_V4_DISCARD</p><p>FWPS_LAYER_INBOUND_TRANSPORT_V6_DISCARD</p> | This filtering layer is located in the receive path for processing any received packets that have been discarded at the transport layer. |
| <p>FWPS_LAYER_OUTBOUND_TRANSPORT_V4</p><p>FWPS_LAYER_OUTBOUND_TRANSPORT_V6</p> | <p>This filtering layer is located in the send path just after a sent packet has been passed to the network layer for processing but before any network layer processing takes place.</p><p>This filtering layer is located at the top of the network layer instead of at the bottom of the transport layer so that any packets that are sent by third-party transports or as raw packets are filtered at this layer.</p> |
| <p>FWPS_LAYER_OUTBOUND_TRANSPORT_V4_DISCARD</p><p>FWPS_LAYER_OUTBOUND_TRANSPORT_V6_DISCARD</p> | This filtering layer is located in the send path for processing any sent packets that have been discarded at the transport layer. |
| <p>FWPS_LAYER_STREAM_V4</p><p>FWPS_LAYER_STREAM_V6</p> | This filtering layer is located in the stream data path. This layer allows for processing network data on a per stream basis. At the stream layer, the network data is bidirectional. |
| <p>FWPS_LAYER_STREAM_V4_DISCARD</p><p>FWPS_LAYER_STREAM_V6_DISCARD</p> | This filtering layer is reserved for future use. |
| <p>FWPS_LAYER_DATAGRAM_DATA_V4</p><p>FWPS_LAYER_DATAGRAM_DATA_V6</p> | This filtering layer is located in the datagram data path. This layer allows for processing network data on a per datagram basis. At the datagram layer, the network data is bidirectional. |
| <p>FWPS_LAYER_DATAGRAM_DATA_V4_DISCARD</p><p>FWPS_LAYER_DATAGRAM_DATA_V6_DISCARD</p> | This filtering layer is located in the datagram data path for processing any datagrams that have been discarded. |
| <p>FWPS_LAYER_INBOUND_ICMP_ERROR_V4</p><p>FWPS_LAYER_INBOUND_ICMP_ERROR_V6</p> | This filtering layer is located in the receive path for processing received ICMP messages for the transport protocol. |
| <p>FWPS_LAYER_INBOUND_ICMP_ERROR_V4_DISCARD</p><p>FWPS_LAYER_INBOUND_ICMP_ERROR_V6_DISCARD</p> | This filtering layer is located in the receive path for processing received ICMP messages that have been discarded. |
| <p>FWPS_LAYER_OUTBOUND_ICMP_ERROR_V4</p><p>FWPS_LAYER_OUTBOUND_ICMP_ERROR_V6</p> | This filtering layer is located in the send path for processing sent ICMP messages for the transport protocol. |
| <p>FWPS_LAYER_OUTBOUND_ICMP_ERROR_V4_DISCARD</p><p>FWPS_LAYER_OUTBOUND_ICMP_ERROR_V6_DISCARD</p> | This filtering layer is located in the send path for processing sent ICMP messages that have been discarded. |
| <p>FWPS_LAYER_ALE_RESOURCE_ASSIGNMENT_V4</p><p>FWPS_LAYER_ALE_RESOURCE_ASSIGNMENT_V6</p> | This filtering layer allows for authorizing transport port assignments, bind requests, promiscuous mode requests, and raw mode requests. |
| <p>FWPS_LAYER_ALE_RESOURCE_ASSIGNMENT_V4_DISCARD</p><p>FWPS_LAYER_ALE_RESOURCE_ASSIGNMENT_V6_DISCARD</p> | This filtering layer allows for processing the following discarded items: transport port assignments, bind requests, promiscuous mode requests, and raw mode requests. |
| <p>FWPS_LAYER_ALE_AUTH_LISTEN_V4</p><p>FWPS_LAYER_ALE_AUTH_LISTEN_V6</p> | This filtering layer allows for authorizing TCP listen requests. |
| <p>FWPS_LAYER_ALE_AUTH_LISTEN_V4_DISCARD</p><p>FWPS_LAYER_ALE_AUTH_LISTEN_V6_DISCARD</p> | This filtering layer allows for processing TCP listen requests that have been discarded. |
| <p>FWPS_LAYER_ALE_AUTH_RECV_ACCEPT_V4</p><p>FWPS_LAYER_ALE_AUTH_RECV_ACCEPT_V6</p> | This filtering layer allows for authorizing accept requests for incoming TCP connections, as well as authorizing incoming non-TCP traffic based on the first packet received. |
| <p>FWPS_LAYER_ALE_AUTH_RECV_ACCEPT_V4_DISCARD</p><p>FWPS_LAYER_ALE_AUTH_RECV_ACCEPT_V6_DISCARD</p> | This filtering layer allows for processing accept requests for incoming TCP connections that have been discarded, as well as processing authorizations for incoming non-TCP traffic that have been discarded. |
| <p>FWPS_LAYER_ALE_AUTH_CONNECT_V4</p><p>FWPS_LAYER_ALE_AUTH_CONNECT_V6</p> | This filtering layer allows for authorizing connect requests for outgoing TCP connections, as well as authorizing outgoing non-TCP traffic based on the first packet sent. |
| <p>FWPS_LAYER_ALE_AUTH_CONNECT_V4_DISCARD</p><p>FWPS_LAYER_ALE_AUTH_CONNECT_V6_DISCARD</p> | This filtering layer allows for processing connect requests for outgoing TCP connections that have been discarded, as well as processing authorizations for outgoing non-TCP traffic that have been discarded. |
| <p>FWPS_LAYER_ALE_FLOW_ESTABLISHED_V4</p><p>FWPS_LAYER_ALE_FLOW_ESTABLISHED_V6</p> | This filtering layer allows for notification of when a TCP connection has been established, or when non-TCP traffic has been authorized. |
| <p>FWPS_LAYER_ALE_FLOW_ESTABLISHED_V4_DISCARD</p><p>FWPS_LAYER_ALE_FLOW_ESTABLISHED_V6_DISCARD</p> | This filtering layer allows for processing when an established TCP connection has been discarded at the flow established layer, as well as when authorized non-TCP traffic has been discarded at the flow established layer. |
| <p>FWPS_LAYER_RESERVED1_V4</p><p>FWPS_LAYER_RESERVED1_V6</p> | This filtering layer is not supported. |
| <p>FWPS_LAYER_NAME_RESOLUTION_CACHE_V4</p><p>FWPS_LAYER_NAME_RESOLUTION_CACHE_V6</p> | This filtering layer allows for querying the names recently resolved by the system. |
| <p>FWPS_LAYER_ALE_RESOURCE_RELEASE_V4</p><p>FWPS_LAYER_ALE_RESOURCE_RELEASE_V6</p> | This filtering layer is used as an opportunity to reclaim resources allocated by the callout driver in any of the ALE_RESOURCE_ASSIGNMENT layers. |
| <p>FWPS_LAYER_ALE_ENDPOINT_CLOSURE_V4</p><p>FWPS_LAYER_ALE_ENDPOINT_CLOSURE_V6</p> | This filtering layer is used as an opportunity to reclaim resources allocated by the callout driver in any of the ALE_AUTH_CONNECT or ALE_AUTH_RECV_ACCEPT layers. |
| <p>FWPS_LAYER_ALE_CONNECT_REDIRECT_V4</p><p>FWPS_LAYER_ALE_CONNECT_REDIRECT_V6</p> | This filtering layer allows for the redirecting of connect requests to a different IPV4/ IPV6 address and TCP/UDP port. |
| <p>FWPS_LAYER_ALE_BIND_REDIRECT_V4</p><p>FWPS_LAYER_ALE_BIND_REDIRECT_V6</p> | This filtering layer allows for the redirecting of bind requests to a different local IPV4/ IPV6 address and/or local TCP/UDP port. |
| FWPS_LAYER_INBOUND_MAC_FRAME_ETHERNET | This filtering layer allows for inspecting the MAC frame data at the inbound lower (to the NDIS protocol driver) layer. **Note**: Available only on Windows 8 and later. |
| FWPS_LAYER_OUTBOUND_MAC_FRAME_ETHERNET | This filtering layer allows for inspecting the MAC frame data at the outbound upper (to the NDIS protocol driver) layer. **Note**: Available only on Windows 8 and later. |
| FWPS_LAYER_INBOUND_MAC_FRAME_NATIVE | This filtering layer allows for inspecting the MAC frame data at the inbound lower (to the NDIS miniport driver) layer. **Note**: Available only on Windows 8 and later. |
| FWPS_LAYER_OUTBOUND_MAC_FRAME_NATIVE | This filtering layer allows for inspecting the MAC frame data at the outbound lower (to the NDIS miniport driver) layer. **Note**: Available only on Windows 8 and later. |
| FWPS_LAYER_INGRESS_VSWITCH_ETHERNET | This filtering layer allows for inspecting the ingress 802.3 data of the Hyper-V extensible switch. **Note**: Available only on Windows 8 and later. |
| FWPS_LAYER_EGRESS_VSWITCH_ETHERNET | This filtering layer allows for inspecting the egress 802.3 data of the Hyper-V extensible switch. **Note**: Available only on Windows 8 and later. |
| <p>FWPS_LAYER_INGRESS_VSWITCH_TRANSPORT_V4</p><p>FWPS_LAYER_INGRESS_VSWITCH_TRANSPORT_V6</p> | This filtering layer allows for inspecting the ingress transport data of the Hyper-V extensible switch. **Note**: Available only on Windows 8 and later. |
| <p>FWPS_LAYER_EGRESS_VSWITCH_TRANSPORT_V4</p><p>FWPS_LAYER_EGRESS_VSWITCH_TRANSPORT_V6</p> | This filtering layer allows for inspecting the egress transport data of the Hyper-V extensible switch. **Note**: Available only on Windows 8 and later. |
| <p>FWPS_LAYER_STREAM_PACKET_V4</p><p>FWPS_LAYER_STREAM_PACKET_V6</p> | This filtering layer allows for inspection of network data on a per-TCP packet basis, including handshake and flow control exchanges. At the stream packet layer, the network data is bidirectional. |
| <p>FWPS_LAYER_IPSEC_KM_DEMUX_V4</p><p>FWPS_LAYER_IPSEC_KM_DEMUX_V6</p> | This filtering layer is used to determine which keying modules are invoked when the local system is the initiator. This is a user-mode filtering layer. |
| <p>FWPS_LAYER_IPSEC_V4</p><p>FWPS_LAYER_IPSEC_V6</p> | This filtering layer allows the keying module to look up quick-mode policy information when negotiating quick-mode security associations. This is a user-mode filtering layer. |
| <p>FWPS_LAYER_IKEEXT_V4</p><p>FWPS_LAYER_IKEEXT_V6</p> | This filtering layer allows the IKE and authenticated IP modules to look up main-mode policy information when negotiating main-mode security associations. This is a user-mode filtering layer. |
| FWPS_LAYER_RPC_UM | This filtering layer allows for inspecting the RPC data fields that are available in user mode. This is a user-mode filtering layer. |
| FWPS_LAYER_RPC_EPMAP | This filtering layer allows for inspecting the RPC data fields that are available in user mode during endpoint resolution. This is a user-mode filtering layer. |
| FWPS_LAYER_RPC_EP_ADD | This filtering layer allows for inspecting the RPC data fields that are available in user mode when a new endpoint is added. This is a user-mode filtering layer. |
| FWPS_LAYER_RPC_PROXY_CONN | This filtering layer allows for inspecting RpcProxy connection requests. This is a user-mode filtering layer. |
| FWPS_LAYER_RPC_PROXY_IF | This filtering layer allows for inspecting the interface used for RpcProxy connections. This is a user-mode filtering layer. |
| FWPS_LAYER_KM_AUTHORIZATION | This filtering layer allows for authorizing security association establishment. |

Each run-time layer identifier has an associated run-time data field identifier that represents a set of constant values. These data field identifiers are declared as FWPS_FIELDS_XXX enumerations in Fwpsk.h. For more information, see [Data Field Identifiers](https://msdn.microsoft.com/library/windows/hardware/ff546312).

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")