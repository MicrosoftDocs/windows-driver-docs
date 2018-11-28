---
title: OID_NIC_SWITCH_ENUM_VPORTS
description: An overlying driver or user-mode application issues an object identifier (OID) method request of OID_NIC_SWITCH_ENUM_VPORTS to obtain an array.
ms.assetid: 4B9587E0-3CA9-46AF-A80E-969E6D563922
ms.date: 08/08/2017
keywords: 
 -OID_NIC_SWITCH_ENUM_VPORTS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_NIC\_SWITCH\_ENUM\_VPORTS


An overlying driver or user-mode application issues an object identifier (OID) method request of OID\_NIC\_SWITCH\_ENUM\_VPORTS to obtain an array. Each element in the array specifies the attributes of a virtual port (VPort) that has been created on a network adapter's NIC switch.

After a successful return from this OID query request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to a buffer that contains the following:

-   An [**NDIS\_NIC\_SWITCH\_VPORT\_INFO\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh451595) structure that defines the number of elements within the array.

-   An array of [**NDIS\_NIC\_SWITCH\_VPORT\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451594) structures. Each of these structures contains information about a VPort on the network adapter's NIC switch.

    **Note**  If no VPorts have been created on the network adapter, the driver sets the **NumElements** member of the [**NDIS\_NIC\_SWITCH\_VPORT\_INFO\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh451595) structure to zero and no [**NDIS\_NIC\_SWITCH\_VPORT\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451594) structures are returned.

     

Remarks
-------

Overlying drivers and user-mode applications issue OID query requests of OID\_NIC\_SWITCH\_ENUM\_VPORTS to enumerate the VPorts that are allocated on a network adapter's NIC switch.

Before the driver or application issues the OID request, it must initialize an [**NDIS\_NIC\_SWITCH\_VPORT\_INFO\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh451595) structure that is passed along with the request. The driver or application must follow these guidelines when initializing the **NDIS\_NIC\_SWITCH\_VPORT\_INFO\_ARRAY** structure:

-   If the NDIS\_NIC\_SWITCH\_VPORT\_INFO\_ARRAY\_ENUM\_ON\_SPECIFIC\_SWITCH flag is set in the **Flags** member, information is returned for all VPorts created on a specified NIC switch. The NIC switch is specified by the **SwitchId** member of that structure.

    **Note**  Starting with Windows Server 2012, the SR-IOV interface supports only the default NIC switch on the network adapter. Regardless of the flags that are set in the **Flags** member, the **SwitchId** member must be set to NDIS\_DEFAULT\_SWITCH\_ID.

     

-   If the NDIS\_NIC\_SWITCH\_VPORT\_INFO\_ARRAY\_ENUM\_ON\_SPECIFIC\_FUNCTION flag is set in the **Flags** member, information is returned for all VPorts attached to a specified PCI Express (PCIe) Physical Function (PF) or Virtual Function (VF) on the network adapter. The PF or VF is specified by the **AttachedFunctionId** member of that structure.

    If the **AttachedFunctionId** member is set to NDIS\_PF\_FUNCTION\_ID, information is returned for all VPorts, including the default VPort, that are attached to the network adapter's PF. If the **AttachedFunctionId** member is set to a valid VF identifier, information is returned for all VPorts to the specified VF.

    **Note**  Starting with Windows Server 2012, only one nondefault VPort can be attached to a VF. However, multiple VPorts (including the default VPort) can be attached to the PF.

     

-   If the **Flags** member is set to zero, information is returned for all VPorts attached to the PF or VF on the network adapter. In this case, the values of the **SwitchId** and **AttachedFunctionId** are ignored.

For more information, see [Enumerating Virtual Ports on a Network Adapter](https://msdn.microsoft.com/library/windows/hardware/hh406710).

### Return Status Codes

NDIS handles the OID method request of the OID\_NIC\_SWITCH\_ENUM\_VPORTS request for miniport drivers. The drivers will not be issued this OID request.

When NDIS handles the OID\_NIC\_SWITCH\_ENUM\_VPORTS request, it returns one of the following status codes:

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
[**NDIS\_NIC\_SWITCH\_VPORT\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451594)

[**NDIS\_NIC\_SWITCH\_VPORT\_INFO\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh451595)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[OID\_NIC\_SWITCH\_CREATE\_SWITCH](oid-nic-switch-create-switch.md)

[OID\_NIC\_SWITCH\_PARAMETERS](oid-nic-switch-parameters.md)

 

 




