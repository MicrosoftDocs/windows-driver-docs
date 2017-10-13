---
title: DEVPROP_TYPEMOD_LIST
description: In Windows Vista and later versions of Windows, the DEVPROP_TYPEMOD_LIST identifier represents a property-data-type modifier that can be combined only with the base-data-type identifiers DEVPROP_TYPE_STRING and DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING to create a property-data-type identifier that represents a REG_MULTI_SZ list of NULL-terminated Unicode strings.
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
---

# DEVPROP_TYPEMOD_LIST


In Windows Vista and later versions of Windows, the DEVPROP_TYPEMOD_LIST identifier represents a property-data-type modifier that can be combined only with the [**base-data-type identifiers**](https://msdn.microsoft.com/library/windows/hardware/ff537793) [**DEVPROP_TYPE_STRING**](devprop-type-string.md) and [**DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING**](devprop-type-security-descriptor-string.md) to create a property-data-type identifier that represents a REG_MULTI_SZ list of NULL-terminated Unicode strings.

Remarks
-------

DEVPROP_TYPEMOD_LIST cannot be combined with [**DEVPROP_TYPE_EMPTY**](devprop-type-empty.md), [**DEVPROP_TYPE_NULL**](devprop-type-null.md), [**DEVPROP_TYPE_SECURITY_DESCRIPTOR**](devprop-type-security-descriptor.md), or any of the fixed length base-data-type identifiers.

To create a property-data-type identifier that represents a string list, perform a bitwise OR between the DEVPROP_TYPEMOD_LIST property-data-type modifier and the corresponding DEVPROP_TYPE_Xxx identifier. For example, to specify a REG_MULTI_SZ list of Unicode strings, perform the following bitwise OR: (DEVPROP_TYPEMOD_LIST | DEVPROP_TYPE_STRING).

The size of a REG_MULTI_SZ list of NULL-terminated Unicode strings is size of the list including the final **NULL** that terminated the list.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DEVPROP_TYPEMOD_LIST%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





