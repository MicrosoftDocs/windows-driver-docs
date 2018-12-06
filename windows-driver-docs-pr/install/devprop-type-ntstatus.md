---
title: DEVPROP_TYPE_NTSTATUS
description: The DEVPROP_TYPE_NTSTATUS identifier represents the base-data-type identifier for the NTSTATUS status code values that are defined in Ntstatus.h.
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
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPROP_TYPE_NTSTATUS


The DEVPROP_TYPE_NTSTATUS identifier represents the base-data-type identifier for the NTSTATUS status code values that are defined in Ntstatus.h.

Remarks
-------

In Windows Vista and later versions of Windows, the [unified device property model](https://msdn.microsoft.com/library/windows/hardware/ff553515) also defines a [**DEVPROP_TYPE_ERROR**](devprop-type-error.md) base-data-type identifier for Microsoft Win32 error code values.

You can combine DEVPROP_TYPE_NTSTATUS only with the [**DEVPROP_TYPEMOD_ARRAY**](devprop-typemod-array.md) property-data-type modifier.

### Setting a Property of This Type

To set a property whose base data type is DEVPROP_TYPE_NTSTATUS, call the corresponding **SetupDiSet***Xxx* property function and set the function input parameters as follows:

- Set the *PropertyType* parameter to DEVPROP_TYPE_NTSTATUS.

- Set the *PropertyBuffer* parameter to a pointer to a buffer that can contain at least one NTSTATUS value.

- Set the *PropertyBufferSize* parameter to <strong>sizeof(</strong>NTSTATUS<strong>)</strong>.

- Set the remaining function parameters as appropriate to set the property.

### Retrieving the Descriptive Text for a NTSTATUS Error Code Value

To retrieve the descriptive text that is associated with an NTSTATUS error code value, call the **FormatMessage** function (documented in the Windows SDK) as follows:

-   Include a bitwise OR of the FORMAT_MESSAGE_FROM_SYSTEM flag and the FORMAT_MESSAGE_FROM_HMODULE flag in the value of the *dwflags* parameter.

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


[**DEVPROP_TYPE_ERROR**](devprop-type-error.md)

[**DEVPROP_TYPEMOD_ARRAY**](devprop-typemod-array.md)

 

 






