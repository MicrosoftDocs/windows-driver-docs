---
title: Forwarding Packets to Physical Network Adapters
description: Forwarding Packets to Physical Network Adapters
ms.assetid: 14A78DB2-6643-471D-97B9-4D8524EC3E73
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Forwarding Packets to Physical Network Adapters


**Note**  This page assumes that you are familiar with the information and diagrams in the following pages:
-   [Forwarding Extensions](forwarding-extensions.md)
-   [Hybrid Forwarding](hybrid-forwarding.md)
-   [Hyper-V Extensible Switch Extensions](hyper-v-extensible-switch-extensions.md)
-   [Overview of the Hyper-V Extensible Switch](overview-of-the-hyper-v-extensible-switch.md)
-   [Teaming Provider Extensions](teaming-provider-extensions.md)

 

This page describes how Hyper-V extensible switch forwarding extensions can forward send requests of packets to underlying physical adapters. One or more physical network adapters can be bound to the extensible switch external network adapter.

For example, the extensible switch external network adapter can be bound to the virtual miniport edge of an NDIS multiplexer (MUX) intermediate driver. The MUX intermediate driver itself can be bound to a team of one or more physical networks on the host. This configuration is known as an *extensible switch team*. For more information about extensible switch teams, see [Types of Physical Network Adapter Configurations](types-of-physical-network-adapter-configurations.md).

In this configuration, the extensible switch extensions are exposed to every network adapter in the extensible switch team. This allows a forwarding extension in the extensible switch driver stack to manage the configuration and use of individual network adapters in the team. For example, the extension can provide support for a load balancing failover (LBFO) solution over the team by forwarding outgoing packets to individual adapters. Such as extension is known as a *teaming provider*. For more information about teaming providers, see [Teaming Provider Extensions](teaming-provider-extensions.md).

If a forwarding extension is installed and enabled in the extensible switch driver stack, it is responsible for making forwarding decisions for each packet that it obtains on the extensible switch ingress data path, unless the packet is an NVGRE packet. (For more information about NVGRE packets, see [Hybrid Forwarding](hybrid-forwarding.md).) Based on these forwarding decisions, the extension can add destination ports into the out-of-band (OOB) data of the packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure. After the packet has completed its traversal of the extensible switch data path, the extensible switch interface delivers the packet to the specified destination ports.

**Note**  If a forwarding extension is not installed or enabled, the extensible switch itself makes the forwarding decisions for packets it obtains from ingress data path. The switch adds the destination ports to the OOB data of the packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure before it forwards the packet up the extensible switch egress data path.

 

When the forwarding extension's [*FilterSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff549966) function is called, the *NetBufferList* parameter contains a pointer to a linked list of [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures. Each of these structures specifies a packet obtained from the ingress data path. Within the OOB data of each packet's **NET\_BUFFER\_LIST** structure, the data for destination ports are contained in an [**NDIS\_SWITCH\_FORWARDING\_DESTINATION\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598210) structure. The extension obtains the **NDIS\_SWITCH\_FORWARDING\_DESTINATION\_ARRAY** structure and its elements by calling [*GetNetBufferListDestinations*](https://msdn.microsoft.com/library/windows/hardware/hh598157).

**Note**  To improve performance, a forwarding extension can call the [*GrowNetBufferListDestinations*](https://msdn.microsoft.com/library/windows/hardware/hh598158) function instead of [*GetNetBufferListDestinations*](https://msdn.microsoft.com/library/windows/hardware/hh598157) to obtain a pointer to the [**NDIS\_SWITCH\_FORWARDING\_DESTINATION\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598210) structure. The extension does this if it determines that it needs additional array elements in the packet's OOB data for destination ports. For more information, see [Adding Extensible Switch Destination Port Data to a Packet](adding-extensible-switch-destination-port-data-to-a-packet.md).

 

Each element in the [**NDIS\_SWITCH\_FORWARDING\_DESTINATION\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598210) array defines a destination port and is formatted as an [**NDIS\_SWITCH\_PORT\_DESTINATION**](https://msdn.microsoft.com/library/windows/hardware/hh598224) structure. This structure contains the following members:

-   The **PortId** member contains a value that specifies the destination port on the extensible switch.

-   The **NicIndex** member specifies the index of the network adapter that is connected to the extensible switch port specified by the **PortId** member.

    For more information on these index values, see [Network Adapter Index Values](network-adapter-index-values.md).

If the forwarding extension adds a destination port that is connected to the external network adapter, the extension can specify the index of an underlying physical network adapter. For example, the extension could operate as a teaming provider for LBFO support over an extensible switch team. This allows the extension to balance the traffic overhead by forwarding send requests to different adapters of the team.

The forwarding extension must follow these guidelines when it adds or modifies an [**NDIS\_SWITCH\_PORT\_DESTINATION**](https://msdn.microsoft.com/library/windows/hardware/hh598224) structure to forward send requests to an underlying physical network adapter:

-   If the **PortId** member specifies the extensible switch port to which the external network adapter is connected, the extension must set the **NicIndex** member to one of the following index values:

    -   If only one physical network adapter is bound to the external network adapter, the extension must set the **NicIndex** member to **NDIS\_SWITCH\_DEFAULT\_NIC\_INDEX** or one.

    -   If multiple physical network adapters are bound to the external network adapter, the extension must set the **NicIndex** member to the nonzero index value of the destination network adapter in the extensible switch team.

    **Note**  If the **PortId** member does not specify the extensible switch port to which the external network adapter is connected, the extension must set the **NicIndex** member to **NDIS\_SWITCH\_DEFAULT\_NIC\_INDEX**.

     

-   After the extension has added all of the destination ports for the packet, it must call [**NdisFSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff562616) to forward the packet on the ingress data path.

For more information on how to add destination ports to a packet, see [Forwarding Packets to Hyper-V Extensible Switch Ports](forwarding-packets-to-hyper-v-extensible-switch-ports.md).

For more information on the egress data path, see [Hyper-V Extensible Switch Data Path](hyper-v-extensible-switch-data-path.md).

 

 





