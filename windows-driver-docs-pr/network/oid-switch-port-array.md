---
title: OID\_SWITCH\_PORT\_ARRAY
author: windows-driver-content
description: A Hyper-V extensible switch extension issues an object identifier (OID) query request of OID\_SWITCH\_PORT\_ARRAY to obtain an array. Each element in the array specifies the configuration parameters for an extensible switch port.
ms.assetid: 9ED5E7A5-A23E-48E7-B8A2-9089C81851A1
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_SWITCH_PORT_ARRAY Network Drivers Starting with Windows Vista
---

# OID\_SWITCH\_PORT\_ARRAY


A Hyper-V extensible switch extension issues an object identifier (OID) query request of OID\_SWITCH\_PORT\_ARRAY to obtain an array. Each element in the array specifies the configuration parameters for an extensible switch port.

If the OID query request completes successfully, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](ndis-oid-request.md) structure contains a pointer to a buffer. This buffer contains the following data:

-   An [**NDIS\_SWITCH\_PORT\_ARRAY**](ndis-switch-port-array.md) structure that defines the number of elements within the array.

-   An array of [**NDIS\_SWITCH\_PORT\_PARAMETERS**](ndis-switch-port-parameters.md) structures. Each of these structures contains information about a port on the extensible switch.

    **Note**  If no ports have been created on the extensible switch, the driver sets the **NumElements** member of the [**NDIS\_SWITCH\_PORT\_ARRAY**](ndis-switch-port-array.md) structure to zero and no [**NDIS\_SWITCH\_PORT\_PARAMETERS**](ndis-switch-port-parameters.md) structures are returned.

     

Remarks
-------

The OID\_SWITCH\_PORT\_ARRAY OID must only be issued when the Hyper-V extensible switch has completed activation. Please see [Querying the Hyper-V Extensible Switch Configuration](https://msdn.microsoft.com/library/windows/hardware/hh598293) for more details.

When the extension handles the returned [**NDIS\_SWITCH\_PORT\_PARAMETERS**](ndis-switch-port-parameters.md) structure, it must not assume that the various string members of the **NDIS\_SWITCH\_PORT\_PARAMETERS** structure, such as **PortName**, are null-terminated. The data types for these string members are type-defined by the [**IF\_COUNTED\_STRING**](if-counted-string.md) structure. The driver must determine the string length from the value of the **Length** member of this structure.

**Note**  If the string is null-terminated, the **Length** member must not include the terminating null character.

 

### Return Status Codes

The underlying miniport edge of the extensible switch completes the OID query request of OID\_SWITCH\_PORT\_ARRAY and returns one of the following status codes.

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
<td><p>The length of the information buffer is too small to return the [<strong>NDIS_SWITCH_PORT_ARRAY</strong>](ndis-switch-port-array.md) and its array of [<strong>NDIS_SWITCH_PORT_PARAMETERS</strong>](ndis-switch-port-parameters.md) elements. The underlying miniport edge of the extensible switch sets the <strong>DATA.QUERY_INFORMATION.BytesNeeded</strong> member in the [<strong>NDIS_OID_REQUEST</strong>](ndis-oid-request.md) structure to the minimum buffer size that is required.</p></td>
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

[**NDIS\_SWITCH\_PORT\_ARRAY**](ndis-switch-port-array.md)

[**NDIS\_SWITCH\_PORT\_PARAMETERS**](ndis-switch-port-parameters.md)

[Querying the Hyper-V Extensible Switch Configuration](https://msdn.microsoft.com/library/windows/hardware/hh598293)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_SWITCH_PORT_ARRAY%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


