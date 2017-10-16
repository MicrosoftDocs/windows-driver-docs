---
title: Receive Side Scaling Version 2 (RSSv2)
description: This topic describes Receive Side Scaling Version 2 (RSSv2)
ms.assetid: 192CAA41-0D17-4C06-8F13-68EA7C26D023
keywords: Receive Side Scaling Version 2, RSSv2, Receive Side Scaling Version 2 WDK, RSSv2 network drivers
ms.author: windowsdriverdev
ms.date: 10/12/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

[!include[RSSv2 Beta Prerelease](../rssv2-beta-prerelease.md)]

# Receive Side Scaling Version 2 (RSSv2)

[Receive Side Scaling](ndis-receive-side-scaling2.md) improves the system performance related to handling of network data on multiprocessor systems. NDIS 6.80 and later support RSS Version 2 (RSSv2), which extends RSS by offering dynamic, per-VPort spreading of queues.

RSSv2 uses the NDIS 6.80 Synchronous OID request interface for some of its OIDs. For more info about Synchronous OID calls, see [Synchronous OID request interface](synchronous-oid-request-interface-in-ndis-6-80.md).

## Overview

Compared to RSSv1, RSSv2 shortens the time between the measurement of CPU load and updating the indirection table. This avoids slowdown during high-traffic situations. To accomplish this, RSSv2 performs its actions at IRQL = DISPATCH_LEVEL, in the processor context of handling the request, and only operates on a subset of indirection table entries that point to the current processor. This means that RSSv2 can dynamically spread receive queues over multiple processors much more responsively than RSSv1.

Two new OIDs, [OID_GEN_RECEIVE_SCALE_PARAMETERS_V2](oid-gen-receive-scale-parameters-v2.md) and [OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES](oid-gen-rss-set-indirection-table-entries.md), have been introduced in RSSv2 for miniport drivers to set proper RSS capabilities and control the indirection table respectively. OID_GEN_RECEIVE_SCALE_PARAMETERS_V2 is a Regular OID, while OID_GEN_RSS_SET_INDIRECTION_ENTRIES is a Synchronous OID that cannot return NDIS_STATUS_PENDING. For more info about these OIDs, see their individual reference pages. For more info about Synchronous OIDs, see [Synchronous OID request interface in NDIS 6.80](synchronous-oid-request-interface-in-ndis-6-80.md).

## RSSv2 terminology

- RSSv2: The receive side scaling mechanism supported in Windows 10, version 1709 and later, described in this topic.
- Scaling entity: The miniport adapter itself in Native RSS mode, or a VPort in RSSv2 mode.
- ITE: An indirection table entry of a given scaling entity. The total number of ITEs per VPort cannot exceed **NumberOfIndirectionTableEntriesPerNonDefaultPFVPort** or **NumberOfIndirectionTableEntriesForDefaultVPort** in VMQ mode or 128 in the Native RSS case. **NumberOfIndirectionTableEntriesPerNonDefaultPFVPort** and **NumberOfIndirectionTableEntriesForDefaultVPort** are members of the [NDIS_NIC_SWITCH_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff566583) structure.
- Scaling mode: The per-VPort vmswitch policy which controls how its ITEs are handled at runtime. This can be static (no ITE moves due to load changes) or dyanmic (expansion and coalescing depending on current traffic load).
- Queue: An underlying hardware object (queue) that backs the ITE. Depending on the hardware and indirection table, the configuration queue may back multiple ITEs. The total number of queues, including one that is used by the default queue, cannot exceed the preconfigured limit typically set by an administrator.
- Default queue: A queue which receives packets for which the hash cannot be calculated. Each VPort has a default queue.
- Primary processor: A processor specified as the **ProcessorAffinity** member of the [NDIS_NIC_SWITCH_VPORT_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451597) structure during VPort creation.
- Source CPU: The processor to which the ITE is currently mapped.
- Target CPU: The processor to which the ITE is being re-mapped (using RSSv2).
- Actor CPU: The processor on which RSSv2 requests are being made.

## Advertising RSSv2 capability in a miniport driver

Miniport drivers advertise RSSv2 support by setting the **CapabilitiesFlags** member of the [NDIS_RECEIVE_SCALE_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff567220) structure with the new *NDIS_RSS_CAPS_SUPPORTS_INDEPENDENT_ENTRY_MOVE* flag. This capability is required to enable RSSv2's Dynamic VMQ feature, along with the *NDIS_RECEIVE_FILTER_DYNAMIC_PROCESSOR_AFFINITY_CHANGE_SUPPORTED* flag that enables the older RSSv1 Dynamic VMQ feature for non-default VPorts (VMQs).

If a miniport adapter does not advertise RSSv2 capability, all VMQ-enabled VPorts will stay in static spreading mode even if these VPorts are requested to perform dynamic spreading. The old RSSv1 OID for configuration of RSS parameters, [OID_GEN_RECEIVE_SCALE_PARAMETERS](oid-gen-receive-scale-parameters.md), will be used for these VPorts that are still in static spreading mode.

Miniport drivers only need to implement one RSS control mechanism - either RSSv1 or RSSv2. If the driver advertises RSSv2 support, NDIS will convert RSSv1 OIDs to RSSv2 OIDs if necessary to congifure per-VPort spreading. The miniport driver must support the two new OIDs (OID_GEN_RECEIVE_SCALS_PARAMETERS_V2 and OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES) and modify the behavior of the older OID_GEN_RECEIVE_SCALE_PARAMETERS OID, which will be used only for Query requests in RSSv2 and not for setting RSS parameters.

## Handling RSSv2 OIDs

[OID_GEN_RECEIVE_SCALE_PARAMETERS_V2](oid-gen-receive-scale-parameters-v2.md) is a Regular OID and is handled the same as the older [OID_GEN_RECEIVE_SCALE_PARAMETERS](oid-gen-receive-scale-parameters.md) OID was in RSSv1. [OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES](oid-gen-rss-set-indirection-table-entries.md), however, is a Synchronous OID that cannot return NDIS_STATUS_PENDING. For more details for handling this OID, see its reference page.

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")