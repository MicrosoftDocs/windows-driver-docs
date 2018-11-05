---
title: DEVPROP_TYPE_NULL
description: In Windows Vista and later versions of Windows, the DEVPROP_TYPE_NULL identifier represents a special base-data-type identifier that indicates that a device property exists. However, that the property has no value that is associated with the property.
ms.assetid: 0308206d-5664-4288-a761-ca72e533264c
keywords: ["DEVPROP_TYPE_NULL Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_TYPE_NULL
api_location:
- Devpropdef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPROP_TYPE_NULL


In Windows Vista and later versions of Windows, the DEVPROP_TYPE_NULL identifier represents a special base-data-type identifier that indicates that a device property exists. However, that the property has no value that is associated with the property.

Remarks
-------

Use this base-property-type identifier with the device property functions to delete the value that is associated with a device property.

If a device property function returns this base data type, the property exists, but the property has no value that is associated with it.

The DEVPROP_TYPE_NULL identifier cannot be combined with the property-data-type modifiers [**DEVPROP_TYPEMOD_ARRAY**](devprop-typemod-array.md) or [**DEVPROP_TYPEMOD_LIST**](devprop-typemod-list.md).

**Setting a Property of this Type**

To set a property whose data type is DEVPROP_TYPE_NULL, call the corresponding **SetupDiSet*Xxx*** property function and set the function parameters as follows:

-   Set the *PropertyType* parameter to DEVPROP_TYPE_NULL, the *PropertyBuffer* parameter to **NULL**, and the *PropertyBufferSize* parameter to zero.

-   Set the other function input parameters as appropriate to set the property.

**Retrieving a Property of this Type**

A call to a **SetupDiGet*Xxx*** property function that attempts to retrieve a device property that has no value will succeed and set the \**PropertyType* parameter to DEVPROP_TYPE_NULL.

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

 

 





