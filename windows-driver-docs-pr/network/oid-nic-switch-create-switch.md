---
title: OID_NIC_SWITCH_CREATE_SWITCH
description: NDIS issues an object identifier (OID) method request of OID_NIC_SWITCH_CREATE_SWITCH to create a NIC switch on a network adapter.
ms.date: 08/08/2017
keywords: 
 -OID_NIC_SWITCH_CREATE_SWITCH Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_NIC\_SWITCH\_CREATE\_SWITCH


NDIS issues an object identifier (OID) method request of OID\_NIC\_SWITCH\_CREATE\_SWITCH to create a NIC switch on a network adapter. When it handles this OID request, the miniport driver allocates the resources for the NIC switch on the adapter.

NDIS issues this OID method request to the miniport driver of the network adapter's PCI Express (PCIe) Physical Function (PF). This OID method request is required for PF miniport drivers that support the single root I/O virtualization (SR-IOV) interface.

**Note**  Overlying drivers, such as protocol or filter drivers, cannot issue OID method requests of OID\_NIC\_SWITCH\_CREATE\_SWITCH to the PF miniport driver.

 

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request) structure contains a pointer to an [**NDIS\_NIC\_SWITCH\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_parameters) structure.

## Remarks

When it receives the OID method request of OID\_NIC\_SWITCH\_CREATE\_SWITCH, the PF miniport driver must do the following:

1.  If the PF miniport driver supports static switch creation and configuration, it creates the NIC switch when NDIS calls [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize). When the driver handles this OID request, it must verify the configuration parameters in the [**NDIS\_NIC\_SWITCH\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_parameters) structure. The parameters must be the same as those used by the driver to create the switch during the call to *MiniportInitializeEx*. If this is not true, the driver must fail the OID request.

    For more information, see [Static Creation of a NIC Switch](./static-creation-of-a-nic-switch.md).

2.  If the PF miniport driver supports dynamic switch creation and configuration, the driver must validate the configuration values of the [**NDIS\_NIC\_SWITCH\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_parameters) structure and create the NIC switch based on these values.

    For more information, see [Dynamic Creation of a NIC Switch](./dynamic-creation-of-a-nic-switch.md).

3.  The PF miniport driver must allocate the necessary hardware and software resources for the default VPort on the NIC switch.

    **Note**  The default VPort is always created through an OID request of OID\_NIC\_SWITCH\_CREATE\_SWITCH and deleted through an OID request of [OID\_NIC\_SWITCH\_DELETE\_SWITCH](oid-nic-switch-delete-switch.md). OID requests of [OID\_NIC\_SWITCH\_CREATE\_VPORT](oid-nic-switch-create-vport.md) and [OID\_NIC\_SWITCH\_DELETE\_VPORT](oid-nic-switch-delete-vport.md) are used for the creation and deletion of nondefault VPorts on the NIC switch.

     

4.  The PF miniport driver that supports dynamic switch creation and configuration must enable SR-IOV virtualization on the switch by calling [**NdisMEnableVirtualization**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismenablevirtualization). This call configures the **NumVFs** member and the **VF Enable** bit in the SR-IOV Extended Capability structure of the adapter's PCI Express (PCIe) configuration space.

    For more information about the SR-IOV configuration space, see the PCI-SIG [Single Root I/O Virtualization and Sharing 1.1](https://go.microsoft.com/fwlink/p/?linkid=221742) specification.

    **Note**  If the PF miniport driver supports static switch creation, it enables SR-IOV virtualization after it creates the switch when [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) is called.

     

If the PF miniport driver successfully completes the OID method request of OID\_NIC\_SWITCH\_CREATE\_SWITCH, it allows the following to occur:

-   VFs can be allocated on the NIC switch through OID method requests of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](oid-nic-switch-allocate-vf.md).

-   Nondefault VPorts can be created on the NIC switch through OID method requests of [OID\_NIC\_SWITCH\_CREATE\_VPORT](oid-nic-switch-create-vport.md).

For more information on how to handle this OID request, see [Handling the OID\_NIC\_SWITCH\_CREATE\_SWITCH Request](./handling-the-oid-nic-switch-create-switch-request.md).

### Return Status Codes

The PF miniport driver returns one of the following status codes for the OID method request of OID\_NIC\_SWITCH\_CREATE\_SWITCH.

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
<td><p>One or more of the members of the <a href="/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_parameters" data-raw-source="[&lt;strong&gt;NDIS_NIC_SWITCH_PARAMETERS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_parameters)"><strong>NDIS_NIC_SWITCH_PARAMETERS</strong></a> structure have invalid values.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The length of the information buffer is less than sizeof(<a href="/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_parameters" data-raw-source="[&lt;strong&gt;NDIS_NIC_SWITCH_PARAMETERS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_parameters)"><strong>NDIS_NIC_SWITCH_PARAMETERS</strong></a>). The PF miniport driver must set the <strong>DATA.METHOD_INFORMATION.BytesNeeded</strong> member in the <a href="/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
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
[*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize)

[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request)

[**NDIS\_NIC\_SWITCH\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_parameters)

[**NdisMEnableVirtualization**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismenablevirtualization)

[OID\_NIC\_SWITCH\_ALLOCATE\_VF](oid-nic-switch-allocate-vf.md)

[OID\_NIC\_SWITCH\_CREATE\_VPORT](oid-nic-switch-create-vport.md)

