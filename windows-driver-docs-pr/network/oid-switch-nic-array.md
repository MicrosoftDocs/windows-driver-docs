---
title: OID\_SWITCH\_NIC\_ARRAY
author: windows-driver-content
description: A Hyper-V extensible switch extension issues an object identifier (OID) query request of OID\_SWITCH\_NIC\_ARRAY to obtain an array.
ms.assetid: CA9958DF-4389-4B4F-B110-03F500E27A1B
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_SWITCH_NIC_ARRAY Network Drivers Starting with Windows Vista
---

# OID\_SWITCH\_NIC\_ARRAY


A Hyper-V extensible switch extension issues an object identifier (OID) query request of OID\_SWITCH\_NIC\_ARRAY to obtain an array. Each element in the array specifies the configuration parameters of a virtual network adapter that is associated with an extensible switch port.

If the OID query request is completed successfully, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to a buffer. This buffer contains the following data:

-   An [**NDIS\_SWITCH\_NIC\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598212) structure that defines the number of elements in the array. This structure also specifies the offset to the first element in the array.

-   An array of [**NDIS\_SWITCH\_NIC\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598215) structures. Each of these structures contains information about a network adapter that is connected to an extensible switch port.

    **Note**  If no network adapters are connected to extensible switch ports, the underlying miniport edge of the extensible switch sets the **NumElements** member of the [**NDIS\_SWITCH\_NIC\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598212) structure to zero. In this case, no [**NDIS\_SWITCH\_NIC\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598215) structures are returned.

     

Remarks
-------

The OID\_SWITCH\_NIC\_ARRAY OID must only be issued when the Hyper-V extensible switch has completed activation. Please see [Querying the Hyper-V Extensible Switch Configuration](https://msdn.microsoft.com/library/windows/hardware/hh598293) for more details.

When the extension processes the returned [**NDIS\_SWITCH\_NIC\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598215) structure, it must not assume that the various string members of the [**NDIS\_SWITCH\_PORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598229) structure, such as **NicFriendlyName**, are NULL-terminated. The data types for these string members are type-defined by the [**IF\_COUNTED\_STRING**](https://msdn.microsoft.com/library/windows/hardware/hh451419) structure. The driver must determine the string length from the value of the **Length** member of this structure.

**Note**  If the string is null-terminated, the **Length** member must not include the terminating null character.

 

### Return Status Codes

The underlying miniport edge of the extensible switch completes the OID query request of OID\_SWITCH\_NIC\_ARRAY and returns one of the following status codes.

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
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The length of the information buffer is too small to return the [<strong>NDIS_SWITCH_NIC_ARRAY</strong>](https://msdn.microsoft.com/library/windows/hardware/hh598212) and its array of [<strong>NDIS_SWITCH_NIC_PARAMETERS</strong>](https://msdn.microsoft.com/library/windows/hardware/hh598215) elements. The underlying miniport edge of the extensible switch sets the <strong>DATA.QUERY_INFORMATION.BytesNeeded</strong> member in the [<strong>NDIS_OID_REQUEST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure to the minimum buffer size that is required.</p></td>
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

[**NDIS\_SWITCH\_NIC\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598212)

[**NDIS\_SWITCH\_NIC\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598215)

[Querying the Hyper-V Extensible Switch Configuration](https://msdn.microsoft.com/library/windows/hardware/hh598293)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_SWITCH_NIC_ARRAY%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


