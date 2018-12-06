---
title: DEVPROP_TYPEMOD_ARRAY
description: In Windows Vista and later versions of Windows, the DEVPROP_TYPEMOD_ARRAY identifier represents a property-data-type modifier that can be combined with the base-data-type identifiers to create a property-data-type identifier that represents an array of base-data-type values.
ms.assetid: 33f12b66-c81a-451b-851a-b58a34a8fe9e
keywords: ["DEVPROP_TYPEMOD_ARRAY Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_TYPEMOD_ARRAY
api_location:
- Devpropdef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPROP_TYPEMOD_ARRAY


In Windows Vista and later versions of Windows, the DEVPROP_TYPEMOD_ARRAY identifier represents a property-data-type modifier that can be combined with the [**base-data-type identifiers**](https://msdn.microsoft.com/library/windows/hardware/ff537793) to create a property-data-type identifier that represents an array of base-data-type values.

Remarks
-------

The DEVPROP_TYPEMOD_ARRAY identifier can be combined only with the fixed-length base-data-type identifiers ([**DEVPROPTYPE**](https://msdn.microsoft.com/library/windows/hardware/ff543546) values) that are associated with data. The DEVPROP_TYPEMOD_ARRAY identifier cannot be combined with [**DEVPROP_TYPE_EMPTY**](devprop-type-empty.md), [**DEVPROP_TYPE_NULL**](devprop-type-null.md), or any of the variable-length base-data-type identifiers.

To create a property-data-type identifier that represents an array of base-data-type values, perform a bitwise OR between DEVPROP_TYPEMOD_ARRAY and the corresponding DEVPROP_TYPE_*Xxx* identifier. For example, to specify an array of unsigned bytes, perform the following bitwise OR: (DEVPROP_TYPEMOD_ARRAY | [**DEVPROP_TYPE_BYTE**](devprop-type-byte.md)).

The size, in bytes, of an array of base-data-type values is the size, in bytes, of the array.

For information about how to create a property-data-type identifier that represents a [REG_MULTI_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) list of NULL-terminated Unicode strings, see [**DEVPROP_TYPEMOD_LIST**](devprop-typemod-list.md).

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

## See also


[**DEVPROPTYPE**](https://msdn.microsoft.com/library/windows/hardware/ff543546)

[**DEVPROP_TYPEMOD_LIST**](devprop-typemod-list.md)

 

 






