---
title: DEVPROP_TYPE_SBYTE
description: In Windows Vista and later versions of Windows, the DEVPROP_TYPE_BYTE identifier represents the base-data-type identifier that indicates the data type is a SBYTE-typed signed integer.
ms.assetid: d2c503aa-4427-4745-b3c2-57b6ebd0e93c
keywords: ["DEVPROP_TYPE_SBYTE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_TYPE_SBYTE
api_location:
- Devpropdef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPROP_TYPE_SBYTE


In Windows Vista and later versions of Windows, the DEVPROP_TYPE_BYTE identifier represents the base-data-type identifier that indicates the data type is a SBYTE-typed signed integer.

Remarks
-------

DEVPROP_TYPE_SBYTE can be combined only with the [**DEVPROP_TYPEMOD_ARRAY**](devprop-typemod-array.md) property-data-type modifier.

**Setting a Property of this Type**

To set a property whose data type is DEVPROP_TYPE_BYTE, call the corresponding **SetupDiSet*Xxx*** property function, and set the function parameters as follows:

- Set the *PropertyType* parameter to DEVPROP_TYPE_BYTE, set the *PropertyBuffer* parameter to a pointer to a buffer that can contain at least one BYTE value, and set the *PropertyBufferSize* parameter to <strong>sizeof(</strong>BYTE<strong>)</strong>.

- Set the other function input parameters as appropriate to set the property.

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

 

 





