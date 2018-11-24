---
title: Overview of NVGRE Task Offload
description: Describes an overview of Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload
ms.assetid: 5890AF7E-93E1-4E19-B483-C75657D749EB
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload


## NVGRE Encapsulation Packet Format

In this case, a protocol or filter driver will generate the (non-LSO) packets, including the GRE encapsulation, and send the packets on the wire. On the receive side, these (non-RSS, VMQ) packets are passed to the protocol driver without any modifications. Note that the NVGRE Task Offload feature does not specify the offloading of the encapsulation and decapsulation operations.

## Send and Receive Offloads

On the send path, the following task offloads need to account for encapsulation:

-   Checksum computation of IPv4 and TCP or UDP payload
-   Large Send Offload version 1 (LSO\_v1) and Large Send Offload version 2 (LSO\_v2)

For send-side offloads, the miniport must perform corresponding operations on the tunnel (outer) IP header, the transport (inner) IP header, and the TCP header.

On the receive path, the following task offloads need to account for encapsulation:

-   Checksum validation of IPv4 and TCP or UDP payload
-   Receive side scaling (RSS)
-   VMQ

For receive-side offloads, the NIC must parse the encapsulation protocol headers. For example, for GRE encapsulation, the NIC must parse the GRE header and perform task offloads on the transport (inner) and/or tunnel (outer) IP headers.

 

 





