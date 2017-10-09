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
---

# DEVPROP_TYPEMOD_ARRAY


In Windows Vista and later versions of Windows, the DEVPROP_TYPEMOD_ARRAY identifier represents a property-data-type modifier that can be combined with the [**base-data-type identifiers**](https://msdn.microsoft.com/library/windows/hardware/ff537793) to create a property-data-type identifier that represents an array of base-data-type values.

Remarks
-------

The DEVPROP_TYPEMOD_ARRAY identifier can be combined only with the fixed-length base-data-type identifiers ([**DEVPROPTYPE**](https://msdn.microsoft.com/library/windows/hardware/ff543546) values) that are associated with data. The DEVPROP_TYPEMOD_ARRAY identifier cannot be combined with [**DEVPROP_TYPE_EMPTY**](devprop-type-empty.md), [**DEVPROP_TYPE_NULL**](devprop-type-null.md), or any of the variable-length base-data-type identifiers.

To create a property-data-type identifier that represents an array of base-data-type values, perform a bitwise OR between DEVPROP_TYPEMOD_ARRAY and the corresponding DEVPROP_TYPE_*Xxx* identifier. For example, to specify an array of unsigned bytes, perform the following bitwise OR: (DEVPROP_TYPEMOD_ARRAY | [**DEVPROP_TYPE_BYTE**](devprop-type-byte.md)).

The size, in bytes, of an array of base-data-type values is the size, in bytes, of the array.

For information about how to create a property-data-type identifier that represents a REG_MULTI_SZ list of NULL-terminated Unicode strings, see [**DEVPROP_TYPEMOD_LIST**](devprop-typemod-list.md).

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DEVPROP_TYPEMOD_ARRAY%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





