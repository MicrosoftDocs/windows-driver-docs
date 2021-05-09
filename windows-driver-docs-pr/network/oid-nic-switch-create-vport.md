---
title: OID_NIC_SWITCH_CREATE_VPORT
description: An overlying driver issues an object identifier (OID) method request of OID_NIC_SWITCH_CREATE_VPORT to create a nondefault virtual port (VPort) on a network adapter's NIC switch.
ms.date: 08/08/2017
keywords: 
 -OID_NIC_SWITCH_CREATE_VPORT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_NIC\_SWITCH\_CREATE\_VPORT


An overlying driver issues an object identifier (OID) method request of OID\_NIC\_SWITCH\_CREATE\_VPORT to create a nondefault virtual port (VPort) on a network adapter's NIC switch. This OID method request also attaches the created VPort to the network adapter's PCI Express (PCIe) Physical Function (PF) or a previously allocated PCIe Virtual Function (VF).

Overlying drivers issue this OID method request to the miniport driver for the network adapter's PF. This OID method request is required for PF miniport drivers that support the single root I/O virtualization (SR-IOV) interface.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request) structure contains a pointer to the [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vport_parameters) structure.

## Remarks

The overlying driver initializes the [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vport_parameters) structure with the configuration information about the nondefault VPort to be created. The configuration information includes the PCIe function to which the nondefault VPort is attached and the number of queue pairs for the nondefault VPort.

When the PF miniport driver is issued the OID request, the driver allocates the hardware and software resources associated with the specified nondefault VPort. After all the resources are successfully allocated, the PF miniport driver completes the OID successfully by returning NDIS\_STATUS\_SUCCESS from [*MiniportOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request).

If the OID\_NIC\_SWITCH\_CREATE\_VPORT request completes successfully, the PF miniport driver and the overlying driver must retain the **VPortId** value of the nondefault VPort for successive operations. The **VPortId** value is used during these operations:

-   NDIS and the overlying drivers use the **VPortId** value to identify the nondefault VPort in successive OID requests related to this VPort, such as [OID\_NIC\_SWITCH\_VPORT\_PARAMETERS](oid-nic-switch-vport-parameters.md) and [OID\_NIC\_SWITCH\_DELETE\_VPORT](oid-nic-switch-delete-vport.md).

-   During send operations, NDIS specifies the **VPortId** value to identify the VPort from which a packet was sent. This value is specified within the out-of-band (OOB) [**NDIS\_NET\_BUFFER\_LIST\_FILTERING\_INFO**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_net_buffer_list_filtering_info) data of the [NET\_BUFFER\_LIST](./net-buffer-list-structure.md) structure.

-   During receive operations, the PF miniport driver specifies the **VPortId** value to which a packet is to be forwarded. This value is also specified in the OOB [**NDIS\_NET\_BUFFER\_LIST\_FILTERING\_INFO**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_net_buffer_list_filtering_info) data of the [NET\_BUFFER\_LIST](./net-buffer-list-structure.md) structure.

For more information, see [Creating a Virtual Port](./creating-a-virtual-port.md).

**Note**  The default VPort always exists and is not created though an OID request of OID\_NIC\_SWITCH\_CREATE\_VPORT. The default VPort has an identifier of NDIS\_DEFAULT\_VPORT\_ID. When the PF miniport driver creates a NIC switch, the driver automatically attaches the default VPort to the PF of the network adapter.

 

### Return Status Codes

NDIS or the PF miniport driver returns one of the following status codes for the OID method request of OID\_NIC\_SWITCH\_CREATE\_SWITCH.

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
<td><p>The PF miniport driver either does not support the SR-IOV interface or is not enabled to use the interface.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_INVALID_PARAMETER</p></td>
<td><p>One or more of the members of the <a href="/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vport_parameters" data-raw-source="[&lt;strong&gt;NDIS_NIC_SWITCH_VPORT_PARAMETERS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vport_parameters)"><strong>NDIS_NIC_SWITCH_VPORT_PARAMETERS</strong></a> structure have invalid values.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The length of the information buffer is less than sizeof(<a href="/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vport_parameters" data-raw-source="[&lt;strong&gt;NDIS_NIC_SWITCH_VPORT_PARAMETERS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vport_parameters)"><strong>NDIS_NIC_SWITCH_VPORT_PARAMETERS</strong></a>). The PF miniport driver must set the <strong>DATA.METHOD_INFORMATION.BytesNeeded</strong> member in the <a href="/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
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
[*MiniportOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request)

[**NDIS\_NIC\_SWITCH\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_parameters)

[**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vport_parameters)

[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request)

[NET\_BUFFER\_LIST](./net-buffer-list-structure.md)

[OID\_NIC\_SWITCH\_ALLOCATE\_VF](oid-nic-switch-allocate-vf.md)

[OID\_NIC\_SWITCH\_DELETE\_VPORT](oid-nic-switch-delete-vport.md)

[OID\_NIC\_SWITCH\_PARAMETERS](oid-nic-switch-parameters.md)

[OID\_NIC\_SWITCH\_VPORT\_PARAMETERS](oid-nic-switch-vport-parameters.md)

