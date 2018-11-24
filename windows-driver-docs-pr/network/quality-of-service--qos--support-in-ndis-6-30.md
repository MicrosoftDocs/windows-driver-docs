---
title: Quality of Service (QoS) Support in NDIS 6.30
description: Quality of Service (QoS) Support in NDIS 6.30
ms.assetid: B425C05C-0F65-4F94-AECD-0BAD35DA441F
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Quality of Service (QoS) Support in NDIS 6.30


NDIS 6.30 and later provide support for quality of service (QoS). Miniport drivers use NDIS QoS for traffic prioritization of transmit, or *egress*, packets over a network adapter that is compliant with IEEE 802.1 Data Center Bridging (DCB).

IEEE 802.1 Data Center Bridging (DCB) is a collection of standards that defines a unified 802.3 Ethernet media interface, or fabric, for local area network (LAN) and storage area network (SAN) technologies. DCB extends the current 802.1 bridging specification to support the co-existence of LAN- and SAN-based applications over the same networking fabric within a data center. DCB also supports technologies, such as Fibre Channel over Ethernet (FCoE) and iSCSI, by defining link-level policies that prevents packet loss.

NDIS QoS support for DCB allows a miniport driver to be configured with traffic classes that specify a set of policies. Each policy determine how the network adapter handles egress packets for prioritized delivery.

Each traffic class specifies the following policies that are applied to egress packets:

<a href="" id="priority-level-and-flow-control"></a>Priority Level and Flow Control  
This policy defines the IEEE 802.1p priority level and optional flow control algorithms for the egress traffic.

<a href="" id="traffic-selection-algorithms--tsas-"></a>Traffic Selection Algorithms (TSAs)  
This policy specifies how the network adapter selects egress traffic for delivery from its transmit queues. For example, the adapter could select egress packets based on IEEE 802.1p priority or the percentage of the egress bandwidth that is allocated to each traffic class.

For more information about NDIS QoS support for DCB, see [NDIS QoS for Data Center Bridging](ndis-qos-for-data-center-bridging.md).

 

 





