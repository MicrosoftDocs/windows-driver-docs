---
title: OID_NIC_SWITCH_ENUM_SWITCHES
ms.topic: reference
description: An overlying driver or user-mode application issues an object identifier (OID) query request of OID_NIC_SWITCH_ENUM_SWITCHES to obtain an array.
ms.date: 08/08/2017
keywords: 
 -OID_NIC_SWITCH_ENUM_SWITCHES Network Drivers Starting with Windows Vista
---

# OID\_NIC\_SWITCH\_ENUM\_SWITCHES


An overlying driver or user-mode application issues an object identifier (OID) query request of OID\_NIC\_SWITCH\_ENUM\_SWITCHES to obtain an array. Each element in the array specifies the attributes of a NIC switch that has been created on a network adapter.

After a successful return from this OID query request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to a buffer that contains the following:

-   An [**NDIS\_NIC\_SWITCH\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_info_array) structure that defines the number of elements within the array.

-   An array of [**NDIS\_NIC\_SWITCH\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_info) structures. Each of these structures contains the information about a single NIC switch created on the network adapter.

    **Note**  If the network adapter has no NIC switches, the driver sets the **NumElements** member of the [**NDIS\_NIC\_SWITCH\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_info_array) structure to zero and no [**NDIS\_NIC\_SWITCH\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_info) structures are returned.

     

## Remarks

Overlying drivers and user-mode applications issue OID query requests of OID\_NIC\_SWITCH\_ENUM\_SWITCHES to enumerate the NIC switches created on a network adapter.

**Note**  Starting with Windows Server 2012, the single root I/O virtualization (SR-IOV) interface only supports the default NIC switch on the network adapter. Therefore, the returned [**NDIS\_NIC\_SWITCH\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_info_array) structure must specify a single [**NDIS\_NIC\_SWITCH\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_info) element for the default NIC switch, which is referenced by the identifier of NDIS\_DEFAULT\_SWITCH\_ID.

 

### Return Status Codes

NDIS handles the OID query request of the OID\_NIC\_SWITCH\_ENUM\_SWITCHES request for miniport drivers. The drivers will not be issued this OID request.

When NDIS handles the OID\_NIC\_SWITCH\_ENUM\_SWITCHES request, it returns one of the following status codes.

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
<td><p>The miniport driver either does not support the SR-IOV interface or is not enabled to use the interface.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_INVALID_PARAMETER</p></td>
<td><p>One or more of the members of the <a href="/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_delete_vport_parameters" data-raw-source="[&lt;strong&gt;NDIS_NIC_SWITCH_INFO_ARRAY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_delete_vport_parameters)"><strong>NDIS_NIC_SWITCH_INFO_ARRAY</strong></a> structure have invalid values.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The information buffer was too short. NDIS sets the <strong>DATA.QUERY_INFORMATION.BytesNeeded</strong> member in the <a href="/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
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
[**NDIS\_NIC\_SWITCH\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_info)

[**NDIS\_NIC\_SWITCH\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_info_array)

[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)

[OID\_NIC\_SWITCH\_CREATE\_SWITCH](oid-nic-switch-create-switch.md)

[OID\_NIC\_SWITCH\_PARAMETERS](oid-nic-switch-parameters.md)

