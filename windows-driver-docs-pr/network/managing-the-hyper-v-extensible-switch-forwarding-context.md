---
title: Managing the Hyper-V Extensible Switch Forwarding Context
description: Managing the Hyper-V Extensible Switch Forwarding Context
ms.date: 04/20/2017
---

# Managing the Hyper-V Extensible Switch Forwarding Context


**Note**  This page assumes that you are familiar with the information and diagrams in [Overview of the Hyper-V Extensible Switch](overview-of-the-hyper-v-extensible-switch.md) and [Hybrid Forwarding](hybrid-forwarding.md).



The [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure for each packet that traverses the Hyper-V extensible switch data path contains out-of-band (OOB) data. This data specifies the source port from where the packet originated, as well as one or more destination ports for packet delivery. This OOB data is known as the *extensible switch forwarding context*.

**Note**  The extensible switch forwarding context is different from the [**NET\_BUFFER\_LIST\_CONTEXT**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list_context) structure. This allows extensions to allocate their own context structures without affecting the forwarding context.

The extensible switch forwarding context is allocated and freed in the following way:

-   When a packet arrives at the extensible switch from a network adapter, the extensible switch interface allocates the forwarding context and associates it with the packet's [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure.

    When the packet is delivered to its destination ports, the interface frees the forwarding context from the packet's [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure.

-   If an extensible switch extension injects a new or cloned packet into the extensible switch data path, it must allocate the forwarding context before it calls [**NdisFSendNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfsendnetbufferlists).

    After the extension allocates a [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list_context) structure for a new or cloned packet, it must call the [*AllocateNetBufferListForwardingContext*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_allocate_net_buffer_list_forwarding_context) function to allocate the forwarding context for the packet. When the send packet request is completed, the extension must call [*FreeNetBufferListForwardingContext*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_free_net_buffer_list_forwarding_context) before it frees or reuses the **NET\_BUFFER\_LIST** structure.

    **Note**  When the extension calls [*AllocateNetBufferListForwardingContext*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_allocate_net_buffer_list_forwarding_context), the source port for the packet is set to **NDIS\_SWITCH\_DEFAULT\_PORT\_ID**. This specifies that the packet originated from an extension instead of arriving at an extensible switch port. Under certain conditions, the extension may want to change the source port for the packet. For more information, see [Modifying a Packet's Extensible Switch Source Port Data](modifying-a-packet-s-extensible-switch-source-port-data.md).

    For more information, see [Hyper-V Extensible Switch Send and Receive Operations](hyper-v-extensible-switch-send-and-receive-operations.md).

All extensible switch extensions can call the following extensible switch handler functions to access the data within the packet's forwarding context:

<a href="" id="allocatenetbufferlistforwardingcontext"></a>[*AllocateNetBufferListForwardingContext*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_allocate_net_buffer_list_forwarding_context)  
Allocates the extensible switch forwarding context and prepares a [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure for send or receive operations within the extensible switch.

<a href="" id="copynetbufferlistinfo"></a>[*CopyNetBufferListInfo*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_copy_net_buffer_list_info)  
Copies the forwarding context from a source packet's [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list_context) structure to a destination packet's **NET\_BUFFER\_LIST** structure. This data includes the extensible switch source port and network adapter information. The extensible switch destination port information can also be copied to the destination packet.

<a href="" id="freenetbufferlistforwardingcontext"></a>[*FreeNetBufferListForwardingContext*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_free_net_buffer_list_forwarding_context)  
Frees the resources in the extensible switch forwarding context of a [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure. This data was used for send or receive operations in a Hyper-V extensible switch, and was previously allocated by calling the [*AllocateNetBufferListForwardingContext*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_allocate_net_buffer_list_forwarding_context) function.

<a href="" id="getnetbufferlistdestinations"></a>[*GetNetBufferListDestinations*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_get_net_buffer_list_destinations)  
Returns the destination ports from the forwarding context of a packet's [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list_context) structure.

A forwarding extension is responsible for adding destination ports for a packet, unless the packet is an NVGRE packet. (For more information, see [Hybrid Forwarding](hybrid-forwarding.md).) The extension calls the following extensible switch handler functions to add or update the destination ports within the packet's forwarding context:

<a href="" id="addnetbufferlistdestination"></a>[*AddNetBufferListDestination*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_add_net_buffer_list_destination)  
Adds a single destination to the extensible switch forwarding context area for a packet that is specified by a [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list_context) structure.

**Note**  This call commits the change to the forwarding context area. In this case, the forwarding extension does not need to call [*UpdateNetBufferListDestinations*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_update_net_buffer_list_destinations).

<a href="" id="grownetbufferlistdestinations"></a>[*GrowNetBufferListDestinations*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_grow_net_buffer_list_destinations)  
Increases the size of the destination port array in the forwarding context area of a packet's [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list_context) structure.

<a href="" id="updatenetbufferlistdestinations"></a>[*UpdateNetBufferListDestinations*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_update_net_buffer_list_destinations)  
Commits modifications that the extension made to one or more extensible switch destination ports of a packet. This function updates the forwarding context of a packet's [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list_context) structure with these changes.

**Note**  After the forwarding extension commits the changes for destination ports to the forwarding context, destination ports cannot be removed and only the **IsExcluded** member of a destination port's [**NDIS\_SWITCH\_PORT\_DESTINATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_switch_port_destination) structure can be changed. For more information, see [Excluding Packet Delivery to Extensible Switch Destination Ports](excluding-packet-delivery-to-extensible-switch-destination-ports.md).

## Related topics


[Hyper-V Extensible Switch Forwarding Context](hyper-v-extensible-switch-forwarding-context.md)

[Hyper-V Extensible Switch Forwarding Context Data Types](hyper-v-extensible-switch-forwarding-context-data-types.md)
