---
title: Forwarding Extensions
description: Forwarding Extensions
ms.assetid: 7ABBB3F3-66F5-4651-8A5A-94940F3FD82D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Forwarding Extensions


A forwarding extension has the same capabilities as a filtering extension, but is responsible for performing the core packet forwarding and filtering tasks of the extensible switch. These tasks include the following:

-   Determining the destination ports for a packet.

    **Note**  If the packet is an NVGRE packet, the Hyper-V Network Virtualization (HNV) component of the extensible switch determines the destination ports and forwards the packet. For more information, see [Hybrid Forwarding](hybrid-forwarding.md).

     

-   Filtering packets by enforcing standard port policies, such as security, profile, or virtual LAN (VLAN) policies.

    **Note**  The extensible switch still performs filtering based on built-in policies. These policies include access control lists (ACLs) and quality of service (QoS).

     

**Note**  If a forwarding extension is not installed and enabled in the extensible switch, the switch determines a packet's destination ports as well as filters packets based on standard port settings.

 

Forwarding extensions are layered immediately above the extensible switch extension miniport driver in the egress and ingress data path. For more information about these data paths, see [Hyper-V Extensible Switch Data Path](hyper-v-extensible-switch-data-path.md).

A forwarding extension can do the following with packets that were obtained on the ingress data path:

-   It can filter packet traffic and enforce custom and standard port or switch policies for packet delivery through the extensible switch. When the forwarding extension filters packets in the ingress data path, it applies filtering rules based on the source port as well as the destination ports that the extension assigns to the packet.

    Custom policies are defined by the independent software vendor (ISV). Standard policies are defined by the extensible switch interface. Property settings for these types of policies are managed through the Hyper-V WMI management layer. The forwarding extension is configured with these property settings through an object identifier (OID) request of [OID\_SWITCH\_PORT\_PROPERTY\_UPDATE](https://msdn.microsoft.com/library/windows/hardware/hh598278) and [OID\_SWITCH\_PROPERTY\_UPDATE](https://msdn.microsoft.com/library/windows/hardware/hh598283).

    For more information on extensible switch policies, see [Managing Hyper-V Extensible Switch Policies](managing-hyper-v-extensible-switch-extensibility-policies.md).

-   It can inject new, modified, or cloned packets into the ingress data path.

    For more information, see [Hyper-V Extensible Switch Send and Receive Operations](hyper-v-extensible-switch-send-and-receive-operations.md).

-   It can determine the delivery of the packet to one or more extensible switch destination ports. This allows the forwarding extension to add destination ports for the delivery of a packet to extensible switch ports.

    For more information on how to add destination ports, see [Adding Extensible Switch Destination Port Data to a Packet](adding-extensible-switch-destination-port-data-to-a-packet.md).

A forwarding extension can do the following with packets that were obtained on the egress data path:

-   It can filter packet traffic and enforce custom and standard port or switch policies for packet delivery through the extensible switch. When the forwarding extension filters packets in the egress data path, it can apply filtering rules based on the source or destination ports for a packet.

-   It can exclude the delivery of the packet to one or more extensible switch destination ports. This allows the forwarding extension to exclude the delivery of a packet to extensible switch ports.

    For more information on how to exclude packet delivery to extensible switch ports, see [Excluding Packet Delivery to Extensible Switch Destination Ports](excluding-packet-delivery-to-extensible-switch-destination-ports.md).

    **Note**  The forwarding extension can only exclude packet delivery when it handles the packet on the egress data path. The extension can only add or modify destination ports for the packet on the ingress data path.

     

-   It can modify the packet data. If the forwarding extension needs to modify the data in a packet, it must first clone the packet before it assigns port destinations. After the packet has been modified and port destinations assigned, the extension must inject the modified packet into the egress data path.

    For more information, see [Cloning Packet Traffic](cloning-or-duplicating-packet-traffic.md).

Besides inspecting OID requests and NDIS status indications, a forwarding extension can do the following:

-   It can inject OIDs or NDIS status indications into the extensible switch control path. This allows the forwarding extension to create or modify OIDs and status indications and forward them to or from underlying physical network adapters.

    For example, the extensible switch external network adapter can be bound to the virtual miniport edge of an NDIS multiplexer (MUX) intermediate driver. The MUX intermediate driver itself can be bound to a team of one or more physical networks on the host. This configuration is known as an *extensible switch team*.

    In this configuration, the extensible switch extensions are exposed to every network adapter in the extensible switch team. This allows the forwarding extension in the extensible switch driver stack to manage the configuration and use of individual network adapters in the team. For example, the extension can provide support for a load balancing failover (LBFO) solution over the team by forwarding outgoing packets to individual adapters. Such an extension is known as a *teaming provider*.

    By acting as a teaming provider, the forwarding extension can create or modify OID requests to enable or disable hardware capabilities on an adapter in the team. The teaming provider can also create or modify NDIS status indications based on changes to one or more adapters in the team.

    For more information about teaming providers, see [Teaming Provider Extensions](teaming-provider-extensions.md).

-   It can veto the creation of an extensible switch port or network adapter connection by returning STATUS\_DATA\_NOT\_ACCEPTED for the applicable extensible switch OIDs. For example, the forwarding extension can veto a port creation request by returning STATUS\_DATA\_NOT\_ACCEPTED when the driver receives an OID set request of [OID\_SWITCH\_PORT\_CREATE](https://msdn.microsoft.com/library/windows/hardware/hh598272).

    **Note**  Forwarding extensions do not create or delete ports or network adapter connections. The protocol edge of the extensible switch issues OIDs to notify the underlying extensions about the creation or deletion of ports or network adapter connections. For more information, see [Hyper-V Extensible Switch Port and Network Adapter States](hyper-v-extensible-switch-port-and-network-adapter-states.md).

     

-   It can veto the addition or update of an extensible switch or port policy by returning STATUS\_DATA\_NOT\_ACCEPTED for the applicable extensible switch OIDs. For example, the forwarding extension can veto the addition of a port policy by returning STATUS\_DATA\_NOT\_ACCEPTED when the driver receives an OID set request of [OID\_SWITCH\_PORT\_PROPERTY\_ADD](https://msdn.microsoft.com/library/windows/hardware/hh598275).

    For more information about extensible switch policies, see [Managing Hyper-V Extensible Switch Policies](managing-hyper-v-extensible-switch-extensibility-policies.md).

A forwarding extension has the following requirements:

-   A forwarding extension must be developed as an NDIS filter driver that supports the extensible switch interface.

    For more information about filter drivers, see [NDIS Filter Drivers](ndis-filter-drivers2.md).

    For more information on how to write a forwarding extension, see [Writing Hyper-V Extensible Switch Extensions](writing-hyper-v-extensible-switch-extensions.md).

-   The INF file for a forwarding extension must install the extension as a modifying filter driver. NDIS-monitoring filter drivers cannot be installed in the extensible switch driver stack.

    For more information about modifying filter drivers, see [Types of Filter Drivers](types-of-filter-drivers.md).

    For more information about the INF requirements for modifying filter drivers, see [Configuring an INF File for a Modifying Filter Driver](configuring-an-inf-file-for-a-modifying-filter-driver.md).

-   The **FilterClass** value in the INF file for the extension must be set to **ms\_switch\_forward**. For more information, see [INF Requirements for Hyper-V Extensible Switch Extensions](inf-requirements-for-hyper-v-extensions.md).

-   Only one forwarding extension can be enabled in the driver stack for each instance of an extensible switch.

For more information about extensible switch teams, see [Types of Physical Network Adapter Configurations](types-of-physical-network-adapter-configurations.md).

For more information about forwarding extensions, see the following pages:

-   [Teaming Provider Extensions](teaming-provider-extensions.md)
-   [Hybrid Forwarding](hybrid-forwarding.md)

## Related topics


[Forwarding Packets to Hyper-V Extensible Switch Ports](forwarding-packets-to-hyper-v-extensible-switch-ports.md)

[Forwarding Packets to Physical Network Adapters](forwarding-packets-to-physical-network-adapters.md)

[Overview of the Hyper-V Extensible Switch](overview-of-the-hyper-v-extensible-switch.md)

 

 






