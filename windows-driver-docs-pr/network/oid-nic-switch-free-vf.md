---
title: OID_NIC_SWITCH_FREE_VF
description: An overlying driver issues an object identifier (OID) set request of OID_NIC_SWITCH_FREE_VF to free the resources for a network adapter's PCI Express (PCIe) Virtual Function (VF).Overlying drivers issue this OID set request to the miniport driver for the network adapter's PCIe Physical Function (PF). This OID set request is required for PF miniport drivers that support the single root I/O virtualization (SR-IOV) interface.
ms.assetid: B1A72D34-286A-4A70-8BE3-F21324B92187
ms.date: 08/08/2017
keywords: 
 -OID_NIC_SWITCH_FREE_VF Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_NIC\_SWITCH\_FREE\_VF


An overlying driver issues an object identifier (OID) set request of OID\_NIC\_SWITCH\_FREE\_VF to free the resources for a network adapter's PCI Express (PCIe) Virtual Function (VF).

Overlying drivers issue this OID set request to the miniport driver for the network adapter's PCIe Physical Function (PF). This OID set request is required for PF miniport drivers that support the single root I/O virtualization (SR-IOV) interface.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_NIC\_SWITCH\_FREE\_VF\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451579) structure.

The overlying driver specifies the identifier of the VF to be freed through the **VFId** member of this structure. The driver obtained this identifier from an earlier OID method request of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](oid-nic-switch-allocate-vf.md).

Remarks
-------

An overlying driver issues an OID set request of OID\_NIC\_SWITCH\_FREE\_VF to free the resources for a VF. These resources were previously allocated through an OID method request of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](oid-nic-switch-allocate-vf.md).

For more information about how to free VF resources, see [Freeing Resources for a Virtual Function](https://msdn.microsoft.com/library/windows/hardware/hh439570).

**Note**  Once an overlying driver requests resource allocation for a VF, that driver is the only component that can request the freeing of the resources for the same VF. The overlying driver must issue an OID set request of OID\_NIC\_SWITCH\_FREE\_VF to free the VF resources. Before the overlying driver can be halted, it must free the resources for each VF that was allocated by the driver's [OID\_NIC\_SWITCH\_ALLOCATE\_VF](oid-nic-switch-allocate-vf.md) request.

 

### Return status codes

The miniport driver's [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function returns one of the following values for this request:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>NDIS_STATUS_SUCCESS</strong></p></td>
<td><p>The miniport driver completed the request successfully.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_PENDING</strong></p></td>
<td><p>The miniport driver will complete the request asynchronously. After the miniport driver has completed all processing, it must succeed the request by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563622" data-raw-source="[&lt;strong&gt;NdisMOidRequestComplete&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563622)"><strong>NdisMOidRequestComplete</strong></a> function, passing <strong>NDIS_STATUS_SUCCESS</strong> for the <em>Status</em> parameter.</p></td>
</tr>
<tr class="odd">
<td><p><strong>NDIS_STATUS_NOT_ACCEPTED</strong></p></td>
<td><p>The miniport driver is resetting.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_REQUEST_ABORTED</strong></p></td>
<td><p>The miniport driver stopped processing the request. For example, NDIS called the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559432" data-raw-source="[&lt;em&gt;MiniportResetEx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559432)"><em>MiniportResetEx</em></a> function.</p></td>
</tr>
</tbody>
</table>

 

NDIS returns one of the following status codes for this request:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>NDIS_STATUS_SUCCESS</strong></p></td>
<td><p>The OID request completed successfully.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_NOT_SUPPORTED</strong></p></td>
<td><p>The PF miniport driver either does not support the SR-IOV interface or is not enabled to use the interface.</p></td>
</tr>
<tr class="odd">
<td><p><strong>NDIS_STATUS_FILE_NOT_FOUND</strong></p></td>
<td><p>One or more of the members of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451579" data-raw-source="[&lt;strong&gt;NDIS_NIC_SWITCH_FREE_VF_PARAMETERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451579)"><strong>NDIS_NIC_SWITCH_FREE_VF_PARAMETERS</strong></a> structure have invalid values. For example, the <strong>VFId</strong> member might specify a VF that either has not been allocated or that has VPorts that have not been deleted.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_INVALID_LENGTH</strong></p></td>
<td><p>The information buffer is too small. NDIS sets the <strong>DATA.SET_INFORMATION.BytesNeeded</strong> member in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566710)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
</tr>
</tbody>
</table>

 

Requirements
------------

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
[**NDIS\_NIC\_SWITCH\_FREE\_VF\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451579)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NdisCloseAdapterEx**](https://msdn.microsoft.com/library/windows/hardware/ff561640)

[OID\_NIC\_SWITCH\_ALLOCATE\_VF](oid-nic-switch-allocate-vf.md)

[OID\_NIC\_SWITCH\_CREATE\_VPORT](oid-nic-switch-create-vport.md)

[OID\_NIC\_SWITCH\_DELETE\_VPORT](oid-nic-switch-delete-vport.md)

[OID\_NIC\_SWITCH\_DELETE\_SWITCH](oid-nic-switch-delete-switch.md)

 

 




