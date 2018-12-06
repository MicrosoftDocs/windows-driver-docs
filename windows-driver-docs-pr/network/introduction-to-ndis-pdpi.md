---
title: Introduction to the NDIS PacketDirect Provider Interface
description: This section provides an introduction to the NDIS PacketDirect Provider Interface (PDPI)
ms.assetid: E85ED51E-BDE5-43BE-93BA-19F214670B8F
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to the NDIS PacketDirect Provider Interface


The PacketDirect Provider Interface (PDPI) extends NDIS with an accelerated I/O model, for both physical and virtual environments, that can increase the number of packets processed per second by an order of magnitude and significantly decrease jitter when compared to the traditional NDIS I/O path.

## Background


The traditional I/O model in Windows was implemented to be a multipurpose, general I/O platform that was intended to work with multiple media types with many different characteristics and where networking was only one aspect of the overall system. Today, as network virtualization has become a prevalent technology in datacenters, the traditional NDIS I/O model in the Windows Server OS is not only not sufficient to keep up with the network intensive workloads that we expect to become more and more common but also an inappropriate model to dedicate resources to network I/O processing. In datacenter environments, it is not uncommon to implement a single purpose machine dedicated to networking doing functions that were usually reserved for hardware appliances. Examples of these network appliances include software load balancers, DDoS appliances and forwarding gateways. To make matters worse, there are mechanisms on other OS’ to accelerate I/O that make these alternative OS’ the preferred platform to build network intensive applications such as virtual appliances.

PacketDirect (PD) extends the current NDIS model with an accelerated network I/O path that is optimized for packet per second (pps) counts an order of a magnitude higher than what has been seen with the traditional NDIS I/O model. This is accomplished through:

-   Reduced latency
-   Reduced cycles/packet
-   Linear speed up with use of additional system resources

PacketDirect exists side-by-side with the traditional model. The new PD path can be used when an application prefers it and there are sufficient hardware resources to accommodate it. PD is not meant to replace the traditional I/O model and assumes that a client writing to the PD interface will have strict partitioning requirements for the underlying resources based on the system topology. PD is meant to be the new high speed data path that will help a Windows system replace high pps workloads that have been traditionally done in hardware, saving data center owners millions in infrastructure costs.

## PacketDirect Concepts


PD works by allowing a PD client to explicitly manage networking traffic from a network adapter (NIC). PD gives the PD client control of the high performance send and receive functionality of the NIC through the PackageDirect client interface (PDCI). Internally, the PDCI send/receive functions are mapped directly to the PDPI. PD send/receive functions operate on PD queues created by the PD client on PD-capable NICs. PD provides the PD clients with the ability to set custom filters for very specific types of traffic or very generic traffic, based on the needs of the PD client. This allows the PD client to direct certain incoming packets to its PD queues. Packet processing in the PD model always takes place in an execution context that’s owned (or controlled/coordinated) by the PD client. The PD-capable NIC driver is completely passive, meaning it does not actively forward incoming packets or completion indications for sent packets to the PD client in a driver-owned execution context such as a DPC or worker-thread.

If a PD client does not understand how to process a packet or receives a control packet in one of its queues, such as an ARP, LLDP, or other protocol packets, the PD client can reroute the packet back to the current I/O path for processing. This allows PD to continue to process the packets that it has context for and not waste cycles on control traffic.

**Important**  There can be one PD provider and one PD client per net adapter. Therefore, there can be multiple PD clients and PD providers on a single system.

 

The PD client has control over the resources that are allocated to PD in the system. In cases of high network traffic, the PD client is responsible for minimizing its workload so that the OS can be responsive to other workloads.

The PacketDirect platform implemented by Windows maps the client interface to the provider interface. The platform controls buffer management and ability to re-inject packets received via PD to the current NDIS receive path. It also handles the interaction with PD clients for satisfying the NDIS control path requirements such as NIC disabling, going into low-power, system shutdown, and surprise removal in a fashion that does NOT hamper the PD data path performance.

**PacketDirect Provider Interface (PDPI)**

The PDPI allows NIC drivers to expose their high-performance send and receive functionality to the Windows OS. The functions implemented are a subset of the complete MiniPort functionality and are generic to all NICs that implement PD. For reference documentation for PDPI, see [PacketDirect Provider Interface (PDPI) Reference](https://msdn.microsoft.com/library/windows/hardware/dn931858).

**PacketDirect Client Interface (PDCI)**

The PDCI allows first-party Windows services/applications (e.g., Load-balancer, NAT, VM-switch, etc.) to speed up their data path by leveraging the PacketDirect I/O model through use of the PD clients. This interface is a layer 2 interface just like the current NDIS send/receive interface. The main functionality PDCI provides (in addition to PDPI access) is PD packet buffer allocation/management, a back-channel for injecting packets back to regular NDIS receive path, handling of NDIS power/PnP events.

## Related topics


[PacketDirect Provider Interface (PDPI) Reference](https://msdn.microsoft.com/library/windows/hardware/dn931858)

 

 






