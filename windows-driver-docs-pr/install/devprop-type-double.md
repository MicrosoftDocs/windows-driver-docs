---
title: DEVPROP_TYPE_DOUBLE
description: In Windows Vista and later versions of Windows, the DEVPROP_TYPE_DOUBLE identifier represents the base-data-type identifier that indicates that the data type is a DOUBLE-typed IEEE floating-point number.
ms.assetid: c04f8538-ce0d-4eaf-a4d5-86968dbc18fd
keywords: ["DEVPROP_TYPE_DOUBLE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_TYPE_DOUBLE
api_location:
- Devpropdef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPROP_TYPE_DOUBLE


In Windows Vista and later versions of Windows, the DEVPROP_TYPE_DOUBLE identifier represents the base-data-type identifier that indicates that the data type is a DOUBLE-typed IEEE floating-point number.

Remarks
-------

DEVPROP_TYPE_DOUBLE can be combined only with the [**DEVPROP_TYPEMOD_ARRAY**](devprop-typemod-array.md) property-data-type modifier.

### Setting a Property of this Type

To set a property whose base data type is DEVPROP_TYPE_DOUBLE, call the corresponding SetupDiSet*Xxx* property function and set the function input parameters as follows:

-   Set the *PropertyType* parameter to DEVPROP_TYPE_DOUBLE, set the *PropertyBuffer* parameter to a pointer to a buffer that can contain at least one ULONG value, and set the *PropertyBufferSize* parameter to `sizeof(DOUBLE)`.

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

 

 





