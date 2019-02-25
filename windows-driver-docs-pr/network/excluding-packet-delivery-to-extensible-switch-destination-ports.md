---
title: Excluding Packet Delivery to Extensible Switch Destination Ports
description: Excluding Packet Delivery to Extensible Switch Destination Ports
ms.assetid: 04BF02A6-360F-482E-A86B-31232AFCB778
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Excluding Packet Delivery to Extensible Switch Destination Ports


This topic describes how Hyper-V extensible switch extensions can exclude the delivery of packets to extensible switch ports. The destination ports for a packet are specified within the out-of-band (OOB) forwarding context within the packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure. For more information on this context, see [Hyper-V Extensible Switch Forwarding Context](hyper-v-extensible-switch-forwarding-context.md).

**Note**  This page assumes that you are familiar with the information and diagrams in [Overview of the Hyper-V Extensible Switch](overview-of-the-hyper-v-extensible-switch.md) and [Hybrid Forwarding](hybrid-forwarding.md).


**Note**  In the extensible switch interface, NDIS filter drivers are known as *extensible switch extensions* and the driver stack is known as the *extensible switch driver stack*. For more information about the extensions, see [Hyper-V Extensible Switch Extensions](hyper-v-extensible-switch-extensions.md).

Filtering and forwarding extensions can exclude the delivery of packets obtained on the extensible switch ingress or egress data paths. Excluding packet delivery can be done in the following ways:

-   The extension can drop the packet by completing the packet request or indication. This excludes the delivery of a packet to any extensible switch port. This method can be used on packets that have one or more destination ports.

    For packets obtained on the extensible switch ingress data path, the extension completes the packet send request by calling [**NdisFSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff562618).

    For packets obtained on the extensible switch egress data path, the extension completes the packet receive indication by calling [**NdisFReturnNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff562613).

-   For packets obtained on the egress data path with multiple destination ports, the extension can exclude packet delivery by modifying the data for one or more destination ports. The extension does this by setting the **IsExcluded** member of the destination port's [**NDIS\_SWITCH\_PORT\_DESTINATION**](https://msdn.microsoft.com/library/windows/hardware/hh598224) structure to a value of one. This method allows the packet to be delivered to those ports whose **IsExcluded** value is set to zero.

    **Note**  Packets obtained on the ingress data path do not contain destination ports. This data is only available after the extensible switch forwards the packet up the egress data path.

After the extension has modified the destination port's **IsExcluded** value, it must forward the packet in the egress data path to overlying extensions. However, if the **IsExcluded** data for all the packet's destination ports is set to one, the extension should drop the packet by completing the packet receive indication instead of forwarding it.

**Note**  After an extension has set the destination port's **IsExcluded** value to one, overlying extensions on the egress data path cannot change this value to zero.

**Note**  Capturing extensions cannot exclude the delivery of packets to extensible switch ports.

Filtering and forwarding extensions must follow these guidelines for excluding packet delivery to extensible switch ports:

-   On the extensible switch ingress data path, filtering and forwarding extensions can exclude packet delivery based on a policy criteria for a packet's source port or data.

    The source port information is stored in the [**NDIS\_SWITCH\_FORWARDING\_DETAIL\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh598211) union in the OOB data of the packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure. The extension obtains the data by using the [**NET\_BUFFER\_LIST\_SWITCH\_FORWARDING\_DETAIL**](https://msdn.microsoft.com/library/windows/hardware/hh598259) macro.

    If the extension excludes the delivery of a packet obtained from the ingress data path, it must drop the packet by completing the packet send request.

-   On the extensible switch ingress data path, forwarding extensions determine a packet's destination ports and add this information to the packet's OOB data. Based on policy criteria enforced by the extension, it can exclude packet delivery to a port by not adding its destination port information to the OOB data.

    For more information about this procedure, see [Adding Extensible Switch Destination Port Data to a Packet](adding-extensible-switch-destination-port-data-to-a-packet.md).

-   On the extensible switch egress data path, filtering and forwarding extensions can exclude the delivery of the packet based on policy criteria. For example, filtering extensions can exclude packet delivery based on policy criteria for a packet's source port or destination ports.

    Extensions exclude the delivery of a packet to destination ports by following these steps:

    1.  The extension obtains the packet's destination ports by calling [*GetNetBufferListDestinations*](https://msdn.microsoft.com/library/windows/hardware/hh598157). If the call returns NDIS\_STATUS\_SUCCESS, the *Destinations* parameter contains a pointer to an [**NDIS\_SWITCH\_FORWARDING\_DESTINATION\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598210) structure. This structure specifies the extensible switch destination ports of the packet. Each destination port is formatted as an [**NDIS\_SWITCH\_PORT\_DESTINATION**](https://msdn.microsoft.com/library/windows/hardware/hh598224) structure.

        **Note**  If the **NumDestinations** member of the [**NDIS\_SWITCH\_FORWARDING\_DESTINATION\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598210) structure contains a value of zero, the packet has no data for destination ports.

2.  The extension excludes the packet delivery to an extensible switch port by setting the **IsExcluded** member of the destination port's [**NDIS\_SWITCH\_PORT\_DESTINATION**](https://msdn.microsoft.com/library/windows/hardware/hh598224) structure to a value of one.

    **Note**  If the extension excludes delivery of the packet to all of its destination ports, the extension must drop the packet by completing the packet's receive indication.

3.  If the extension excludes delivery to one or all destination ports in a packet, it must do the following:

    -   The extension must call [*UpdateNetBufferListDestinations*](https://msdn.microsoft.com/library/windows/hardware/hh598303) to commit these changes to the packet's OOB data.

    -   The extension must call [*ReportFilteredNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/hh598297). When this function is called, the extensible switch interface increments counters and logs events for the excluded packet. The extension must make this call before it forwards the packet in the extensible switch data path from which it obtained the packet.

    Similarly, if the extension completes the packet send request or indication to exclude delivery to all ports for the packet, it must also call [*ReportFilteredNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/hh598297).

    **Note**  The extension can create a linked list of [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures for packets that the extension is excluding. When the extension calls [*ReportFilteredNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/hh598297), it sets the *NetBufferLists* parameter to a pointer to the linked list.

For more information about the extensible switch ingress and egress data paths, see [Hyper-V Extensible Switch Data Path](hyper-v-extensible-switch-data-path.md).