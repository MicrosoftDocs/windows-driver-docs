---
title: DEVPKEY_DeviceClass_NoInstallClass
description: DEVPKEY_DeviceClass_NoInstallClass
keywords: ["DEVPKEY_DeviceClass_NoInstallClass Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DeviceClass_NoInstallClass
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_DeviceClass_NoInstallClass


The DEVPKEY_DeviceClass_NoInstallClass device setup class property represents a Boolean flag that controls whether devices in a [device setup class](./overview-of-device-setup-classes.md) are displayed in the **Add Hardware Wizard**.

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
<td align="left"><p>DEVPKEY_DeviceClass_NoInstallClass</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-boolean.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_BOOLEAN&lt;/strong&gt;](devprop-type-boolean.md)"><strong>DEVPROP_TYPE_BOOLEAN</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Corresponding registry value name</strong></p></td>
<td align="left"><p><strong>NoInstallClass</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Setting the value of DEVPKEY_DeviceClass_NoInstallClass to DEVPROP_TRUE indicates that installation of devices in the class does not require end-user interaction. If this value is not set to DEVPROP_TRUE, the Add Hardware Wizard does display devices for the device setup class.

The **NoInstallClass** registry value for a device setup class can be set by an [**INF AddReg directive**](./inf-addreg-directive.md) that is included in the [**INF ClassInstall32 section**](./inf-classinstall32-section.md) of the INF file that installs the class.

You can call [**SetupDiGetClassProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyw) or [**SetupDiGetClassPropertyEx**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyexw) to retrieve the value of DEVPKEY_DeviceClass_NoInstallClass.

Windows Server 2003, Windows XP, and Windows 2000 support this property, but do not support the DEVPKEY_DeviceClass_NoInstallClass property key. You can access the value of this property by accessing the corresponding **NoInstallClass** registry value under the class registry key. For information about how to access value entries under the class registry key, see [Accessing Registry Entry Values Under the Class Registry Key](./accessing-registry-entry-values-under-the-class-registry-key.md).

## Requirements

**Version**: Windows Vista and later versions of Windows
**Header**: Devpkey.h (include Devpkey.h)


## See also


[**INF AddReg Directive**](./inf-addreg-directive.md)

[**INF ClassInstall32 Section**](./inf-classinstall32-section.md)

[**SetupDiGetClassProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyw)

[**SetupDiGetClassPropertyEx**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyexw)

 

