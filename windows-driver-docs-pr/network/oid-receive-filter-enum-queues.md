---
title: OID\_RECEIVE\_FILTER\_ENUM\_QUEUES
author: windows-driver-content
description: Overlying drivers and user-mode applications issue object identifier (OID) query requests of OID\_RECEIVE\_FILTER\_ENUM\_QUEUES to obtain a list of all the receive queues that are allocated on a network adapter.
ms.assetid: e8a946a2-9ee9-42a0-8175-fbc592d404d1
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_RECEIVE_FILTER_ENUM_QUEUES Network Drivers Starting with Windows Vista
---

# OID\_RECEIVE\_FILTER\_ENUM\_QUEUES


Overlying drivers and user-mode applications issue object identifier (OID) query requests of OID\_RECEIVE\_FILTER\_ENUM\_QUEUES to obtain a list of all the receive queues that are allocated on a network adapter.

After a successful return from the OID query request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](ndis-oid-request.md) structure contains a pointer to an [**NDIS\_RECEIVE\_QUEUE\_INFO\_ARRAY**](ndis-receive-queue-info-array.md) structure that is followed by an [**NDIS\_RECEIVE\_QUEUE\_INFO**](ndis-receive-queue-info.md) structure for each filter.

Remarks
-------

NDIS obtained the information from an internal cache of the data that it received from the [OID\_RECEIVE\_FILTER\_ALLOCATE\_QUEUE](oid-receive-filter-allocate-queue.md) and [OID\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS](oid-receive-filter-queue-parameters.md) OID requests.

Overlying drivers and user-mode applications issue OID query requests of OID\_RECEIVE\_FILTER\_ENUM\_QUEUES to enumerate the receive queues on a network adapter.

If a protocol driver issues the request, the request type inside the [**NDIS\_OID\_REQUEST**](ndis-oid-request.md) structure is set to **NdisRequestQueryInformation** and this OID returns an array of all the receive queues that the protocol driver allocated on the network adapter. If a user-mode application issued the request, the request type inside the **NDIS\_OID\_REQUEST** structure is set to **NdisRequestQueryStatistics**, and this OID returns an array of information for all the receive queues on the network adapter.

### Return Status Codes

NDIS handles the OID query request of OID\_RECEIVE\_FILTER\_ENUM\_QUEUES for miniport drivers, and returns one of the following status codes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Status code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>NDIS_STATUS_SUCCESS</strong></p></td>
<td><p>The request completed successfully. The <strong>InformationBuffer</strong> points to an [<strong>NDIS_RECEIVE_QUEUE_INFO_ARRAY</strong>](ndis-receive-queue-info-array.md) structure.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_PENDING</strong></p></td>
<td><p>The request is pending completion. NDIS will pass the final status code and results to the OID request completion handler of the caller after the request has completed.</p></td>
</tr>
<tr class="odd">
<td><p><strong>NDIS_STATUS_INVALID_LENGTH</strong></p></td>
<td><p>The information buffer was too short. NDIS set the <strong>DATA</strong>.<strong>METHOD_INFORMATION</strong>.<strong>BytesNeeded</strong> member in the [<strong>NDIS_OID_REQUEST</strong>](ndis-oid-request.md) structure to the minimum buffer size that is required.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_FAILURE</strong></p></td>
<td><p>The request failed for other reasons.</p></td>
</tr>
</tbody>
</table>

 

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
<td><p>Supported in NDIS 6.20 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_OID\_REQUEST**](ndis-oid-request.md)

[**NDIS\_RECEIVE\_QUEUE\_INFO**](ndis-receive-queue-info.md)

[**NDIS\_RECEIVE\_QUEUE\_INFO\_ARRAY**](ndis-receive-queue-info-array.md)

[OID\_RECEIVE\_FILTER\_ALLOCATE\_QUEUE](oid-receive-filter-allocate-queue.md)

[OID\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS](oid-receive-filter-queue-parameters.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_RECEIVE_FILTER_ENUM_QUEUES%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


