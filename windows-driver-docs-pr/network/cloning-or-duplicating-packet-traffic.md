---
title: Cloning Packet Traffic
description: Cloning Packet Traffic
ms.assetid: 6BAE348D-B5BA-4B74-8D9B-79B146427D8C
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Cloning Packet Traffic


This topic describes how Hyper-V extensible switch extensions clone, or duplicate, packets and inject them into the extensible switch data path. For more information on cloning packets, see [Cloned NET\_BUFFER\_LIST Structures](cloned-net-buffer-list-structures.md).

**Note**  This page assumes that you are familiar with the information and diagrams in [Overview of the Hyper-V Extensible Switch](overview-of-the-hyper-v-extensible-switch.md) and [Hybrid Forwarding](hybrid-forwarding.md).

**Note**  In the extensible switch interface, NDIS filter drivers are known as *extensible switch extensions* and the driver stack is known as the *extensible switch driver stack*. For more information about the extensions, see [Hyper-V Extensible Switch Extensions](hyper-v-extensible-switch-extensions.md).

Extensible switch filtering and forwarding extensions can inject cloned packets into the extensible switch ingress or egress data path by following these guidelines:

-   The extension must first allocate a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568389) structure for the cloned packet. The extension must then copy the packet data from the original packet to the cloned packet. For more information on how to clone packets, see [Derived NET\_BUFFER\_LIST Structures](derived-net-buffer-list-structures.md).

-   After the extension allocates a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568389) structure, it must call the [*AllocateNetBufferListForwardingContext*](https://msdn.microsoft.com/library/windows/hardware/hh598134) handler function to allocate the extensible switch forwarding context for the packet.

    The forwarding context resides in the out-of-band (OOB) data of the packet. It contains forwarding information for the packet, such as its source port and an array of one or more destination ports.

    For more information about the forwarding context, see [Hyper-V Extensible Switch Forwarding Context](hyper-v-extensible-switch-forwarding-context.md).

-   The extension must copy the OOB data, including the existing source port, from the original packet to the cloned packet by calling [*CopyNetBufferListInfo*](https://msdn.microsoft.com/library/windows/hardware/hh598136). If the extension plans to inject the packet into the ingress data path, it must also copy the destination ports from the OOB data of the original packet.

    When it copies the OOB data, the extension must follow these guidelines:

    -   If the filtering extension plans to inject the packet into the ingress data path, it must call [*CopyNetBufferListInfo*](https://msdn.microsoft.com/library/windows/hardware/hh598136) with the NDIS\_SWITCH\_COPY\_NBL\_INFO\_FLAGS\_PRESERVE\_DESTINATIONS flag unspecified. This causes the original packet's destination ports to not be copied to the cloned packets. When the filtering extension injects this packet into the ingress data path, destination ports will be added to the packet by either an underlying forwarding extension (if enabled in the driver stack) or the miniport edge of the extensible switch.

    -   If the filtering extension plans to inject the packet into the egress data path, it must call [*CopyNetBufferListInfo*](https://msdn.microsoft.com/library/windows/hardware/hh598136) with the NDIS\_SWITCH\_COPY\_NBL\_INFO\_FLAGS\_PRESERVE\_DESTINATIONS flag specified. This causes the original packet's destination ports to be copied to the cloned packets.

-   If the filtering extension is cloning or duplicating a packet that was obtained from the egress data path, it can change the destination ports for the packet after it calls [*CopyNetBufferListInfo*](https://msdn.microsoft.com/library/windows/hardware/hh598136) with the NDIS\_SWITCH\_COPY\_NBL\_INFO\_FLAGS\_PRESERVE\_DESTINATIONS flag specified. For more information on this procedure, see [Modifying a Packet's Extensible Switch Source Port Data](modifying-a-packet-s-extensible-switch-source-port-data.md).

-   If the forwarding extension is cloning or duplicating a packet that was obtained from the ingress data path, it must add new destination ports for the packet before it injects the packet into the ingress data path. For more information on this procedure, see [Adding Extensible Switch Destination Port Data to a Packet](adding-extensible-switch-destination-port-data-to-a-packet.md).

-   After the extension calls [*CopyNetBufferListInfo*](https://msdn.microsoft.com/library/windows/hardware/hh598136), the packet will be assigned the same source port information that was contained in the original packet.

    The extension can call [*SetNetBufferListSource*](https://msdn.microsoft.com/library/windows/hardware/hh598300) to change the source port information in the packet's out-of-band (OOB) data.

    The extension may want the packet to be treated as if it originated from a particular port. This allows the policies for that port to be applied to the packet. The extension calls [*SetNetBufferListSource*](https://msdn.microsoft.com/library/windows/hardware/hh598300) to change the source port for the packet.

    However, there may be situations where the extension may want to assign the packet's source port identifier to **NDIS\_SWITCH\_DEFAULT\_PORT\_ID**. For example, the extension may want to set the source port identifier to **NDIS\_SWITCH\_DEFAULT\_PORT\_ID** for proprietary control packets that are sent to a device on the external network.

-   In the standard NDIS data path, non-extensible switch OOB data often has different values depending on whether the packet is being indicated as a send or a receive. For example, the [**NDIS\_IPSEC\_OFFLOAD\_V2\_HEADER\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff565812) OOB data is a union of send-and-receive–specific structures

    In the extensible switch data path, all packets move through the extension driver stack as both sends and receives. Because of this, the non-extensible switch OOB data within the packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure will be in either a send or receive format through the duration of the flow through the driver stack.

    The format of this OOB data depends on the source extensible switch port from which the packet arrived at the extensible switch. If the source port is connected to the external network adapter, the non-extensible switch OOB data will be in a receive format. For other ports, this OOB data will be in a send format.

    The source port information is stored in the [**NDIS\_SWITCH\_FORWARDING\_DETAIL\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh598211) union in the OOB data of the packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure. The extension obtains the data by using the [**NET\_BUFFER\_LIST\_SWITCH\_FORWARDING\_DETAIL**](https://msdn.microsoft.com/library/windows/hardware/hh598259) macro.

    **Note**  If the extension clones a packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure, it must take the non-extensible switch OOB data into consideration if it adds or modifies the OOB data. The extension can call [*CopyNetBufferListInfo*](https://msdn.microsoft.com/library/windows/hardware/hh598136) to copy all OOB data from a source packet to a cloned packet. This function will maintain the OOB send or receive format when the data is copied to the packet.



-   When the extension clones a packet, the cloned packet data is located in local, or *trusted*, memory in the parent operating system of the Hyper-V parent partition. This memory cannot be accessed by the child partition. Therefore, it is considered "safe" from unsynchronized updates by the guest operating system that runs in that partition.

    After the original packet has been cloned, the extension must obtain the [**NDIS\_SWITCH\_FORWARDING\_DETAIL\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh598211) union in the cloned packet by using the [**NET\_BUFFER\_LIST\_SWITCH\_FORWARDING\_DETAIL**](https://msdn.microsoft.com/library/windows/hardware/hh598259) macro. The extension must set the **IsPacketDataSafe** member to TRUE. This specifies that all of the packet data is located in trusted memory.

Filtering and forwarding extensions must follow these guidelines for injecting cloned packets into the ingress or egress data path:

-   The extension must call [**NdisFSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff562616) to inject the cloned packet into the ingress data path. The extension must set the *SendFlags* parameter with the appropriate extensible switch flag settings. For more information about these flag settings, see [Hyper-V Extensible Switch Send and Receive Flags](hyper-v-extensible-switch-send-and-receive-flags.md).

    When NDIS calls the extension's [*FilterSendNetBufferListsComplete*](https://msdn.microsoft.com/library/windows/hardware/ff549967) function to complete the send request of the cloned packet, the extension must call [*FreeNetBufferListForwardingContext*](https://msdn.microsoft.com/library/windows/hardware/hh598153) to free the allocated forwarding context. The extension must do this before it frees or reuses the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568389) structure for the packet.

    **Note**  The extension must inject the cloned packet into the ingress data path if it modifies the packet data or source port for a packet that it obtained from the egress data path. It must also inject the cloned packet into the ingress data path if the packet's destination ports are not preserved.



-   The extension must call [**NdisFIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff561820) to inject the cloned packet into the egress data path. The extension must set the *ReceiveFlags* parameter with the appropriate extensible switch flag settings.

    When NDIS calls the extension's [*FilterReturnNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff549964) function to complete the receive request of the cloned packet, the extension must call [*FreeNetBufferListForwardingContext*](https://msdn.microsoft.com/library/windows/hardware/hh598153) before it frees or reuses the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568389) structure for the packet.

    **Note**  Before the forwarding extension calls [**NdisFIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff561820), it must have determined the cloned packet's destination ports and added this data to the packet's OOB data.



-   If the extension clones a packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568389) structure, it must retain ownership of the original packet's **NET\_BUFFER\_LIST** structure until the cloned packet's send or receive request has completed. The extension must use the **ParentNetBufferList** member of the cloned packet's **NET\_BUFFER\_LIST** structure to link to the original packet's **NET\_BUFFER\_LIST** structure.

    **Note**  In NDIS 6.30 (Windows Server 2012), the extension can use the **ParentNetBufferList** member to link to the original packet, but it is not required to do so. In NDIS 6.40 (Windows Server 2012 R2) and later, the extension is required to use the **ParentNetBufferList** member to link to the original packet.

    Once the cloned packet's send or receive request has completed, the extension must complete the send or receive request of the original packet.

    **Note**  If the extension has cloned a packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568389) structure, it can complete the send or receive request of the original packet after it has been cloned.

-   If the extension clones a packet, it can complete the send or receive request of the original packet as soon as it is cloned.

If the forwarding or filtering extension obtains a packet in the egress data path, it cannot inject a cloned version of the packet in this data path if the extension modified the packet data or changed the source port. However, the extension can inject these packets into the ingress data path. This allows the packet to be forwarded and filtered properly through the extensible switch data path.

**Note**  Filtering extensions can only inject cloned packets into the ingress data path if the packet's destination ports are not preserved.

For example, assume that a packet with multiple destination ports was obtained in the extensible switch egress data path. If one destination port requires special handling, such as data encapsulation, the forwarding or filtering extension handles this by following these steps:

1.  Exclude packet delivery to the port that requires special handling. The extension does this by setting the **IsExcluded** member of the destination port's [**NDIS\_SWITCH\_PORT\_DESTINATION**](https://msdn.microsoft.com/library/windows/hardware/hh598224) structure to a value of one. For more information on this procedure, see [Excluding Packet Delivery to Extensible Switch Destination Ports](excluding-packet-delivery-to-extensible-switch-destination-ports.md).

2.  Clone the original packet and perform the required handling of the packet data.

    **Note**  The filtering extension must not add a destination port for the cloned packet. This data will be added later by the forwarding extension or the miniport edge of the extensible switch.

3.  Forward the original packet on the egress data path by calling [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598).

4.  Inject the cloned packet on the ingress data path by calling [**NdisFSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff562616).

For more information about the extensible switch ingress and egress data paths, see [Hyper-V Extensible Switch Data Path](hyper-v-extensible-switch-data-path.md).

**Note**  Capturing extensions cannot clone packet traffic. However, they can originate packet traffic. For more information, see [Originating Packet Traffic](originating-packet-traffic.md).











