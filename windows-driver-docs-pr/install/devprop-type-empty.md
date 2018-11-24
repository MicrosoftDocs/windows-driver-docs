---
title: DEVPROP_TYPE_EMPTY
description: In Windows Vista and later versions of Windows, the DEVPROP_TYPE_EMPTY identifier represents a special base-data-type identifier that indicates that a property does not exist.
ms.assetid: 23d48659-e512-4557-a78b-d3afca7020a3
keywords: ["DEVPROP_TYPE_EMPTY Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_TYPE_EMPTY
api_location:
- Devpropdef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPROP_TYPE_EMPTY


In Windows Vista and later versions of Windows, the DEVPROP_TYPE_EMPTY identifier represents a special base-data-type identifier that indicates that a property does not exist.

Remarks
-------

Use this base-data-type identifier with the device property functions to delete a property.

If a device property function returns this base-data-type identifier, the property does not exist.

**DEVPROP_TYPE_EMPTY** cannot be combined with the property-data-type modifiers [**DEVPROP_TYPEMOD_ARRAY**](devprop-typemod-array.md) or [**DEVPROP_TYPEMOD_LIST**](devprop-typemod-list.md).

### Deleting a Property

To delete a property, call the corresponding SetupDiSet*Xxx* property function and set the function parameters as follows:

-   Set the *PropertyType* parameter to DEVPROP_TYPE_EMPTY, the *PropertyBuffer* parameter to **NULL**, and the *PropertyBufferSize* parameter to zero.

-   Set the other function input parameters as appropriate to set the property.

If DEVPROP_TYPE_EMPTY is used in an attempt to delete a property that does not exist, the delete operation will fail, and a call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return ERROR_NOT_FOUND.

### Retrieving a Property that Does Not Exist

A call to a SetupDiGet*Xxx* property function that attempts to retrieve a device property that does not exist will fail, and a subsequent call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return ERROR_NOT_FOUND. The called SetupAPI property function will set the \**PropertyType* parameter to DEVPROP_TYPE_EMPTY.

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

 

 





