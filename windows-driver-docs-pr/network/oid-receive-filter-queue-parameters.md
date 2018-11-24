---
title: OID_RECEIVE_FILTER_QUEUE_PARAMETERS
description: Overlying drivers issue object identifier (OID) method requests of OID_RECEIVE_FILTER_QUEUE_PARAMETERS to obtain the current configuration parameters of a receive queue.
ms.assetid: f6cd7896-0811-4029-b1d8-8cf800d7813e
ms.date: 08/08/2017
keywords: 
 -OID_RECEIVE_FILTER_QUEUE_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS


Overlying drivers issue object identifier (OID) method requests of OID\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS to obtain the current configuration parameters of a receive queue. The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_RECEIVE\_QUEUE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567211) structure with a queue identifier of type **NDIS\_RECEIVE\_QUEUE\_ID**. After a successful return from the OID method request, the **InformationBuffer** member of the **NDIS\_OID\_REQUEST** structure contains a pointer to an **NDIS\_RECEIVE\_QUEUE\_PARAMETERS** structure.

Overlying drivers issue OID set requests of OID\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS to change the current configuration parameters of a queue. The overlying driver provides a pointer to an [**NDIS\_RECEIVE\_QUEUE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567211) structure in the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure.

Remarks
-------

Overlying drivers issue OID set requests of OID\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS to change the parameters of one or more receive queues. The OID set request is optional for NDIS 6.20 and later miniport drivers. However, the OID request is mandatory for miniport drivers that support the virtual machine queue (VMQ) interface.

**Note**  Only the overlying driver that allocated the queue can change the configuration parameters by issuing OID set requests of OID\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS.

 

The overlying driver obtained the queue identifier input value from an earlier [OID\_RECEIVE\_FILTER\_ALLOCATE\_QUEUE](oid-receive-filter-allocate-queue.md) method OID request.

After the overlying driver allocates a queue, it can change the configuration parameters that have a corresponding change flag (NDIS\_RECEIVE\_QUEUE\_PARAMETER\_*Xxx*\_CHANGED) in the **Flags** member of the [**NDIS\_RECEIVE\_QUEUE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567211) structure. However, after the queue has been allocated, the overlying driver cannot change the configuration parameters that do not have a corresponding change flag.

### Return Status Codes

NDIS handles the OID method request of OID\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS for miniport drivers, and returns one of the following status codes.

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
<td><p>The request completed successfully.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_PENDING</strong></p></td>
<td><p>The request is pending completion. NDIS will pass the final status code and results to the OID request completion handler of the caller after the request has completed.</p></td>
</tr>
<tr class="odd">
<td><p><strong>NDIS_STATUS_INVALID_LENGTH</strong></p></td>
<td><p>The information buffer was too short. NDIS set the <strong>DATA</strong>.<strong>METHOD_INFORMATION</strong>.<strong>BytesNeeded</strong> member in the NDIS_OID_REQUEST structure to the minimum buffer size that is required.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_INVALID_PARAMETER</strong></p></td>
<td><p>The request failed because it tried to enable a capability that the underlying network adapter does not support.</p></td>
</tr>
<tr class="odd">
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


[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_RECEIVE\_QUEUE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567211)

[OID\_RECEIVE\_FILTER\_ALLOCATE\_QUEUE](oid-receive-filter-allocate-queue.md)

[OID\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS](oid-receive-filter-queue-parameters.md)

 

 




