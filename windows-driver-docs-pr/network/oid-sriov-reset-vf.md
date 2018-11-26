---
title: OID_SRIOV_RESET_VF
description: Overlying drivers issue an object identifier (OID) set request of OID_SRIOV_RESET_VF to reset a specified PCI Express (PCIe) Virtual Function (VF) on a network adapter that supports single root I/O virtualization.
ms.assetid: 7D5EB64B-3345-478A-8D42-192939C0B9C2
ms.date: 08/08/2017
keywords: 
 -OID_SRIOV_RESET_VF Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_SRIOV\_RESET\_VF


Overlying drivers issue an object identifier (OID) set request of OID\_SRIOV\_RESET\_VF to reset a specified PCI Express (PCIe) Virtual Function (VF) on a network adapter that supports single root I/O virtualization. Overlying drivers issue this OID set request to the miniport driver of the PCI Express (PCIe) Physical Function (PF) of the network adapter.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_SRIOV\_RESET\_VF\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451682) structure. The overlying driver specifies the identifier of the VF to be reset through the **VFId** member of this structure.

Remarks
-------

A VF can be reset through a PCI Express (PCIe) Function Level Reset (FLR). Because the FLR request is a privileged operation, it can only be performed by the PF miniport driver that runs in the management operating system of a Hyper-V parent partition. Overlying drivers that run in the management operating system are notified of the FLR request and issue the OID set request of OID\_SRIOV\_RESET\_VF to the PF miniport driver.

When it handles this OID request, the PF miniport driver must follow these guidelines:

-   The PF miniport driver must verify that the VF, specified by the **VFId** member of the [**NDIS\_SRIOV\_RESET\_VF\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451682) structure, has resources that have been previously allocated. The PF miniport driver allocates resources for a VF during an OID method request of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](oid-nic-switch-allocate-vf.md). If resources for the specified VF have not been allocated, the driver must fail the OID request.

-   The reset operation must only affect the specified VF. The operation must not affect other VFs or the PF on the same network adapter.

For more information, see [Resetting a Virtual Function](https://msdn.microsoft.com/library/windows/hardware/hh440219).

### Return Status Codes

The PF miniport driver returns one of the following status codes for the set request of OID\_SRIOV\_RESET\_VF.

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
<td><p>One or more of the members of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451682" data-raw-source="[&lt;strong&gt;NDIS_SRIOV_RESET_VF_PARAMETERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451682)"><strong>NDIS_SRIOV_RESET_VF_PARAMETERS</strong></a> structure have invalid values.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The information buffer was too short. The PF miniport driver must set the <strong>DATA.SET_INFORMATION.BytesNeeded</strong> member in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566710)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_FAILURE</p></td>
<td><p>The request failed for other reasons.</p></td>
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
[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_SRIOV\_RESET\_VF\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451682)

[OID\_NIC\_SWITCH\_ALLOCATE\_VF](oid-nic-switch-allocate-vf.md)

 

 




