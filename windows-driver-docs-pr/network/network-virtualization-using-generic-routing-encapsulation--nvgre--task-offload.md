---
title: About Network Virtualization using Generic Routing Encapsulation (NVGRE)
description: This section describes Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload
ms.date: 06/15/2023
---

# About Network Virtualization using Generic Routing Encapsulation (NVGRE)

Hyper-V Network Virtualization supports Network Virtualization using Generic Routing Encapsulation (NVGRE) as the mechanism to virtualize IP addresses. In NVGRE, the virtual machine's packet is encapsulated inside another packet. The header of this new, NVGRE-formatted packet has the appropriate source and destination provider area (PA) IP addresses. In addition, it has a 24-bit Virtual Subnet ID (VSID), which is stored in the GRE header of the new packet.

The following figure shows a GRE-encapsulated packet. On the wire, NVGRE-encapsulated packets look like IP-over-Ethernet packets, except that the payload of the outer IP header is a GRE-encapsulated IP packet (including the Ethernet header).

:::image type="content" source="images/nvgre.png" alt-text="Diagram comparing original packet and GRE-encapsulated packet. Both have MAC, IP header, TCP header, and TCP user data. GRE-encapsulated packet also has outer MAC, outer IP header, and GRE.":::

NDIS 6.30 (available in Windows Server 2012 and later) introduces NVGRE Task Offload, which makes it possible to use NVGRE-formatted packets with:

- Large Send Offload (LSO)
- Virtual Machine Queue (VMQ)
- Transmit (Tx) checksum offload (IPv4, TCP, UDP)
- Receive (Rx) checksum offload (IPv4, TCP, UDP)

NDIS 6.85 introduces support for NVGRE with UDP segmentation offload (USO).

**Note**: It is possible for a protocol driver to offload "mixed mode" packets, which means packets in which the inner and outer IP header versions are different. For example, a packet could have outer IP header as IPv6 and the inner IP header as IPv4.

**Note**: It is also possible for a protocol driver to offload an NVGRE-formatted packet that has no inner TCP or UDP header. For example, an IP packet could have an inner payload that is an Internet Control Message Protocol (ICMP) packet.

For more information about NVGRE, see the following Internet Draft:

- [NVGRE: Network Virtualization using Generic Routing Encapsulation](https://tools.ietf.org/html/rfc7637)

NVGRE is based on Generic Routing Encapsulation (GRE). For more information about GRE, see the following resources:

- [RFC 2784: Generic Routing Encapsulation (GRE)](https://tools.ietf.org/html/rfc2784)
- [RFC 2890: Key and Sequence Number Extensions to GRE](https://tools.ietf.org/html/rfc2890)

This section includes:

- [Overview of Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload](overview-of-network-virtualization-using-generic-routing-encapsulation--nvgre--task-offload.md)
- [Supporting NVGRE in Large Send Offload (LSO)](supporting-nvgre-in-large-send-offload--lso-.md)
- [Supporting NVGRE in UDP Segmentation Offload (USO)](nvgre-support-with-udp-segmentation-offload.md)
- [Supporting NVGRE in Checksum Offload](supporting-nvgre-in-checksum-offload.md)
- [Supporting NVGRE in RSS and VMQ Receive Task Offloads](supporting-nvgre-in-rss-and-vmq-receive-task-offloads.md)
- [Locating the Transport Header for Encapsulated Packets in the Receive Path](locating-the-transport-header-for-encapsulaged-packets-in-the-receive-path.md)
- [Determining the NVGRE Task Offload Capabilities of a Network Adapter](determining-the-nvgre-task-offload-capabilities-of-a-network-adapter.md)
- [Querying and Changing NVGRE Task Offload State](querying-and-changing-nvgre-task-offload-state.md)
- [Standardized INF Keywords for NVGRE Task Offload](standardized-inf-keywords-for-nvgre-task-offload.md)

## Related topics

[Offloading Checksum Tasks](offloading-checksum-tasks.md)

[Offloading the Segmentation of Large TCP Packets](offloading-the-segmentation-of-large-tcp-packets.md)

[TCP/IP Task Offload](task-offload.md)
