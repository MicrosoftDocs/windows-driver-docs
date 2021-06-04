---
title: OID_GEN_ISOLATION_PARAMETERS
description: NDIS and overlying drivers issue an object identifier (OID) request of OID_GEN_ISOLATION_PARAMETERS to obtain the multi-tenancy configuration (isolation) parameters that are set on a VM network adapter's port.
ms.date: 08/08/2017
keywords: 
 -OID_GEN_ISOLATION_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_ISOLATION\_PARAMETERS


NDIS and overlying drivers issue an object identifier (OID) request of OID\_GEN\_ISOLATION\_PARAMETERS to obtain the multi-tenancy configuration (isolation) parameters that are set on a VM network adapter's port.

Although each routing domain is configured separately on the port, this OID returns parameters for all of the routing domains in a single query.

An overlying driver should issue this OID in two steps:

1.  Io query the required buffer size, issue the OID query with the **Size** member of the **Header** member of the [**NDIS\_ISOLATION\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_isolation_parameters) structure set to **NDIS\_SIZEOF\_NDIS\_ISOLATION\_PARAMETERS\_REVISION\_1**. (See **NDIS\_STATUS\_INVALID\_LENGTH** below.)
2.  Issue the OID with an **InformationBuffer** of the required size.

If the OID query request is completed successfully, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to a buffer. This buffer contains the following data, in order:

1.  An [**NDIS\_ISOLATION\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_isolation_parameters) structure

2.  One or more [**NDIS\_ROUTING\_DOMAIN\_ENTRY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_routing_domain_entry) structures, one for each routing domain

3.  One or more [**NDIS\_ROUTING\_DOMAIN\_ISOLATION\_ENTRY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_routing_domain_isolation_entry) structures, grouped by routing domain

In each [**NDIS\_ROUTING\_DOMAIN\_ENTRY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_routing_domain_entry) structure, the **FirstIsolationInfoEntryOffset** member contains the offset from the beginning of the OID information buffer (that is, the beginning of the buffer that the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure points to) to the first [**NDIS\_ROUTING\_DOMAIN\_ISOLATION\_ENTRY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_routing_domain_isolation_entry) for that routing domain. The offset in the **NextIsolationInfoEntryOffset** member of the last structure in the list is zero.

If no multi-tenancy configuration parameters are set on the VM network adapter, the network adapter miniport driver sets the **DATA.QUERY\_INFORMATION.BytesWritten** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure to zero and returns **NDIS\_STATUS\_SUCCESS**. In this case, the data within the **DATA.QUERY\_INFORMATION.InformationBuffer** member is not modified by the miniport driver.

## Remarks

### Return Status Codes

The VM network adapter miniport driver returns one of the following status codes for this OID request:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Status Code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>NDIS_STATUS_SUCCESS</strong></p></td>
<td><p>The OID request completed successfully.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_INVALID_LENGTH</strong></p></td>
<td><p>The length of the information buffer is too small to return the requested information. The VM network adapter miniport driver sets the <strong>DATA.METHOD_INFORMATION.BytesNeeded</strong> member in the <a href="/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size, in bytes, that is required.</p></td>
</tr>
<tr class="odd">
<td><p><strong>NDIS_STATUS_FAILURE</strong></p></td>
<td><p>The request failed for other reasons.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.40 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_ISOLATION\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_isolation_parameters)

[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)

[**NDIS\_ROUTING\_DOMAIN\_ENTRY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_routing_domain_entry)

[**NDIS\_ROUTING\_DOMAIN\_ISOLATION\_ENTRY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_routing_domain_isolation_entry)

[**NDIS\_STATUS\_ISOLATION\_PARAMETERS\_CHANGE**](ndis-status-isolation-parameters-change.md)

