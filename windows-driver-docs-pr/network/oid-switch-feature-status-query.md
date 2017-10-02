---
title: OID_SWITCH_FEATURE_STATUS_QUERY
author: windows-driver-content
description: The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) method request of OID\_SWITCH\_FEATURE\_STATUS\_QUERY to obtain custom status information from an extension about the extensible switch.
ms.assetid: 580EFBD0-7798-4C56-99C5-84EADB8F8E82
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_SWITCH_FEATURE_STATUS_QUERY Network Drivers Starting with Windows Vista
---

# OID\_SWITCH\_FEATURE\_STATUS\_QUERY


The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) method request of OID\_SWITCH\_FEATURE\_STATUS\_QUERY to obtain custom status information from an extension about the extensible switch. This information is known as *feature status* information. The format of this information is defined by the independent software vendor (ISV).

After a successful return from this OID method request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to a buffer. This buffer contains the following data:

-   An [**NDIS\_SWITCH\_FEATURE\_STATUS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598208) structure that specifies the parameters for the type of feature status information to be returned.

-   An [**NDIS\_SWITCH\_FEATURE\_STATUS\_CUSTOM**](https://msdn.microsoft.com/library/windows/hardware/hh598207) structure that contains the feature status information for the extensible switch.

Remarks
-------

For guidelines on how to handle an OID set request of OID\_SWITCH\_FEATURE\_STATUS\_QUERY, see [Managing Custom Switch Feature Status Information](https://msdn.microsoft.com/library/windows/hardware/hh598193).

### Return Status Codes

The extension returns one of the following status codes for the OID method request of OID\_SWITCH\_FEATURE\_STATUS\_QUERY.

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
<td><p>The length of the information buffer is too small to return the feature status information as well as the [<strong>NDIS_SWITCH_FEATURE_STATUS_CUSTOM</strong>](https://msdn.microsoft.com/library/windows/hardware/hh598207) and [<strong>NDIS_SWITCH_FEATURE_STATUS_PARAMETERS</strong>](https://msdn.microsoft.com/library/windows/hardware/hh598208) structures. The underlying miniport edge of the extensible switch sets the <strong>DATA.METHOD_INFORMATION.BytesNeeded</strong> member in the [<strong>NDIS_OID_REQUEST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure to the minimum buffer size that is required.</p></td>
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

[**NDIS\_SWITCH\_PROPERTY\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/hh598257)

[**NDIS\_SWITCH\_FEATURE\_STATUS\_CUSTOM**](https://msdn.microsoft.com/library/windows/hardware/hh598207)

[**NDIS\_SWITCH\_FEATURE\_STATUS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598208)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_SWITCH_FEATURE_STATUS_QUERY%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


