---
title: Receive Side Scaling Version 2 (RSSv2)
description: This topic describes Receive Side Scaling Version 2 (RSSv2)
keywords: Receive Side Scaling Version 2, RSSv2, Receive Side Scaling Version 2 WDK, RSSv2 network drivers
ms.date: 10/12/2017
---

# Receive Side Scaling Version 2 (RSSv2)

Receive Side Scaling improves the system performance related to handling of network data on multiprocessor systems. NDIS 6.80 and later support RSS Version 2 (RSSv2), which extends RSS by offering dynamic, per-VPort spreading of queues.

## Overview

Compared to RSSv1, RSSv2 shortens the time between the measurement of CPU load and updating the indirection table. This avoids slowdown during high-traffic situations. To accomplish this, RSSv2 performs its actions at IRQL = DISPATCH_LEVEL, in the processor context of handling the request, and only operates on a subset of indirection table entries that point to the current processor. This means that RSSv2 can dynamically spread receive queues over multiple processors much more responsively than RSSv1.

Two OIDs, [OID_GEN_RECEIVE_SCALE_PARAMETERS_V2](oid-gen-receive-scale-parameters-v2.md) and [OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES](oid-gen-rss-set-indirection-table-entries.md), have been introduced in RSSv2 for miniport drivers to set proper RSS capabilities and control the indirection table respectively. OID_GEN_RECEIVE_SCALE_PARAMETERS_V2 is a Regular OID, while OID_GEN_RSS_SET_INDIRECTION_ENTRIES is a Synchronous OID that cannot return NDIS_STATUS_PENDING. For more info about these OIDs, see their individual reference pages. For more info about Synchronous OIDs, see [Synchronous OID request interface in NDIS 6.80](synchronous-oid-request-interface-in-ndis-6-80.md).

## RSSv2 terminology

This topic uses the following terms:

| Term | Definition |
| --- | --- |
| RSSv1 | The first generation receive side scaling mechanism. Uses [OID_GEN_RECEIVE_SCALE_PARAMETERS](oid-gen-receive-scale-parameters.md). |
| RSSv2 | The second generation receive side scaling mechanism supported in Windows 10, version 1803 and later, described in this topic. |
| Scaling entity| The miniport adapter itself in Native RSS mode, or a VPort in RSSv2 mode. |
| ITE | An indirection table entry (ITE) of a given scaling entity. The total number of ITEs per VPort cannot exceed **NumberOfIndirectionTableEntriesPerNonDefaultPFVPort** or **NumberOfIndirectionTableEntriesForDefaultVPort** in VMQ mode or 128 in the Native RSS case. **NumberOfIndirectionTableEntriesPerNonDefaultPFVPort** and **NumberOfIndirectionTableEntriesForDefaultVPort** are members of the [NDIS_NIC_SWITCH_CAPABILITIES](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_capabilities) structure. |
| Scaling mode | The per-VPort vmswitch policy that controls how its ITEs are handled at runtime. This can be static (no ITE moves due to load changes) or dyanmic (expansion and coalescing depending on current traffic load). |
| Queue | An underlying hardware object (queue) that backs an ITE. Depending on the hardware and indirection table, the configuration queue may back multiple ITEs. The total number of queues, including one that is used by the default queue, cannot exceed the preconfigured limit typically set by an administrator. |
| Default processor | A processor that receives packets for which the hash cannot be calculated. Each VPort has a default processor.
| Primary processor | A processor specified as the **ProcessorAffinity** member of the [NDIS_NIC_SWITCH_VPORT_PARAMETERS](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vport_parameters) structure during VPort creation. This processor can be updated at runtime and specifies where VMQ traffic is directed. |
| Source CPU | The processor to which the ITE is currently mapped. |
| Target CPU | The processor to which the ITE is being re-mapped (using RSSv2). |
| Actor CPU | The processor on which RSSv2 requests are being made. |

## Advertising RSSv2 capability in a miniport driver

Miniport drivers advertise RSSv2 support by setting the **CapabilitiesFlags** member of the [NDIS_RECEIVE_SCALE_CAPABILITIES](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_scale_capabilities) structure with the *NDIS_RSS_CAPS_SUPPORTS_INDEPENDENT_ENTRY_MOVE* flag. This capability is required to enable RSSv2's CPU load balancing feature, along with the *NDIS_RECEIVE_FILTER_DYNAMIC_PROCESSOR_AFFINITY_CHANGE_SUPPORTED* flag that enables RSSv1 dynamic balancing for non-default VPorts (VMQs).

> [!NOTE]
> Upper layer protocols assume that the primary processor of the default VPort can be moved for RSSv2 miniport drivers.

If a miniport adapter does not advertise RSSv2 capability, all VMQ-enabled VPorts stay in static spreading mode even if these VPorts are requested to perform dynamic spreading. The RSSv1 OID for configuration of RSS parameters, [OID_GEN_RECEIVE_SCALE_PARAMETERS](oid-gen-receive-scale-parameters.md), is used for these VPorts that are still in static spreading mode.

Miniport drivers only need to implement one RSS control mechanism - either RSSv1 or RSSv2. If the driver advertises RSSv2 support, NDIS will convert RSSv1 OIDs to RSSv2 OIDs if necessary to configure per-VPort spreading. The miniport driver must support the two new OIDs and modify the behavior of the RSSv1 OID_GEN_RECEIVE_SCALE_PARAMETERS OID as follows:

- [OID_GEN_RECEIVE_SCALE_PARAMETERS](oid-gen-receive-scale-parameters.md) is used only for Query requests in RSSv2 and not for setting RSS parameters.
- [OID_GEN_RECEIVE_SCALE_PARAMETERS_V2](oid-gen-receive-scale-parameters-v2.md) is a Query and a Set OID used for configuring the scaling entity's parameters such as the number of queues, the number of ITEs, RSS enablement/disablement, and hash key updates.
- [OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES](oid-gen-rss-set-indirection-table-entries.md) is a Method OID used to perform modification of indirection table entries.

## Handling RSSv2 OIDs

[OID_GEN_RECEIVE_SCALE_PARAMETERS](oid-gen-receive-scale-parameters.md) is only used to query the current RSS parameters of a given scaling entity. In RSSv1, this OID is used to set parameters. For RSSv2-capable miniport drivers, NDIS automatically performs this role conversion for the driver and issues the following two OIDs to set parameters instead.

[OID_GEN_RECEIVE_SCALE_PARAMETERS_V2](oid-gen-receive-scale-parameters-v2.md) is a Regular OID and is handled the same as the OID_GEN_RECEIVE_SCALE_PARAMETERS OID was handled in RSSv1. This OID is not visible to NDIS light-weight filter drivers (LWFs) prior to NDIS 6.80.

[OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES](oid-gen-rss-set-indirection-table-entries.md), however, is a [Synchronous OID](synchronous-oid-request-interface-in-ndis-6-80.md) that cannot return NDIS_STATUS_PENDING. This OID must be executed and completed in the processor context which originated the OID. Like OID_GEN_RECEIVE_SCALE_PARAMETERS_V2, it is also not visible to NDIS LWFs prior to NDIS 6.80. LWFs in NDIS 6.80 and later are not permitted to delay this OID or move to another processor. Its payload contains an array of simple "move ITE" actions, each of which contains a command to move a single ITE for a scaling entity to a different target CPU. Elements of the array can reference different scaling entities (VPorts).

Each type of NDIS driver, miniport, filter, and protocol, have entry points to support the Synchronous OID request interface:

| NDIS driver type | Synchronous OID handler(s) | Function to originate Synchronous OIDs |
| --- | --- | --- |
| Miniport | [*MiniportSynchronousOidRequest*](/windows-hardware/drivers/ddi/ndis/nf-ndis-miniport_synchronous_oid_request) | N/A |
| Filter | <ul><li>[*FilterSynchronousOidRequest*](/windows-hardware/drivers/ddi/ndis/nf-ndis-filter_synchronous_oid_request)</li><li>[*FilterSynchronousOidRequestComplete*](/windows-hardware/drivers/ddi/ndis/nf-ndis-filter_synchronous_oid_request_complete)</li></ul> | [**NdisFSynchronousOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfsynchronousoidrequest) |
| Protocol | N/A | [**NdisSynchronousOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissynchronousoidrequest) |

## RSS state transitions, ITE updates, and primary/default processors

### Steering parameters

In RSSv2, different parameters are used to steer traffic to the correct CPU depending on the RSS state (enabled or disabled). When RSS is disabled, only the primary processor is used for directing traffic. When RSS is enabled, both the default processor and all ITEs are used for directing traffic. These *steering parameters* are labele as "active" or "inactive", summarized in the following table:

| Steering parameter | RSS disabled | RSS enabled |
| --- | --- | --- |
| Primary processor | Active | Inactive |
| Default processor | Inactive | Active |
| ITE[0..N] | Inactive | Active |

When a steering parameter is in the *active* state, it directs the traffic. From the moment of an RSS state transition that makes a parameter *inactive*, miniport drivers must track changes to the parameter until the reverse transition activates it again. This means that a miniport driver needs to track all updates to the default processor and indirection table entries while RSS is disabled for that scaling entity. When RSS is enabled, the current tracked state for the default processor and indirection table should take effect.

For example, consider the scenario when software vRSS is already enabled. In this case, the indirection table already exists in the upper layer protocol and is actively used by the upper layer's software spreading code. If, during hardware RSS enablement, all entries start pointing to the primary processor before the updates to *move* the indirection table entries are issued to and executed by the hardware, the primary processor might experience a short jam. If the miniport driver has tracked default processor and ITE information, it can direct traffic to where it is already expected by the upper layer.

Note that while miniport drivers must track all updates to inactive steering parameters, they should defer validation of those parameters until the RSS state change attempts to make these parameters *active*. For example, in the case of software spreading while hardware RSS is disabled, upper layer protocols can use any processor for spreading (including outside the adapter's RSS set). The upper layers ensure that, at the moment of RSS state transition, all *inactive* parameters are valid for the new RSS state. However, the miniport dirver should still validate the parameters and fail the RSS state transition if it discovers that any tracked *inactive* steering parameters are invalid.

### Initial state and updates to steering parameters

The following table describes the initial state of the scaling entity after creation (for example, after VPort creation), as well as how the parameters can be updated:

| Parameter | Description |
| --- | --- |
| Primary processor | <ul><li>Initialized with the **Affinity** processor specified during VPort creation.</li><li>Can be updated using the [OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES](oid-gen-rss-set-indirection-table-entries.md) OID with the **NDIS_RSS_SET_INDIRECTION_ENTRY_FLAG_PRIMARY_PROCESSOR** flag set.</li><li>Can be updated using the [OID_NIC_SWITCH_VPORT_PARAMETERS](oid-nic-switch-vport-parameters.md) OID with the **NDIS_NIC_SWITCH_VPORT_PARAMS_PROCESSOR_AFFINITY_CHANGED** flag set (this is the compatibility path for existing cmdlet's).</li><li>Can be read using the [OID_NIC_SWITCH_VPORT_PARAMETERS](oid-nic-switch-vport-parameters.md) OID with the **NDIS_NIC_SWITCH_VPORT_PARAMS_PROCESSOR_AFFINITY_CHANGED** flag (this is the compatibility path for existing cmdlet's).</li><li>Post-initialization moves of the primary processor do not affect the default processor or the contents of the indirection table.</li></ul> |
| Default processor | <ul><li>Initialized with the **Affinity** processor specified during VPort creation.</li><li>Can be updated using the [OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES](oid-gen-rss-set-indirection-table-entries.md) OID with the **NDIS_RSS_SET_INDIRECTION_ENTRY_FLAG_DEFAULT_PROCESSOR** flag set.</li></ul> |
| Indirection table | <ul><li>**NumberOfIndirectionTableEntries** is set to **1**.</li><li>The only entry is initialized with the **Affinity** processor specified during VPort creation.</li><li>Can be updated using the [OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES](oid-gen-rss-set-indirection-table-entries.md) OID.</li></ul> |

Updates to ITEs and the primary/default processors (using OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES) is invoked from the processor to which the corresponding entry currently points. For a given VPort, the upper layer ensures that no OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES OIDs to move ITEs or set the primary/default processors will be issued in these circumstances:

1. While [OID_GEN_RECEIVE_SCALE_PARAMETERS_V2](oid-gen-receive-scale-parameters-v2.md) is in progress.
2. After the VPort deletion sequence is initiated. For example, the upper layer issues the set filter OID only after the last OID to move ITEs is completed.

### RSS disablement

During RSS disablement, the upper layer protocol might choose to either point all the ITEs to the primary processor, then issue the OID to disable RSS, or it might choose to leave the indirection table as-is and disable RSS. In either case, receive traffic should target the primary processor.

RSSv2 maintains a requirement from RSSv1 that permits the upper layer protocol to delete a VPort without first disabling RSS. The upper layer can set the receive filter on the VPort to zero, thus ensuring that no receive traffic flows through the VPort, then proceed with VPort deletion without disabling RSS. The upper layer guarantees that no OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES OIDs will be issued during or after VPort deletion.

During both RSS disablement and VPort deletion, the miniport driver should take care of any pending internal operations that might exist because of previous queue moves.

### RSSv2 invariants

The upper layer protocol ensures that important invariants are not violated before performing management functions or ITE moves. For example:

1. Before reducing the number of queues, the upper layer ensures that the indirection table does not reference more processors than the new number of queues for a VPort.
2. The upper layer should not request an indirection table update that violates the currently configured number of queues for a VPort. The miniport driver should enforce this and return a failure.
3. Before changing the number of indirection table entries for VMMQ-RESTRICTED adapters, the upper layer ensures that the contents of the indirection table are normalized to the power of 2.

## Related links

[OID_GEN_RECEIVE_SCALE_PARAMETERS_V2](oid-gen-receive-scale-parameters-v2.md)

[OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES](oid-gen-rss-set-indirection-table-entries.md)

[Synchronous OID request interface in NDIS 6.80](synchronous-oid-request-interface-in-ndis-6-80.md)
