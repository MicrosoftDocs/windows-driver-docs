---
title: Built-in callout identifiers
description: This section describes built-in callout identifiers.
ms.assetid: c0200388-1e79-41b9-890c-ce0034b329d8
keywords:
- Built-in callout identifiers network drivers
ms.date: 11/08/2017
ms.localizationpriority: medium
---

# Built-in callout identifiers

The identifiers for the callouts that are built into the Windows Filtering Platform are each represented by a GUID. These identifiers are defined as follows.

> [!NOTE]
> The V4 and V6 suffixes at the end of the callout identifiers indicate whether the callout is for the IPv4 network stack or the IPv6 network stack.

| Built-in callout identifier | Callout description |
| --- | --- |
| <p>FWPM_CALLOUT_IPSEC_INBOUND_TRANSPORT_V4</p><p>FWPM_CALLOUT_IPSEC_INBOUND_TRANSPORT_V6</p> | Verifies that each received packet that is supposed to arrive over a transport mode security association arrives securely. This callout is applicable at the transport layer. |
| <p>FWPM_CALLOUT_IPSEC_OUTBOUND_TRANSPORT_V4</p><p>FWPM_CALLOUT_IPSEC_OUTBOUND_TRANSPORT_V6</p> | Indicates to IPsec the outbound traffic that must be secured over transport mode security associations. This callout is applicable at the transport layer. |
| <p>FWPM_CALLOUT_IPSEC_INBOUND_TUNNEL_V4</p><p>FWPM_CALLOUT_IPSEC_INBOUND_TUNNEL_V6</p> | Verifies that each received packet that is supposed to arrive over a tunnel mode security association arrives securely. This callout is applicable at the transport layer. |
| <p>FWPM_CALLOUT_IPSEC_OUTBOUND_TUNNEL_V4</p><p>FWPM_CALLOUT_IPSEC_OUTBOUND_TUNNEL_V6</p> | Indicates to IPsec the outbound traffic that must be secured over tunnel mode security associations. This callout is applicable at the transport layer. |
| <p>FWPM_CALLOUT_IPSEC_FORWARD_INBOUND_TUNNEL_V4</p><p>FWPM_CALLOUT_IPSEC_FORWARD_INBOUND_TUNNEL_V6</p> | Verifies that each received packet that is supposed to arrive over a tunnel mode security association arrives securely. This callout is applicable at the forward layer. |
| <p>FWPM_CALLOUT_IPSEC_FORWARD_OUTBOUND_TUNNEL_V4</p><p>FWPM_CALLOUT_IPSEC_FORWARD_OUTBOUND_TUNNEL_V6</p> | Indicates to IPsec the outbound traffic that must be secured over a tunnel mode security association. This callout is applicable at the forward layer. |
| <p>FWPM_CALLOUT_IPSEC_INBOUND_INITIATE_SECURE_V4</p><p>FWPM_CALLOUT_IPSEC_INBOUND_INITIATE_SECURE_V6</p> | Verifies that each incoming connection that is supposed to arrive securely does so. This callout is applicable at the ALE accept layer. |
| <p>FWPM_CALLOUT_IPSEC_ALE_CONNECT_V4</p><p>FWPM_CALLOUT_IPSEC_ALE_CONNECT_V6</p> | Applies IPsec policy modifiers to client applications. |
| <p>FWPM_CALLOUT_WFP_TRANSPORT_LAYER_V4_SILENT_DROP</p><p>FWPM_CALLOUT_WFP_TRANSPORT_LAYER_V6_SILENT_DROP</p> | Silently drops all incoming packets for which TCP does not have a listening endpoint. This callout is applicable at the inbound transport layer. |
| <p>FWPM_CALLOUT_TCP_CHIMNEY_CONNECT_LAYER_V4</p><p>FWPM_CALLOUT_TCP_CHIMNEY_CONNECT_LAYER_V6</p> | Enables or disables TCP chimney offload for each outgoing connection. |
| <p>FWPM_CALLOUT_TCP_CHIMNEY_ACCEPT_LAYER_V4</p><p>FWPM_CALLOUT_TCP_CHIMNEY_ACCEPT_LAYER_V6</p> | Enables or disables TCP chimney offload for each incoming connection. |

