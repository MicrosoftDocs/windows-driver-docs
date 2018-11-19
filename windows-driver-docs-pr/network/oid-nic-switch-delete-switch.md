---
title: OID_NIC_SWITCH_DELETE_SWITCH
description: NDIS issues an object identifier (OID) set request of OID_NIC_SWITCH_DELETE_SWITCH to delete a NIC switch from a network adapter.
ms.assetid: 5785B30F-B67F-4D5A-A93A-243D33B9CAE8
ms.date: 08/08/2017
keywords: 
 -OID_NIC_SWITCH_DELETE_SWITCH Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_NIC\_SWITCH\_DELETE\_SWITCH


NDIS issues an object identifier (OID) set request of OID\_NIC\_SWITCH\_DELETE\_SWITCH to delete a NIC switch from a network adapter.

NDIS issues this OID set request to the miniport driver of the network adapter's PCI Express (PCIe) Physical Function (PF). This OID set request is required for PF miniport drivers that support the single root I/O virtualization (SR-IOV) interface.

**Note**  Overlying drivers, such as protocol or filter drivers, cannot issue this OID method request to the PF miniport driver.

 

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_NIC\_SWITCH\_DELETE\_SWITCH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451575) structure.

Remarks
-------

An OID set request of OID\_NIC\_SWITCH\_DELETE\_SWITCH deletes a NIC switch that was previously created through an OID method request of [OID\_NIC\_SWITCH\_CREATE\_SWITCH](oid-nic-switch-create-switch.md).

When it receives the OID method request of OID\_NIC\_SWITCH\_DELETE\_SWITCH, the PF miniport driver must do the following:

1.  If the PF miniport driver supports static creation and configuration of NIC switches, it must free the software resources associated with the specified NIC switch. However, the driver can only free the hardware resources for the NIC switch when [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) is called.

    For more information about static NIC switch creation, see [Static Creation of a NIC Switch](https://msdn.microsoft.com/library/windows/hardware/hh440256).

2.  If the PF miniport driver supports the dynamic creation and configuration of NIC switches, it must free the hardware and software resources associated with the specified NIC switch.

    For more information about dynamic NIC switch creation, see [Dynamic Creation of a NIC Switch](https://msdn.microsoft.com/library/windows/hardware/hh406694).

3.  If the PF miniport driver supports the dynamic creation and all the NIC switches have been deleted, the driver must disable virtualization on the adapter by calling [**NdisMEnableVirtualization**](https://msdn.microsoft.com/library/windows/hardware/hh451481). To disable virtualization, the network adapter must set the *EnableVirtualization* parameter to FALSE and the *NumVFs* parameter to zero.

    [**NdisMEnableVirtualization**](https://msdn.microsoft.com/library/windows/hardware/hh451481) clears the **NumVFs** member and the **VF Enable** bit in the SR-IOV Extended Capability structure in the PCI configuration space of the network adapter's PF.

    **Note**  If the PF miniport driver supports static creation and configuration of NIC switches, it must only call [**NdisMEnableVirtualization**](https://msdn.microsoft.com/library/windows/hardware/hh451481) when [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) is called.

     

For more information, see [Deleting a NIC Switch](https://msdn.microsoft.com/library/windows/hardware/hh439415).

### Return Status Codes

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
<td><p>One or more of the members of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451575" data-raw-source="[&lt;strong&gt;NDIS_NIC_SWITCH_DELETE_SWITCH_PARAMETERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451575)"><strong>NDIS_NIC_SWITCH_DELETE_SWITCH_PARAMETERS</strong></a> structure have invalid values.</p></td>
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
[*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_NIC\_SWITCH\_DELETE\_SWITCH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451575)

[OID\_NIC\_SWITCH\_ALLOCATE\_VF](oid-nic-switch-allocate-vf.md)

[OID\_NIC\_SWITCH\_CREATE\_SWITCH](oid-nic-switch-create-switch.md)

[OID\_NIC\_SWITCH\_DELETE\_VPORT](oid-nic-switch-delete-vport.md)

[OID\_NIC\_SWITCH\_FREE\_VF](oid-nic-switch-free-vf.md)

 

 




