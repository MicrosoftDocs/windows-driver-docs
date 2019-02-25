---
title: Management filtering layer identifiers
description: This section describes management filtering layer identifiers.
ms.assetid: 3287d763-9d73-4bf3-8a32-81acb27f0d36
keywords:
- Management filtering layer identifiers network drivers
ms.date: 11/08/2017
ms.localizationpriority: medium
---

# Management filtering layer identifiers

The management filtering layer identifiers are generally used by user-mode applications and are each represented by a GUID, which is 128 bits in size. These identifiers are defined as follows.

> [!NOTE]
> The V4 and V6 suffixes at the end of the layer identifiers indicate whether the layer is located in the IPv4 network stack or in the IPv6 network stack.

| Management filtering layer identifier | Filtering layer description |
| --- | --- |
| <p>FWPM_LAYER_INBOUND_IPPACKET_V4</p><p>FWPM_LAYER_INBOUND_IPPACKET_V6</p> | This filtering layer is located in the receive path just after the IP header of a received packet has been parsed but before any IP header processing takes place. No IPsec decryption or reassembly has occurred. |
| <p>FWPM_LAYER_INBOUND_IPPACKET_V4_DISCARD</p><p>FWPM_LAYER_INBOUND_IPPACKET_V6_DISCARD</p> | This filtering layer is located in the receive path for processing any received packets that have been discarded at the network layer. |
| <p>FWPM_LAYER_OUTBOUND_IPPACKET_V4</p><p>FWPM_LAYER_OUTBOUND_IPPACKET_V6</p> | This filtering layer is located in the send path just before the sent packet is evaluated for fragmentation. All IP header processing is complete and all extension headers are in place. Any IPsec authentication and encryption has already occurred. |
| <p>FWPM_LAYER_OUTBOUND_IPPACKET_V4_DISCARD</p><p>FWPM_LAYER_OUTBOUND_IPPACKET_V6_DISCARD</p> | This filtering layer is located in the send path for processing any sent packets that have been discarded at the network layer. |
| <p>FWPM_LAYER_IPFORWARD_V4</p><p>FWPM_LAYER_IPFORWARD_V6</p> | This filtering layer is located in the forwarding path at the point where a received packet is forwarded. |
| <p>FWPM_LAYER_IPFORWARD_V4_DISCARD</p><p>FWPM_LAYER_IPFORWARD_V6_DISCARD</p> | This filtering layer is located in the forwarding path for processing any forwarded packets that have been discarded at the forward layer. |
| <p>FWPM_LAYER_INBOUND_TRANSPORT_V4</p><p>FWPM_LAYER_INBOUND_TRANSPORT_V6</p> | This filtering layer is located in the receive path just after a received packet's header has been parsed by the network stack at the transport layer, but before any transport layer processing takes place. |
| <p>FWPM_LAYER_INBOUND_TRANSPORT_V4_DISCARD</p><p>FWPM_LAYER_INBOUND_TRANSPORT_V6_DISCARD</p> | This filtering layer is located in the receive path for processing any received packets that have been discarded at the transport layer. |
| <p>FWPM_LAYER_OUTBOUND_TRANSPORT_V4</p><p>FWPM_LAYER_OUTBOUND_TRANSPORT_V6</p> | <p>This filtering layer is located in the send path just after a sent packet has been passed to the network layer for processing but before any network layer processing takes place.</p><p>This filtering layer is located at the top of the network layer instead of at the bottom of the transport layer so that any packets that are sent by third-party transports or as raw packets are filtered at this layer.</p> |
| <p>FWPM_LAYER_OUTBOUND_TRANSPORT_V4_DISCARD</p><p>FWPM_LAYER_OUTBOUND_TRANSPORT_V6_DISCARD</p> | This filtering layer is located in the send path for processing any sent packets that have been discarded at the transport layer. |
| <p>FWPM_LAYER_STREAM_V4</p><p>FWPM_LAYER_STREAM_V6</p> | This filtering layer is located in the stream data path. This layer allows for processing network data on a per stream basis. At the stream layer, the network data is bidirectional. |
| <p>FWPM_LAYER_STREAM_V4_DISCARD</p><p>FWPM_LAYER_STREAM_V6_DISCARD</p> | This filtering layer is reserved for future use. |
| <p>FWPM_LAYER_DATAGRAM_DATA_V4</p><p>FWPM_LAYER_DATAGRAM_DATA_V6</p> | This filtering layer is located in the datagram data path. This layer allows for processing network data on a per datagram basis. At the datagram layer, the network data is bidirectional. |
| <p>FWPM_LAYER_DATAGRAM_DATA_V4_DISCARD</p><p>FWPM_LAYER_DATAGRAM_DATA_V6_DISCARD</p> | This filtering layer is located in the datagram data path for processing any datagrams that have been discarded. |
| <p>FWPM_LAYER_INBOUND_ICMP_ERROR_V4</p><p>FWPM_LAYER_INBOUND_ICMP_ERROR_V6</p> | This filtering layer is located in the receive path for processing received ICMP messages for the transport protocol. |
| <p>FWPM_LAYER_INBOUND_ICMP_ERROR_V4_DISCARD</p><p>FWPM_LAYER_INBOUND_ICMP_ERROR_V6_DISCARD</p> | This filtering layer is located in the receive path for processing received ICMP messages that have been discarded. |
| <p>FWPM_LAYER_OUTBOUND_ICMP_ERROR_V4</p><p>FWPM_LAYER_OUTBOUND_ICMP_ERROR_V6</p> | This filtering layer is located in the send path for processing sent ICMP messages for the transport protocol. |
| <p>FWPM_LAYER_OUTBOUND_ICMP_ERROR_V4_DISCARD</p><p>FWPM_LAYER_OUTBOUND_ICMP_ERROR_V6_DISCARD</p> | This filtering layer is located in the send path for processing sent ICMP messages that have been discarded. |
| <p>FWPM_LAYER_ALE_AUTH_CONNECT_V4</p><p>FWPM_LAYER_ALE_AUTH_CONNECT_V6</p> | This filtering layer allows for authorizing connect requests for outgoing TCP connections, as well as authorizing outgoing non-TCP traffic based on the first packet sent. |
| <p>FWPM_LAYER_ALE_AUTH_CONNECT_V4_DISCARD</p><p>FWPM_LAYER_ALE_AUTH_CONNECT_V6_DISCARD</p> | This filtering layer allows for processing connect requests for outgoing TCP connections that have been discarded, as well as processing authorizations for outgoing non-TCP traffic that have been discarded. |
| <p>FWPM_LAYER_ALE_FLOW_ESTABLISHED_V4</p><p>FWPM_LAYER_ALE_FLOW_ESTABLISHED_V6</p> | This filtering layer allows for notification of when a TCP connection has been established, or when non-TCP traffic has been authorized. |
| <p>FWPM_LAYER_ALE_FLOW_ESTABLISHED_V4_DISCARD</p><p>FWPM_LAYER_ALE_FLOW_ESTABLISHED_V6_DISCARD</p> | This filtering layer allows for processing when an established TCP connection has been discarded at the flow established layer, as well as when authorized non-TCP traffic has been discarded at the flow established layer. |
| <p>FWPM_LAYER_ALE_AUTH_LISTEN_V4</p><p>FWPM_LAYER_ALE_AUTH_LISTEN_V6</p> | This filtering layer allows for authorizing TCP listen requests. |
| <p>FWPM_LAYER_ALE_AUTH_LISTEN_V4_DISCARD</p><p>FWPM_LAYER_ALE_AUTH_LISTEN_V6_DISCARD</p> | This filtering layer allows for processing TCP listen requests that have been discarded. |
| <p>FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V4</p><p>FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V6</p> | This filtering layer allows for authorizing accept requests for incoming TCP connections, as well as authorizing incoming non-TCP traffic based on the first packet received. |
| <p>FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V4_DISCARD</p><p>FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V6_DISCARD</p> | This filtering layer allows for processing accept requests for incoming TCP connections that have been discarded, as well as processing authorizations for incoming non-TCP traffic that have been discarded. |
| <p>FWPM_LAYER_ALE_AUTH_ROUTE_V4</p><p>FWPM_LAYER_ALE_AUTH_ROUTE_V6</p> | This filtering layer allows for inspecting and filtering the route and path parameters of bind and connect requests. |
| <p>FWPM_LAYER_ALE_ENDPOINT_CLOSURE_V4</p><p>FWPM_LAYER_ALE_ENDPOINT_CLOSURE_V6</p> | This filtering layer is used as an opportunity to reclaim resources allocated by the callout driver in any of the ALE_AUTH_CONNECT or ALE_AUTH_RECV_ACCEPT layers. |
| <p>FWPM_LAYER_ALE_RESOURCE_ASSIGNMENT_V4</p><p>FWPM_LAYER_ALE_RESOURCE_ASSIGNMENT_V6</p> | This filtering layer allows for authorizing transport port assignments, bind requests, promiscuous mode requests, and raw mode requests. |
| <p>FWPM_LAYER_ALE_RESOURCE_ASSIGNMENT_V4_DISCARD</p><p>FWPM_LAYER_ALE_RESOURCE_ASSIGNMENT_V6_DISCARD</p> | This filtering layer allows for processing the following discarded items: transport port assignments, bind requests, promiscuous mode requests, and raw mode requests. |
| <p>FWPM_LAYER_ALE_RESOURCE_RELEASE_V4</p><p>FWPM_LAYER_ALE_RESOURCE_RELEASE_V6</p> | This filtering layer is used as an opportunity to reclaim resources allocated by the callout driver in any of the ALE_RESOURCE_ASSIGNMENT layers. |
| <p>FWPM_LAYER_IPSEC_KM_DEMUX_V4</p><p>FWPM_LAYER_IPSEC_KM_DEMUX_V6</p> | This filtering layer is used to determine which keying modules are invoked when the local system is the initiator. This is a user-mode filtering layer. |
| <p>FWPM_LAYER_IPSEC_V4</p><p>FWPM_LAYER_IPSEC_V6</p> | This filtering layer allows the keying module to look up quick-mode policy information when negotiating quick-mode security associations. This is a user-mode filtering layer. |
| <p>FWPM_LAYER_IKEEXT_V4</p><p>FWPM_LAYER_IKEEXT_V6</p> | This filtering layer allows the IKE and authenticated IP modules to look up main-mode policy information when negotiating main-mode security associations. This is a user-mode filtering layer. |
| FWPM_LAYER_RPC_UM | This filtering layer allows for inspecting the RPC data fields that are available in user mode. This is a user-mode filtering layer. |
| FWPM_LAYER_RPC_EPMAP | This filtering layer allows for inspecting the RPC data fields that are available in user mode during endpoint resolution. This is a user-mode filtering layer. |
| FWPM_LAYER_RPC_EP_ADD | This filtering layer allows for inspecting the RPC data fields that are available in user mode when a new endpoint is added. This is a user-mode filtering layer. |
| FWPM_LAYER_RPC_PROXY_CONN | This filtering layer allows for inspecting RpcProxy connection requests. This is a user-mode filtering layer. |
| FWPM_LAYER_RPC_PROXY_IF | This filtering layer allows for inspecting the interface used for RpcProxy connections. This is a user-mode filtering layer. |
| FWPM_LAYER_INBOUND_MAC_FRAME_ETHERNET | This filtering layer allows for inspecting the MAC frame data at the inbound lower (to the NDIS protocol driver) layer. **Note**: Available only on Windows 8 and later. |
| FWPM_LAYER_OUTBOUND_MAC_FRAME_ETHERNET | This filtering layer allows for inspecting the MAC frame data at the outbound upper (to the NDIS protocol driver) layer. **Note**: Available only on Windows 8 and later. |
| FWPM_LAYER_INBOUND_MAC_FRAME_NATIVE | This filtering layer allows for inspecting the MAC frame data at the inbound lower (to the NDIS miniport driver) layer. **Note**: Available only on Windows 8 and later. |
| FWPM_LAYER_OUTBOUND_MAC_FRAME_NATIVE | This filtering layer allows for inspecting the MAC frame data at the outbound lower (to the NDIS miniport driver) layer. **Note**: Available only on Windows 8 and later. |
| FWPM_LAYER_INGRESS_VSWITCH_ETHERNET | This filtering layer allows for inspecting the ingress 802.3 data of the Hyper-V extensible switch. **Note**: Available only on Windows 8 and later. |
| FWPM_LAYER_EGRESS_VSWITCH_ETHERNET | This filtering layer allows for inspecting the egress 802.3 data of the Hyper-V extensible switch. **Note**: Available only on Windows 8 and later. |
| <p>FWPM_LAYER_INGRESS_VSWITCH_TRANSPORT_V4</p><p>FWPM_LAYER_INGRESS_VSWITCH_TRANSPORT_V6</p> | This filtering layer allows for inspecting the ingress transport data of the Hyper-V extensible switch. **Note**: Available only on Windows 8 and later. |
| <p>FWPM_LAYER_EGRESS_VSWITCH_TRANSPORT_V4</p><p>FWPM_LAYER_EGRESS_VSWITCH_TRANSPORT_V6</p> | This filtering layer allows for inspecting the egress transport data of the Hyper-V extensible switch. **Note**: Available only on Windows 8 and later. |

