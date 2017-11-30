---
title: OID_NIC_SWITCH_ENUM_SWITCHES
author: windows-driver-content
description: An overlying driver or user-mode application issues an object identifier (OID) query request of OID_NIC_SWITCH_ENUM_SWITCHES to obtain an array.
ms.assetid: 706C3F1C-239F-4731-A38E-E150D26C79A5
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_NIC_SWITCH_ENUM_SWITCHES Network Drivers Starting with Windows Vista
---

# OID\_NIC\_SWITCH\_ENUM\_SWITCHES


An overlying driver or user-mode application issues an object identifier (OID) query request of OID\_NIC\_SWITCH\_ENUM\_SWITCHES to obtain an array. Each element in the array specifies the attributes of a NIC switch that has been created on a network adapter.

After a successful return from this OID query request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to a buffer that contains the following:

-   An [**NDIS\_NIC\_SWITCH\_INFO\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh451584) structure that defines the number of elements within the array.

-   An array of [**NDIS\_NIC\_SWITCH\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451582) structures. Each of these structures contains the information about a single NIC switch created on the network adapter.

    **Note**  If the network adapter has no NIC switches, the driver sets the **NumElements** member of the [**NDIS\_NIC\_SWITCH\_INFO\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh451584) structure to zero and no [**NDIS\_NIC\_SWITCH\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451582) structures are returned.

     

Remarks
-------

Overlying drivers and user-mode applications issue OID query requests of OID\_NIC\_SWITCH\_ENUM\_SWITCHES to enumerate the NIC switches created on a network adapter.

**Note**  Starting with Windows Server 2012, the single root I/O virtualization (SR-IOV) interface only supports the default NIC switch on the network adapter. Therefore, the returned [**NDIS\_NIC\_SWITCH\_INFO\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh451584) structure must specify a single [**NDIS\_NIC\_SWITCH\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451582) element for the default NIC switch, which is referenced by the identifier of NDIS\_DEFAULT\_SWITCH\_ID.

 

### Return Status Codes

NDIS handles the OID query request of the OID\_NIC\_SWITCH\_ENUM\_SWITCHES request for miniport drivers. The drivers will not be issued this OID request.

When NDIS handles the OID\_NIC\_SWITCH\_ENUM\_SWITCHES request, it returns one of the following status codes.

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
<td><p>The miniport driver either does not support the SR-IOV interface or is not enabled to use the interface.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_INVALID_PARAMETER</p></td>
<td><p>One or more of the members of the [<strong>NDIS_NIC_SWITCH_INFO_ARRAY</strong>](https://msdn.microsoft.com/library/windows/hardware/hh451577) structure have invalid values.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The information buffer was too short. NDIS sets the <strong>DATA.QUERY_INFORMATION.BytesNeeded</strong> member in the [<strong>NDIS_OID_REQUEST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure to the minimum buffer size that is required.</p></td>
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
[**NDIS\_NIC\_SWITCH\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451582)

[**NDIS\_NIC\_SWITCH\_INFO\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh451584)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[OID\_NIC\_SWITCH\_CREATE\_SWITCH](oid-nic-switch-create-switch.md)

[OID\_NIC\_SWITCH\_PARAMETERS](oid-nic-switch-parameters.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_NIC_SWITCH_ENUM_SWITCHES%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


