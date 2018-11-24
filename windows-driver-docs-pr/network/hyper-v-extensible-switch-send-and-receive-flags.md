---
title: Hyper-V Extensible Switch Send and Receive Flags
description: Hyper-V Extensible Switch Send and Receive Flags
ms.assetid: FBA506EC-4E9F-4964-9C9C-FF4910DDA908
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hyper-V Extensible Switch Send and Receive Flags


**Note**  This page assumes that you are familiar with the information and diagrams in [Overview of the Hyper-V Extensible Switch](overview-of-the-hyper-v-extensible-switch.md) and [Hybrid Forwarding](hybrid-forwarding.md).

 

Packet traffic that moves over the Hyper-V extensible switch data path is obtained by extensions in the following way:

-   An extension obtains a packet from the ingress data path when its [*FilterSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff549966) function is called. The extension forwards the packet to underlying extensions on the ingress data path by calling [**NdisFSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff562616). Filtering and forwarding extensions can also drop the packet from the ingress data path by calling [**NdisFSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff562618).

-   An extension obtains a packet from the egress data path when its [*FilterReceiveNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff549960) function is called. The extension forwards the packet to overlying extensions on the egress data path by calling [**NdisFIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff561820). Filtering and forwarding extensions can also drop the packet from the egress data path by calling [**NdisFReturnNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff562613).

The following flags may be set in the *SendFlags* parameter of [*FilterSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff549966) or [**NdisFSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff562616):

<a href="" id="ndis-send-flags-switch-single-source"></a>**NDIS\_SEND\_FLAGS\_SWITCH\_SINGLE\_SOURCE**  
If this flag is set, all packets in a linked list of [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures originated from the same Hyper-V extensible switch source port.

When NDIS calls [*FilterSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff549966), it will set this flag if the extensible switch extensible interface has grouped multiple packets from the same source port. For the best performance, the extensions should keep this grouping in place and set this flag when it calls [**NdisFSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff562616). The extension can also add any originated or cloned packets to the linked list of [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures if the extension uses the same source port as the other packets in the list.

**Note**  If each packet in the linked list of [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures uses the same source port, the extension should set the **NDIS\_SEND\_COMPLETE\_FLAGS\_SWITCH\_SINGLE\_SOURCE** flag in the *SendCompleteFlags* parameter of [**NdisFSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff562618) when it completes the send request.

 

<a href="" id="ndis-send-flags-switch-destination-group"></a>**NDIS\_SEND\_FLAGS\_SWITCH\_DESTINATION\_GROUP**  
If this flag is set, all packets in a linked list of [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures are to be forwarded to the same extensible switch destination port.

A forwarding extension can use this flag for a linked list of [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures that it forwards on the ingress data path after it determines each packet's destination ports. This flag is consumed and removed by the underlying miniport edge of the extensible switch before it forwards the packets up the egress data path.

Capturing and filtering extensions cannot use this flag.

**Note**  The forwarding extension only determines the packet's destination ports for non-NVGRE packets. If the packet is an NVGRE packet, the Hyper-V Network Virtualization (HNV) component determines the packet's destination ports and forwards the packet. For more information, see [Hybrid Forwarding](hybrid-forwarding.md).

 

For the best performance, forwarding extensions should set this flag if all packets in the linked list are to be forwarded to the same destination port. By setting this flag, the extension is acknowledging that all packets in the linked list have the same destination port elements in the extensible switch forwarding context.

**Note**  The forwarding extension must not set this flag for a linked list of packets that have multiple destination ports.

 

The following flags may be set in the *ReceiveFlags* parameter of [*FilterReceiveNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff549960) or [**NdisFIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff561820):

<a href="" id="ndis-receive-flags-switch-single-source"></a>**NDIS\_RECEIVE\_FLAGS\_SWITCH\_SINGLE\_SOURCE**  
If this flag is set, all packets in a linked list of [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures originated from the same Hyper-V extensible switch source port.

When NDIS calls [*FilterReceiveNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff549960), it will set this flag if the extensible switch has grouped multiple packets from the same source port. For the best performance, the extensions should keep this grouping in place and set this flag when it calls [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598). The extensions should also add any originated or cloned packets to the linked list of [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures if the packet has the same source port as the other packets in the list.

**Note**  If each packet in the linked list of [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures use the same source port, the extension should set the **NDIS\_RETURN\_FLAGS\_SWITCH\_SINGLE\_SOURCE** flag in the *ReturnFlags* parameter of [*FilterReturnNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff549964) when the receive request completes. The extension must set this flag in the *ReturnFlags* parameter if it calls [**NdisFReturnNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff562613) to return packets that it did not originate or clone.

 

<a href="" id="ndis-receive-flags-switch-destination-group"></a>**NDIS\_RECEIVE\_FLAGS\_SWITCH\_DESTINATION\_GROUP**  
If this flag is set, all packets in a linked list of [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures are to be forwarded to the same extensible switch destination port.

When NDIS calls [*FilterReceiveNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff549960), it will set this flag if the extensible switch has grouped multiple packets that have the same destination ports. For the best performance, the extensions should keep this grouping in place and set this flag when it calls [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598). The extensions should also add any originated or cloned packets to the linked list of [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures if the packet has the same destination ports as the other packets in the list.

**Note**  When an extension calls [**NdisFIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff561820), it must not set the **NDIS\_RECEIVE\_FLAGS\_RESOURCES** flag in the *ReceiveFlags* parameter. The extensible switch interface ignores this flag and will complete the receive indication by calling [*FilterReturnNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff549964).

 

 

 





