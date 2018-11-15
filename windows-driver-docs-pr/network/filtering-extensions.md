---
title: Filtering Extensions
description: Filtering Extensions
ms.assetid: EDE50213-DFA0-4D8B-9E15-12AED8FDE5CA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filtering Extensions


A Hyper-V extensible switch filtering extension can inspect, modify, and insert packets into the extensible switch data path. Based on extensible switch port and switch policy settings, the extension can drop a packet or exclude its delivery to one or more destination ports.

Filtering extensions are invoked after capturing extensions in the ingress data path and after the forwarding extensions in the egress data path. For more information about these data paths, see [Hyper-V Extensible Switch Data Path](hyper-v-extensible-switch-data-path.md).

A filtering extension can do the following with packets that were obtained on the ingress data path:

-   Filter packet traffic and enforce custom port or switch policies for packet delivery through the extensible switch. When the filtering extension filters packets in the ingress data path, it can apply filtering rules based only on the source port and network adapter connection from which the packet originated. This information is stored in the out-of-band (OOB) data of a packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure and can be obtained by using the [**NET\_BUFFER\_LIST\_SWITCH\_FORWARDING\_DETAIL**](https://msdn.microsoft.com/library/windows/hardware/hh598259) macro.

    **Note**  Packets obtained on the ingress data path do not contain destination ports. Filtering packets based on destination ports can be done only on packets obtained on the egress data path.

    Custom policies are defined by the independent software vendor (ISV). Property settings for this policy type are managed through the Hyper-V WMI management layer. The filtering extension is configured with these property settings through an object identifier (OID) request of [OID\_SWITCH\_PORT\_PROPERTY\_UPDATE](https://msdn.microsoft.com/library/windows/hardware/hh598278) and [OID\_SWITCH\_PROPERTY\_UPDATE](https://msdn.microsoft.com/library/windows/hardware/hh598283).

    For more information on custom extensible port or switch policies, see [Managing Hyper-V Extensible Switch Policies](managing-hyper-v-extensible-switch-extensibility-policies.md).

    **Note**  Only forwarding extensions can enforce standard port policies for packet delivery through the extensible switch.

-   Inject new, modified, or cloned packets into the ingress data path.

    For more information, see [Hyper-V Extensible Switch Send and Receive Operations](hyper-v-extensible-switch-send-and-receive-operations.md).

A filtering extension can do the following with packets that were obtained on the egress data path:

-   Filter packet traffic and enforce custom port or switch policies for packet delivery through the extensible switch. When the filtering extension filters packets in the egress data path, it can apply filtering rules based on the source or destination ports for a packet. Destination port data is stored in the OOB data of a packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure. Extensions obtain this information by calling the [*GetNetBufferListDestinations*](https://msdn.microsoft.com/library/windows/hardware/hh598157) function.

-   Exclude the delivery of the packet to one or more extensible switch destination ports. This allows the filtering extension to exclude the delivery of a packet to extensible switch ports.

    For more information on how to exclude packet delivery to extensible switch ports, see [Excluding Packet Delivery to Extensible Switch Destination Ports](excluding-packet-delivery-to-extensible-switch-destination-ports.md).

-   Manage the traffic flow to one or more destination ports by postponing the forwarding of packets up the egress data path.

    For example, a filtering extension that supports quality of service (QoS) functionality may want to immediately call [**NdisFSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff562616) to forward packets that are specified with a higher priority value. Depending on the traffic flow, the extension may want to forward packets with a lower priority value at a later time.

-   Modify the packet data. If the filtering extension needs to modify the data in a packet, it must first clone the packet without preserving port destinations. Then, the extension must inject the modified packet into the ingress data path. This allows the underlying extensions to enforce policies on the modified packet and the forwarding extension can add port destinations.

    For more information, see [Cloning Packet Traffic](cloning-or-duplicating-packet-traffic.md).

Besides inspecting OID requests and NDIS status indications, a filtering extension can do the following:

-   Veto the creation of an extensible switch port or network adapter connection by returning STATUS\_DATA\_NOT\_ACCEPTED for the applicable extensible switch OIDs. For example, the filtering extension can veto a port creation request by returning STATUS\_DATA\_NOT\_ACCEPTED when the driver receives an OID set request of [OID\_SWITCH\_PORT\_CREATE](https://msdn.microsoft.com/library/windows/hardware/hh598272).

    **Note**  Filtering extensions do not create or delete ports or network adapter connections. The protocol edge of the extensible switch issues OIDs to notify the underlying filter drivers about the creation or deletion of ports or network adapter connections. For more information, see [Hyper-V Extensible Switch Port and Network Adapter States](hyper-v-extensible-switch-port-and-network-adapter-states.md).

-   Veto the addition or update of an extensible switch or port policy by returning STATUS\_DATA\_NOT\_ACCEPTED for the applicable extensible switch OIDs. For example, the filtering extension can veto the addition of a port policy by returning STATUS\_DATA\_NOT\_ACCEPTED when the extension receives an OID set request of [OID\_SWITCH\_PORT\_PROPERTY\_ADD](https://msdn.microsoft.com/library/windows/hardware/hh598275).

    For more information about extensible switch policies, see [Managing Hyper-V Extensible Switch Policies](managing-hyper-v-extensible-switch-extensibility-policies.md).

A filtering extension has the following requirements:

-   A filtering extension must be developed as an NDIS filter driver that supports the extensible switch interface.

    For more information about filter drivers, see [NDIS Filter Drivers](ndis-filter-drivers2.md).

    For more information on how to write a filtering extension, see [Writing Hyper-V Extensible Switch Extensions](writing-hyper-v-extensible-switch-extensions.md).

    **Note**  The Windows Filtering Platform (WFP) provides an in-box extensible switch filtering extension (Wfplwfs.sys ). This extension allows WFP filters or callout drivers to intercept packets along the Hyper-V extensible switch data path. This allows the filters or callout drivers to perform packet inspection or modification by using the WFP management and system functions. For an overview of WFP, see [Windows Filtering Platform](porting-packet-processing-drivers-and-apps-to-wfp.md).

-   The INF file for a filtering extension must install the driver as a modifying filter driver. NDIS-monitoring filter drivers cannot be installed in the extensible switch driver stack.

    For more information about modifying filter drivers, see [Types of Filter Drivers](types-of-filter-drivers.md).

    For more information about the INF requirements for modifying filter drivers, see [Configuring an INF File for a Modifying Filter Driver](configuring-an-inf-file-for-a-modifying-filter-driver.md).

-   The **FilterClass** value in the INF file for the filter driver must be set to **ms\_switch\_filter**. For more information, see [INF Requirements for Hyper-V Extensible Switch Extensions](inf-requirements-for-hyper-v-extensions.md).

-   Any number of filtering extensions can be bound and enabled in the driver stack for each instance of an extensible switch. By default, multiple filtering extensions are ordered based on when they were installed. For example, multiple filtering extensions are layered in the extensible switch driver stack with the most recently installed extension layered above other filtering extensions in the stack.

    After they are bound and enabled in an extensible switch instance, the layering of filtering extensions in the extensible switch driver stack can be reordered. For more information, see [Reordering Hyper-V Extensible Switch Extensions](reordering-hyper-v-extensibility-switch-extensions.md).