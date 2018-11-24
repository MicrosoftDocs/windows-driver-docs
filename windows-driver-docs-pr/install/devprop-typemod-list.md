---
title: DEVPROP_TYPEMOD_LIST
description: In Windows Vista and later versions of Windows, the DEVPROP_TYPEMOD_LIST identifier represents a property-data-type modifier that can be combined only with the base-data-type identifiers DEVPROP_TYPE_STRING and DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING to create a property-data-type identifier that represents a [REG_MULTI_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) list of NULL-terminated Unicode strings.
ms.assetid: 0beaa778-55c9-45ac-8163-91d82794a845
keywords: ["DEVPROP_TYPEMOD_LIST Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_TYPEMOD_LIST
api_location:
- Devpropdef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPROP_TYPEMOD_LIST


In Windows Vista and later versions of Windows, the DEVPROP_TYPEMOD_LIST identifier represents a property-data-type modifier that can be combined only with the [**base-data-type identifiers**](https://msdn.microsoft.com/library/windows/hardware/ff537793) [**DEVPROP_TYPE_STRING**](devprop-type-string.md) and [**DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING**](devprop-type-security-descriptor-string.md) to create a property-data-type identifier that represents a [REG_MULTI_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) list of NULL-terminated Unicode strings.

Remarks
-------

DEVPROP_TYPEMOD_LIST cannot be combined with [**DEVPROP_TYPE_EMPTY**](devprop-type-empty.md), [**DEVPROP_TYPE_NULL**](devprop-type-null.md), [**DEVPROP_TYPE_SECURITY_DESCRIPTOR**](devprop-type-security-descriptor.md), or any of the fixed length base-data-type identifiers.

To create a property-data-type identifier that represents a string list, perform a bitwise OR between the DEVPROP_TYPEMOD_LIST property-data-type modifier and the corresponding DEVPROP_TYPE_Xxx identifier. For example, to specify a [REG_MULTI_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) list of Unicode strings, perform the following bitwise OR: (DEVPROP_TYPEMOD_LIST | DEVPROP_TYPE_STRING).

The size of a [REG_MULTI_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) list of NULL-terminated Unicode strings is size of the list including the final **NULL** that terminated the list.

For information about how to create a property-data-type identifier that represents an array of fixed length data values, see [**DEVPROP_TYPEMOD_ARRAY**](devprop-typemod-array.md).

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


[**DEVPROP_TYPEMOD_ARRAY**](devprop-typemod-array.md)

 

 






