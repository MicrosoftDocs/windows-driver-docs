---
title: DEVPROP_TYPE_BINARY
description: In Windows Vista and later versions of Windows, the DEVPROP_TYPE_BINARY identifier represents the base-data-type identifier that indicates that the data type is an array of BYTE-typed unsigned values.
ms.assetid: ee20f0f1-fff9-41a9-a880-f8f577320e41
keywords: ["DEVPROP_TYPE_BINARY Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_TYPE_BINARY
api_location:
- Devpropdef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPROP_TYPE_BINARY


In Windows Vista and later versions of Windows, the DEVPROP_TYPE_BINARY identifier represents the base-data-type identifier that indicates that the data type is an array of BYTE-typed unsigned values.

Remarks
-------

The DEVPROP_TYPE_BINARY property type cannot be combined with the property-data-type modifiers.

### Setting a Property of this Type

To set a property whose base data type is DEVPROP_TYPE_BINARY, call the corresponding SetupDiSet*Xxx* property function and set the function input parameters as follows:

-   Set the *PropertyType* parameter to DEVPROP_TYPE_BINARY, set the *PropertyBuffer* parameter to a pointer to a buffer that contains an array of BYTE value, and set the *PropertyBufferSize* parameter to the size, in bytes, of the buffer.

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

 

 





