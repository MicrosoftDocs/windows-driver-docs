---
title: DEVPROP_MASK_TYPE
description: In Windows Vista and later versions of Windows, the DEVPROP_MASK_TYPE mask can be combined in a bitwise AND with a property-data-type identifier to extract the base-data-type identifier from a property-data-type identifier.
ms.assetid: 5d1d5cb2-d967-47b4-bde7-fdf4248b1913
keywords: ["DEVPROP_MASK_TYPE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_MASK_TYPE
api_location:
- Devpropdef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPROP_MASK_TYPE


In Windows Vista and later versions of Windows, the DEVPROP_MASK_TYPE mask can be combined in a bitwise AND with a [property-data-type identifier](https://msdn.microsoft.com/library/windows/hardware/ff541476) to extract the [**base-data-type identifier**](https://msdn.microsoft.com/library/windows/hardware/ff537793) from a property-data-type identifier.

Remarks
-------

This mask cannot be used as a base-data-type identifier, a property-data-type modifier, or a property-data-type identifier.

For information about how to extract the DEVPROP_TYPEMOD_Xxx [**property-data-type modifier**](https://msdn.microsoft.com/library/windows/hardware/ff549770) from a property-data-type identifier, see [**DEVPROP_MASK_TYPEMOD**](devprop-mask-typemod.md).

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


[**DEVPROP_MASK_TYPEMOD**](devprop-mask-typemod.md)

 

 






