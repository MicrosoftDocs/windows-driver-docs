---
title: Overview of NDIS QoS Parameters
description: Overview of NDIS QoS Parameters
ms.assetid: E9321805-2930-410A-81BC-F7978517E89E
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of NDIS QoS Parameters


NDIS Quality of Service (QoS) parameters specify the policies and settings of traffic classes that the network adapter uses for transmit, or *egress*, packet delivery. NDIS QoS parameters contain the following settings:

-   Priority level and flow control settings. These settings define the IEEE 802.1p priority level and optional flow control algorithms for the transmit, or *egress*, traffic.

    For more information, see [Priority Levels and Flow Control](priority-levels-and-flow-control.md).

-   Traffic selection algorithm (TSA) settings. These settings define how the network adapter selects egress traffic from its transmit queues. For example, the adapter could use the strict priority TSA and select egress packets based only on IEEE 802.1p priority. The adapter could also use the Enhanced Transmission Selection (ETS) TSA that moderates egress traffic among traffic classes based on their bandwidth allocation.

    For more information, see [Transmission Selection Algorithms (TSAs)](transmission-selection-algorithms--tsas-.md).

-   Traffic classifications that specify the assignment of IEEE 802.1p priority levels to packets that contain data that matches a classification condition, such as an EtherType or destination TCP port. For more information, see [NDIS QoS Traffic Classifications](ndis-qos-traffic-classifications.md).

    **Note**  Traffic classifications are also known as "application priorities" in the IEEE 802.1 specifications.

     

NDIS QoS defines the following types of parameters:

<a href="" id="local-ndis-qos-parameters"></a>Local NDIS QoS Parameters  
Local NDIS QoS parameters specify the core QoS settings for a miniport driver and its network adapter. These parameters persist in the system registry, and are administered locally to the miniport driver in the following way:

-   Through an NDIS object identifier (OID) method request of [OID\_QOS\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451835) that is issued by the DCB component. This OID request contains an [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure that specifies the local NDIS QoS parameters.

    For more information on the DCB component, see [NDIS QoS Architecture for Data Center Bridging](ndis-qos-architecture-for-data-center-bridging.md).

-   Through proprietary registry settings for the network adapter. The miniport driver reads these settings when its [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function is called by NDIS.

-   Through settings issued to the miniport driver through a management application developed by the independent hardware vendor (IHV).

For more information about how the miniport driver obtains its local NDIS QoS parameters, see [Setting Local NDIS QoS Parameters](setting-local-ndis-qos-parameters.md).

<a href="" id="remote-ndis-qos-parameters"></a>Remote NDIS QoS Parameters  
Remote NDIS QoS parameters are those that are configured on a remote peer that the network adapter is connected to over the data link. The miniport driver discovers these parameters through the Data Center Bridging Exchange (DCBX) protocol that is specified by the IEEE 802.1Qaz draft standard.

DCBX requires that the miniport driver maintain only one set of remote QoS parameters that were received from a single data-link peer. The miniport driver must issue an NDIS status indication when its remote QoS parameters are either received from a peer for the first time or change later. For example, the driver may change its remote NDIS QoS parameters because it received a different set of QoS parameters from its remote peer. For more information on this process, see [Indicating Changes to the Remote NDIS QoS Parameters](indicating-changes-to-the-remote-ndis-qos-parameters.md).

For more information about how the miniport driver obtains its remote NDIS QoS parameters, see [Receiving Remote NDIS QoS Parameters](receiving-remote-ndis-qos-parameters.md).

<a href="" id="operational-ndis-qos-parameters"></a>Operational NDIS QoS Parameters  
Operational NDIS QoS parameters are those that the miniport driver resolves for traffic prioritization over the data-link connection to a remote peer. The miniport driver resolves its operational NDIS QoS parameters from its local or remote NDIS QoS parameters.

The miniport driver must issue an NDIS status indication when its operational QoS parameters are either resolved for the first time or change later. For example, the driver may change its operational NDIS QoS parameters because it received a different set of QoS parameters from its remote peer. For more information on how to generate this status indication, see [Indicating Changes to the Operational NDIS QoS Parameters](indicating-changes-to-the-operational-ndis-qos-parameters.md).

For more information about how the miniport driver resolves its operational NDIS QoS parameters, see [Resolving Operational NDIS QoS Parameters](resolving-operational-ndis-qos-parameters.md).

 

 





