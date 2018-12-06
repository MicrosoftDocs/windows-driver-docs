---
title: DEVPROP_TYPE_SECURITY_DESCRIPTOR
description: In Windows Vista and later versions of Windows, the DEVPROP_TYPE_SECURITY_DESCRIPTOR identifier represents the base-data-type identifier that indicates the data type is a variable-length, self-relative, SECURITY_DESCRIPTOR-typed, security descriptor.
ms.assetid: e8eea343-adaa-41b8-9556-962b5e6903fb
keywords: ["DEVPROP_TYPE_SECURITY_DESCRIPTOR Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_TYPE_SECURITY_DESCRIPTOR
api_location:
- Devpropdef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPROP_TYPE_SECURITY_DESCRIPTOR


In Windows Vista and later versions of Windows, the DEVPROP_TYPE_SECURITY_DESCRIPTOR identifier represents the base-data-type identifier that indicates the data type is a variable-length, self-relative, SECURITY_DESCRIPTOR-typed, security descriptor.

Remarks
-------

DEVPROP_TYPE_SECURITY_DESCRIPTOR cannot be combined with the property-data-type modifiers.

### Setting a Property of this Type

To set a property whose base data type is DEVPROP_TYPE_SECURITY_DESCRIPTOR, call the corresponding **SetupDiSet*Xxx*** property function and set the function input parameters as follows:

-   Set the *PropertyType* parameter to DEVPROP_TYPE_SECURITY_DESCRIPTOR, set the *PropertyBuffer* parameter to a pointer to a buffer that contains a variable length SECURITY_DESCRIPTOR structure, and set the *PropertyBufferSize* parameter to the size, in bytes, of the security descriptor structure.

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

 

 





