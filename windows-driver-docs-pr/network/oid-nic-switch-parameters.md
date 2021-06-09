---
title: OID_NIC_SWITCH_PARAMETERS
description: An overlying driver issues an object identifier (OID) method request of OID_NIC_SWITCH_PARAMETERS to obtain the current configuration parameters of a specified NIC switch on a network adapter.
ms.date: 08/08/2017
keywords: 
 -OID_NIC_SWITCH_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_NIC\_SWITCH\_PARAMETERS


An overlying driver issues an object identifier (OID) method request of OID\_NIC\_SWITCH\_PARAMETERS to obtain the current configuration parameters of a specified NIC switch on a network adapter. NDIS handles these OID method requests for the miniport driver.

Overlying drivers issue an OID set request of OID\_NIC\_SWITCH\_PARAMETERS to set the configuration parameters of a specified NIC switch on a network adapter. These OID set requests are issued to the miniport driver of the network adapter's PCI Express (PCIe) Physical Function (PF). These OID set requests are required for PF miniport drivers that support the single root I/O virtualization (SR-IOV) interface.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to an [**NDIS\_NIC\_SWITCH\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_parameters) structure.

The overlying driver specifies the NIC switch for the OID method or set request by setting the **SwitchId** member of the [**NDIS\_NIC\_SWITCH\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_parameters) structure to the switch identifier. The overlying driver obtains the switch identifier through one of the following ways:

-   From a previous OID method request of [OID\_NIC\_SWITCH\_ENUM\_SWITCHES](oid-nic-switch-enum-switches.md).

-   From the **NicSwitchArray** member of the [**NDIS\_BIND\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_bind_parameters) structure. NDIS passes a pointer to this structure in the *BindParameters* parameter of the [*ProtocolBindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_bind_adapter_ex) function.

-   From the **NicSwitchArray** member of the [**NDIS\_FILTER\_ATTACH\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_filter_attach_parameters) structure. NDIS passes a pointer to this structure in the *AttachParameters* parameter of the [*FilterAttach*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_attach) function.

**Note**  Starting with Windows Server 2012, Windows supports only the default NIC switch on the network adapter. The **SwitchId** member of the [**NDIS\_NIC\_SWITCH\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_parameters) structure must be set to NDIS\_DEFAULT\_SWITCH\_ID.

 

## Remarks

The overlying driver issues OID\_NIC\_SWITCH\_PARAMETERS requests in the following way:

-   The overlying driver issues an OID method request of OID\_NIC\_SWITCH\_PARAMETERS to obtain the current parameters of a specified NIC switch. For more information, see [Querying the Parameters of a NIC Switch](./querying-the-parameters-of-a-nic-switch.md).

    **Note**  NDIS handles OID method requests of OID\_NIC\_SWITCH\_PARAMETERS for the PF miniport driver.

     

-   The overlying driver issues an OID set request of OID\_NIC\_SWITCH\_PARAMETERS to change the current parameters of a specified NIC switch. For more information, see [Setting the Parameters of a NIC Switch](./setting-the-parameters-of-a-nic-switch.md).

    **Note**  The PF miniport driver handles OID set requests of OID\_NIC\_SWITCH\_PARAMETERS.

     

### Return Status Codes

NDIS or the PF miniport driver returns the following status codes for set or method OID requests of OID\_NIC\_SWITCH\_PARAMETERS.

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
<td><p>The PF miniport driver either does not support the single root I/O virtualization (SR-IOV) interface or is not enabled to use the interface.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_INVALID_PARAMETER</p></td>
<td><p>One or more of the members of the <a href="/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_parameters" data-raw-source="[&lt;strong&gt;NDIS_NIC_SWITCH_PARAMETERS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_parameters)"><strong>NDIS_NIC_SWITCH_PARAMETERS</strong></a> structure have invalid values.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The information buffer was too short. NDIS or the PF miniport driver sets the <strong>DATA.METHOD_INFORMATION.BytesNeeded</strong> member (for OID method requests) or <strong>DATA.SET_INFORMATION.BytesNeeded</strong> member (for OID set requests) in the <a href="/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_REINIT_REQUIRED</p></td>
<td><p>The PF miniport driver requires a reinitialization of the network adapter to apply the changes to the NIC switch.</p></td>
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
[*FilterAttach*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_attach)

[**NDIS\_BIND\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_bind_parameters)

[**NDIS\_FILTER\_ATTACH\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_filter_attach_parameters)

[**NDIS\_NIC\_SWITCH\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_parameters)

[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)

[OID\_NIC\_SWITCH\_CREATE\_SWITCH](oid-nic-switch-create-switch.md)

[OID\_NIC\_SWITCH\_ENUM\_SWITCHES](oid-nic-switch-enum-switches.md)

[*ProtocolBindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_bind_adapter_ex)

