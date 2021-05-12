---
title: OID_NIC_SWITCH_CURRENT_CAPABILITIES
description: An overlying driver issues an object identifier (OID) query request of OID_NIC_SWITCH_CURRENT_CAPABILITIES to obtain the currently enabled hardware capabilities of the NIC switch in a network adapter.
ms.date: 08/08/2017
keywords: 
 -OID_NIC_SWITCH_CURRENT_CAPABILITIES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_NIC\_SWITCH\_CURRENT\_CAPABILITIES


An overlying driver issues an object identifier (OID) query request of OID\_NIC\_SWITCH\_CURRENT\_CAPABILITIES to obtain the currently enabled hardware capabilities of the NIC switch in a network adapter.

After a successful return from the OID query request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request) structure contains a pointer to an [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_capabilities) structure.

## Remarks

Starting with NDIS 6.20, miniport drivers supply the currently enabled NIC switch hardware capabilities on the network adapter when its [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function is called. The driver initializes an [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_capabilities) structure with the NIC switch hardware capabilities and sets the **CurrentNicSwitchCapabilities** member of the [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_hardware_assist_attributes) structure to a pointer to the **NDIS\_NIC\_SWITCH\_CAPABILITIES** structure. The miniport driver then calls the [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes) function and sets the *MiniportAttributes* parameter to a pointer to an **NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES** structure.

**Note**  Starting with NDIS 6.30, miniport drivers that support the single root I/O virtualization (SR-IOV) interface must register the enabled hardware capabilities of the NIC switch. Drivers register these capabilities by calling [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes).

 

Overlying protocol and filter drivers do not have to issue OID query requests of OID\_NIC\_SWITCH\_CURRENT\_CAPABILITIES. NDIS provides the currently enabled NIC switch hardware capabilities of a network adapter to these drivers in the following way:

-   NDIS reports the currently enabled NIC switch hardware capabilities of an underlying network adapter to overlying protocol drivers in the **NicSwitchCapabilities** member of the [**NDIS\_BIND\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_bind_parameters) structure during the bind operation.

-   NDIS reports the currently enabled NIC switch hardware capabilities of an underlying network adapter to overlying filter drivers in the **NicSwitchCapabilities** member of the [**NDIS\_FILTER\_ATTACH\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_filter_attach_parameters) structure during the attach operation.

### Return Status Codes

NDIS handles the OID query request of the OID\_NIC\_SWITCH\_CURRENT\_CAPABILITIES request for miniport drivers. The drivers will not be issued this OID request.

When NDIS handles the OID\_NIC\_SWITCH\_CURRENT\_CAPABILITIES request, it returns one of the following status codes:

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
<td><p>The request completed successfully. The <strong>InformationBuffer</strong> points to an <a href="/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_capabilities" data-raw-source="[&lt;strong&gt;NDIS_NIC_SWITCH_CAPABILITIES&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_capabilities)"><strong>NDIS_NIC_SWITCH_CAPABILITIES</strong></a> structure.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_NOT_SUPPORTED</p></td>
<td><p>The miniport driver either does not support the single root I/O virtualization (SR-IOV) interface or is not enabled to use the interface.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The length of the information buffer is less than sizeof(<a href="/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_capabilities" data-raw-source="[&lt;strong&gt;NDIS_NIC_SWITCH_CAPABILITIES&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_capabilities)"><strong>NDIS_NIC_SWITCH_CAPABILITIES</strong></a>). The miniport driver must set the <strong>DATA.QUERY_INFORMATION.BytesNeeded</strong> member in the <a href="/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
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
<td><p>Supported in NDIS 6.20 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_BIND\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_bind_parameters)

[**NDIS\_FILTER\_ATTACH\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_filter_attach_parameters)

[**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_hardware_assist_attributes)

[**NDIS\_NIC\_SWITCH\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_capabilities)

[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request)

