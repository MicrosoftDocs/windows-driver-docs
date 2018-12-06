---
title: DEVPROP_TYPE_FILETIME
description: In Windows Vista and later versions of Windows, the DEVPROP_TYPE_FILETIME property type represents the base-data-type identifier that indicates that the data type is a FILETIME-typed value.
ms.assetid: e81585ae-ee47-456b-b29b-24217fab5f9a
keywords: ["DEVPROP_TYPE_FILETIME Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_TYPE_FILETIME
api_location:
- Devpropdef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPROP_TYPE_FILETIME


In Windows Vista and later versions of Windows, the DEVPROP_TYPE_FILETIME property type represents the base-data-type identifier that indicates that the data type is a FILETIME-typed value.

Remarks
-------

We recommend that all time values be represented in Coordinated Universal Time (UTC) units.

DEVPROP_TYPE_FILETIME can be combined only with the [**DEVPROP_TYPEMOD_ARRAY**](devprop-typemod-array.md) property-data-type modifier.

### Setting a Property of this Type

To set a property whose base data type is DEVPROP_TYPE_FILETIME, call the corresponding SetupDiSet*Xxx* property function and set the function input parameters as follows:

-   Set the *PropertyType* parameter to DEVPROP_TYPE_DATE, set the *PropertyBuffer* parameter to a pointer to a buffer that contains a FILETIME structure, and set the *PropertyBufferSize* parameter to `sizeof(FILETIME)`.

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

 

 





