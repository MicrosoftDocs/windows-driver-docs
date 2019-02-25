---
title: NDIS QoS Traffic Classes
description: NDIS QoS Traffic Classes
ms.assetid: 0DE61F97-7173-4D91-90F3-20EAFB810251
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS QoS Traffic Classes


NDIS Quality of Service (QoS) traffic classes specify a set of policies that determine how the network adapter handles transmit, or *egress*, packets for prioritized delivery. Each traffic class specifies the following policies that are applied to egress packets:

<a href="" id="priority-level-and-flow-control"></a>Priority Level and Flow Control  
This policy defines the IEEE 802.1p priority level and optional flow control algorithms for the egress traffic.

For more information, see [Priority Levels and Flow Control](priority-levels-and-flow-control.md).

<a href="" id="traffic-selection-algorithms--tsas-"></a>Traffic Selection Algorithms (TSAs)  
This policy specifies how the network adapter selects egress traffic for delivery from its transmit queues. For example, the adapter could select egress packets based on IEEE 802.1p priority or the percentage of the egress bandwidth that is allocated to each traffic class.

For more information, see [Transmission Selection Algorithms (TSAs)](transmission-selection-algorithms--tsas-.md).

**Note**  Bandwidth allocation is only supported for the Enhanced Transmission Selection (ETS) TSA. For more information, see [Enhanced Transmission Selection (ETS) Algorithm](enhanced-transmission-selection--ets--algorithm.md).

 

Traffic classes are specified through object identifier (OID) method requests of [OID\_QOS\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451835). This OID request contains an [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure that specifies the following NDIS QoS parameters:

-   The number of traffic classes to be configured on the network adapter. Each traffic class is identified by a value in the range from zero to (**NumTrafficClasses**–1), where **NumTrafficClasses** is a member of the [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure.

    **Note**  Starting with NDIS 6.30, NDIS QoS supports a maximum of NDIS\_QOS\_MAXIMUM\_TRAFFIC\_CLASSES (8) traffic classes. The network adapter must support a minimum of three traffic classes.

     

-   The 802.1p priority level associated with the traffic class.

-   The TSA associated with the traffic class.

-   The transmit bandwidth allocated to each traffic class that uses the ETS TSA.

OID method requests of [OID\_QOS\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451835) also specify traffic classifications. These classifications define the relationship between egress packets and IEEE 802.1p priority levels. For more information, see [NDIS QoS Traffic Classifications](ndis-qos-traffic-classifications.md).

 

 





