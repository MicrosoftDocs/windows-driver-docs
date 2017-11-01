---
title: OID_NIC_SWITCH_DELETE_VPORT
author: windows-driver-content
description: An overlying driver issues an object identifier (OID) set request of OID_NIC_SWITCH_DELETE_VPORT to delete a nondefault virtual port (VPort) that was previously created on a network adapter's NIC switch.
ms.assetid: D762035C-33AC-4579-8EA0-6A422AE4CA76
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_NIC_SWITCH_DELETE_VPORT Network Drivers Starting with Windows Vista
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
<td><p>One or more of the members of the [<strong>NDIS_NIC_SWITCH_DELETE_VPORT_PARAMETERS</strong>](https://msdn.microsoft.com/library/windows/hardware/hh451577) structure have invalid values.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The length of the information buffer is less than sizeof([<strong>NDIS_NIC_SWITCH_DELETE_VPORT_PARAMETERS</strong>](https://msdn.microsoft.com/library/windows/hardware/hh451577)). The PF miniport driver must set the <strong>DATA.SET_INFORMATION.BytesNeeded</strong> member in the [<strong>NDIS_OID_REQUEST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure to the minimum buffer size that is required.</p></td>
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_NIC_SWITCH_DELETE_VPORT%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


