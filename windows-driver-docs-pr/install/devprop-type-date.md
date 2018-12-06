---
title: DEVPROP_TYPE_DATE
description: In Windows Vista and later versions of Windows, the DEVPROP_TYPE_DATE property type represents the base-data-type identifier that indicates that the data type is a DOUBLE-typed value that specifies the number of days since December 31, 1899.
ms.assetid: 0314e7da-d1da-4989-b2cd-90a51c3c8938
keywords: ["DEVPROP_TYPE_DATE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_TYPE_DATE
api_location:
- Devpropdef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPROP_TYPE_DATE


In Windows Vista and later versions of Windows, the DEVPROP_TYPE_DATE property type represents the base-data-type identifier that indicates that the data type is a DOUBLE-typed value that specifies the number of days since December 31, 1899. For example, January 1, 1900, is 1.0; January 2, 1900, is 2.0; and so on.

Remarks
-------

DEVPROP_TYPE_DATE can be combined only with the [**DEVPROP_TYPEMOD_ARRAY**](devprop-typemod-array.md) property-data-type modifier.

### Setting a Property of this Type

To set a property whose base data type is DEVPROP_TYPE_DATE, call the corresponding SetupDiSet*Xxx* property function and set the function input parameters as follows:

-   Set the *PropertyType* parameter to DEVPROP_TYPE_DATE, set the *PropertyBuffer* parameter to a pointer to a buffer that contains a DATE value, and set the *PropertyBufferSize* parameter to `sizeof(DATE)`.

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

 

 





