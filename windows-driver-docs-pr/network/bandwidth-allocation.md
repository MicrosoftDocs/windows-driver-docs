---
title: Bandwidth Allocation
description: Bandwidth Allocation
ms.date: 04/20/2017
---

# Bandwidth Allocation


Bandwidth allocation is a component of the Enhanced Transmission Selection (ETS) algorithm. ETS is specified in the IEEE 802.1Qaz draft standard. This standard is part of the framework for the IEEE 802.1 Data Center Bridging (DCB) interface.

Under ETS, each traffic class is assigned a percentage of the bandwidth that is available to transmit packets between two directly connected peers. If the bandwidth allocated to a traffic class is not completely used, ETS allows the unused bandwidth to be shared by traffic classes that have different IEEE 802.1p priority levels.

NDIS Quality of Service (QoS) parameters are specified through the [**NDIS\_QOS\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_qos_parameters) structure. The **TcBandwidthAssignmentTable** member contains an array that specifies the bandwidth allocation for traffic classes that use the ETS algorithm.

For more information about priority levels, see [IEEE 802.1p Priority Levels](ieee-802-1p-priority-levels.md).

 

