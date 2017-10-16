---
title: DEVPROP_TYPE_FLOAT
description: In Windows Vista and later versions of Windows, the DEVPROP_TYPE_INT64 identifier represents the base-data-type identifier that indicates that the data type is a FLOAT-typed IEEE floating-point number.
ms.assetid: b83a0510-674e-4141-9d3f-25efcb08aea0
keywords: ["DEVPROP_TYPE_FLOAT Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_TYPE_FLOAT
api_location:
- Devpropdef.h
api_type:
- HeaderDef
---

# DEVPROP_TYPE_FLOAT


In Windows Vista and later versions of Windows, the DEVPROP_TYPE_INT64 identifier represents the base-data-type identifier that indicates that the data type is a FLOAT-typed IEEE floating-point number.

Remarks
-------

DEVPROP_TYPE_FLOAT can be combined only with the [**DEVPROP_TYPEMOD_ARRAY**](devprop-typemod-array.md) property-data-type modifier.

**Setting a Property of this Type**

To set a property whose base data type is DEVPROP_TYPE_FLOAT, call the corresponding SetupDiSet*Xxx* property function, setting the function input parameters as follows:

-   Set the *PropertyType* parameter to DEVPROP_TYPE_FLOAT, set the *PropertyBuffer* parameter to a pointer to a buffer that can contain at least one FLOAT value, and set the *PropertyBufferSize* parameter to `sizeof(FLOAT)`.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DEVPROP_TYPE_FLOAT%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




