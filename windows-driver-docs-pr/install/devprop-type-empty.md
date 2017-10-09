---
title: DEVPROP\_TYPE\_EMPTY
description: In Windows Vista and later versions of Windows, the DEVPROP\_TYPE\_EMPTY identifier represents a special base-data-type identifier that indicates that a property does not exist.
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
---

# DEVPROP\_TYPE\_EMPTY


In Windows Vista and later versions of Windows, the DEVPROP\_TYPE\_EMPTY identifier represents a special base-data-type identifier that indicates that a property does not exist.

Remarks
-------

Use this base-data-type identifier with the device property functions to delete a property.

If a device property function returns this base-data-type identifier, the property does not exist.

**DEVPROP\_TYPE\_EMPTY** cannot be combined with the property-data-type modifiers [**DEVPROP\_TYPEMOD\_ARRAY**](devprop-typemod-array.md) or [**DEVPROP\_TYPEMOD\_LIST**](devprop-typemod-list.md).

### Deleting a Property

To delete a property, call the corresponding SetupDiSet*Xxx* property function and set the function parameters as follows:

-   Set the *PropertyType* parameter to DEVPROP\_TYPE\_EMPTY, the *PropertyBuffer* parameter to **NULL**, and the *PropertyBufferSize* parameter to zero.

-   Set the other function input parameters as appropriate to set the property.

If DEVPROP\_TYPE\_EMPTY is used in an attempt to delete a property that does not exist, the delete operation will fail, and a call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return ERROR\_NOT\_FOUND.

### Retrieving a Property that Does Not Exist

A call to a SetupDiGet*Xxx* property function that attempts to retrieve a device property that does not exist will fail, and a subsequent call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return ERROR\_NOT\_FOUND. The called SetupAPI property function will set the \**PropertyType* parameter to DEVPROP\_TYPE\_EMPTY.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DEVPROP_TYPE_EMPTY%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




