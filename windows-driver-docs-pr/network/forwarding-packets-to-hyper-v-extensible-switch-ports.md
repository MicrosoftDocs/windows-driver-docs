---
title: Forwarding Packets to Hyper-V Extensible Switch Ports
description: Forwarding Packets to Hyper-V Extensible Switch Ports
ms.assetid: C8DA9064-21EE-45F4-BE6D-D24851C5480B
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Forwarding Packets to Hyper-V Extensible Switch Ports


This page describes how a Hyper-V extensible switch forwarding extension can forward packets to one or more ports. This type of extension can also forward packets to individual network adapters that are connected to the extensible switch external network adapter.

**Note**  Only the extensible switch forwarding extension or the extensible switch itself can forward packets to extensible switch ports.

 

**Note**  This page assumes that you are familiar with the information and diagrams in [Overview of the Hyper-V Extensible Switch](overview-of-the-hyper-v-extensible-switch.md) and [Hybrid Forwarding](hybrid-forwarding.md).

 

**Note**  In the extensible switch interface, NDIS filter drivers are known as *extensible switch extensions* and the driver stack is known as the *extensible switch driver stack*. For more information about extensions, see [Hyper-V Extensible Switch Extensions](hyper-v-extensible-switch-extensions.md).

 

If a forwarding extension is installed and enabled in the extensible switch driver stack, it is responsible for making forwarding decisions for each packet that it obtains on the extensible switch ingress data path. Based on these forwarding decisions, the extension adds destination ports into the destination port array in the out-of-band (OOB) data of the packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure. After the packet has completed its traversal of the extensible switch data path, the extensible switch interface delivers the packet to the specified destination ports.

**Note**  If a forwarding extension is not installed or enabled, the extensible switch makes the forwarding decisions for packets it obtains from the ingress data path. The switch adds the destination ports to the OOB data of the packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure before it forwards the packet up the extensible switch egress data path.

 

**Note**  If the packet is an NVGRE packet, the forwarding extension can add destination ports to the destination port array. However, the Hyper-V Network Virtualization (HNV) component of the extensible switch is responsible for determining the destination ports and forwarding the packet. For more information, see [Hybrid Forwarding](hybrid-forwarding.md).

 

The forwarding extension can add port destinations only to packets obtained from the ingress data path. After the packet is forwarded up the egress data path, filtering and forwarding extensions can exclude packet delivery to extensible switch ports. For more information, see [Excluding Packet Delivery to Extensible Switch Destination Ports](excluding-packet-delivery-to-extensible-switch-destination-ports.md).

Within the OOB data of a packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure, the data for destination ports are contained in an [**NDIS\_SWITCH\_FORWARDING\_DESTINATION\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598210) structure. Each element in the array defines a destination port and is formatted as an [**NDIS\_SWITCH\_PORT\_DESTINATION**](https://msdn.microsoft.com/library/windows/hardware/hh598224) structure.

The forwarding extension can call the following Hyper-V Extensible Switch handler functions to manage the [**NDIS\_SWITCH\_FORWARDING\_DESTINATION\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598210) structure and its [**NDIS\_SWITCH\_PORT\_DESTINATION**](https://msdn.microsoft.com/library/windows/hardware/hh598224) elements:

<a href="" id="addnetbufferlistdestination"></a>[*AddNetBufferListDestination*](https://msdn.microsoft.com/library/windows/hardware/hh598133)  
This function adds a single destination port to the [**NDIS\_SWITCH\_FORWARDING\_DESTINATION\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598210) structure in the packet's OOB data.

<a href="" id="getnetbufferlistdestinations"></a>[*GetNetBufferListDestinations*](https://msdn.microsoft.com/library/windows/hardware/hh598157)  
This function returns a pointer to the [**NDIS\_SWITCH\_FORWARDING\_DESTINATION\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598210) structure in a packet's OOB data.

<a href="" id="grownetbufferlistdestinations"></a>[*GrowNetBufferListDestinations*](https://msdn.microsoft.com/library/windows/hardware/hh598158)  
This function adds more destination port elements to the [**NDIS\_SWITCH\_FORWARDING\_DESTINATION\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598210) structure of a packet's OOB data.

<a href="" id="updatenetbufferlistdestinations"></a>[*UpdateNetBufferListDestinations*](https://msdn.microsoft.com/library/windows/hardware/hh598303)  
This function commits the modifications that the extension made to add or exclude one or more destination ports for a packet. These changes are committed to the [**NDIS\_SWITCH\_FORWARDING\_DESTINATION\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598210) structure in the packet's OOB data.

When the forwarding extension's [*FilterSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff549966) function is called, the *NetBufferList* parameter contains a pointer to a linked list of [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures. Each of these structures specifies a packet obtained from the ingress data path.

For each [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure in this list, the forwarding extension adds destination ports for the packet by following these steps:

1.  The extension makes forwarding decisions for the packet based on various types of criteria. These criteria include the following:

    -   Policy criteria based on the packet's source port and network adapter connection. The forwarding extension obtains this information by using the [**NET\_BUFFER\_LIST\_SWITCH\_FORWARDING\_DETAIL**](https://msdn.microsoft.com/library/windows/hardware/hh598259) macro.

    -   Policy criteria for an extensible switch port based on the packet's payload data. For example, a policy for an extensible switch port may include a filter to allow delivery of only IP version 4 (IPv4) packets.

    **Note**  If the packet is an NVGRE packet, the HNV component of the extensible switch is responsible for forwarding the packet. However, the forwarding extension can apply its own policy criteria in the ingress and egress paths. For more information, see [Hybrid Forwarding](hybrid-forwarding.md).

     

2.  If the extension determines that the packet can be forwarded to one or more extensible switch ports, it must add destination ports to the packet's OOB data. For more information about this procedure, see [Adding Extensible Switch Destination Port Data to a Packet](adding-extensible-switch-destination-port-data-to-a-packet.md).

    **Note**  If the packet is an NVGRE packet, the forwarding extension is not required to add destination ports. For more information, see [Hybrid Forwarding](hybrid-forwarding.md).

     

3.  If the extension determines that the packet cannot be forwarded to any extensible switch port, it must drop the packet.

    **Note**  This is not true if the packet is an NVGRE packet. For more information, see [Hybrid Forwarding](hybrid-forwarding.md).

     

4.  If the extension has added one or more destination ports for the packet, it must call [**NdisFSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff562616) to forward the packet on the egress data path.

    **Note**  If the packet is an NVGRE packet, the HNV component of the extensible switch is responsible for forwarding the packet. For more information, see [Hybrid Forwarding](hybrid-forwarding.md).

     

For more information about the extensible switch ingress and egress data paths, see [Hyper-V Extensible Switch Data Path](hyper-v-extensible-switch-data-path.md).

 

 





