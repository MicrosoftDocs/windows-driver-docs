---
title: DEVPROP_TYPE_DECIMAL
description: In Windows Vista and later versions of Windows, the DEVPROP_TYPE_INT64 identifier represents the base-data-type identifier that indicates that the data type is a DECIMAL-typed value.
ms.assetid: 3aacffd6-3259-489b-992d-e2771858c1e6
keywords: ["DEVPROP_TYPE_DECIMAL Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_TYPE_DECIMAL
api_location:
- Devpropdef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPROP_TYPE_DECIMAL


In Windows Vista and later versions of Windows, the DEVPROP_TYPE_INT64 identifier represents the base-data-type identifier that indicates that the data type is a DECIMAL-typed value.

Remarks
-------

DEVPROP_TYPE_DECIMAL can be combined only with the [**DEVPROP_TYPEMOD_ARRAY**](devprop-typemod-array.md) property-data-type modifier.

### Setting a Property of this Type

To set a property whose data type is DEVPROP_TYPE_DECIMAL, call the corresponding SetupDiSet*Xxx* property function and set the function input parameters as follows:

-   Set the *PropertyType* parameter to DEVPROP_TYPE_DECIMAL, set the *PropertyBuffer* parameter to a pointer to a buffer that can contain at least one DECIMAL value, and set the *PropertyBufferSize* parameter to `sizeof(DECIMAL)`.

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

 

 





