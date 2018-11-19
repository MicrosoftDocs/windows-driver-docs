---
title: OID_SWITCH_PROPERTY_ADD
description: The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID_SWITCH_PROPERTY_ADD to notify extensible switch extensions about the addition of a switch policy property.
ms.assetid: 63A6D2BE-81F4-4D27-B5DF-68466EFF306E
ms.date: 08/08/2017
keywords: 
 -OID_SWITCH_PROPERTY_ADD Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_SWITCH\_PROPERTY\_ADD


The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID\_SWITCH\_PROPERTY\_ADD to notify extensible switch extensions about the addition of a switch policy property

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to a buffer. This buffer contains the following data:

-   An [**NDIS\_SWITCH\_PROPERTY\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598255) structure that specifies the identification and type of an extensible switch policy.

-   A property buffer that contains the parameters for an extensible switch policy. The property buffer contains a structure that is based on the **PropertyType** member of the [**NDIS\_SWITCH\_PROPERTY\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598255) structure.

    **Note**  Starting with Windows Server 2012, the **PropertyType** member must be set to **NdisSwitchPropertyTypeCustom** and the property buffer must contain an [**NDIS\_SWITCH\_PROPERTY\_CUSTOM**](https://msdn.microsoft.com/library/windows/hardware/hh598247) structure.

     

Remarks
-------

A forwarding extension can handle the OID set request of OID\_SWITCH\_PROPERTY\_ADD. All other types of extensions must call [**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830) to forward the OID request to the next extension in the extensible switch driver stack.

The extension can veto the addition of the switch property by returning NDIS\_STATUS\_DATA\_NOT\_ACCEPTED for the OID request. For example, if an extension cannot allocate resources to enforce its updated policies on the switch, it should veto the addition request.

**Note**  If the extension returns other NDIS\_STATUS\_*Xxx* error status codes, the creation notification is also vetoed. However, returning status codes for transitory scenarios, such as returning NDIS\_STATUS\_RESOURCES, could result in a retry of the creation notification.

 

If the extension does not veto the OID request, it should monitor the status when the request is completed. The extension should do this to determine whether the OID request was vetoed by underlying extensions in the extensible switch control path or by the extensible switch interface.

For guidelines on how to handle an OID set request of OID\_SWITCH\_PROPERTY\_ADD, see [Managing Switch Policies](https://msdn.microsoft.com/library/windows/hardware/hh598203).

### Return Status Codes

If the forwarding extension completes the OID set request of OID\_SWITCH\_PROPERTY\_ADD, it returns one of the following status codes.

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
<td><p>NDIS_STATUS_DATA_NOT_ACCEPTED</p></td>
<td><p>The extension has vetoed the switch policy addition notification.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_FAILURE</p></td>
<td><p>The OID request failed for other reasons.</p></td>
</tr>
</tbody>
</table>

 

If the extension does not complete the OID set request of OID\_SWITCH\_PROPERTY\_ADD, the request is completed by the underlying miniport edge of the extensible switch. The miniport edge returns the following status code.

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

[**NDIS\_SWITCH\_PROPERTY\_CUSTOM**](https://msdn.microsoft.com/library/windows/hardware/hh598247)

[**NDIS\_SWITCH\_PROPERTY\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598255)

[**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830)

 

 




