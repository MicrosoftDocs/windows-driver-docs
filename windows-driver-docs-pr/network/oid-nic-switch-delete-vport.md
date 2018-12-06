---
title: OID_NIC_SWITCH_DELETE_VPORT
description: An overlying driver issues an object identifier (OID) set request of OID_NIC_SWITCH_DELETE_VPORT to delete a nondefault virtual port (VPort) that was previously created on a network adapter's NIC switch.
ms.assetid: D762035C-33AC-4579-8EA0-6A422AE4CA76
ms.date: 08/08/2017
keywords: 
 -OID_NIC_SWITCH_DELETE_VPORT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_NIC\_SWITCH\_DELETE\_VPORT


An overlying driver issues an object identifier (OID) set request of OID\_NIC\_SWITCH\_DELETE\_VPORT to delete a nondefault virtual port (VPort) that was previously created on a network adapter's NIC switch. The overlying driver can delete a VPort that it has previously created only by issuing an OID method request of [OID\_NIC\_SWITCH\_CREATE\_VPORT](oid-nic-switch-create-vport.md).

Overlying drivers issue this OID set request to the miniport driver for the network adapter's PCIe Physical Function (PF). This OID set request is required for PF miniport drivers that support the single root I/O virtualization (SR-IOV) interface.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to the [**NDIS\_NIC\_SWITCH\_DELETE\_VPORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451577) structure.

Remarks
-------

An overlying driver, such as a protocol or filter driver, can only delete a nondefault VPort that it has previously created. The overlying driver creates a VPort by issuing an OID method request of [OID\_NIC\_SWITCH\_CREATE\_VPORT](oid-nic-switch-create-vport.md).

When the PF miniport driver receives the OID request of OID\_NIC\_SWITCH\_DELETE\_VPORT, the driver must free the hardware and software resources that were allocated for the specified VPort.

For more information, see [Deleting a Virtual Port](https://msdn.microsoft.com/library/windows/hardware/hh439418).

**Note**  Only nondefault VPorts can be explicitly deleted through OID requests of OID\_NIC\_SWITCH\_DELETE\_VPORT. The default VPort is implicitly deleted when the PF miniport driver deletes the default NIC switch. For more information, see [Deleting a NIC Switch](https://msdn.microsoft.com/library/windows/hardware/hh439415).

 

### Return Status Codes

The PF miniport driver returns one of the following status codes for the OID set request of OID\_NIC\_SWITCH\_DELETE\_VPORT.

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
<td><p>One or more of the members of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451577" data-raw-source="[&lt;strong&gt;NDIS_NIC_SWITCH_DELETE_VPORT_PARAMETERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451577)"><strong>NDIS_NIC_SWITCH_DELETE_VPORT_PARAMETERS</strong></a> structure have invalid values.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The length of the information buffer is less than sizeof(<a href="https://msdn.microsoft.com/library/windows/hardware/hh451577" data-raw-source="[&lt;strong&gt;NDIS_NIC_SWITCH_DELETE_VPORT_PARAMETERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451577)"><strong>NDIS_NIC_SWITCH_DELETE_VPORT_PARAMETERS</strong></a>). The PF miniport driver must set the <strong>DATA.SET_INFORMATION.BytesNeeded</strong> member in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566710)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
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
[**NDIS\_NIC\_SWITCH\_DELETE\_VPORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451577)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NdisCloseAdapterEx**](https://msdn.microsoft.com/library/windows/hardware/ff561640)

[OID\_NIC\_SWITCH\_CREATE\_VPORT](oid-nic-switch-create-vport.md)

[OID\_NIC\_SWITCH\_DELETE\_SWITCH](oid-nic-switch-delete-switch.md)

 

 




