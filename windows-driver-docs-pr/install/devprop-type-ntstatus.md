---
title: DEVPROP\_TYPE\_NTSTATUS
description: The DEVPROP\_TYPE\_NTSTATUS identifier represents the base-data-type identifier for the NTSTATUS status code values that are defined in Ntstatus.h.
ms.assetid: 7593d24d-8e89-409e-9047-0c14268b8e62
keywords: ["DEVPROP_TYPE_NTSTATUS Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_TYPE_NTSTATUS
api_location:
- Devpropdef.h
api_type:
- HeaderDef
---

# DEVPROP\_TYPE\_NTSTATUS


The DEVPROP\_TYPE\_NTSTATUS identifier represents the base-data-type identifier for the NTSTATUS status code values that are defined in Ntstatus.h.

Remarks
-------

In Windows Vista and later versions of Windows, the [unified device property model](https://msdn.microsoft.com/library/windows/hardware/ff553515) also defines a [**DEVPROP\_TYPE\_ERROR**](devprop-type-error.md) base-data-type identifier for Microsoft Win32 error code values.

You can combine DEVPROP\_TYPE\_NTSTATUS only with the [**DEVPROP\_TYPEMOD\_ARRAY**](devprop-typemod-array.md) property-data-type modifier.

### Setting a Property of This Type

To set a property whose base data type is DEVPROP\_TYPE\_NTSTATUS, call the corresponding **SetupDiSet***Xxx* property function and set the function input parameters as follows:

-   Set the *PropertyType* parameter to DEVPROP\_TYPE\_NTSTATUS.

-   Set the *PropertyBuffer* parameter to a pointer to a buffer that can contain at least one NTSTATUS value.

-   Set the *PropertyBufferSize* parameter to **sizeof(**NTSTATUS**)**.

-   Set the remaining function parameters as appropriate to set the property.

### Retrieving the Descriptive Text for a NTSTATUS Error Code Value

To retrieve the descriptive text that is associated with an NTSTATUS error code value, call the **FormatMessage** function (documented in the Windows SDK) as follows:

-   Include a bitwise OR of the FORMAT\_MESSAGE\_FROM\_SYSTEM flag and the FORMAT\_MESSAGE\_FROM\_HMODULE flag in the value of the *dwflags* parameter.

-   Set the *lpSource* parameter to a handle to the *NtDLL.dll* module, which is the source for the descriptive text.

-   Set the *dwMessageID* parameter to the error code value.

-   Set the other options and parameters as appropriate to retrieve the descriptive text.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Windows Vista and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Devpropdef.h (include Devpropdef.h)</td>
</tr>
</tbody>
</table>

## See also


[**DEVPROP\_TYPE\_ERROR**](devprop-type-error.md)

[**DEVPROP\_TYPEMOD\_ARRAY**](devprop-typemod-array.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DEVPROP_TYPE_NTSTATUS%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





