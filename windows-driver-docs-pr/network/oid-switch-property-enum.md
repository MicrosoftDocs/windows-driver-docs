---
title: OID_SWITCH_PROPERTY_ENUM
author: windows-driver-content
description: The Hyper-V extensible switch extension issues an object identifier (OID) method request of OID_SWITCH_PROPERTY_ENUM to obtain an array.
ms.assetid: 45277355-4486-4CE0-ACBF-68D6BC6B79E7
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_SWITCH_PROPERTY_ENUM Network Drivers Starting with Windows Vista
---

# OID\_SWITCH\_PROPERTY\_ENUM


The Hyper-V extensible switch extension issues an object identifier (OID) method request of OID\_SWITCH\_PROPERTY\_ENUM to obtain an array. This array contains the provisioned switch policies that match the specified criteria. Each element in the array specifies the properties of an extensible switch policy.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to a buffer. This buffer contains the following data:

-   An [**NDIS\_SWITCH\_PROPERTY\_ENUM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598253) structure that specifies the parameters for the extensible switch policy enumeration.

-   An array of [**NDIS\_SWITCH\_PROPERTY\_ENUM\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh598250) structures. Each of these structures contains information about an extensible switch policy.

    **Note**  If the extension has not been provisioned with instances of the specified extensible switch policy, the extension sets the **NumProperties** member of the [**NDIS\_SWITCH\_PROPERTY\_ENUM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598253) structure to zero and no [**NDIS\_SWITCH\_PROPERTY\_ENUM\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh598250) structures are returned.

     

Remarks
-------

The OID\_SWITCH\_PROPERTY\_ENUM OID must only be issued when the Hyper-V extensible switch has completed activation. Please see [Querying the Hyper-V Extensible Switch Configuration](https://msdn.microsoft.com/library/windows/hardware/hh598293) for more details.

Unlike OID query requests of [OID\_SWITCH\_PORT\_PROPERTY\_ENUM](oid-switch-port-property-enum.md), the extension does not have to call any *ReferenceSwitchXxx* or *DereferenceSwitchXxx* functions when it issues the OID\_SWITCH\_PROPERTY\_ENUM request down the extensible switch driver stack.

**Note**  If the extension receives the OID method request of OID\_SWITCH\_PROPERTY\_ENUM, it must not complete the OID request. Instead, it must call [**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830) to forward the OID request down the extensible switch driver stack.

 

### Return Status Codes

The underlying miniport edge of the extensible switch completes the OID query request of OID\_SWITCH\_PROPERTY\_ENUM and returns one of the following status codes.

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
<td><p>The length of the information buffer is too small to return the [<strong>NDIS_SWITCH_PROPERTY_ENUM_PARAMETERS</strong>](https://msdn.microsoft.com/library/windows/hardware/hh598253) structure and its array of [<strong>NDIS_SWITCH_PROPERTY_ENUM_INFO</strong>](https://msdn.microsoft.com/library/windows/hardware/hh598250) elements. The underlying miniport edge of the extensible switch sets the <strong>DATA.METHOD_INFORMATION.BytesNeeded</strong> member in the [<strong>NDIS_OID_REQUEST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure to the minimum buffer size that is required.</p></td>
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

[**NDIS\_SWITCH\_PROPERTY\_ENUM\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh598250)

[**NDIS\_SWITCH\_PROPERTY\_ENUM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598253)

[Querying the Hyper-V Extensible Switch Configuration](https://msdn.microsoft.com/library/windows/hardware/hh598293)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_SWITCH_PROPERTY_ENUM%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


