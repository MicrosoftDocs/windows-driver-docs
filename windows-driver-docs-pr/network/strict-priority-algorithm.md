---
title: Strict Priority Algorithm
description: Strict Priority Algorithm
ms.date: 04/20/2017
---

# Strict Priority Algorithm


Strict priority is a transmission selection algorithm (TSA) that is specified in the IEEE 802.1Q-2005 standard. This standard is part of the framework for the IEEE 802.1 Data Center Bridging (DCB) interface.

When the network adapter employs the strict priority TSA, it selects packets for transmission based solely on the packet's specified IEEE 802.1p priority level. As a result, packets with higher priority levels are always transmitted before packets with lower priority levels.

The miniport driver specifies its support for the strict priority TSA by setting NDIS\_QOS\_CAPABILITIES\_STRICT\_TSA\_SUPPORTED in the **Flags** member of the [**NDIS\_QOS\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_qos_capabilities) structure. The driver uses this structure to register its NDIS QoS and DCB capabilities in the call to [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes).

For more information about priority levels, see [IEEE 802.1p Priority Levels](ieee-802-1p-priority-levels.md).

**Note**  Starting with NDIS 6.30, the miniport driver that supports NDIS Quality of Service (QoS) for the DCB interface must advertise support for the strict priority TSA.

 

 

