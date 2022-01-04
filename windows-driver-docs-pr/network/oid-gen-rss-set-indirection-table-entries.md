---
title: OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES
description: This topic describes OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES
keywords: OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES, OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES RSSv2
ms.date: 10/11/2017
---

# OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES

[!include[RSSv2 Beta Prerelease](../includes/rssv2-beta-prerelease.md)]

The OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES OID is sent to [RSSv2](receive-side-scaling-version-2-rssv2-.md)-capable miniport drivers to perform moves of individual indirection table entries. This OID is a [Synchronous OID](synchronous-oid-request-interface-in-ndis-6-80.md), meaning it cannot return NDIS_STATUS_PENDING. It is issued as a Method request only, at IRQL == DISPATCH_LEVEL. 

This call uses the *XxxSynchronousOidRequest* entry point, where *Xxx* is either *Miniport* or *Filter* depending on the type of driver receiving the request. This entry point causes a system bug check if it sees an NDIS_STATUS_PENDING return status.

OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES uses the [NDIS_RSS_SET_INDIRECTION_ENTRIES](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_rss_set_indirection_entries) structure to instruct a miniport adapter to synchronously perform a set of actions, where each action moves a single entry of the RSS indirection table of a specified VPort to a target specified CPU.

## Remarks

This OID must execute and complete in the processor context that issued it. Miniport drivers must fully execute this OID upon returning NDIS_STATUS_SUCCESS to the upper layer. This means that the miniport driver should be prepared to receive back-to-back OID requests to move multiple ITEs on a new processor immediately after the first move finishes with NDIS_STATUS_SUCCESS. 

> [!TIP]
> Fully executing this OID means that the miniport driver must be ready to successfully attempt another action to move an ITE. It does not prescribe where in-flight receive traffic is indicated right after the queue move, which can either be on the source CPU or the target CPU.

Upper layer protocols issue OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES to set ITEs and/or the primary and default processor parameters to point to different processors. 

This OID can be issued for either *active* or *inactive* traffic steering parameters. For more information about steering parameters, see [Receive side scaling version 2 (RSSv2)](receive-side-scaling-version-2-rssv2-.md). For parameters/ITEs in the *inactive* state, the miniport driver should validate and cache the target processor until the next relevant RSS state change (enablement or disablement). At that point, cached processor numbers become *active* and are used for directing the traffic. Updates to *active* parameters (which must also be validated) should be taken immediately into effect to direct the traffic.

OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES must be issued to a miniport adapter with the *NDIS_OID_REQUEST_FLAGS_VPORT_ID_VALID* flag cleared. This is because of the possibility of different VPorts being referenced by different elements in the array.

This OID is invoked only at IRQL == DISPATCH_LEVEL.

Miniport drivers should be prepared to handle at least as many indirection table entry move actions as they advertise in the [NDIS_NIC_SWITCH_CAPABILITIES](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_capabilities) structure. This is defined in the **NumberOfIndirectionTableEntriesPerNonDefaultVPort** or **NumberOfIndirectionTableEntriesForDefaultVPort** member of that structure, or **128** in Native RSS mode.

Miniport drivers should attempt to execute as many entries as they can and update the **EntryStatus** member of each [NDIS_RSS_SET_INDIRECTION_ENTRY](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_rss_set_indirection_entry) with the result of the operation.

### OID handler for OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES

The OID handler for OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES is expected to behave as follows:

- A return of NDIS_STATUS_PENDING is not permitted due to the OID's Synchronous call type.
- Finalize any incoming ITE moves that were destined for the current CPU (previously initiated on remote processors). 
- It is strongly recommended for miniport drivers to perform a full parameter validation pass. If not possible, perform one-by-one validation and execution of array entries. Miniport drivers should specifically check if all the referenced objects are valid:
    - Returning NDIS_STATUS_PENDING in the **EntryStatus** field for an ITE is not permitted.
    - The miniport adapter exists and is in a good state. Else, set the **EntryStatus** field of the entry to NDIS_STATUS_ADAPTER_NOT_FOUND, NDIS_STATUS_ADAPTER_NOT_READY, etc.
    - Each VPort exists and is in a good state. Else, set the **EntryStatus** field of the entry to NDIS_STATUS_INVALID_PORT, NDIS_STATUS_INVALID_PORT_STATE, etc.
    - Each indirection table entry index is within the configured range. This range is either 0xFFFF or is in the [0...NumberOfIndirectionTableEntries - 1] range set by the [OID_GEN_RECEIVE_SCALE_PARAMETERS_V2](oid-gen-receive-scale-parameters-v2.md) OID. The 0xFFFF and 0xFFFE entry indices have special meanings: 0xFFFF defines the default processor, while 0xFFFE defines the primary processor. On error, the handler sets the **EntryStatus** field of the entry to NDIS_STATUS_INVALID_PARAMETER.
    - The upper layer and the miniport driver expect that the ITE points to the current processor (actor CPU) before the move. In other words, the ITE cannot be redirected remotely. If this is not true, set the **EntryStatus** field of the entry to NDIS_STATUS_NOT_ACCEPTED.
    - All target processors are valid and are part of the miniport adapter's RSS set. Else, set the **EntryStatus** field of the entry to NDIS_STATUS_INVALID_DATA.
- Either subsequently or as part of the parameter validation pass, validate the resource situation. Validate that the number of queues to be used after a full batch move (evacuation) does not exceed the **NumberOfQueues** set in the [NDIS_RECEIVE_SCALE_PARAMETERS_V2](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_scale_parameters_v2) structure during an [OID_GEN_RECEIVE_SCALE_PARAMETERS_V2](oid-gen-receive-scale-parameters-v2.md) request. Otherwise, NDIS_STATUS_NO_QUEUES is returned. NDIS_STATUS_NO_QUEUES should be used for all conditions that represent a violation of the configured number of queues. NDIS_STATUS_RESOURCES should only be used to designate transient out-of-memory conditions.
- As part of resource checks, for each scaling entity (for example, VPort), the miniport driver must handle a condition when all ITEs that point to the currrent CPU are moved away from it..

If all of the above checks pass, the miniport driver should be able to unconditionally apply the new configuration and must set the **EntryStatus** field of each entry to NDIS_STATUS_SUCCESS.

In general, the handler for this OID should be very light weight. It should not call NDIS or operating system services other than for possible synchronization operations like spinlocks and [**NdisMConfigMSIXTableEntry**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismconfigmsixtableentry).

The miniport driver should not call NDIS to indicate status or PnP events.

The miniport driver should also not use receive/transmit complete indications in the context of this OID handler, as doing so leads to recursion. The upper layer can invoke this OID from the context of receive or transmit indications.

### Moving all indirection table entries

Miniport drivers should recognize and handle a special request that moves all indirection table entries away from the current CPU. Because RSSv2 operates with individual ITE moves, miniport drivers must guarantee the atomicity of the overall operation. If it encounters an error in the middle of a batch while processing the corresponding array of move commands, the miniport driver should revert all commands that were already performed and mark all commands as "failed" in the per-command **EntryStatus** field. The upper layer protocol always expects the "move all ITEs" batch to contain either all commands marked as "succeeded," or all commands marked as "failed," and it will assume that traffic obeys the resulting state (either before or after the move). If the upper layer sees only some entries marked as "failed," it will bug check the system and point to the miniport driver as the cause.

To aid the miniport driver's handling of the "move all ITEs" command, and to avoid deadlocks, upper layer protocols group move commands in the batch in pairs of **SwitchId + VPortId** fields, such that:

- Commands that the upper layer wants to be executed together, as part of the "move all" command, for the same VPort are placed consecutively in the overall batch.
- The miniport driver should not attempt to execute the overall command batch, which may target different VPorts, in a "move all" fashion. Only the group of commands that target the same VPort (tagged with the same **SwitchId + VPortId** pair) need to be executed conforming to the "move all" semantics.
- When the upper layer does not care about "move all" semantics, it might interleave commands to the same VPort with commands to different VPort(s). In this case, if the second group of commands to the same VPort can't be executed because of a "number of queues" violation, the miniport driver marks that group with the corresponding status code (NDIS_STATUS_NO_QUEUES) and the upper layer takes responsibility for recovering.

For example, if the upper layer protocol interleaves a series of commands like this:

- `VPort=1 ITE[0,1]`
- `VPort=2 ITE[0]`
- `VPort=1 ITE[2]`

The miniport driver does not need to attempt to atomically execute all four move commands, or all three move commands for `VPort=1` (`ITE[0,1,2]`). It only needs to execute the `VPort=1 ITE[0,1]` group in a "move all" fashion, then the `VPort=2 ITE[0]` group, then `VPort=1 ITE[2]`. All three command groups might have a different outcome. For example, the groups for `VPort=1 ITE[0,1]` and `VPort=2 ITE[0]` might succeed, and the `VPort=1 ITE[2]` group might fail. The outcome should be reflected in the corresponding **EntryStatus** member of each command structure. This way, the miniport driver does not need to take precautions for safe execution of the overall batch (for example, lock the whole adapter). Only those commands that target a specific VPort need to be serialized, finer-grained per-VPort locking can be used, and certain deadlocks are avoided.

> [!NOTE]
> The entire group of the command entries must be marked with the same entry status.

### Error conditions and status codes

This OID returns the following status codes when an error occurs:

| Status code | Error condition |
| --- | --- |
| NDIS_STATUS_INVALID_LENGTH | The OID was malformed. |
| NDIS_STATUS_INVALID_PARAMETER | Other fields, either in the header or in the OID itself (but not in individual command entries) contain invalid values. |

## Requirements

**Version**: Windows 10, version 1709
**Header**: Ntddndis.h (include Ndis.h)

## See also

- [Receive Side Scaling Version 2 (RSSv2)](receive-side-scaling-version-2-rssv2-.md)
- [NDIS_RSS_SET_INDIRECTION_ENTRIES](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_rss_set_indirection_entries)
- [NDIS_RSS_SET_INDIRECTION_ENTRY](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_rss_set_indirection_entry)
- [NDIS_NIC_SWITCH_CAPABILITIES](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_capabilities)
- [OID_GEN_RECEIVE_SCALE_PARAMETERS_V2](oid-gen-receive-scale-parameters-v2.md)
- [NDIS_RECEIVE_SCALE_PARAMETERS_V2](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_scale_parameters_v2)
