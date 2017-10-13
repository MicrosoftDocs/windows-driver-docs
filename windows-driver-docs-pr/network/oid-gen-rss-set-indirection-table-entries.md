---
title: OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES
description: This topic describes OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES
ms.assetid: F59D861C-B7DB-4C28-8842-4FDBAE1B95F1
keywords: OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES, OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES RSSv2
ms.author: windowsdriverdev
ms.date: 10/11/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

[!include[RSSv2 Beta Prerelease](../rssv2-beta-prerelease.md)]

# OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES

The OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES OID is sent to RSSv2-capable miniport drivers to perform moves of individual indirection table entries. This OID is a [Synchronous OID](synchronous-oid-request-interface-in-ndis-6-80.md), meaning it cannot return NDIS_STATUS_PENDING. It is issued as a Method request only, at IRQL = DISPATCH_LEVEL. 

OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES uses the [NDIS_RSS_SET_INDIRECTION_ENTRIES](https://msdn.microsoft.com/library/windows/hardware/9AB69EC6-FE78-4242-89C7-D36AA16676BF) structure to instruct a miniport adapter to synchronously perform a set of actions, where each action moves a single entry of the RSS indirection table of a specified VPort to a target specified CPU.

## Remarks

This OID must execute and complete in the processor context that issued it. Miniport drivers must fully execute this OID upon returning NDIS_STATUS_SUCCESS to the upper layer. This means that the miniport driver should be prepared to receive back-to-back OID requests to move multiple ITEs on a new processor immediately after the first move finishes with NDIS_STATUS_SUCCESS. 

> [!TIP]
> Fully executing this OID means that the miniport driver must be ready to successfully attempt another action to move an ITE. It does not prescribe where in-flight receive traffic is indicated right after the queue move, which can either be on the source CPU or the target CPU.

OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES must be issued to a miniport adapter with the *NDIS_OID_REQUEST_FLAGS_VPORT_ID_VALID* flag cleared. This is because of the possibility of different VPorts being referenced by different elements in the array.

Miniport drivers should be prepared to handle at least as many indirection table entry move actions as they advertise in the [NDIS_NIC_SWITCH_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff566583) structure. This is defined in the **NumberOfIndirectionTableEntriesPerNonDefaultVPort** or **NumberOfIndirectionTableEntriesForDefaultVPort** member of that structure, or **128** in Native RSS mode.

Miniport drivers should attempt to execute as many entries as they can and update the **EntryStatus** member of each [NDIS_RSS_SET_INDIRECTION_ENTRY](https://msdn.microsoft.com/library/windows/hardware/4430E19F-C603-4C52-8FC8-C36197FD2996) with the result of the operation.

The OID handler for OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES is expected to behave as follows:

- A return of NDIS_STATUS_PENDING is not permitted due to the OID's Synchronous call type.
- Finalize any incoming ITE moves that were destined for the current CPU (previously initiated on remote processors). 
- Depending on locking schema, ideally perform a full parameter validation pass. If not possible, perform one-by-one validation and execution of array entries. Miniport drivers should specifically check if all the referenced objects are valid:
    - The miniport adapter exists and is in a good state. Else, set the **EntryStatus** field of the entry to NDIS_STATUS_ADAPTER_NOT_FOUND, NDIS_STATUS_ADAPTER_NOT_READY, etc.
    - Each VPort exists and is in a good state. Else, set the **EntryStatus** field of the entry to NDIS_STATUS_INVALID_PORT, NDIS_STATUS_INVALID_PORT_STATE, etc.
    - Each indirection table entry index is within the configured range. This range is either 0xFFFF or is in the [0...NumberOfIndirectionTableEntries - 1] range set by the [OID_GEN_RECEIVE_SCALE_PARAMETERS_V2](oid-gen-receive-scale-parameters-v2.md) OID. The 0xFFFF and 0xFFFE entry indices have special meanings: 0xFFFF defines the default queue, while 0xFFFE defines the primary processor. On error, the handler sets the **EntryStatus** field of the entry to NDIS_STATUS_INVALID_PARAMETER.
    - The upper layer and the miniport driver expect that the ITE points to the current processor (actor CPU) before the move. In other words, the ITE cannot be redirected remotely. If this is not true, set the **EntryStatus** field of the entry to NDIS_STATUS_NOT_ACCEPTED.
    - All target processors are valid and are part of the miniport adapter's RSS set. Else, set the **EntryStatus** field of the entry to NDIS_STATUS_INVALID_DATA.
- Either subsequently or as part of the parameter validation pass, validate the resource situation. Validate that the number of queues to be used after a full batch move (evacuation) does not exceed the **NumberOfQueues** set in the [NDIS_RECEIVE_SCALE_PARAMETERS_V2](https://msdn.microsoft.com/library/windows/hardware/96EAB6EE-BF9A-46AD-8DED-5D9BD2B6F219) structure during an [OID_GEN_RECEIVE_SCALE_PARAMETERS_V2](oid-gen-receive-scale-parameters-v2.md) request. Otherwise, NDIS_STATUS_RESOURCES is returned. 
    - As part of resource checks, for each scaling entity (for example, VPort), the miniport driver must handle a condition when all ITEs that point to the currrent CPU are moved away from it. To facilitate this, the upper layer will mark all entries of the evacuated VPort with a special *NDIS_SET_INDIRECTION_ENTRY_FLAG_EVACUATE* flag. This lets the miniport driver know that all ITEs of a given VPort are being moved away from the Actor CPU to a different target CPU (or set of target CPUs), while at the same time a new CPU is added to the indirection table. Therefore, the queue limit per VPort will not be violated after the move.

If all of the above checks pass, the miniport driver should be able to unconditionally apply the new configuration and must set the **EntryStatus** field of each entry to NDIS_STATUS_SUCCESS.

## Requirements

| | |
| --- | --- |
| Version | Windows 10, version 1709 |
| Header | Ntddndis.h (include Ndis.h) |

## See also

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")