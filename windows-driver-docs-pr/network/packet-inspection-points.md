---
title: Packet Inspection Points
description: Packet Inspection Points
keywords:
- packet inspection points WDK Windows Filtering Platform
ms.date: 04/20/2017
---

# Packet Inspection Points

## Incoming packets


Incoming packets that are destined for an address that is assigned to the receiving computer (local host traffic) traverse up WFP layers in the following order:

<a href="" id="ip-packet--network-layer-"></a>**IP Packet (Network Layer)**  
All IP packets, including IP packet fragments, are available for inspection at this layer. However, when packets are IPsec-protected, deep content inspection or modification cannot be performed at this layer because the packets are not yet authenticated or decrypted.

<a href="" id="transport-layer"></a>**Transport Layer**  
All stand-alone or fully reassembled packets are available for inspection at this layer. IPsec-protected packets have been authenticated or decrypted.

<a href="" id="application-layer-enforcement--ale--receive-or-accept"></a>**Application Layer Enforcement (ALE) Receive or Accept**  
The very first packet that arrives at a local endpoint is indicated at this layer. For example, an arriving TCP synchronize (SYN) segment or the first UDP message that is associated with a UDP flow would be indicated. Packets that are required to re-authorize a connection, for example, after a firewall policy change, are also indicated at this layer, and the ALE reauthorization flag will be set.

<a href="" id="datagram-data-or-stream"></a>**Datagram Data or Stream**  
UDP messages and non-ICMP error messages are indicated at the datagram data layer.  This layer allows for inspecting network data on a per datagram basis. At the datagram layer, the network data is bidirectional. TCP data flows (data streams only) are available for inspection at the stream layer.

## Outgoing packets

Outgoing packets that originate from an address that is assigned to the sending computer (local host sourced traffic) traverse down the following WFP layers:

<a href="" id="ale-connect"></a>**ALE Connect**  
TCP connection requests (made before the SYN segment is generated) and the first UDP message that is sent to a remote endpoint are indicated at this layer.

<a href="" id="datagram-data-or-stream"></a>**Datagram Data or Stream**  

UDP messages and non-ICMP error messages are indicated at the datagram data layer.  This layer allows for inspecting network data on a per datagram basis. At the datagram layer, the network data is bidirectional. TCP data flows (data streams only) are available for inspection at the stream layer.

<a href="" id="transport-and-icmp-error"></a>**Transport and ICMP Error**  
The transport filtering layer is located in the send path just after a sent packet has been passed to the network layer for processing but before any network layer processing takes place. This filtering layer is located at the top of the network layer instead of at the bottom of the transport layer so that any packets that are sent by third-party transports or as raw packets are filtered at this layer.

The ICMP Error filtering layer is located in the send path for inspecting received ICMP error messages for the transport protocol.

<a href="" id="ip-packet"></a>**IP Packet**  
IP packet fragments are not indicated; inspection of outgoing IP fragments is currently unavailable.

IP packets or fragments that do not originate from, or are not destined for, an address that is assigned to the local computer are available for inspection at the forwarding layer. For example, if a packet that is destined for a local client is modified to have a nonlocal destination address and then is injected into the receive path, it will be injected into the forwarding layer. Similarly, if a packet that originates from a local source address is modified to have a nonlocal source address, it will be delivered to the forwarding layer after it is injected into the send path.

 

 





