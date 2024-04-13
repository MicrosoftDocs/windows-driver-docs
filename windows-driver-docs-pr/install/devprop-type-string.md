---
title: DEVPROP_TYPE_STRING
description: In Windows Vista and later versions of Windows, the DEVPROP_TYPE_STRING property type represents the base-data-type identifier that indicates that the data type is a NULL-terminated Unicode string.
keywords: ["DEVPROP_TYPE_STRING Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_TYPE_STRING
api_location:
- Devpropdef.h
api_type:
- HeaderDef
ms.date: 10/17/2018
ms.topic: reference
---

# DEVPROP_TYPE_STRING


In Windows Vista and later versions of Windows, the DEVPROP_TYPE_STRING property type represents the base-data-type identifier that indicates that the data type is a NULL-terminated Unicode string.

## Remarks

DEVPROP_TYPE_STRING can be combined only with the [**DEVPROP_TYPEMOD_LIST**](devprop-typemod-list.md) property-data-type modifier.

### Setting a Property of this Type

To set a property whose base data type is DEVPROP_TYPE_STRING, call the corresponding **SetupDiSet*Xxx*** property function, setting the function input parameters as follows:

-   Set the *PropertyType* parameter to DEVPROP_TYPE_STRING, set the *PropertyBuffer* parameter to a pointer to a buffer that contains a NULL-terminated Unicode string, and set the *PropertyBufferSize* parameter to the size, in bytes, of the string, including the NULL terminator.

-   Set the other function input parameters as appropriate to set the property.

## Requirements

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

 

 





