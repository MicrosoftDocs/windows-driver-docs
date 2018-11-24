---
title: DEVPROP_TYPE_DEVPROPKEY
description: In Windows Vista and later versions of Windows, the DEVPROP_TYPE_DEVPROPKEY identifier represents the base-data-type identifier that indicates the data type is a DEVPROPKEY-typed device property key.
ms.assetid: 4b0f0f33-9a9e-498a-b2f3-e215bac68dd9
keywords: ["DEVPROP_TYPE_DEVPROPKEY Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_TYPE_DEVPROPKEY
api_location:
- Devpropdef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPROP_TYPE_DEVPROPKEY


In Windows Vista and later versions of Windows, the DEVPROP_TYPE_DEVPROPKEY identifier represents the base-data-type identifier that indicates the data type is a DEVPROPKEY-typed device property key.

Remarks
-------

The DEVPROP_TYPE_DEVPROPKEY property type can be combined only with the [**DEVPROP_TYPEMOD_ARRAY**](devprop-typemod-array.md) property-data-type modifier.

### Setting a Property of this Type

To set a property whose base data type is DEVPROP_TYPE_DEVPROPKEY, call the corresponding SetupDiSet*Xxx* property function and set the function input parameters as follows:

-   Set the *PropertyType* parameter to DEVPROP_TYPE_DEVPROPKEY, set the *PropertyBuffer* parameter to a pointer to a buffer that contains a DEVPROPKEY structure, and set the *PropertyBufferSize* parameter to `sizeof(DEVPROPKEY)`.

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

 

 





