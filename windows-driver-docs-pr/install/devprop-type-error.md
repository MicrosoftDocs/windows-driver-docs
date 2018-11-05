---
title: DEVPROP_TYPE_ERROR
description: The DEVPROP_TYPE_ERROR identifier represents the base-data-type identifier for the Microsoft Win32 error code values that are defined in WINERROR.H.
ms.assetid: fe8fa3de-a984-4c6f-902f-5eda24402a65
keywords: ["DEVPROP_TYPE_ERROR Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_TYPE_ERROR
api_location:
- Devpropdef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPROP_TYPE_ERROR


The DEVPROP_TYPE_ERROR identifier represents the base-data-type identifier for the Microsoft Win32 error code values that are defined in WINERROR.H.

Remarks
-------

In Windows Vista and later versions of Windows, the [unified device property model](https://msdn.microsoft.com/library/windows/hardware/ff553515) also defines a [**DEVPROP_TYPE_NTSTATUS**](devprop-type-ntstatus.md) base-data-type identifier for NTSTATUS error code values.

You can combine DEVPROP_TYPE_ERROR only with the [**DEVPROP_TYPEMOD_ARRAY**](devprop-typemod-array.md) property-data-type modifier.

### Setting a Property of This Type

To set a property whose base data type is DEVPROP_TYPE_ERROR, call the corresponding SetupDiSet*Xxx* property function and set the function input parameters as follows:

-   Set the *PropertyType* parameter to DEVPROP_TYPE_ERROR.

-   Set the *PropertyBuffer* parameter to a pointer to a buffer that can contain at least one Win32 error code value.

-   Set the *PropertyBufferSize* parameter to `sizeof(ULONG)`.

-   Set the remaining function parameters as appropriate to set the property.

### Retrieving the Descriptive Text for a Win32 Error Code Value

To retrieve the descriptive text that is associated with a Win32 error code, call the [**FormatMessage**](https://msdn.microsoft.com/library/windows/desktop/ms679351) function (documented in the Windows SDK) as follows:

-   Include the FORMAT_MESSAGE_FROM_SYSTEM flag in the value of the *dwflags* parameter.

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


[**DEVPROP_TYPE_NTSTATUS**](devprop-type-ntstatus.md)

[**DEVPROP_TYPEMOD_ARRAY**](devprop-typemod-array.md)

 

 






