---
title: DEVPROP_TYPE_DEVPROPTYPE
description: In Windows Vista and later versions of Windows, the DEVPROP_TYPE_DEVPROPTYPE identifier represents the base-data-type identifier that indicates the data type is a DEVPROPTYPE-typed value.
ms.assetid: d50a26d4-0af5-4cc5-aaa4-8587b64fc1a8
keywords: ["DEVPROP_TYPE_DEVPROPTYPE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_TYPE_DEVPROPTYPE
api_location:
- Devpropdef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPROP_TYPE_DEVPROPTYPE


In Windows Vista and later versions of Windows, the DEVPROP_TYPE_DEVPROPTYPE identifier represents the base-data-type identifier that indicates the data type is a DEVPROPTYPE-typed value.

Remarks
-------

The DEVPROP_TYPE_DEVPROPTYPE property type can be combined only with the [**DEVPROP_TYPEMOD_ARRAY**](devprop-typemod-array.md) property-data-type modifier.

### Setting a Property of this Type

To set a property whose base data type is DEVPROP_TYPE_DEVPROPTYPE, call the corresponding SetupDiSet*Xxx* property function, setting the function input parameters as follows:

-   Set the *PropertyType* parameter to DEVPROP_TYPE_DEVPROPTYPE, set the *PropertyBuffer* parameter to a pointer to a buffer that contains a DEVPROPTYPE value, and set the *PropertyBufferSize* parameter to `sizeof(DEVPROPTYPE)`.

-   Set the remaining function parameters as appropriate to set the property.

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

 

 





