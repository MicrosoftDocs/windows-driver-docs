---
title: Traffic Class Priority Assignment
description: Traffic Class Priority Assignment
ms.assetid: 846AC7E6-28D9-4610-9493-BE547869AB15
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Traffic Class Priority Assignment


The Enhanced Transmission Selection (ETS) algorithm specifies a method by which a traffic class is assigned an 802.1p priority level. ETS is specified in the IEEE 802.1Qaz draft standard. This standard is part of the framework for the IEEE 802.1 Data Center Bridging (DCB) interface.

NDIS Quality of Service (QoS) traffic classes specify a set of policies that determine how the network adapter handles transmit, or *egress*, packets. Under ETS, each traffic class is assigned an IEEE 802.1p priority level in which to transmit packets. A traffic class can be assigned to one or more IEEE 802.1p priority levels. However, each IEEE 802.1p priority level can only be assigned to one traffic class.

NDIS QoS parameters are specified through the [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure. The **PriorityAssignmentTable** member contains an array that specifies the priority assignments for each traffic class.

For more information about priority levels, see [IEEE 802.1p Priority Levels](ieee-802-1p-priority-levels.md).

 

 





