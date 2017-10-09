---
title: DEVPROP\_TYPE\_DEVPROPKEY
description: In Windows Vista and later versions of Windows, the DEVPROP\_TYPE\_DEVPROPKEY identifier represents the base-data-type identifier that indicates the data type is a DEVPROPKEY-typed device property key.
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
---

# DEVPROP\_TYPE\_DEVPROPKEY


In Windows Vista and later versions of Windows, the DEVPROP\_TYPE\_DEVPROPKEY identifier represents the base-data-type identifier that indicates the data type is a DEVPROPKEY-typed device property key.

Remarks
-------

The DEVPROP\_TYPE\_DEVPROPKEY property type can be combined only with the [**DEVPROP\_TYPEMOD\_ARRAY**](devprop-typemod-array.md) property-data-type modifier.

### Setting a Property of this Type

To set a property whose base data type is DEVPROP\_TYPE\_DEVPROPKEY, call the corresponding SetupDiSet*Xxx* property function and set the function input parameters as follows:

-   Set the *PropertyType* parameter to DEVPROP\_TYPE\_DEVPROPKEY, set the *PropertyBuffer* parameter to a pointer to a buffer that contains a DEVPROPKEY structure, and set the *PropertyBufferSize* parameter to `sizeof(DEVPROPKEY)`.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DEVPROP_TYPE_DEVPROPKEY%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




