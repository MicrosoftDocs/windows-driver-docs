---
title: DEVPKEY_DeviceClass_IconPath
description: DEVPKEY_DeviceClass_IconPath
keywords: ["DEVPKEY_DeviceClass_IconPath Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DeviceClass_IconPath
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_DeviceClass_IconPath


The DEVPKEY_DeviceClass_IconPath device property represents an icon list for a [device setup class](./overview-of-device-setup-classes.md).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr>
<th>Attribute</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_DeviceClass_IconPath</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-string-list.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_STRING_LIST&lt;/strong&gt;](devprop-type-string-list.md)"><strong>DEVPROP_TYPE_STRING_LIST</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Corresponding registry value name</strong></p></td>
<td align="left"><p><strong>IconPath</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

## Remarks

You can call [**SetupDiGetClassProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyw) or [**SetupDiGetClassPropertyEx**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyexw) to retrieve the value of DEVPKEY_DeviceClass_IconPath.

A DEVPKEY_DeviceClass_IconPath value is a [REG_MULTI_SZ](/windows/desktop/SysInfo/registry-value-types)-typed list of icon resource specifiers in the format that is used by the Windows shell. The format of an icon resource specifier is "*executable-file-path*,*resource-identifier*," where *executable-file-path* contains the fully qualified path of the file on a computer that contains the icon resource and *resource-identifier* specifies an integer that identifies the resource. For example, the icon resource specifier "%SystemRoot%\\system32\\DLL1.dll,-12" contains the executable file path "%SystemRoot%\\system32\\DLL1.dll" and the resource identifier "-12".

Windows Server 2003, Windows XP, and Windows 2000 do not support this property. For information about how to access icon information for a device setup class on these versions of Windows, see [Accessing Icon Properties of a Device Setup Class](./accessing-icon-properties-of-a-device-setup-class.md).

## Requirements

**Version**: Windows Vista and later versions of Windows
**Header**: Devpkey.h (include Devpkey.h)


## See also


[**SetupDiGetClassProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyw)

[**SetupDiGetClassPropertyEx**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyexw)

[**SetupDiLoadClassIcon**](/windows/win32/api/setupapi/nf-setupapi-setupdiloadclassicon)

 

