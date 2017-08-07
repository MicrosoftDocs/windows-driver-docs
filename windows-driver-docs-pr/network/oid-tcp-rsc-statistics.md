---
title: OID\_TCP\_RSC\_STATISTICS
author: windows-driver-content
description: As a query, NDIS and overlying drivers or user-mode applications use the OID\_TCP\_RSC\_STATISTICS OID to get the receive-segment coalescing (RSC) statistics of a miniport adapter.
ms.assetid: CD289868-1925-4222-8A4D-359118124325
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_TCP_RSC_STATISTICS Network Drivers Starting with Windows Vista
---

# OID\_TCP\_RSC\_STATISTICS


As a query, NDIS and overlying drivers or user-mode applications use the OID\_TCP\_RSC\_STATISTICS OID to get the receive-segment coalescing (RSC) statistics of a miniport adapter.

NDIS 6.30 and later miniport drivers that provide RSC services must support this OID. Otherwise, this OID is optional.

Remarks
-------

The **InformationBuffer** member of [**NDIS\_OID\_REQUEST**](ndis-oid-request.md) structure contains an [**NDIS\_RSC\_STATISTICS\_INFO**](ndis-rsc-statistics-info.md) structure.

The miniport driver must maintain the statistics in the members of the [**NDIS\_RSC\_STATISTICS\_INFO**](ndis-rsc-statistics-info.md) structure as follows:

-   The driver must increment the coalesced packet count in the **CoalescedPkts** member by one every time a packet is added to a single coalesced unit (SCU).
-   The driver must increment the coalesced octet count in the **CoalescedOctets** member by the size of the TCP payload of the packet every time a packet is added to a SCU.
-   The driver must increment the coalesced events count **CoalesceEvents** member by one every time a SCU is finalized. All such SCUs should have a non-zero **CoalescedSegCount** value.
-   The driver must increment the abort count in the **Aborts** member by one every time it encounters an exception other than the IP datagram length being exceeded. This count should include the cases where a packet is not coalesced because of hardware resources.

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
<td><p>Supported for NDIS 6.30 and later drivers in Windows 8.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_OID\_REQUEST**](ndis-oid-request.md)

[**NDIS\_RSC\_STATISTICS\_INFO**](ndis-rsc-statistics-info.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_TCP_RSC_STATISTICS%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


