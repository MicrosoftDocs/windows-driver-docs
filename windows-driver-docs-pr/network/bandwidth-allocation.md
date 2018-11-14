---
title: Bandwidth Allocation
description: Bandwidth Allocation
ms.assetid: 775B4085-6028-441F-9D52-341077FF1647
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Bandwidth Allocation


Bandwidth allocation is a component of the Enhanced Transmission Selection (ETS) algorithm. ETS is specified in the IEEE 802.1Qaz draft standard. This standard is part of the framework for the IEEE 802.1 Data Center Bridging (DCB) interface.

Under ETS, each traffic class is assigned a percentage of the bandwidth that is available to transmit packets between two directly connected peers. If the bandwidth allocated to a traffic class is not completely used, ETS allows the unused bandwidth to be shared by traffic classes that have different IEEE 802.1p priority levels.

NDIS Quality of Service (QoS) parameters are specified through the [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure. The **TcBandwidthAssignmentTable** member contains an array that specifies the bandwidth allocation for traffic classes that use the ETS algorithm.

For more information about priority levels, see [IEEE 802.1p Priority Levels](ieee-802-1p-priority-levels.md).

 

 





