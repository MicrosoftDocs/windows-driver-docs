---
title: UDP Receive Segment Coalescing Offload (URO)
description: Rules for coalescing UDP packets and how to write a URO miniport driver.
ms.date: 01/29/2024
---

# UDP Receive Segment Coalescing Offload (URO)

Starting in WIN11_NEXT, UDP Receive Segment Coalescing Offload (URO) enables network interface cards (NICs) to coalesce UDP receive segments. NICs can combine UDP datagrams from the same flow that match a set of rules into a logically contiguous buffer. These combined datagrams are then indicated to the Windows networking stack as a single large packet. 

Coalescing UPD datagrams reduces the CPU cost to process packets in high-bandwidth flows, resulting in higher throughput and fewer cycles per byte.

The following sections describe the rules for coalescing UDP packets and how to write a URO miniport driver.

- [Rules for coalescing UDP packets](#rules-for-coalescing-udp-packets)
- [Write a URO miniport driver](#write-a-uro-miniport-driver)
- [Programming considerations for URO drivers](#programming-considerations-for-uro-drivers)

## Rules for coalescing UDP packets 

URO coalescing can only be attempted on packets that meet all the following criteria:

- **IpHeader.Version** is identical for all packets.
- **IpHeader.SourceAddress** and **IpHeader.DestinationAddress** are identical for all packets.
- **UdpHeader.SourcePort** and **UdpHeader.DestinationPort** are identical for all packets.
- **UdpHeader.Length** is identical for all packets, except the last packet, which may be less.
- **UdpHeader.Length** must be nonzero.
- **UdpHeader.Checksum**, if non-zero, must be correct on all packets. This means that receive checksum offload must validate the packet.
- **Layer 2 headers** must be identical for all packets.

If the packets are IPv4, they must also meet the following criteria:

- **IPv4Header.Protocol** == 17 (UDP) for all packets.
- **EthernetHeader.EtherType** == 0x0800 for all packets.
- The **IPv4Header.HeaderChecksum** on received packets must be correct. This means that receive checksum offload must validate the header.
- **IPv4Header.HeaderLength** == 5 (no IPv4 Option Headers) for all packets.
- **IPv4Header.ToS** is identical for all packets.
- **IPv4Header.ECN** is identical for all packets.
- **IPv4Header.DontFragment** is identical for all packets.
- **IPv4Header.TTL** is identical for all packets.
- **IPv4Header.TotalLength** == **UdpHeader.Length** + length(**IPv4Header**) for all packets.

If the packets are IPv6, they must also meet the following criteria:

- **IPv6Header.NextHeader** == 17 (UDP) for all packets (no extension headers).
- **EthernetHeader.EtherType** == 0x86dd (IPv6) for all packets.
- **IPv6Header.TrafficClass** and **IPv6Header.ECN** are identical for all packets.
- **IPv6Header.FlowLabel** is identical for all packets.
- **IPv6Header.HopLimit** is identical for all packets.
- **IPv6Header.PayloadLength** == **UdpHeader.Length** for all packets.

### URO packet structure

The resulting Single Coalesced Unit (SCU) must have a single IP header and UDP header, followed by the UDP payload for all coalesced datagrams concatenated together.

URO indications must set the **IPv4Header.TotalLength** field to the total length of the SCU, or **IPv6Header.PayloadLength** field to the length of the UDP payload and **UdpHeader.Length** field to the length of coalesced payloads.

If Layer 2 (L2) headers are present in coalesced datagrams, the SCU must contain a valid L2 header. The L2 header in the SCU must resemble the L2 header of the coalesced datagrams.

### Checksum validation and indication

URO indications must set the **IPv4Header.HeaderChecksum** and **UdpHeader.Checksum** fields to zero and fill out the checksum offload out-of-band information on the SCU indicating IPv4 and UDP checksum success.

A packet that matches all conditions for being coalesced but fails checksum validation must be indicated separately. Packets received after it must not be coalesced with packets received before it. 

For example, suppose packets 1, 2, 3, 4, and 5 are received from the same flow, but packet 3 fails checksum validation. Packets 1 and 2 can be coalesced together, and packets 4 and 5 can be coalesced together, but packet 3 must not be coalesced with either SCU. Packets 1 and 2 must not be coalesced together with packets 4 and 5. Packet 2 is the last packet in an SCU and packet 4 starts a new SCU. Additionally, the SCU containing packets 1 and 2 must be indicated before packet 3 is indicated and packet 3 must be indicated before the SCU containing packets 4 and 5.

### Packet coalescing and flow separation

Packets from multiple flows may be coalesced in parallel, as hardware and memory permit. Packets from different flows must not be coalesced together.

Packets from multiple receives interleaved may be separated and coalesced with their respective flows. For example, given flows A, B, and C, if packets arrive in the order A, A, B, C, B, A, the packets from the A flow may be coalesced into AAA, and the packets from the B flow coalesced into BB, while the packet from the C flow may be indicated normally or coalesced with a pending SCU from flow C.

The packets within a given flow must not be reordered with respect to each other. For example, the packets from the A flow must be coalesced in the order received, regardless of the packets from the B and C flows received in between.

## Write a URO miniport driver

Starting in NDIS 6.89, the NDIS interface for URO facilitates communication between TCP/IP and the NDIS miniport driver.

### Report URO capability

A miniport driver advertises support for URO in the **UdpRsc** member of the [**NDIS_OFFLOAD**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_offload) structure, which it passes to the [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes) function.

### Query URO capability

To check if a miniport driver supports URO, NDIS drivers and other applications can query the [OID_TCP_OFFLOAD_HARDWARE_CAPABILITIES](/windows-hardware/drivers/network/oid-tcp-connection-offload-hardware-capabilities) OID, which returns the **NDIS_OFFLOAD** structure.

### Query URO state

To determine the current URO state, NDIS drivers and other applications can query the [OID_TCP_OFFLOAD_CURRENT_CONFIG](oid-tcp-offload-current-config.md) OID request. NDIS handles this OID and doesn't pass it down to the miniport.

### Change URO state

URO can be enabled or disabled by issuing the [**OID_TCP_OFFLOAD_PARAMETERS**](oid-tcp-offload-parameters.md) OID request. This OID uses an [**NDIS_OFFLOAD_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_offload_parameters) structure. In this structure, the **UdpRsc.Enabled** member can have the following values:

| Value                                        | Meaning |
|----------------------------------------------|---------|
| **NDIS_OFFLOAD_PARAMETERS_UDP_RSC_NO_CHANGE**<br>0 | The miniport driver shouldn't change the current setting. |
| **NDIS_OFFLOAD_PARAMETERS_UDP_RSC_DISABLED**<br>1 | URO is disabled. |
| **NDIS_OFFLOAD_PARAMETERS_UDP_RSC_ENABLED**<br>2  | URO is enabled. |

When a driver processes a **OID_TCP_OFFLOAD_PARAMETERS** OID request with the `NDIS_OFFLOAD_PARAMETERS_UDP_RSC_DISABLED` flag set, the NIC must wait to complete the request until all existing coalesced segments and outstanding URO indications are indicated. This ensures synchronization of URO enable/disable events across NDIS components. 

After the miniport driver processes the **OID_TCP_OFFLOAD_PARAMETERS** OID request, the miniport driver must issue an [**NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG**](ndis-status-task-offload-current-config.md) status indication with the updated offload state.

The `NDIS_OFFLOAD_PARAMETERS_SKIP_REGISTRY_UPDATE` flag in [**NDIS_OFFLOAD_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_offload_parameters) allows for runtime-only disabling of URO. Changes made with this flag aren't saved to the registry. 

### Opt-out of URO in NDIS 6.89 and later
Drivers targeting NDIS 6.89 and later should understand URO packets and handle them gracefully. To opt-out of URO:

- Lightweight filter (LWF) drivers set the `NDIS_FILTER_DRIVER_UDP_RSC_NOT_SUPPORTED` flag in the [**NDIS_FILTER_DRIVER_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_filter_driver_characteristics) structure.
- Protocol drivers set the `NDIS_PROTOCOL_DRIVER_UDP_RSC_NOT_SUPPORTED` flag in the [**NDIS_PROTOCOL_DRIVER_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_protocol_driver_characteristics) structure.

This approach ensures components that are unfamiliar with URO don't receive URO NBLs. NDIS disables URO on the miniport during binding if an LWF or protocol driver that doesn’t support URO is present.

## Programming considerations for URO drivers

Consider the following issues when implementing a URO-capable miniport driver.

### Winsock URO API
For information on the Winsock URO API, see [IPPROTO_UDP socket options](/windows/win32/winsock/ipproto-udp-socket-options). See the information on **UDP_RECV_MAX_COALESCED_SIZE** and **UDP_COALESCED_INFO**.

### Windows TCP/IP stack updates

The Microsoft TCP/IP transport enables URO at bind time with NDIS, unless configuration prevents it from doing so.

WFP callouts can use `FWP_CALLOUT_FLAG_ALLOW_URO` in [**FWPS_CALLOUT2**](/windows-hardware/drivers/ddi/fwpsk/ns-fwpsk-fwps_callout2_) to advertise their support for URO. If an incompatible WFP callout is registered at a URO-sensitive layer, then the OS will disable URO while the callout is active.

If a socket opts-in to URO with a max coalesced size greater than or equal to the hardware offload size, then the stack will deliver the NBLs from hardware unmodified to the socket.
If a socket opts-in to a smaller max coalesced size, the stack will break the coalesced receive into the smaller size for the socket.

If a socket doesn't opt-in to URO, then the stack will resegment receives for that socket. In the absence of hardware URO, the existing software URO feature will continue to be available.