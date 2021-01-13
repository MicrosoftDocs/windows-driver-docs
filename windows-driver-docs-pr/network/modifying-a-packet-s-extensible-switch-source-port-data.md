---
title: Modifying a Packet's Extensible Switch Source Port Data
description: Modifying a Packet's Extensible Switch Source Port Data
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Modifying a Packet's Extensible Switch Source Port Data


The Hyper-V extensible switch source port is specified by the **SourcePortId** member in the [**NDIS\_SWITCH\_FORWARDING\_DETAIL\_NET\_BUFFER\_LIST\_INFO**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_switch_forwarding_detail_net_buffer_list_info) structure. This structure is contained in the out-of-band (OOB) forwarding context of the packet's [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure. For more information about this context, see [Hyper-V Extensible Switch Forwarding Context](hyper-v-extensible-switch-forwarding-context.md).

The extensible switch extension must follow these guidelines for modifying a packet's source port identifier:

-   The extensible switch extension must call [*SetNetBufferListSource*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_set_net_buffer_list_source) to modify the source port for a packet. The extension must not directly modify the **SourcePortId** member of the [**NDIS\_SWITCH\_FORWARDING\_DETAIL\_NET\_BUFFER\_LIST\_INFO**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_switch_forwarding_detail_net_buffer_list_info) structure.

-   If the extension is creating or cloning a packet, it must call the [*AllocateNetBufferListForwardingContext*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_allocate_net_buffer_list_forwarding_context) function after it calls [**NdisAllocateNetBufferList**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocatenetbufferlist). This function allocates an extensible switch context area for the OOB data that is used for forwarding information for the packet.

    When the extension calls [*AllocateNetBufferListForwardingContext*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_allocate_net_buffer_list_forwarding_context), the **SourcePortId** member is set to **NDIS\_SWITCH\_DEFAULT\_PORT\_ID**. This specifies that the packet originated from an extension instead of arriving at an extensible switch port.

    Packets with a source port of **NDIS\_SWITCH\_DEFAULT\_PORT\_ID** are treated by the extensible switch extension data path as privileged and trusted. Such traffic should not be subjected to the policies that are applied to packets from other source ports. For example, packets with a source port identifier of **NDIS\_SWITCH\_DEFAULT\_PORT\_ID** bypass the built-in extensible switch policies that are applied by the underlying miniport edge of the extensible switch. These policies include access control lists (ACLs) and quality of service (QoS).

    When the extension is originating packet traffic, it should use the source port of **NDIS\_SWITCH\_DEFAULT\_PORT\_ID** sparingly and carefully. In most cases, the extension should modify the source port identifier to an active port on the extensible switch. This allows the policies of that port to be applied to the packet.

    However, there may be situations where the extension has to use the source port of **NDIS\_SWITCH\_DEFAULT\_PORT\_ID** for packets that it originates. For example, if the extension originates a control packet that has to be sent to its destination on the physical or virtual network, it should use **NDIS\_SWITCH\_DEFAULT\_PORT\_ID** for the source port identifier. This ensures that the packet will not be filtered and rejected by underlying extensions in the extensible switch driver stack.

 

