---
title: DEVPROP_MASK_TYPE
description: In Windows Vista and later versions of Windows, the DEVPROP_MASK_TYPE mask can be combined in a bitwise AND with a property-data-type identifier to extract the base-data-type identifier from a property-data-type identifier.
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


In Windows Vista and later versions of Windows, the DEVPROP_MASK_TYPE mask can be combined in a bitwise AND with a [property-data-type identifier](/previous-versions/ff541476(v=vs.85)) to extract the [**base-data-type identifier**](/previous-versions/ff537793(v=vs.85)) from a property-data-type identifier.

## Remarks

This mask cannot be used as a base-data-type identifier, a property-data-type modifier, or a property-data-type identifier.

For information about how to extract the DEVPROP_TYPEMOD_Xxx [**property-data-type modifier**](/previous-versions/ff549770(v=vs.85)) from a property-data-type identifier, see [**DEVPROP_MASK_TYPEMOD**](devprop-mask-typemod.md).

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


[**DEVPROP_MASK_TYPEMOD**](devprop-mask-typemod.md)

 

