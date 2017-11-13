---
title: Built-in callout identifiers
author: windows-driver-content
description: This section describes built-in callout identifiers.
ms.assetid: c0200388-1e79-41b9-890c-ce0034b329d8
keywords:
- Built-in callout identifiers network drivers
ms.author: windowsdriverdev
ms.date: 11/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")