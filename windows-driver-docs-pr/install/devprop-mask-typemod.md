---
title: DEVPROP_MASK_TYPEMOD
description: In Windows Vista and later versions of Windows, the DEVPROP_MASK_TYPEMOD mask can be combined in a bitwise AND with a property-data-type identifier to extract the DEVPROP_TYPEMOD_Xxx property-data-type modifier from a property-data-type identifier.
ms.assetid: 9ed153d7-dd37-4978-9e03-44efac2ab97a
keywords: ["DEVPROP_MASK_TYPEMOD Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_MASK_TYPEMOD
api_location:
- Devpropdef.h
api_type:
- HeaderDef
---

# DEVPROP_MASK_TYPEMOD


In Windows Vista and later versions of Windows, the DEVPROP_MASK_TYPEMOD mask can be combined in a bitwise AND with a [property-data-type identifier](https://msdn.microsoft.com/library/windows/hardware/ff541476) to extract the DEVPROP_TYPEMOD_*Xxx* [**property-data-type modifier**](https://msdn.microsoft.com/library/windows/hardware/ff549770) from a property-data-type identifier.

Remarks
-------

This mask cannot be used as a base-data-type identifier, a property-data-type modifier, or property-data-type identifier.

For information about how to extract the [**base-data-type identifier**](https://msdn.microsoft.com/library/windows/hardware/ff537793) from a property-data-type identifier, see [**DEVPROP_MASK_TYPE**](devprop-mask-type.md).

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


[**DEVPROP_MASK_TYPE**](devprop-mask-type.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DEVPROP_MASK_TYPEMOD%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





