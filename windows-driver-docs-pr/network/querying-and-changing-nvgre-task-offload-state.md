---
title: Querying and Changing NVGRE Task Offload State
description: This section describes how to query or change the current Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload state of an NVGRE-capable miniport driver.
ms.assetid: 2F493F35-0D6D-4D23-A5CD-FA3990B3EAB5
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Querying and Changing NVGRE Task Offload State


This section describes how to query or change the current [Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload](network-virtualization-using-generic-routing-encapsulation--nvgre--task-offload.md) state of an NVGRE-capable miniport driver. NVGRE task offload can be enabled by default, but it must not be operationally active by default. A NIC should not begin performing task offloads on encapsulated packets until this feature is enabled explicitly by an NDIS protocol or filter driver.

## Querying NVGRE Task Offload State


To query a miniport driver's current NVGRE task offload state, an NDIS protocol or filter driver uses the [OID\_TCP\_OFFLOAD\_CURRENT\_CONFIG](https://msdn.microsoft.com/library/windows/hardware/ff569805) OID request. This will return an [**NDIS\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566705) structure whose **EncapsulatedPacketTaskOffloadGre** member is an [**NDIS\_ENCAPSULATED\_PACKET\_TASK\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/jj991956) structure that contains **NDIS\_OFFLOAD\_SUPPORTED** if those offloads are currently enabled for GRE-encapsulated packets and **NDIS\_OFFLOAD\_NOT\_SUPPORTED** otherwise. NDIS handles this OID and does not pass it down to the miniport.

**Note**  To determine whether a miniport driver supports NVGRE task offload, use the [OID\_TCP\_OFFLOAD\_HARDWARE\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569806) OID request as described in [Determining the NVGRE Task Offload Capabilities of a Network Adapter](determining-the-nvgre-task-offload-capabilities-of-a-network-adapter.md).

 

## Changing NVGRE Task Offload State


An NDIS protocol or filter driver can enable or disable NVGRE task offload by issuing the [OID\_TCP\_OFFLOAD\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569807) OID request. This OID uses an [**NDIS\_OFFLOAD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566706) structure. In this structure, the **EncapsulatedPacketTaskOffload** member can have the following values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Term</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>NDIS_OFFLOAD_SET_NO_CHANGE</strong></p></td>
<td align="left"><p>The NVGRE task offload state is unchanged.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>NDIS_OFFLOAD_SET_ON</strong></p></td>
<td align="left"><p>Specify this flag to enable NVGRE task offload.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>NDIS_OFFLOAD_SET_OFF</strong></p></td>
<td align="left"><p>Specify this flag to disable NVGRE task offload.</p></td>
</tr>
</tbody>
</table>

 

After the miniport driver processes the [OID\_TCP\_OFFLOAD\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569807) OID request, it must issue an [**NDIS\_STATUS\_TASK\_OFFLOAD\_CURRENT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff567424) status indication with the updated offload state.

When a miniport driver receives a [OID\_TCP\_OFFLOAD\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569807) OID request in which the **NDIS\_OFFLOAD\_SET\_OFF** flag is specified, the driver should indicate any existing encapsulated packets that are partially processed for task offloads up the stack before completing the OID request.

Base task offloads for normal packets are enabled by existing OIDs such as [OID\_OFFLOAD\_ENCAPSULATION](https://msdn.microsoft.com/library/windows/hardware/ff569762) and [OID\_RECEIVE\_FILTER\_ALLOCATE\_QUEUE](https://msdn.microsoft.com/library/windows/hardware/ff569784). The **EncapsulatedPacketTaskOffload** member setting supplements these OIDs and instructs the NIC to also do these offloads for encapsulated packets.

 

 





