---
title: OID_PACKET_COALESCING_FILTER_MATCH_COUNT
description: NDIS issues an OID query request of OID_PACKET_COALESCING_FILTER_MATCH_COUNT to obtain the number of packets that were cached, or coalesced, on the network adapter.
ms.assetid: 3325865D-A329-4562-8270-CC2F42043D48
ms.date: 08/08/2017
keywords: 
 -OID_PACKET_COALESCING_FILTER_MATCH_COUNT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_PACKET\_COALESCING\_FILTER\_MATCH\_COUNT


NDIS issues an OID query request of OID\_PACKET\_COALESCING\_FILTER\_MATCH\_COUNT to obtain the number of packets that were cached, or *coalesced*, on the network adapter. The network adapter coalesces received packets if the adapter is enabled for [NDIS packet coalescing](https://msdn.microsoft.com/library/windows/hardware/hh451601) and the packet matches a receive filter.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to a caller-allocated ULONG64 variable. Before a successful return from the query request, the driver updates the ULONG64 variable with the number of packets that have matched receive filters on the network adapter.

Remarks
-------

Starting with NDIS 6.30, drivers that support [NDIS packet coalescing](https://msdn.microsoft.com/library/windows/hardware/hh451601) must support OID query requests of OID\_PACKET\_COALESCING\_FILTER\_MATCH\_COUNT.

**Note**  Drivers that support the [single root I/O virtualization (SR-IOV)](https://msdn.microsoft.com/library/windows/hardware/hh440235) or [virtual machine queue (VMQ)](https://msdn.microsoft.com/library/windows/hardware/ff571035) interfaces are not required to support OID query requests of this OID.

 

A miniport driver that supports packet coalescing must increment a ULONG64 counter for each received packet that was coalesced on the network adapter. Packets are coalesced if they match a receive filter, which overlying drivers download to the miniport driver through OID method requests of [OID\_RECEIVE\_FILTER\_SET\_FILTER](oid-receive-filter-set-filter.md).

The driver returns the value of this counter when it handles an OID query request of OID\_PACKET\_COALESCING\_FILTER\_MATCH\_COUNT.

The miniport driver must not clear the counter after it handles the OID query request of OID\_PACKET\_COALESCING\_FILTER\_MATCH\_COUNT. The miniport driver must only clear the counter if the following conditions are true:

-   The miniport driver handles an OID set request of [OID\_PNP\_SET\_POWER](oid-pnp-set-power.md) to resume to a full-power state of NdisDeviceStateD0.

-   NDIS calls the miniport driver's [*MiniportResetEx*](https://msdn.microsoft.com/library/windows/hardware/ff559432) function to reset the underlying network adapter.

For more information about packet coalescing, see [NDIS Packet Coalescing](https://msdn.microsoft.com/library/windows/hardware/hh205393).

### Return status codes

The miniport driver returns one of the following status codes for the OID method request of OID\_PACKET\_COALESCING\_FILTER\_MATCH\_COUNT:

<a href="" id="ndis-status-success"></a>NDIS\_STATUS\_SUCCESS  
The OID request completed successfully.

<a href="" id="ndis-status-invalid-length"></a>NDIS\_STATUS\_INVALID\_LENGTH  
The information buffer was too short. The driver sets the **DATA.SET\_INFORMATION.BytesNeeded** member in the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure to the minimum buffer size that is required.

<a href="" id="ndis-status-failure"></a>NDIS\_STATUS\_FAILURE  
The request failed for other reasons.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.30 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[*MiniportResetEx*](https://msdn.microsoft.com/library/windows/hardware/ff559432)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[OID\_PNP\_SET\_POWER](oid-pnp-set-power.md)

[OID\_RECEIVE\_FILTER\_SET\_FILTER](oid-receive-filter-set-filter.md)

 

 




