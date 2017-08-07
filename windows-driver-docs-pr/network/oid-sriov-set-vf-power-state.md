---
title: OID\_SRIOV\_SET\_VF\_POWER\_STATE
author: windows-driver-content
description: An overlying driver issues an object identifier (OID) set request of OID\_SRIOV\_SET\_VF\_POWER\_STATE to change the power state of a specified PCI Express (PCIe) Virtual Function (VF) on the network adapter.
ms.assetid: 9723518E-2312-48F9-820A-19F5567A33DB
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_SRIOV_SET_VF_POWER_STATE Network Drivers Starting with Windows Vista
---

# OID\_SRIOV\_SET\_VF\_POWER\_STATE


An overlying driver issues an object identifier (OID) set request of OID\_SRIOV\_SET\_VF\_POWER\_STATE to change the power state of a specified PCI Express (PCIe) Virtual Function (VF) on the network adapter. Since changing the power state is a privileged operation, overlying drivers issue this OID set request to the miniport driver of the PCIe Physical Function (PF) on the network adapter. The PF miniport driver then sets the specified power state on the VF.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](ndis-oid-request.md) structure contains a pointer to an [**NDIS\_SRIOV\_SET\_VF\_POWER\_STATE\_PARAMETERS**](ndis-sriov-set-vf-power-state-parameters.md) structure.

Remarks
-------

When the PF miniport driver is issued this OID set request, it must follow these guidelines:

-   The PF miniport driver must verify that the VF, specified by the **VFId** member of the [**NDIS\_SRIOV\_SET\_VF\_POWER\_STATE\_PARAMETERS**](ndis-sriov-set-vf-power-state-parameters.md) structure, has resources that have been previously allocated. The PF miniport driver allocates resources for a VF during an OID method request of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](oid-nic-switch-allocate-vf.md). If the specified VF is not in an allocated state, the driver must fail the OID request.

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
<td><p>One or more of the members of the [<strong>NDIS_SRIOV_SET_VF_POWER_STATE_PARAMETERS</strong>](ndis-sriov-set-vf-power-state-parameters.md) structure have invalid values.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The information buffer was too short. The PF miniport driver must set the <strong>DATA.SET_INFORMATION.BytesNeeded</strong> member in the [<strong>NDIS_OID_REQUEST</strong>](ndis-oid-request.md) structure to the minimum buffer size that is required.</p></td>
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
[**NDIS\_OID\_REQUEST**](ndis-oid-request.md)

[**NDIS\_SRIOV\_SET\_VF\_POWER\_STATE\_PARAMETERS**](ndis-sriov-set-vf-power-state-parameters.md)

[OID\_NIC\_SWITCH\_ALLOCATE\_VF](oid-nic-switch-allocate-vf.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_SRIOV_SET_VF_POWER_STATE%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


