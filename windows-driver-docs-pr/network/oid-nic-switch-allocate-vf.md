---
title: OID_NIC_SWITCH_ALLOCATE_VF
description: An overlying driver issues an object identifier (OID) method request of OID_NIC_SWITCH_ALLOCATE_VF to allocate resources for a PCI Express (PCIe) Virtual Function (VF).
ms.date: 08/08/2017
keywords: 
 -OID_NIC_SWITCH_ALLOCATE_VF Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_NIC\_SWITCH\_ALLOCATE\_VF


An overlying driver issues an object identifier (OID) method request of OID\_NIC\_SWITCH\_ALLOCATE\_VF to allocate resources for a PCI Express (PCIe) Virtual Function (VF). The VF is exposed on a network adapter that supports the single root I/O virtualization (SR-IOV) interface.

Overlying drivers issue this OID method request to the miniport driver for the network adapter's PCIe Physical Function (PF). This OID method request is required for PF miniport drivers that support the single root I/O virtualization (SR-IOV) interface.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to an [**NDIS\_NIC\_SWITCH\_VF\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vf_parameters) structure.

## Remarks

The PF miniport driver allocates software resources for a VF when the driver handles an object identifier (OID) method request of OID\_NIC\_SWITCH\_ALLOCATE\_VF. Even though the hardware resources have been allocated for a VF, it is considered to be nonoperational until the PF miniport driver successfully completes the OID\_NIC\_SWITCH\_ALLOCATE\_VF.

For more information about how to allocate VF resources, see [Allocating Resources for a Virtual Function](./allocating-resources-for-a-virtual-function.md).

**Note**  After an overlying driver requests resource allocation for a VF, that driver is the only component that can request the freeing of the resources for the same VF. The overlying driver must issue an OID set request of [OID\_NIC\_SWITCH\_FREE\_VF](oid-nic-switch-free-vf.md) to free the VF resources. Before the overlying driver can be halted, it must free the resources for each VF that was allocated by the driver's OID\_NIC\_SWITCH\_ALLOCATE\_VF request.

 

### Return Status Codes

The PF miniport driver returns one of the following status codes for the OID method request of OID\_NIC\_SWITCH\_ALLOCATE\_VF.

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
<td><p>One or more of the members of the <a href="/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vf_parameters" data-raw-source="[&lt;strong&gt;NDIS_NIC_SWITCH_VF_PARAMETERS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vf_parameters)"><strong>NDIS_NIC_SWITCH_VF_PARAMETERS</strong></a> structure have invalid values.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The length of the information buffer is less than sizeof(<a href="/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vf_parameters" data-raw-source="[&lt;strong&gt;NDIS_NIC_SWITCH_VF_PARAMETERS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vf_parameters)"><strong>NDIS_NIC_SWITCH_VF_PARAMETERS</strong></a>). The PF miniport driver must set the <strong>DATA.METHOD_INFORMATION.BytesNeeded</strong> member in the <a href="/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
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
[**NDIS\_MAKE\_RID**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndis_make_rid)

[OID\_NIC\_SWITCH\_CREATE\_SWITCH](oid-nic-switch-create-switch.md)

[OID\_NIC\_SWITCH\_CREATE\_VPORT](oid-nic-switch-create-vport.md)

[**NDIS\_NIC\_SWITCH\_VF\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vf_parameters)

[OID\_NIC\_SWITCH\_FREE\_VF](oid-nic-switch-free-vf.md)

