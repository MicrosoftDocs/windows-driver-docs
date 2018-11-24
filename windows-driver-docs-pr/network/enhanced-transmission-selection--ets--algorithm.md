---
title: Enhanced Transmission Selection (ETS) Algorithm
description: Enhanced Transmission Selection (ETS) Algorithm
ms.assetid: 952ECB1E-96AD-4717-8E49-68558E7E9AD4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enhanced Transmission Selection (ETS) Algorithm


Enhanced Transmission Selection (ETS) is a transmission selection algorithm (TSA) that is specified by the IEEE 802.1Qaz draft standard. This standard is part of the framework for the IEEE 802.1 Data Center Bridging (DCB) interface.

Transmission selection based solely on IEEE 802.1p priority levels can lead to situations in which higher-priority traffic blocks lower-priority traffic. ETS ensures fairness by allowing a minimum amount of bandwidth to be allocated to traffic classes that are assigned to different 802.1p priority levels.

Each traffic class is allocated a percentage of the available bandwidth on the data link between directly connected peers. If a traffic class doesn't use its allocated bandwidth, ETS allows other traffic classes to use the available bandwidth that the traffic class is not using.

NDIS Quality of Service (QoS) traffic classes are defined through OID method requests of [OID\_QOS\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451835). This OID request contains an [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure which specifies the following traffic class attributes:

-   The number of traffic classes that is specified by the **NumTrafficClasses** member.

-   The TSA used by the traffic class. This is specified by the **TsaAssignmentTable** member. If the table element for the traffic class is set to NDIS\_QOS\_TSA\_ETS, the traffic class uses the ETS TSA.

-   The 802.1p priority that is assigned to the traffic class. A traffic class can be assigned to one or more priority levels. However, each priority level can only be assigned to one traffic class.

    For more information, see [Traffic Class Priority Assignment](traffic-class-priority-assignment.md).

-   The bandwidth allocated for the traffic class. This is specified by the **TcBandwidthAssignmentTable** member. This table is only valid for traffic classes that use the ETS TSA.

    For more information about ETS bandwidth allocation, see [Bandwidth Allocation](bandwidth-allocation.md).

For more information about priority levels, see [IEEE 802.1p Priority Levels](ieee-802-1p-priority-levels.md).

 

 





