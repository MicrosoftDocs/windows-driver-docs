---
title: NVGRE Task Offload
description: This section describes Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload
ms.assetid: D1BE5659-4491-411B-9D32-9CB7A141A240
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload

Hyper-V Network Virtualization supports Network Virtualization using Generic Routing Encapsulation (NVGRE) as the mechanism to virtualize IP addresses. In NVGRE, the virtual machine's packet is encapsulated inside another packet. The header of this new, NVGRE-formatted packet has the appropriate source and destination provider area (PA) IP addresses. In addition, it has a 24-bit Virtual Subnet ID (VSID), which is stored in the GRE header of the new packet.

The following figure shows a GRE-encapsulated packet. On the wire, NVGRE-encapsulated packets look like IP-over-Ethernet packets, except that the payload of the outer IP header is a GRE-encapsulated IP packet (including the Ethernet header).

![comparison between original packet and packet with gre encapsulation. both contain mac (gre contains inner mac), ip header (gre contains inner ip header), tcp header, and tcp user data. in addition, packet with gre encapsulation contains outer mac, outer ip header, and gre.](images/nvgre.png)

NDIS 6.30 (available in Windows Server 2012 and later) introduces NVGRE Task Offload, which makes it possible to use NVGRE-formatted packets with:

-   Large Send Offload (LSO)
-   Virtual Machine Queue (VMQ)
-   Transmit (Tx) checksum offload (IPv4, TCP, UDP)
-   Receive (Rx) checksum offload (IPv4, TCP, UDP)

**Note**  It is possible for a protocol driver to offload "mixed mode" packets, which means packets in which the inner and outer IP header versions are different. For example, a packet could have outer IP header as IPv6 and the inner IP header as IPv4.

 

**Note**  It is also possible for a protocol driver to offload an NVGRE-formatted packet that has no inner TCP or UDP header. For example, an IP packet could have an inner payload that is an Internet Control Message Protocol (ICMP) packet.

 

For more information about NVGRE, see the following Internet Draft:

-   [NVGRE: Network Virtualization using Generic Routing Encapsulation](http://ietfreport.isoc.org/idref/draft-sridharan-virtualization-nvgre/)

NVGRE is based on Generic Routing Encapsulation (GRE). For more information about GRE, see the following resources:

-   [RFC 2784: Generic Routing Encapsulation (GRE)](http://tools.ietf.org/html/rfc2784)
-   [RFC 2890: Key and Sequence Number Extensions to GRE](http://tools.ietf.org/html/rfc2890)

This section includes:

-   [Overview of Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload](overview-of-network-virtualization-using-generic-routing-encapsulation--nvgre--task-offload.md)
-   [Supporting NVGRE in Large Send Offload (LSO)](supporting-nvgre-in-large-send-offload--lso-.md)
-   [Supporting NVGRE in Checksum Offload](supporting-nvgre-in-checksum-offload.md)
-   [Supporting NVGRE in RSS and VMQ Receive Task Offloads](supporting-nvgre-in-rss-and-vmq-receive-task-offloads.md)
-   [Locating the Transport Header for Encapsulated Packets in the Receive Path](locating-the-transport-header-for-encapsulaged-packets-in-the-receive-path.md)
-   [Determining the NVGRE Task Offload Capabilities of a Network Adapter](determining-the-nvgre-task-offload-capabilities-of-a-network-adapter.md)
-   [Querying and Changing NVGRE Task Offload State](querying-and-changing-nvgre-task-offload-state.md)
-   [Standardized INF Keywords for NVGRE Task Offload](standardized-inf-keywords-for-nvgre-task-offload.md)

## Related topics


[Offloading Checksum Tasks](offloading-checksum-tasks.md)

[Offloading the Segmentation of Large TCP Packets](offloading-the-segmentation-of-large-tcp-packets.md)

[TCP/IP Task Offload](task-offload.md)

 

 






