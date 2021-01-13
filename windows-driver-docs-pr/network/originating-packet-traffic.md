---
title: Originating Packet Traffic
description: Originating Packet Traffic
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Originating Packet Traffic


This topic describes how Hyper-V extensions originate new packets and inject them into the extensible switch data path.

**Note**  This page assumes that you are familiar with the information and diagrams in [Overview of the Hyper-V Extensible Switch](overview-of-the-hyper-v-extensible-switch.md) and [Hybrid Forwarding](hybrid-forwarding.md).

 

**Note**  In the extensible switch interface, NDIS filter drivers are known as *extensible switch extensions* and the driver stack is known as the *extensible switch driver stack*. For more information about the extensions, see [Hyper-V Extensible Switch Extensions](hyper-v-extensible-switch-extensions.md).

 

Extensible switch extensions can only inject new packets into the extensible switch ingress data path. This ensures that the extensible switch interface can filter and forward these packets correctly. Extensions must follow these guidelines for injecting new packets into the ingress data path:

-   The extension must first allocate a [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list_context) structure for a new packet.

-   After the extension allocates a [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list_context) structure for a new packet, it must call the [*AllocateNetBufferListForwardingContext*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_allocate_net_buffer_list_forwarding_context) handler function to allocate the extensible switch forwarding context for the packet.

    The forwarding context resides in the out-of-band (OOB) data of the packet. It contains forwarding information for the packet, such as its source port and an array of one or more destination ports.

    For more information about the forwarding context, see [Hyper-V Extensible Switch Forwarding Context](hyper-v-extensible-switch-forwarding-context.md).

-   After the extension calls [*AllocateNetBufferListForwardingContext*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_allocate_net_buffer_list_forwarding_context), the source port for the packet will be set to **NDIS\_SWITCH\_DEFAULT\_PORT\_ID**. A packet with a source port identifier of **NDIS\_SWITCH\_DEFAULT\_PORT\_ID** is trusted and bypasses the extensible switch port policies, such as access control lists (ACLs) and quality of service (QoS).

    The extension may want the packet to be treated as if it originated from a particular port. This allows the policies for that port to be applied to the packet. The extension calls [*SetNetBufferListSource*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_set_net_buffer_list_source) to change the source port for the packet.

    However, there may be situations where the extension may want to assign the packet's source port identifier to **NDIS\_SWITCH\_DEFAULT\_PORT\_ID**. For example, the extension may want to set the source port identifier to **NDIS\_SWITCH\_DEFAULT\_PORT\_ID** for proprietary control packets that are sent to a device on the external network.

-   If the forwarding extension is sending a new packet on the ingress data path, it must determine the destination ports for the packet. For more information on this procedure, see [Adding Extensible Switch Destination Port Data to a Packet](adding-extensible-switch-destination-port-data-to-a-packet.md).

    **Note**  A capturing or filtering extension cannot add new destination ports to the new packet.

     

-   When the extension creates a new packet, the packet data is located in local, or *trusted*, memory in the parent operating system of the Hyper-V parent partition. This memory is not accessible by the child partition. Therefore, it is considered "safe" from unsynchronized updates by the guest operating system that runs in that partition.

    The extension must obtain the [**NDIS\_SWITCH\_FORWARDING\_DETAIL\_NET\_BUFFER\_LIST\_INFO**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_switch_forwarding_detail_net_buffer_list_info) union for the new packet by using the [**NET\_BUFFER\_LIST\_SWITCH\_FORWARDING\_DETAIL**](/windows-hardware/drivers/ddi/ndis/nf-ndis-net_buffer_list_switch_forwarding_detail) macro. The extension must set the **IsPacketDataSafe** member to TRUE. This specifies that all of the packet data is located in trusted memory.

-   When the extension calls [**NdisFSendNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfsendnetbufferlists) to inject the packet into the ingress data path, it must set the *Flags* parameter with the appropriate extensible switch flag settings. For more information about these flag settings, see [Hyper-V Extensible Switch Send and Receive Flags](hyper-v-extensible-switch-send-and-receive-flags.md).

-   When NDIS calls the extension's [*FilterSendNetBufferListsComplete*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_send_net_buffer_lists_complete) function to complete the send request of the new packet, the extension must call [*FreeNetBufferListForwardingContext*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_free_net_buffer_list_forwarding_context) to free the allocated forwarding context. The extension must do this before it frees or reuses the [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list_context) structure for the packet.

For more information about the extensible switch ingress and egress data paths, see [Hyper-V Extensible Switch Data Path](hyper-v-extensible-switch-data-path.md).

 

