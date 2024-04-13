---
title: OID_TCP_RSC_STATISTICS
ms.topic: reference
description: As a query, NDIS and overlying drivers or user-mode applications use the OID_TCP_RSC_STATISTICS OID to get the receive-segment coalescing (RSC) statistics of a miniport adapter.
ms.date: 08/08/2017
keywords: 
 -OID_TCP_RSC_STATISTICS Network Drivers Starting with Windows Vista
---

# OID\_TCP\_RSC\_STATISTICS


As a query, NDIS and overlying drivers or user-mode applications use the OID\_TCP\_RSC\_STATISTICS OID to get the receive-segment coalescing (RSC) statistics of a miniport adapter.

NDIS 6.30 and later miniport drivers that provide RSC services must support this OID. Otherwise, this OID is optional.

## Remarks

The **InformationBuffer** member of [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains an [**NDIS\_RSC\_STATISTICS\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_rsc_statistics_info) structure.

The miniport driver must maintain the statistics in the members of the [**NDIS\_RSC\_STATISTICS\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_rsc_statistics_info) structure as follows:

-   The driver must increment the coalesced packet count in the **CoalescedPkts** member by one every time a packet is added to a single coalesced unit (SCU).
-   The driver must increment the coalesced octet count in the **CoalescedOctets** member by the size of the TCP payload of the packet every time a packet is added to a SCU.
-   The driver must increment the coalesced events count **CoalesceEvents** member by one every time a SCU is finalized. All such SCUs should have a non-zero **CoalescedSegCount** value.
-   The driver must increment the abort count in the **Aborts** member by one every time it encounters an exception other than the IP datagram length being exceeded. This count should include the cases where a packet is not coalesced because of hardware resources.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported for NDIS 6.30 and later drivers in Windows 8.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)

[**NDIS\_RSC\_STATISTICS\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_rsc_statistics_info)

 

