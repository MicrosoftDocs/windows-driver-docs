---
title: OID_SWITCH_NIC_ARRAY
description: A Hyper-V extensible switch extension issues an object identifier (OID) query request of OID_SWITCH_NIC_ARRAY to obtain an array.
ms.date: 08/08/2017
keywords: 
 -OID_SWITCH_NIC_ARRAY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_SWITCH\_NIC\_ARRAY


A Hyper-V extensible switch extension issues an object identifier (OID) query request of OID\_SWITCH\_NIC\_ARRAY to obtain an array. Each element in the array specifies the configuration parameters of a virtual network adapter that is associated with an extensible switch port.

If the OID query request is completed successfully, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to a buffer. This buffer contains the following data:

-   An [**NDIS\_SWITCH\_NIC\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_array) structure that defines the number of elements in the array. This structure also specifies the offset to the first element in the array.

-   An array of [**NDIS\_SWITCH\_NIC\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_parameters) structures. Each of these structures contains information about a network adapter that is connected to an extensible switch port.

    **Note**  If no network adapters are connected to extensible switch ports, the underlying miniport edge of the extensible switch sets the **NumElements** member of the [**NDIS\_SWITCH\_NIC\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_array) structure to zero. In this case, no [**NDIS\_SWITCH\_NIC\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_parameters) structures are returned.

     

## Remarks

The OID\_SWITCH\_NIC\_ARRAY OID must only be issued when the Hyper-V extensible switch has completed activation. Please see [Querying the Hyper-V Extensible Switch Configuration](./querying-the-hyper-v-extensible-switch-configuration.md) for more details.

When the extension processes the returned [**NDIS\_SWITCH\_NIC\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_parameters) structure, it must not assume that the various string members of the [**NDIS\_SWITCH\_PORT\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_port_parameters) structure, such as **NicFriendlyName**, are NULL-terminated. The data types for these string members are type-defined by the [**IF\_COUNTED\_STRING**](/windows/win32/api/ifdef/ns-ifdef-if_counted_string_lh) structure. The driver must determine the string length from the value of the **Length** member of this structure.

**Note**  If the string is null-terminated, the **Length** member must not include the terminating null character.

 

### Return Status Codes

The underlying miniport edge of the extensible switch completes the OID query request of OID\_SWITCH\_NIC\_ARRAY and returns one of the following status codes.

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
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The length of the information buffer is too small to return the <a href="/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_array" data-raw-source="[&lt;strong&gt;NDIS_SWITCH_NIC_ARRAY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_array)"><strong>NDIS_SWITCH_NIC_ARRAY</strong></a> and its array of <a href="/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_parameters" data-raw-source="[&lt;strong&gt;NDIS_SWITCH_NIC_PARAMETERS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_parameters)"><strong>NDIS_SWITCH_NIC_PARAMETERS</strong></a> elements. The underlying miniport edge of the extensible switch sets the <strong>DATA.QUERY_INFORMATION.BytesNeeded</strong> member in the <a href="/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
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

[**NDIS\_SWITCH\_NIC\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_array)

[**NDIS\_SWITCH\_NIC\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_parameters)

[Querying the Hyper-V Extensible Switch Configuration](./querying-the-hyper-v-extensible-switch-configuration.md)

