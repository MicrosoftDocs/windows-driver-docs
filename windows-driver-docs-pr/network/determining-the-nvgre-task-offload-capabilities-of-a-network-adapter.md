---
title: Determining the NVGRE Task Offload Capabilities of a Network Adapter
description: This section describes how to determine the NVGRE Task Offload capabilities of a network adapter
ms.date: 04/20/2017
---

# Determining the NVGRE Task Offload Capabilities of a Network Adapter


A miniport driver that supports [Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload](network-virtualization-using-generic-routing-encapsulation--nvgre--task-offload.md) reports this capability by means of the [**NDIS\_OFFLOAD**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_offload) structure that its [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function passes to [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes).

## Reporting NVGRE Task Offload Capability


In the [**NDIS\_OFFLOAD**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_offload) structure, the **Header** member must be set as follows:

-   The **Revision** member must be set to **NDIS\_OFFLOAD\_REVISION\_3**.
-   The **Size** member must be set to **NDIS\_SIZEOF\_NDIS\_OFFLOAD\_REVISION\_3**.

To report its support for NVGRE task offload, a miniport driver sets the following members in the [**NDIS\_ENCAPSULATED\_PACKET\_TASK\_OFFLOAD**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_encapsulated_packet_task_offload) structure, which is stored in the **EncapsulatedPacketTaskOffloadGre** member of the [**NDIS\_OFFLOAD**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_offload) structure that the miniport driver's [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function passes to [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes):

-   Set the **MaxHeaderSizeSupported** member to the maximum header size from the beginning of the packet to the beginning of the inner TCP or UDP payload (the last byte of TCP or UDP inner header) that the NIC must support for all of these task offloads. The protocol driver is expected to not offload processing of a packet whose combined encapsulation headers exceed this size.

    **Note**  256 bytes is a good default value that should cover all possible cases.

     

-   Set the other members to indicate which types of task offload the miniport driver supports for encapsulated packets. For a list of the flags that can be set for these members, see the Remarks section of [**NDIS\_ENCAPSULATED\_PACKET\_TASK\_OFFLOAD**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_encapsulated_packet_task_offload).

## Querying NVGRE Task Offload Capability


To determine whether a miniport driver supports NVGRE task offload, protocol and filter drivers can issue the [OID\_TCP\_OFFLOAD\_HARDWARE\_CAPABILITIES](./oid-tcp-offload-hardware-capabilities.md) OID request, which returns the [**NDIS\_OFFLOAD**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_offload) structure.

**Note**  To determine whether the miniport driver's NVGRE capability is currently enabled, use the [OID\_TCP\_OFFLOAD\_CURRENT\_CONFIG](./oid-tcp-offload-current-config.md) OID request as described in [Querying and Changing NVGRE Task Offload State](querying-and-changing-nvgre-task-offload-state.md).

 

**Note**  To enable or disable the miniport driver's NVGRE capability, use the [OID\_TCP\_OFFLOAD\_PARAMETERS](./oid-tcp-offload-parameters.md) OID request as described in [Querying and Changing NVGRE Task Offload State](querying-and-changing-nvgre-task-offload-state.md).

 

 

