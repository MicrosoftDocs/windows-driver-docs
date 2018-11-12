---
title: Resolving Operational NDIS QoS Parameters
description: Resolving Operational NDIS QoS Parameters
ms.assetid: F6C486B4-ABD5-413A-9E2D-283D83802C2B
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Resolving Operational NDIS QoS Parameters


Operational NDIS Quality of Service (QoS) parameters are those that the miniport driver uses for traffic prioritization over the data-link connection to a remote peer. The miniport driver derives, or *resolves*, its operational NDIS QoS parameters from one of the following:

-   The local NDIS QoS parameters that are administered locally on the miniport driver. For more information about how the miniport driver obtains its local QoS parameters, see [Setting Local NDIS QoS Parameters](setting-local-ndis-qos-parameters.md).

-   The remote NDIS QoS parameters that the miniport driver receives from a remote peer on the data link. For more information about how the miniport driver obtains its remote QoS parameters, see [Receiving Remote NDIS QoS Parameters](receiving-remote-ndis-qos-parameters.md).

Local, remote, and operational NDIS QoS parameters consist of the following types of data:

-   Priority level and flow control settings. These settings define the IEEE 802.1p priority level and optional flow control algorithms for the transmit, or *egress*, traffic.

    For more information, see [Priority Levels and Flow Control](priority-levels-and-flow-control.md).

-   Traffic selection algorithm (TSA) settings. These settings define how the network adapter selects egress traffic from its transmit queues.

    For example, the adapter could use the strict priority TSA and select egress packets based only on IEEE 802.1p priority. The adapter could also use the Enhanced Transmission Selection (ETS) TSA that moderates egress traffic among traffic classes based on their bandwidth allocation.

    For more information, see [Transmission Selection Algorithms (TSAs)](transmission-selection-algorithms--tsas-.md).

-   Traffic classifications that specify the assignment of IEEE 802.1p priority levels to packets that contain data which matches a classification condition, such as an EtherType or destination TCP port. For more information, see [NDIS QoS Traffic Classifications](ndis-qos-traffic-classifications.md).

    **Note**  Traffic classifications are also known as "application priorities" in the IEEE 802.1 specifications.

     

The miniport driver resolves its operational settings from its local or remote NDIS QoS parameters by following these guidelines:

-   If the local Data Center Bridging Exchange (DCBX) Willing state is enabled, the miniport driver must resolve its operational QoS parameters from its remote QoS parameters.

    For more information about how the miniport driver handles remote NDIS QoS parameters, see [Receiving Remote NDIS QoS Parameters](receiving-remote-ndis-qos-parameters.md).

-   If the local DCBX Willing state is disabled, the miniport driver must resolve its operational QoS parameters from its local QoS parameters.

    For more information about how the miniport driver handles local NDIS QoS parameters, see [Setting Local NDIS QoS Parameters](setting-local-ndis-qos-parameters.md).

-   The miniport driver can also resolve its operational QoS parameters based on any proprietary QoS settings that are defined by the independent hardware vendor (IHV). The driver can only do this for QoS parameters that are not configured remotely by the peer or locally by the operating system.

-   The miniport driver must issue an NDIS status indication when its operational QoS parameters are either resolved for the first time or change later. For example, the driver may change its operational NDIS QoS parameters because it received a different set of QoS parameters from its remote peer. For more information on how to generate this status indication, see [Indicating Changes to the Operational NDIS QoS Parameters](indicating-changes-to-the-operational-ndis-qos-parameters.md).

For more information about the local DCBX Willing state, see [Managing the Local DCBX Willing State](managing-the-local-dcbx-willing-state.md).

For more information on the methods used to resolve QoS operational parameters, refer to the IEEE 802.1Qaz draft standard.

 

 





