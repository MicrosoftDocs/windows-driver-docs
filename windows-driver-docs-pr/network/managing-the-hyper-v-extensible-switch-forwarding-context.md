---
title: Managing the Hyper-V Extensible Switch Forwarding Context
description: Managing the Hyper-V Extensible Switch Forwarding Context
ms.assetid: 63FBEBFA-BD57-4350-89C3-9F0FAAA18973
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing the Hyper-V Extensible Switch Forwarding Context


**Note**  This page assumes that you are familiar with the information and diagrams in [Overview of the Hyper-V Extensible Switch](overview-of-the-hyper-v-extensible-switch.md) and [Hybrid Forwarding](hybrid-forwarding.md).



The [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure for each packet that traverses the Hyper-V extensible switch data path contains out-of-band (OOB) data. This data specifies the source port from where the packet originated, as well as one or more destination ports for packet delivery. This OOB data is known as the *extensible switch forwarding context*.

**Note**  The extensible switch forwarding context is different from the [**NET\_BUFFER\_LIST\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff568389) structure. This allows extensions to allocate their own context structures without affecting the forwarding context.

The extensible switch forwarding context is allocated and freed in the following way:

-   When a packet arrives at the extensible switch from a network adapter, the extensible switch interface allocates the forwarding context and associates it with the packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

    When the packet is delivered to its destination ports, the interface frees the forwarding context from the packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

-   If an extensible switch extension injects a new or cloned packet into the extensible switch data path, it must allocate the forwarding context before it calls [**NdisFSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff562616).

    After the extension allocates a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568389) structure for a new or cloned packet, it must call the [*AllocateNetBufferListForwardingContext*](https://msdn.microsoft.com/library/windows/hardware/hh598134) function to allocate the forwarding context for the packet. When the send packet request is completed, the extension must call [*FreeNetBufferListForwardingContext*](https://msdn.microsoft.com/library/windows/hardware/hh598153) before it frees or reuses the **NET\_BUFFER\_LIST** structure.

    **Note**  When the extension calls [*AllocateNetBufferListForwardingContext*](https://msdn.microsoft.com/library/windows/hardware/hh598134), the source port for the packet is set to **NDIS\_SWITCH\_DEFAULT\_PORT\_ID**. This specifies that the packet originated from an extension instead of arriving at an extensible switch port. Under certain conditions, the extension may want to change the source port for the packet. For more information, see [Modifying a Packet's Extensible Switch Source Port Data](modifying-a-packet-s-extensible-switch-source-port-data.md).

    For more information, see [Hyper-V Extensible Switch Send and Receive Operations](hyper-v-extensible-switch-send-and-receive-operations.md).

All extensible switch extensions can call the following extensible switch handler functions to access the data within the packet's forwarding context:

<a href="" id="allocatenetbufferlistforwardingcontext"></a>[*AllocateNetBufferListForwardingContext*](https://msdn.microsoft.com/library/windows/hardware/hh598134)  
Allocates the extensible switch forwarding context and prepares a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure for send or receive operations within the extensible switch.

<a href="" id="copynetbufferlistinfo"></a>[*CopyNetBufferListInfo*](https://msdn.microsoft.com/library/windows/hardware/hh598136)  
Copies the forwarding context from a source packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568389) structure to a destination packet's **NET\_BUFFER\_LIST** structure. This data includes the extensible switch source port and network adapter information. The extensible switch destination port information can also be copied to the destination packet.

<a href="" id="freenetbufferlistforwardingcontext"></a>[*FreeNetBufferListForwardingContext*](https://msdn.microsoft.com/library/windows/hardware/hh598153)  
Frees the resources in the extensible switch forwarding context of a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure. This data was used for send or receive operations in a Hyper-V extensible switch, and was previously allocated by calling the [*AllocateNetBufferListForwardingContext*](https://msdn.microsoft.com/library/windows/hardware/hh598134) function.

<a href="" id="getnetbufferlistdestinations"></a>[*GetNetBufferListDestinations*](https://msdn.microsoft.com/library/windows/hardware/hh598157)  
Returns the destination ports from the forwarding context of a packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568389) structure.

A forwarding extension is responsible for adding destination ports for a packet, unless the packet is an NVGRE packet. (For more information, see [Hybrid Forwarding](hybrid-forwarding.md).) The extension calls the following extensible switch handler functions to add or update the destination ports within the packet's forwarding context:

<a href="" id="addnetbufferlistdestination"></a>[*AddNetBufferListDestination*](https://msdn.microsoft.com/library/windows/hardware/hh598133)  
Adds a single destination to the extensible switch forwarding context area for a packet that is specified by a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568389) structure.

**Note**  This call commits the change to the forwarding context area. In this case, the forwarding extension does not need to call [*UpdateNetBufferListDestinations*](https://msdn.microsoft.com/library/windows/hardware/hh598303).

<a href="" id="grownetbufferlistdestinations"></a>[*GrowNetBufferListDestinations*](https://msdn.microsoft.com/library/windows/hardware/hh598158)  
Increases the size of the destination port array in the forwarding context area of a packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568389) structure.

<a href="" id="updatenetbufferlistdestinations"></a>[*UpdateNetBufferListDestinations*](https://msdn.microsoft.com/library/windows/hardware/hh598303)  
Commits modifications that the extension made to one or more extensible switch destination ports of a packet. This function updates the forwarding context of a packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568389) structure with these changes.

**Note**  After the forwarding extension commits the changes for destination ports to the forwarding context, destination ports cannot be removed and only the **IsExcluded** member of a destination port's [**NDIS\_SWITCH\_PORT\_DESTINATION**](https://msdn.microsoft.com/library/windows/hardware/hh598224) structure can be changed. For more information, see [Excluding Packet Delivery to Extensible Switch Destination Ports](excluding-packet-delivery-to-extensible-switch-destination-ports.md).

## Related topics


[Hyper-V Extensible Switch Forwarding Context](hyper-v-extensible-switch-forwarding-context.md)

[Hyper-V Extensible Switch Forwarding Context Data Types](hyper-v-extensible-switch-forwarding-context-data-types.md)










