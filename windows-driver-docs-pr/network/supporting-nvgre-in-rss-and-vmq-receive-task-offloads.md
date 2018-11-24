---
title: Supporting NVGRE in RSS and VMQ Receive Task Offloads
description: This section describes supporting NVGRE in RSS and VMQ receive task offloads
ms.assetid: 42660D55-31C0-4101-9EA1-159EBB76B019
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting NVGRE in RSS and VMQ Receive Task Offloads


NDIS 6.30 (Windows Server 2012) introduces [Network Virtualization using Generic Routing Encapsulation (NVGRE)](network-virtualization-using-generic-routing-encapsulation--nvgre--task-offload.md). NDIS miniport drivers and NICs that perform [Receive Side Scaling](receive-scaling.md) (RSS) and [Virtual Machine Queue (VMQ)](virtual-machine-queue--vmq-.md) receive task offloads should do so in a way that supports NVGRE.

**Note**  This page assumes that you are familiar with the information in [Offloading the Segmentation of Large TCP Packets](offloading-the-segmentation-of-large-tcp-packets.md).

 

If the miniport driver supports RSS and VMQ for encapsulated packets, it must advertise those capabilities in the **RssSupported** and **VmqSupported** members of the [**NDIS\_ENCAPSULATED\_PACKET\_TASK\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/jj991956) structure. If the miniport advertised these capabilities, received an [OID\_TCP\_OFFLOAD\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569807) OID request, and succeeded the OID, the NIC must perform RSS and VMQ on the advertised encapsulated packet types.

For supported encapsulated packets that it is able to parse, the NIC must perform RSS on the TCP or UDP header in the payload of the transport (inner) IP header and VMQ on the inner MAC header.

For performing RSS and VMQ, the NIC must get to the transport (inner) IP header of the encapsulated packet as described in [Locating the Transport Header for Encapsulated Packets in the Receive Path](locating-the-transport-header-for-encapsulaged-packets-in-the-receive-path.md) and check the protocol number. If the NIC receives a packet that uses a protocol that the NIC can parse, the NIC should:

-   Perform RSS by doing a 4-tuple hash on the transport (inner) IP header and the TCP or UDP header.
    -   For encapsulated packets whose protocol the miniport cannot parse, the NIC should perform a 2-tuple hash on the source and destination address fields in the tunnel (outer) IP header.
    -   For encapsulated packets that do not contain a TCP or UDP header immediately following the transport (inner) IP header, the NIC should perform a 2-tuple hash on the source and destination address fields in the tunnel (outer) IP header.
-   Perform VMQ by using the Ethernet header in the encapsulated packet. For encapsulated packets that do not contain an Ethernet header (within the encapsulated packet), VMQ should be performed using the outermost Ethernet header.

 

 





