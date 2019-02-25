---
title: DEVPROP_TYPE_STRING_LIST
description: In Windows Vista and later versions of Windows, the DEVPROP_TYPE_STRING_LIST property type represents the base-data-type identifier that indicates that the data type is a [REG_MULTI_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types)-typed list of Unicode strings.
ms.assetid: 91cfba02-cdd4-4918-8fc1-7e7793058074
keywords: ["DEVPROP_TYPE_STRING_LIST Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_TYPE_STRING_LIST
api_location:
- Devpropdef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPROP_TYPE_STRING_LIST


In Windows Vista and later versions of Windows, the DEVPROP_TYPE_STRING_LIST property type represents the base-data-type identifier that indicates that the data type is a [REG_MULTI_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types)-typed list of Unicode strings.

Remarks
-------

DEVPROP_TYPE_STRING_LIST cannot be combined with the property-data-type modifiers.

### Setting a Property of this Type

To set a property whose base data type is DEVPROP_TYPE_STRING_LIST, call the corresponding **SetupDiSet*Xxx*** property function and set the function input parameters as follows:

-   Set the *PropertyType* parameter to DEVPROP_TYPE_STRING_LIST, set the *PropertyBuffer* parameter to a pointer to a buffer that contains a [REG_MULTI_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) list of Unicode strings, and set the *PropertyBufferSize* parameter to the size, in bytes, of the list, including the final list NULL terminator.

-   Set the other function input parameters as appropriate to set the property.

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

 

 





