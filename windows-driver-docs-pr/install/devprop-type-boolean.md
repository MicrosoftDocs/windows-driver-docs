---
title: DEVPROP_TYPE_BOOLEAN
description: In Windows Vista and later versions of Windows, the DEVPROP_TYPE_BOOLEAN property type represents the base-data-type identifier that indicates that the data type is a DEVPROP_BOOLEAN-typed Boolean value.
ms.assetid: f0e960b7-be71-4117-b978-5877e5bf771f
keywords: ["DEVPROP_TYPE_BOOLEAN Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_TYPE_BOOLEAN
api_location:
- Devpropdef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPROP_TYPE_BOOLEAN


In Windows Vista and later versions of Windows, the DEVPROP_TYPE_BOOLEAN property type represents the base-data-type identifier that indicates that the data type is a DEVPROP_BOOLEAN-typed Boolean value.

Remarks
-------

The DEVPROP_BOOLEAN data type and valid Boolean values are defined as follows:

``` syntax
typedef CHAR DEVPROP_BOOLEAN, *PDEVPROP_BOOLEAN;
#define DEVPROP_TRUE  ((DEVPROP_BOOLEAN)-1)
#define DEVPROP_FALSE ((DEVPROP_BOOLEAN) 0)
```

DEVPROP_TYPE_BOOLEAN can be combined only with the [**DEVPROP_TYPEMOD_ARRAY**](devprop-typemod-array.md) property-data-type modifier.

### Setting a Property of this Type

To set a property whose base data type is DEVPROP_TYPE_BOOLEAN, call the corresponding SetupDiSet*Xxx* property function and set the function input parameters as follows:

-   Set the *PropertyType* parameter to DEVPROP_TYPE_BOOLEAN, set the *PropertyBuffer* parameter to a pointer to a buffer that contains a DEVPROP_FALSE or DEVPROP_TRUE value, and set the *PropertyBufferSize* parameter to `sizeof(DEVPROP_BOOLEAN)`.

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

 

 





