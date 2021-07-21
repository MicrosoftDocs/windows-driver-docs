---
title: DEVPKEY_DeviceClass_ClassCoInstallers
description: DEVPKEY_DeviceClass_ClassCoInstallers
keywords: ["DEVPKEY_DeviceClass_ClassCoInstallers Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DeviceClass_ClassCoInstallers
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_DeviceClass_ClassCoInstallers


The DEVPKEY_DeviceClass_ClassCoInstallers device property represents a list of the class co-installers that are installed for a [device setup class](./overview-of-device-setup-classes.md).

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
<td align="left"><p>DEVPKEY_DeviceClass_ClassCoInstallers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-string-list.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_STRING_LIST&lt;/strong&gt;](devprop-type-string-list.md)"><strong>DEVPROP_TYPE_STRING_LIST</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Data format</strong></p></td>
<td align="left"><p>"<em>coinstaller1.dll</em>,<em>coinstaller1-entry-point</em>\0…<em>coinstallerN.dll</em>,<em>coinstallerN-entry-point</em>\0\0"</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read and write access by installation applications and installers</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Corresponding registry value name</strong></p></td>
<td align="left"><p><strong>HLM\System\CurrentControlSet\Control\CoDeviceInstallers{</strong><em>device-setup-class-guid</em><strong>}</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Each class installer in the class co-installer list is identified by its DLL and entry point.

For information about how to install a class co-installer, see [Registering a Class Co-installer](./registering-a-class-co-installer.md).

You can retrieve the value of DEVPKEY_DeviceClass_ClassCoInstallers by calling [**SetupDiGetClassProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyw) or [**SetupDiGetClassPropertyEx**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyexw). You can set DEVPKEY_DeviceClass_ClassCoInstallers by calling [**SetupDiSetClassProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetclasspropertyw) or [**SetupDiSetClassPropertyEx**](/windows/win32/api/setupapi/nf-setupapi-setupdisetclasspropertyexw).

Windows Server 2003, Windows XP, and Windows 2000 support this property, but do not support the DEVPKEY_DeviceClass_ClassCoInstallers property key. For information about how to access the corresponding information on these earlier versions of Windows, see [Accessing the Co-installers Registry Entry Value of a Device Setup Class](./accessing-the-co-installers-registry-entry-value-of-a-device-setup-cla.md).

## Requirements

**Version**: Windows Vista and later versions of Windows
**Header**: Devpkey.h (include Devpkey.h)


## See also


[**SetupDiGetClassProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyw)

[**SetupDiGetClassPropertyEx**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyexw)

[**SetupDiSetClassProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetclasspropertyw)

[**SetupDiSetClassPropertyEx**](/windows/win32/api/setupapi/nf-setupapi-setupdisetclasspropertyexw)

 

