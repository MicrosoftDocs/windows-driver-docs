---
title: OID_NIC_SWITCH_ENUM_VFS
description: An overlying driver or user-mode application issues an object identifier (OID) method request of OID_NIC_SWITCH_ENUM_VFS to obtain an array.
ms.assetid: ABACB70C-9307-4560-93DD-0475AD1FFF10
ms.date: 08/08/2017
keywords: 
 -OID_NIC_SWITCH_ENUM_VFS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_NIC\_SWITCH\_ENUM\_VFS


An overlying driver or user-mode application issues an object identifier (OID) method request of OID\_NIC\_SWITCH\_ENUM\_VFS to obtain an array. Each element in the array specifies the attributes of a PCI Express (PCIe) Virtual Function (VF) that are attached to a NIC switch on a network adapter's NIC switch.

After a successful return from this OID query request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to a buffer that contains the following:

-   An [**NDIS\_NIC\_SWITCH\_VF\_INFO\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh451592) structure that defines the number of elements within the array.

-   An array of [**NDIS\_NIC\_SWITCH\_VF\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451591) structures. Each of these structures contains information about a single VF on a NIC switch of the network adapter. A VF is attached to a NIC switch through OID method requests of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](oid-nic-switch-allocate-vf.md).

    **Note**  If no VFs are attached to a NIC switch on the network adapter, the **NumElements** member of the [**NDIS\_NIC\_SWITCH\_VF\_INFO\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh451592) structure is set to zero and no [**NDIS\_NIC\_SWITCH\_VF\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451591) structures are returned.

     

Remarks
-------

Overlying drivers and user-mode applications issue OID method requests of OID\_NIC\_SWITCH\_ENUM\_VFS to enumerate the VFs attached to a network adapter's NIC switch.

Before the driver or application issues the OID request, it must initialize an [**NDIS\_NIC\_SWITCH\_VF\_INFO\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh451592) structure that is passed along with the request. The driver or application must follow these guidelines when initializing the **NDIS\_NIC\_SWITCH\_VF\_INFO\_ARRAY** structure:

-   If the NDIS\_NIC\_SWITCH\_VF\_INFO\_ARRAY\_ENUM\_ON\_SPECIFIC\_SWITCH flag is set in the **Flags** member, the driver or application must set the **SwitchId** member to the NIC switch identifier on the SR-IOV network adapter. By setting these members in this way, VF information is returned only for the specified NIC switch on the SR-IOV network adapter.

    **Note**  The overlying driver and user-mode application can obtain the NIC switch identifiers by issuing an OID query request of [OID\_NIC\_SWITCH\_ENUM\_SWITCHES](oid-nic-switch-enum-switches.md).

     

-   If the **Flags** member is set to zero, the driver or application must set the **SwitchId** member to zero. By setting these members in this way, VF information is returned for all NIC switch on the SR-IOV network adapter.

**Note**  Starting with Windows Server 2012, Windows supports only the default NIC switch on the network adapter. Regardless of the flags set in the **Flags** member, the **SwitchId** member must be set to NDIS\_DEFAULT\_SWITCH\_ID.

 

For more information about NIC switches, see [NIC Switches](https://msdn.microsoft.com/library/windows/hardware/hh439961).

### Return Status Codes

NDIS handles the OID method request of the OID\_NIC\_SWITCH\_ENUM\_VFS request for miniport drivers. The drivers will not be issued this OID request.

When NDIS handles the OID\_NIC\_SWITCH\_ENUM\_VFS request, it returns one of the following status codes.

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
<td><p>The miniport driver either does not support the single root I/O virtualization (SR-IOV) interface or is not enabled to use the interface.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_INVALID_PARAMETER</p></td>
<td><p>One or more of the members of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451592" data-raw-source="[&lt;strong&gt;NDIS_NIC_SWITCH_VF_INFO_ARRAY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451592)"><strong>NDIS_NIC_SWITCH_VF_INFO_ARRAY</strong></a> structure have invalid values.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The information buffer was too short. NDIS sets the <strong>DATA.METHOD_INFORMATION.BytesNeeded</strong> member in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566710)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
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
[**NDIS\_NIC\_SWITCH\_VF\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451591)

[**NDIS\_NIC\_SWITCH\_VF\_INFO\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh451592)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[OID\_NIC\_SWITCH\_ALLOCATE\_VF](oid-nic-switch-allocate-vf.md)

[OID\_NIC\_SWITCH\_CREATE\_SWITCH](oid-nic-switch-create-switch.md)

[OID\_NIC\_SWITCH\_VF\_PARAMETERS](oid-nic-switch-vf-parameters.md)

 

 




