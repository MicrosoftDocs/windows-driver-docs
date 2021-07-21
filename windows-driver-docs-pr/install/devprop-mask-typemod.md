---
title: DEVPROP_MASK_TYPEMOD
description: In Windows Vista and later versions of Windows, the DEVPROP_MASK_TYPEMOD mask can be combined in a bitwise AND with a property-data-type identifier to extract the DEVPROP_TYPEMOD_Xxx property-data-type modifier from a property-data-type identifier.
keywords: ["DEVPROP_MASK_TYPEMOD Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_MASK_TYPEMOD
api_location:
- Devpropdef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPROP_MASK_TYPEMOD


In Windows Vista and later versions of Windows, the DEVPROP_MASK_TYPEMOD mask can be combined in a bitwise AND with a [property-data-type identifier](/previous-versions/ff541476(v=vs.85)) to extract the DEVPROP_TYPEMOD_*Xxx* [**property-data-type modifier**](/previous-versions/ff549770(v=vs.85)) from a property-data-type identifier.

## Remarks

This mask cannot be used as a base-data-type identifier, a property-data-type modifier, or property-data-type identifier.

For information about how to extract the [**base-data-type identifier**](/previous-versions/ff537793(v=vs.85)) from a property-data-type identifier, see [**DEVPROP_MASK_TYPE**](devprop-mask-type.md).

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

## See also


[**DEVPROP_MASK_TYPE**](devprop-mask-type.md)

 

