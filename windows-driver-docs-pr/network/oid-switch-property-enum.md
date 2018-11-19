---
title: OID_SWITCH_PROPERTY_ENUM
description: The Hyper-V extensible switch extension issues an object identifier (OID) method request of OID_SWITCH_PROPERTY_ENUM to obtain an array.
ms.assetid: 45277355-4486-4CE0-ACBF-68D6BC6B79E7
ms.date: 08/08/2017
keywords: 
 -OID_SWITCH_PROPERTY_ENUM Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
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
<td><p>The length of the information buffer is too small to return the <a href="https://msdn.microsoft.com/library/windows/hardware/hh598253" data-raw-source="[&lt;strong&gt;NDIS_SWITCH_PROPERTY_ENUM_PARAMETERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh598253)"><strong>NDIS_SWITCH_PROPERTY_ENUM_PARAMETERS</strong></a> structure and its array of <a href="https://msdn.microsoft.com/library/windows/hardware/hh598250" data-raw-source="[&lt;strong&gt;NDIS_SWITCH_PROPERTY_ENUM_INFO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh598250)"><strong>NDIS_SWITCH_PROPERTY_ENUM_INFO</strong></a> elements. The underlying miniport edge of the extensible switch sets the <strong>DATA.METHOD_INFORMATION.BytesNeeded</strong> member in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566710)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
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

 

 




