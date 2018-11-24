---
title: DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING
description: In Windows Vista and later versions of Windows, the DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING identifier represents the base-data-type identifier that indicates the data type is a NULL-terminated Unicode string that contains a security descriptor in the Security Descriptor Definition Language (SDDL) format.
ms.assetid: 2d791816-bb0e-4275-953f-1492886e9545
keywords: ["DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING
api_location:
- Devpropdef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING


In Windows Vista and later versions of Windows, the DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING identifier represents the base-data-type identifier that indicates the data type is a NULL-terminated Unicode string that contains a security descriptor in the Security Descriptor Definition Language (SDDL) format.

Remarks
-------

DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING can be combined only with the [**DEVPROP_TYPEMOD_LIST**](devprop-typemod-list.md) property-data-type modifier.

### Setting a Property of this Type

To set a property whose base data type is DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING, call the corresponding **SetupDiSet*Xxx*** property function and set the function input parameters as follows:

-   Set the *PropertyType* parameter to DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING, set the *PropertyBuffer* parameter to a pointer to a buffer that contains a NULL-terminated security descriptor string, and set the *PropertyBufferSize* parameter to the size, in bytes, of the security descriptor string, including the NULL terminator.

-   Set the other function input parameters as appropriate to set the property.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Devpropdef.h (include Devpropdef.h)</td>
</tr>
</tbody>
</table>

 

 





