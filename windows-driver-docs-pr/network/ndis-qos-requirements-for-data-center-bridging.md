---
title: NDIS QoS Requirements for Data Center Bridging
description: NDIS QoS Requirements for Data Center Bridging
ms.assetid: 09BEFF6C-6887-42BA-A44B-5BFE65DBD69E
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS QoS Requirements for Data Center Bridging


To support NDIS Quality of Service (QoS) for IEEE 802.1 Data Center Bridging (DCB), the miniport driver and network adapter must support the following:

-   The miniport driver and network adapter must support Priority-based Flow Control (PFC) as specified by the IEEE 802.1Qbb draft standard.

-   The miniport driver and network adapter must support the Enhanced Transmission Selection (ETS) algorithm as specified by the IEEE 802.1Qaz draft standard.

-   The miniport driver and network adapter must support a minimum of three NDIS QoS traffic classes, and must support a minimum of two ETS-based traffic classes. Of these two, at least one ETS-based traffic class must support PFC.

    For more information about traffic classes, see [NDIS QoS Traffic Classes](ndis-qos-traffic-classes.md).

-   The miniport driver and network adapter must support the strict priority algorithm for transmission selection as specified by the IEEE 802.1Q-2005 standard.

For NDIS QoS, the miniport driver and network adapter can optionally support the Data Center Bridging Exchange (DCBX) protocol as specified by the IEEE 802.1Qaz draft standard. To support DCBX, the miniport driver and adapter must also support the Link Layer Discovery Protocol (LLDP) protocol as specified in the IEEE 802.1AB-2005 standard.

In addition, the miniport driver itself must support the following for NDIS QoS:

-   The miniport driver must support NDIS 6.30 or later versions of NDIS.

-   The miniport driver must support object identifier (OID) method requests of [OID\_QOS\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451835) for setting NDIS QoS parameters. For more information, see [Setting Local NDIS QoS Parameters](setting-local-ndis-qos-parameters.md).

    **Note**  NDIS handles most of the NDIS QoS OID requests for the miniport driver with the exception of [OID\_QOS\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451835).

     

-   The miniport driver must be able to resolve conflicting NDIS QoS parameter settings that were received over a DCBX frame that was sent from the remote peer. The driver resolves conflicts between its local and remote NDIS QoS parameters to determine its operational NDIS QoS parameters that the network adapter uses for prioritized packet transmission. For more information about this process, see [Resolving Operational NDIS QoS Parameters](resolving-operational-ndis-qos-parameters.md).

-   The miniport driver must be able to issue NDIS status indications when its operational NDIS QoS parameters change. For more information about this process, see [Indicating Changes to the Operational NDIS QoS Parameters](indicating-changes-to-the-operational-ndis-qos-parameters.md).

-   The miniport driver must be able to issue NDIS status indications when it detects a change in the NDIS QoS parameters on the remote peer. For more information about this process, see [Indicating Changes to the Remote NDIS QoS Parameters](indicating-changes-to-the-remote-ndis-qos-parameters.md).

 

 





