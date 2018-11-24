---
title: OID_SWITCH_PORT_ARRAY
description: A Hyper-V extensible switch extension issues an object identifier (OID) query request of OID_SWITCH_PORT_ARRAY to obtain an array. Each element in the array specifies the configuration parameters for an extensible switch port.
ms.assetid: 9ED5E7A5-A23E-48E7-B8A2-9089C81851A1
ms.date: 08/08/2017
keywords: 
 -OID_SWITCH_PORT_ARRAY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_SWITCH\_PORT\_ARRAY


A Hyper-V extensible switch extension issues an object identifier (OID) query request of OID\_SWITCH\_PORT\_ARRAY to obtain an array. Each element in the array specifies the configuration parameters for an extensible switch port.

If the OID query request completes successfully, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to a buffer. This buffer contains the following data:

-   An [**NDIS\_SWITCH\_PORT\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598221) structure that defines the number of elements within the array.

-   An array of [**NDIS\_SWITCH\_PORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598229) structures. Each of these structures contains information about a port on the extensible switch.

    **Note**  If no ports have been created on the extensible switch, the driver sets the **NumElements** member of the [**NDIS\_SWITCH\_PORT\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598221) structure to zero and no [**NDIS\_SWITCH\_PORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598229) structures are returned.

     

Remarks
-------

The OID\_SWITCH\_PORT\_ARRAY OID must only be issued when the Hyper-V extensible switch has completed activation. Please see [Querying the Hyper-V Extensible Switch Configuration](https://msdn.microsoft.com/library/windows/hardware/hh598293) for more details.

When the extension handles the returned [**NDIS\_SWITCH\_PORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598229) structure, it must not assume that the various string members of the **NDIS\_SWITCH\_PORT\_PARAMETERS** structure, such as **PortName**, are null-terminated. The data types for these string members are type-defined by the [**IF\_COUNTED\_STRING**](https://msdn.microsoft.com/library/windows/hardware/hh451419) structure. The driver must determine the string length from the value of the **Length** member of this structure.

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
<td><p>The length of the information buffer is too small to return the <a href="https://msdn.microsoft.com/library/windows/hardware/hh598221" data-raw-source="[&lt;strong&gt;NDIS_SWITCH_PORT_ARRAY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh598221)"><strong>NDIS_SWITCH_PORT_ARRAY</strong></a> and its array of <a href="https://msdn.microsoft.com/library/windows/hardware/hh598229" data-raw-source="[&lt;strong&gt;NDIS_SWITCH_PORT_PARAMETERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh598229)"><strong>NDIS_SWITCH_PORT_PARAMETERS</strong></a> elements. The underlying miniport edge of the extensible switch sets the <strong>DATA.QUERY_INFORMATION.BytesNeeded</strong> member in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566710)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
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

[**NDIS\_SWITCH\_PORT\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598221)

[**NDIS\_SWITCH\_PORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598229)

[Querying the Hyper-V Extensible Switch Configuration](https://msdn.microsoft.com/library/windows/hardware/hh598293)

 

 




