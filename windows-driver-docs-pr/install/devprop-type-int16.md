---
title: DEVPROP_TYPE_INT16
description: In Windows Vista and later versions of Windows, the DEVPROP_TYPE_INT16 identifier represents the base-data-type identifier that indicates the data type is a SHORT-typed signed integer.
ms.assetid: a126a7c2-744e-4eaf-9b3d-45bd4286de73
keywords: ["DEVPROP_TYPE_INT16 Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_TYPE_INT16
api_location:
- Devpropdef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPROP_TYPE_INT16


In Windows Vista and later versions of Windows, the DEVPROP_TYPE_INT16 identifier represents the base-data-type identifier that indicates the data type is a SHORT-typed signed integer.

Remarks
-------

DEVPROP_TYPE_SHORT can be combined only with the [**DEVPROP_TYPEMOD_ARRAY**](devprop-typemod-array.md) property-data-type modifier.

**Setting a Property of this Type**

To set a property whose base data type is DEVPROP_TYPE_INT16, call the corresponding **SetupDiSet*Xxx*** property function and set the function input parameters as follows:

- Set the *PropertyType* parameter to DEVPROP_TYPE_INT16, set the *PropertyBuffer* parameter to a pointer to a buffer that can contain at least one SHORT value, and set the *PropertyBufferSize* parameter to <strong>sizeof(</strong>SHORT<strong>)</strong>.

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

 

 





