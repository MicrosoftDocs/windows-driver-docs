---
title: DEVPROP_TYPE_CURRENCY
description: In Windows Vista and later versions of Windows, the DEVPROP_TYPE_CURRENCY identifier represents the base-data-type identifier that indicates that the data type is a CURRENCY-typed value.
ms.assetid: e79d4351-79a0-4e7a-9290-dd02d317a958
keywords: ["DEVPROP_TYPE_CURRENCY Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_TYPE_CURRENCY
api_location:
- Devpropdef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPROP_TYPE_CURRENCY


In Windows Vista and later versions of Windows, the DEVPROP_TYPE_CURRENCY identifier represents the base-data-type identifier that indicates that the data type is a CURRENCY-typed value.

Remarks
-------

DEVPROP_TYPE_CURRENCY can be combined only with the [**DEVPROP_TYPEMOD_ARRAY**](devprop-typemod-array.md) property-data-type modifier.

### Setting a Property of This Type

To set a property whose base data type is DEVPROP_TYPE_CURRENCY, call the corresponding SetupDiSet*Xxx* property function and set the function input parameters as follows:

-   Set the *PropertyType* parameter to DEVPROP_TYPE_CURRENCY, set the *PropertyBuffer* parameter to a pointer to a buffer that contains a CURRENCY value, and set the *PropertyBufferSize* parameter to `sizeof(CURRENCY)`.

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

 

 





