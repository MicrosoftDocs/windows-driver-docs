---
title: Allocating VPorts for VMMQ
description: NDIS allocates VPorts when VMMQ is present.
ms.date: 02/28/2021
ms.localizationpriority: medium
---


# Allocating VPorts for VMMQ

NDIS allocates VPorts when the [Virtual Machine Multiple Queues (VMMQ)](overview-of-virtual-machine-multiple-queues.md) capability is present in the following way.

NDIS creates a non-default VPort on the miniport adapter by issuing the [OID\_NIC\_SWITCH\_CREATE\_VPORT](oid-nic-switch-create-vport.md) OID request. When creating an RSS physical function (PF) VPort, NDIS will initialize the [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vport_parameters) structure as follows:

- NDIS sets the **AttachedFunctionId** field to **NDIS\_PF\_FUNCTION\_ID**.

- If VMMQ is enabled, NDIS sets the **NumQueuePairs** field to the number of VMMQ queue pairs that should be used for this VPort. This number includes the default RSS processor for this VPort. It is guaranteed that total number of processors will not exceed this number. If VMMQ is disabled, NDIS sets this value to **one**.

- If VMMQ is enabled, the **ProcessorAffinity** field defines a bitmask of the potential RSS processors that the miniport adapter must use for this VPort. The processors that the network stack used to populate the indirection table entries for the VPort are a subset of the processors that this bitmask identifies. The mask will be a subset of the RSS processors returned from the call to [**NdisGetRssProcessorInformation**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisgetrssprocessorinformation) and the number of set bits might exceed the number of RSS queues requested for the VPort. If VMMQ is disabled, the miniport adapter must use the lowest processor number specified in this bitmask when setting the affinity of the VPort queue.

- NDIS sets the NDIS\_NIC\_SWITCH\_VPORT\_PARAMS\_NUM\_QUEUE\_PAIRS\_CHANGED flag to indicate that the **NumQueuePairs** member has been updated after the VPort has been created. When VMMQ is enabled, the number of queues for default and non-default VPorts can be updated. 