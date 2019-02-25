---
title: DEVPROP_TYPE_GUID
description: In Windows Vista and later versions of Windows, the DEVPROP_TYPE_GUID identifier represents the base-data-type identifier that indicates that the data type is a GUID-typed globally unique identifier (GUID).
ms.assetid: 77080860-c2b3-4c7c-8ab8-e0b02582ffbb
keywords: ["DEVPROP_TYPE_GUID Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_TYPE_GUID
api_location:
- Devpropdef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPROP_TYPE_GUID


In Windows Vista and later versions of Windows, the DEVPROP_TYPE_GUID identifier represents the base-data-type identifier that indicates that the data type is a GUID-typed globally unique identifier (GUID).

Remarks
-------

DEVPROP_TYPE_GUID can be combined only with the [**DEVPROP_TYPEMOD_ARRAY**](devprop-typemod-array.md) property-data-type modifier.

### Setting a Property of this Type

To set a property whose base data type is DEVPROP_TYPE_GUID, call the corresponding SetupDiSet*Xxx* property function and set the function input parameters as follows:

-   Set the *PropertyType* parameter to DEVPROP_TYPE_GUID, set the *PropertyBuffer* parameter to a pointer to a buffer that contains a GUID value, and set the *PropertyBufferSize* parameter to `sizeof(GUID)`.

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

 

 





