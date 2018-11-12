---
title: DEVPROP_TYPE_STRING_INDIRECT
description: The DEVPROP_TYPE_STRING_INDIRECT identifier represents the base-data-type identifier for a NULL-terminated Unicode string that contains an indirect string reference.
ms.assetid: c3a4f627-02d7-47ba-aa62-5d6b0e8dd9cd
keywords: ["DEVPROP_TYPE_STRING_INDIRECT Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROP_TYPE_STRING_INDIRECT
api_location:
- Devpropdef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPROP_TYPE_STRING_INDIRECT


The DEVPROP_TYPE_STRING_INDIRECT identifier represents the base-data-type identifier for a NULL-terminated Unicode string that contains an indirect string reference.

Remarks
-------

An indirect string reference describes a string resource that contains the actual string. The indirect string reference can appear in one of the following formats:

<a href="" id="--path--filename--resourceid"></a>**@**\[<em>path</em>**\\**\]<em>FileName</em>**,-***ResourceID*  
Windows extracts the string from the module that is specified by the *path* and *FileName* entries, and the resource identifier of the string is supplied by the *ResourceID* entry (excluding the required minus sign). The string resource is loaded from the module resource section that best matches one of the caller's preferred UI languages. The *path* entry is optional. If you specify the *path* entry, the module must be located in a directory that is in the system-defined search path.

<a href="" id="-infname--strkey-"></a>**@**<em>InfName</em>**,%**<em>strkey</em>**%**  
Windows extracts the string from the INF **Strings** section of the INF file in the %SystemRoot%\\*inf* directory whose name is supplied by the *InfName* entry. The *strkey* token identifier should match the key of a line in the **Strings** section that best matches one of the caller's preferred UI languages. If no language-specific **Strings** sections exist, Windows uses the default **Strings** section.

You cannot combine DEVPROP_TYPE_STRING_INDIRECT with any of the property-data-type modifiers.

### Setting a Property of This Type

To set a property whose base data type is DEVPROP_TYPE_STRING_INDIRECT, call the corresponding **SetupDiSet***Xxx* property function and set the function input parameters as follows:

-   Set the *PropertyType* parameter to DEVPROP_TYPE_STRING_INDIRECT.

-   Set the *PropertyBuffer* parameter to a pointer to a buffer that contains the NULL-terminated string that supplies an indirect string reference.

-   Set the *PropertyBufferSize* parameter to the size, in bytes, of the string.

-   Set the remaining function parameters as appropriate to set the property.

### Retrieving the Value of This Property Type

When an application calls a **SetupDiGet***Xxx* property function to retrieve the value of a property of this base data type, Windows tries to locate the actual string that the property references. If Windows can retrieve the actual string, it returns the actual string to the caller and identifies the base data type of the retrieved property as [**DEVPROP_TYPE_STRING**](devprop-type-string.md). Otherwise, Windows returns the indirect string reference and identifies the base data type of the retrieved property as DEVPROP_TYPE_STRING_INDIRECT.

### Localizing Static Text

Starting with Windows Vista you can localize custom and standard string-type PnP static-text properties using resources from a PE image's string or resource tables by setting static-text property types to DEVPROP_TYPE_STRING_INDIRECT. You can also add non-localized replacement-string data that can be formatted into the static text.

Strings located in a PE image's STRINGTABLE resource (as typically performed by LoadString) should use the following format:

"@"System32\\mydll.dll,-21\[;Fallback" String\]"

"@System32\\mydll.dll,-21\[;Fallback String with %1, %2, … to %n\[;(Arg1,Arg2,…,ArgN)\]\]"

Strings located in a PE images's message-table resource (as typically performed by RtlFindMessage, more commonly used in drivers) should use the following format:

"@System32\\drivers\\mydriver.sys,\#21\[;Fallback String\]"

"@System32\\drivers\\mydriver.sys,\#21\[;Fallback String with %1, %2, … to %n\[;(Arg1,Arg2,…,ArgN)\]\]"

A "Fallback String" is optional but useful because it can be returned if the resource can’t be found or loaded. The fallback string is also returned to non-interactive system processes that are not impersonating a user, and as such cannot show localized text to users anyways.

This technique enables you to localize static-text pulled from the string or message table resource that best matches the caller’s locale.

Windows will format the trailing arguments into the string (or the fallback string) when they are retrieved from the respective resource table, much as in the same manner as RtlFormatMessage does.

Custom and standard string-type PnP static-text is localized when you set the property by loading the resource from the component performing the set operation, which typically happens under the system default locale for system-level components.

Note: PE images can use either resource table type (STRINGTABLE resources, or message-table resources).

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


[**DEVPROP_TYPE_STRING**](devprop-type-string.md)

 

 






