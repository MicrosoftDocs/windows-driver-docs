---
title: DEVPROP_TYPE_UINT64
description: In Windows Vista and later versions of Windows, the DEVPROP_TYPE_INT64 identifier represents the base-data-type identifier that indicates that the data type is a ULONG64-typed unsigned integer.
ms.assetid: a6dfb90d-0cae-4b63-bc27-57d7b0f6b897
keywords: ["DEVPROP_TYPE_UINT64 Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_TYPE_UINT64
api_location:
- Devpropdef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPROP_TYPE_UINT64


In Windows Vista and later versions of Windows, the DEVPROP_TYPE_INT64 identifier represents the base-data-type identifier that indicates that the data type is a ULONG64-typed unsigned integer.

Remarks
-------

DEVPROP_TYPE_UINT64 can be combined only with the [**DEVPROP_TYPEMOD_ARRAY**](devprop-typemod-array.md) property-data-type modifier.

**Setting a Property of this Type**

To set a property whose base data type is DEVPROP_TYPE_UINT64, call the corresponding **SetupDiSet*Xxx*** property function and set the function input parameters as follows:

- Set the *PropertyType* parameter to DEVPROP_TYPE_UINT64, set the *PropertyBuffer* parameter to a pointer to a buffer that can contain at least one ULONG64 value, and set the *PropertyBufferSize* parameter to <strong>sizeof(</strong>ULONG64<strong>)</strong>.

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

 

 





