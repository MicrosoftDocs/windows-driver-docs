---
title: OID_QOS_REMOTE_PARAMETERS
ms.topic: reference
description: An overlying driver issues an object identifier (OID) query request of OID_QOS_REMOTE_PARAMETERS to obtain the NDIS Quality of Service (QoS) parameters for a remote peer.
ms.date: 08/08/2017
keywords: 
 -OID_QOS_REMOTE_PARAMETERS Network Drivers Starting with Windows Vista
---

# OID\_QOS\_REMOTE\_PARAMETERS


An overlying driver issues an object identifier (OID) query request of OID\_QOS\_REMOTE\_PARAMETERS to obtain the NDIS Quality of Service (QoS) parameters for a remote peer. The miniport driver uses these remote QoS parameters to resolve its operational NDIS QoS parameters. The driver configures the network adapter with the operational parameters in order to perform QoS packet transmission.

After a successful return from the OID query request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to an [**NDIS\_QOS\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_qos_parameters) structure.

**Note**  This OID query request is valid only for miniport drivers that support the IEEE 802.1 Data Center Bridging (DCB) interface.

 

## Remarks

When NDIS handles the OID request of OID\_QOS\_REMOTE\_PARAMETERS successfully, it returns the remote NDIS QoS parameters that it had cached from the previous [**NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE**](./ndis-status-qos-remote-parameters-change.md) status indication that was issued by the miniport driver. The driver issues this status indication to report on the initial set of remote NDIS QoS parameters. The driver also issues this status indication whenever the remote NDIS QoS parameters change.

NDIS returns an [**NDIS\_QOS\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_qos_parameters) structure that is initialized in the following way:

-   If the miniport driver previously issued an [**NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE**](./ndis-status-qos-remote-parameters-change.md) status indication, NDIS caches the [**NDIS\_QOS\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_qos_parameters) data and returns this data for the OID query request of OID\_QOS\_REMOTE\_PARAMETERS.

-   If the miniport driver did not issue an [**NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE**](./ndis-status-qos-remote-parameters-change.md) status indication, NDIS returns an [**NDIS\_QOS\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_qos_parameters) structure with all the members (with the exception of the **Header** member) set to zero.

For more information on remote NDIS QoS parameters, see [Overview of NDIS QoS Parameters](./overview-of-ndis-qos-parameters.md).

### Return Status Codes

NDIS returns one of the following status codes.

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
<td><p>The miniport driver does not support the NDIS QoS interface.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The length of the information buffer is less than sizeof(<a href="/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_qos_parameters" data-raw-source="[&lt;strong&gt;NDIS_QOS_PARAMETERS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_qos_parameters)"><strong>NDIS_QOS_PARAMETERS</strong></a>). NDIS sets the <strong>DATA.QUERY_INFORMATION.BytesNeeded</strong> member in the <a href="/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
</tr>
<tr class="even">
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
[**NdisMOidRequestComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismoidrequestcomplete)

[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)

[**NDIS\_QOS\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_qos_capabilities)

[**NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE**](./ndis-status-qos-operational-parameters-change.md)

[**NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE**](./ndis-status-qos-remote-parameters-change.md)

[OID\_QOS\_PARAMETERS](oid-qos-parameters.md)

