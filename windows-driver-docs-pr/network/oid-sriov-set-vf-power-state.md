---
title: OID_SRIOV_SET_VF_POWER_STATE
description: An overlying driver issues an object identifier (OID) set request of OID_SRIOV_SET_VF_POWER_STATE to change the power state of a specified PCI Express (PCIe) Virtual Function (VF) on the network adapter.
ms.assetid: 9723518E-2312-48F9-820A-19F5567A33DB
ms.date: 08/08/2017
keywords: 
 -OID_SRIOV_SET_VF_POWER_STATE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_SRIOV\_SET\_VF\_POWER\_STATE


An overlying driver issues an object identifier (OID) set request of OID\_SRIOV\_SET\_VF\_POWER\_STATE to change the power state of a specified PCI Express (PCIe) Virtual Function (VF) on the network adapter. Since changing the power state is a privileged operation, overlying drivers issue this OID set request to the miniport driver of the PCIe Physical Function (PF) on the network adapter. The PF miniport driver then sets the specified power state on the VF.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_SRIOV\_SET\_VF\_POWER\_STATE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451683) structure.

Remarks
-------

When the PF miniport driver is issued this OID set request, it must follow these guidelines:

-   The PF miniport driver must verify that the VF, specified by the **VFId** member of the [**NDIS\_SRIOV\_SET\_VF\_POWER\_STATE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451683) structure, has resources that have been previously allocated. The PF miniport driver allocates resources for a VF during an OID method request of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](oid-nic-switch-allocate-vf.md). If the specified VF is not in an allocated state, the driver must fail the OID request.

-   The power state operation must only affect the specified VF. The operation must not affect other VFs or the PF on the same network adapter.

For more information, see [Setting the Power State of a Virtual Function](https://msdn.microsoft.com/library/windows/hardware/hh440230).

### Return Status Codes

The PF miniport driver returns one of the following status codes for the OID set request of OID\_SRIOV\_SET\_VF\_POWER\_STATE.

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
<td><p>One or more of the members of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451683" data-raw-source="[&lt;strong&gt;NDIS_SRIOV_SET_VF_POWER_STATE_PARAMETERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451683)"><strong>NDIS_SRIOV_SET_VF_POWER_STATE_PARAMETERS</strong></a> structure have invalid values.</p></td>
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

[**NDIS\_SRIOV\_SET\_VF\_POWER\_STATE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451683)

[OID\_NIC\_SWITCH\_ALLOCATE\_VF](oid-nic-switch-allocate-vf.md)

 

 




