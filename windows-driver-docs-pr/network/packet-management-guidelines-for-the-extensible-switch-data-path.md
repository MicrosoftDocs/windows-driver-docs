---
title: Packet Management Guidelines for the Extensible Switch Data Path
description: Packet Management Guidelines for the Extensible Switch Data Path
ms.assetid: 18B2BCBA-8428-45CF-93A0-8F7182DBCAA2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Packet Management Guidelines for the Extensible Switch Data Path


This topic describes the guidelines that Hyper-V extensible switch extensions must follow for managing packets obtained on the extensible switch data path.

**Note**  In the extensible switch interface, NDIS filter drivers are known as *extensible switch extensions* and the driver stack is known as the *extensible switch driver stack*. For more information about the extensions, see [Hyper-V Extensible Switch Extensions](hyper-v-extensible-switch-extensions.md).

 

**Note**  This page assumes that you are familiar with the information and diagrams in [Overview of the Hyper-V Extensible Switch](overview-of-the-hyper-v-extensible-switch.md) and [Hybrid Forwarding](hybrid-forwarding.md).

 

Extensions must follow these guidelines for packet management in the extensible switch data path:

-   Extensions that originate packets must call [**NdisFSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff562616) to initiate a send request on the ingress data path. This must be done in this way to allow for proper forwarding of the packet through the extensible switch.

-   A capturing extension can monitor packets on the extensible switch ingress and egress data path. However, this type of extension must always forward packets and must not drop the packets. Also, the capturing extension must not modify the packet data before it forwards the packet.

-   On the extensible switch ingress data path, filtering and forwarding extensions can do the following:

    -   Filtering extensions can filter packet traffic and enforce only custom port or switch policies for packet delivery through the extensible switch. When the extension filters packets in the ingress data path, it can only apply filtering rules based only on the source port and network adapter connection from which the packet originated. This information is stored in the OOB data of a packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure and can be obtained by using the [**NET\_BUFFER\_LIST\_SWITCH\_FORWARDING\_DETAIL**](https://msdn.microsoft.com/library/windows/hardware/hh598259) macro.

        **Note**  Packets obtained on the ingress data path do not contain destination ports. Filtering packets based on destination ports can only be done on packets obtained on the egress data path.

         

    -   Forwarding extensions can filter packet traffic and enforce custom and standard port or switch policies for packet delivery through the extensible switch. When the forwarding extension filters packets in the ingress data path, it applies filtering rules based on the source port as well as the destination ports that the forwarding extension assigns to the packet.

-   On the extensible switch egress data path, filtering and forwarding extensions can do the following:

    -   Filtering extensions can filter packet traffic and enforce only custom port or switch policies for packet delivery through the extensible switch. When the filtering extension filters packets in the egress data path, it can apply filtering rules based only on the destination ports for a packet.

        Destination port data is stored in the OOB data of a packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure. Extensions obtain this information by calling the [*GetNetBufferListDestinations*](https://msdn.microsoft.com/library/windows/hardware/hh598157) function.

    -   Forwarding extensions can filter packet traffic and enforce custom and standard port or switch policies for packet delivery through the extensible switch. When the forwarding extension filters packets in the egress data path, it can apply filtering rules based on the source or destination ports for a packet.

    -   Based on the policies enforced on a packet, the filtering or forwarding extension can exclude the delivery of the packet to one or more destinations. For more information on this procedure, see [Excluding Packet Delivery to Extensible Switch Destination Ports](excluding-packet-delivery-to-extensible-switch-destination-ports.md).

        Based on the policies enforced on a packet, the forwarding extension can exclude the delivery of the packet to one or more destinations. For more information, see [Hybrid Forwarding](hybrid-forwarding.md).

-   On the extensible switch egress data path, filtering and forwarding extensions must not do the following:

    -   Modify the packet data before forwarding the packet on the egress data path.

        If a filtering extension needs to modify the data in a packet, it must first clone the packet without preserving port destinations. Then, the extension must inject the modified packet into the ingress data path. This allows the underlying extensions to enforce policies on the modified packet and the forwarding extension can add port destinations.

        If the forwarding extension needs to modify the data in a packet, it must first clone the packet before it assigns port destinations. After the packet has been modified and port destinations assigned, the extension must inject the modified packet into the ingress data path.

        For more information, see [Cloning Packet Traffic](cloning-or-duplicating-packet-traffic.md).

        **Note**  If the extension clones a packet that was obtained on the egress data path, it can inject the new packet into the egress data path only if it has not changed the packet data and has preserved the original destination port data.

         

    -   Add destination ports to the packet before forwarding the packet.

        **Note**  Forwarding extensions are allowed to add destination ports to packets obtained on the ingress data path.

         

    -   Inject new or cloned data packets into the egress data path.

-   In the standard NDIS data path, non-extensible switch OOB data often has different formats depending on whether the packet is being indicated as a send or a receive. For example, the [**NDIS\_IPSEC\_OFFLOAD\_V2\_HEADER\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff565812) OOB data is a union of send-and receive–specific structures.

    In the extensible switch data path, all packets move through the extension driver stack as both sends and receives. Because of this, the non-extensible switch OOB data within the packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure will be in either a send or receive format through the duration of the flow through the driver stack.

    The format of this OOB data depends upon the source extensible switch port from which the packet arrived at the extensible switch. If the source port is connected to the external network adapter, the non-extensible switch OOB data will be in a receive format. For other ports, this OOB data will be in a send format.

    **Note**  If the extension clones a packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure, it must take the non-extensible switch OOB data into consideration if it adds or modifies the OOB data. The extension must call [*CopyNetBufferListInfo*](https://msdn.microsoft.com/library/windows/hardware/hh598136) to copy the OOB data associated with the extensible switch data path from a source packet to a cloned packet. This function will maintain the OOB send or receive format when the data is copied to the cloned packet.

     

-   If an extension drops a packet from either the ingress of egress data path, it must call [*ReportFilteredNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/hh598297). When this function is called, the extensible switch interface increments counters and logs events for the dropped or excluded packets.

 

 





