---
title: Hyper-V Extensible Switch hybrid forwarding
description: This section describes hybrid forwarding with a Hyper-V Extensible Switch
ms.assetid: 135CA734-1C92-4EEA-81DC-96A6A68ABBE8
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hybrid Forwarding


Starting with NDIS 6.40 (Windows Server 2012 R2, the Hyper-V extensible switch architecture supports hybrid forwarding by the Hyper-V Network Virtualization (HNV) component of the extensible switch and by forwarding extensions.

**Note**  This page assumes that you are familiar with [Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload](network-virtualization-using-generic-routing-encapsulation--nvgre--task-offload.md) and [Overview of the Hyper-V Extensible Switch](overview-of-the-hyper-v-extensible-switch.md).

 

## NVGRE and non-NVGRE packets


In a hybrid forwarding environment, there are two types of packets that enter and leave the Hyper-V extensible switch: NVGRE packets and non-NVGRE packets:

-   NVGRE packets have the encapsulated format that is specified in the [NVGRE: Network Virtualization using Generic Routing Encapsulation](http://ietfreport.isoc.org/idref/draft-sridharan-virtualization-nvgre/) Internet Draft. NVGRE packets are forwarded by the HNV component of the Hyper-V extensible switch.
-   Non-NVGRE packets are just normal network packets. Non-NVGRE packets are forwarded by the forwarding extension (or, in the absence of a forwarding extension, the extensible switch itself).

## Flow of NVGRE and non-NVGRE packets through the switch


In the ingress data path, after the capturing and filtering extensions but before the forwarding extension, if a packet is an NVGRE packet, the extensible switch sets the **NativeForwardingRequired** flag in the [**NDIS\_SWITCH\_FORWARDING\_DETAIL\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh598211) structure for the packet. This structure is contained in the **NetBufferListInfo** member of the packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

**Note**  The **NetBufferListInfo** member of the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) is often referred to as the packet's "out-of-band (OOB) data."

 

If the **NativeForwardingRequired** flag is set in the packet's OOB data, the packet is an NVGRE packet. If it is not set, the packet is a non-NVGRE packet.

Extensions should use the [**NET\_BUFFER\_LIST\_SWITCH\_FORWARDING\_DETAIL**](https://msdn.microsoft.com/library/windows/hardware/hh598259) macro to check the value of the **NativeForwardingRequired** flag.

NVGRE and non-NVGRE packets are treated as follows:

-   The HNV component of the Hyper-V extensible switch forwards (i.e., determines the destination table for) all NVGRE packets
-   The HNV component performs NVGRE encapsulation and decapsulation as needed.
-   The forwarding extension forwards all non-NVGRE packets.
-   The forwarding extension cannot forward NVGRE packets, but it can perform the same filtering actions as a filtering extension, including adding or excluding destination ports or even dropping packets.
-   If there is no forwarding extension, the Hyper-V extensible switch forwards all packets.

For more information, see [Packet Flow through the Extensible Switch Data Path](packet-flow-through-the-extensible-switch-data-path.md).

## Support for third-party network virtualization


A **VirtualSubnetId** can be configured on a VM network adapter port as an external virtual subnet. This feature was added to enable forwarding extensions to provide third-party network virtualization solutions. On ingress, the Hyper-V extensible switch will not set the **NativeForwardingRequired** flag in the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures for these packets. A forwarding extension may then modify the packet headers, as required, during forwarding. Packets that are being modified must be cloned and their **ParentNetBufferList** pointers set to the original **NET\_BUFFER\_LIST**. (See [Cloning Packet Traffic](cloning-or-duplicating-packet-traffic.md).)

## Related topics


[Adding Extensible Switch Destination Port Data to a Packet](adding-extensible-switch-destination-port-data-to-a-packet.md)

[Cloning Packet Traffic](cloning-or-duplicating-packet-traffic.md)

[Forwarding Extensions](forwarding-extensions.md)

[Packet Flow through the Extensible Switch Data Path](packet-flow-through-the-extensible-switch-data-path.md)

[**NET\_BUFFER\_LIST\_SWITCH\_FORWARDING\_DETAIL**](https://msdn.microsoft.com/library/windows/hardware/hh598259)

[**NDIS\_SWITCH\_FORWARDING\_DETAIL\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh598211)

 

 






