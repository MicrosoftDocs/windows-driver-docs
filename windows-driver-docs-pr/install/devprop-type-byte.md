---
title: DEVPROP_TYPE_BYTE
description: In Windows Vista and later versions of Windows, the DEVPROP_TYPE_BYTE identifier represents the base-data-type identifier that indicates the data type is a BYTE-typed unsigned integer.
ms.assetid: cda681f0-948d-4534-bf56-2ad9dd8a845c
keywords: ["DEVPROP_TYPE_BYTE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_TYPE_BYTE
api_location:
- Devpropdef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPROP_TYPE_BYTE


In Windows Vista and later versions of Windows, the DEVPROP_TYPE_BYTE identifier represents the base-data-type identifier that indicates the data type is a BYTE-typed unsigned integer.

Remarks
-------

DEVPROP_TYPE_BYTE can be combined only with the [**DEVPROP_TYPEMOD_ARRAY**](devprop-typemod-array.md) property-data-type modifier.

### Setting a Property of this Type

To set a property whose data type is DEVPROP_TYPE_BYTE, call the corresponding SetupDiSet*Xxx* property function, setting the function input parameters as follows:

-   Set the *PropertyType* parameter to DEVPROP_TYPE_BYTE, set the *PropertyBuffer* parameter to a pointer to a buffer that can contain at least one BYTE value, and set the *PropertyBufferSize* parameter to `sizeof(BYTE)`.

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

 

 





