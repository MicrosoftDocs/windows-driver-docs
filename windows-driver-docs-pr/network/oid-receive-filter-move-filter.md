---
title: OID_RECEIVE_FILTER_MOVE_FILTER
description: An overlying driver issues an object identifier (OID) set request of OID_RECEIVE_FILTER_MOVE_FILTER to move a previously configured receive filter.
ms.date: 08/08/2017
keywords: 
 -OID_RECEIVE_FILTER_MOVE_FILTER Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_RECEIVE\_FILTER\_MOVE\_FILTER


An overlying driver issues an object identifier (OID) set request of OID\_RECEIVE\_FILTER\_MOVE\_FILTER to move a previously configured receive filter. Receive filters are moved from one virtual port (VPort) to a different VPort.

Overlying drivers issue this OID set request to the miniport driver for the network adapter's PCIe Physical Function (PF). This OID set request is required for PF miniport drivers that support the single root I/O virtualization (SR-IOV) interface.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_MOVE\_FILTER\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_move_filter_parameters) structure.

## Remarks

NDIS validates the members of the [**NDIS\_RECEIVE\_FILTER\_MOVE\_FILTER\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_move_filter_parameters) structure before it forwards the OID set request to the PF miniport driver.

The PF miniport driver must handle this OID set request atomically. The driver must be able to configure the network adapter to simultaneously remove the filter from a receive queue and VPort and set it on a different receive queue and VPort.

For more information, see [Moving a Receive Filter to a Virtual Port](./moving-a-receive-filter-to-a-virtual-port.md).

### Return Status Codes

The PF miniport driver returns one of the following status codes for the OID set request of OID\_RECEIVE\_FILTER\_MOVE\_FILTER.

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
<td><p>NDIS_STATUS_SUCCESS</p></td>
<td><p>The OID request completed successfully.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_NOT_SUPPORTED</p></td>
<td><p>The PF miniport driver either does not support the single root I/O virtualization (SR-IOV) interface or is not enabled to use the interface.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_INVALID_PARAMETER</p></td>
<td><p>One or more of the members of the <a href="/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_move_filter_parameters" data-raw-source="[&lt;strong&gt;NDIS_RECEIVE_FILTER_MOVE_FILTER_PARAMETERS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_move_filter_parameters)"><strong>NDIS_RECEIVE_FILTER_MOVE_FILTER_PARAMETERS</strong></a> structure have invalid values.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The length of the information buffer is less than sizeof(<a href="/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_move_filter_parameters" data-raw-source="[&lt;strong&gt;NDIS_RECEIVE_FILTER_MOVE_FILTER_PARAMETERS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_move_filter_parameters)"><strong>NDIS_RECEIVE_FILTER_MOVE_FILTER_PARAMETERS</strong></a>). The PF miniport driver must set the <strong>DATA.SET_INFORMATION.BytesNeeded</strong> member in the <a href="/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_FAILURE</p></td>
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
<td><p>Supported in NDIS 6.30 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


****
[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)

[**NDIS\_RECEIVE\_FILTER\_MOVE\_FILTER\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_move_filter_parameters)

