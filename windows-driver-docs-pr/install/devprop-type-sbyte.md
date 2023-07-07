---
title: DEVPROP_TYPE_SBYTE
description: In Windows Vista and later versions of Windows, the DEVPROP_TYPE_SBYTE identifier represents the base-data-type identifier that indicates the data type is a SBYTE-typed signed integer.
keywords: ["DEVPROP_TYPE_SBYTE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_TYPE_SBYTE
api_location:
- Devpropdef.h
api_type:
- HeaderDef
ms.date: 10/17/2018
ms.topic: reference
---

# DEVPROP_TYPE_SBYTE


The DEVPROP_TYPE_SBYTE identifier represents the base-data-type identifier that indicates the data type is a SBYTE-typed signed integer.

## Remarks

DEVPROP_TYPE_SBYTE can be combined only with the [**DEVPROP_TYPEMOD_ARRAY**](devprop-typemod-array.md) property-data-type modifier.

**Setting a Property of this Type**

To set a property whose data type is DEVPROP_TYPE_SBYTE, call the corresponding **SetupDiSet*Xxx*** property function, and set the function parameters as follows:

- Set the *PropertyType* parameter to DEVPROP_TYPE_SBYTE, set the *PropertyBuffer* parameter to a pointer to a buffer that can contain at least one SBYTE value, and set the *PropertyBufferSize* parameter to <strong>sizeof(</strong>SBYTE<strong>)</strong>.

- Set the other function input parameters as appropriate to set the property.

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

 

 





