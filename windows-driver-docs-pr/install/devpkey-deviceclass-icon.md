---
title: DEVPKEY_DeviceClass_Icon
description: DEVPKEY_DeviceClass_Icon
keywords: ["DEVPKEY_DeviceClass_Icon Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DeviceClass_Icon
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_DeviceClass_Icon


The DEVPKEY_DeviceClass_Icon device property represents the icon for a [device setup class](./overview-of-device-setup-classes.md).

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
<td align="left"><p>DEVPKEY_DeviceClass_Icon</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-string.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_STRING&lt;/strong&gt;](devprop-type-string.md)"><strong>DEVPROP_TYPE_STRING</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The value of DEVPKEY_DeviceClass_Icon is set by an [**INF AddReg directive**](./inf-addreg-directive.md) that is included in the [**INF ClassInstall32 section**](./inf-classinstall32-section.md) that installs the class. To set the value of DEVPKEY_DeviceClass_Icon, use an **AddReg** directive to set the **Icon** registry entry value for the class.

The **Icon** entry value is an integer number in string format. If the number is negative, the absolute value of the number is the resource identifier of the icon in setupapi.dll. If the number is positive, the number is the resource identifier of the icon in the class installer DLL, if there is a class installer, or the class property page provider, if there is no class installer and there is a property page provider. A value of zero is not valid.

You can call [**SetupDiGetClassProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyw) or [**SetupDiGetClassPropertyEx**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyexw) to retrieve the value of DEVPKEY_DeviceClass_Icon.

Windows Server 2003, Windows XP, and Windows 2000 support this property, but do not support the DEVPKEY_DeviceClass_Icon property key. For information about how to access the mini-icon for a device setup class on Windows Server 2003, Windows XP, and Windows 2000, see [Accessing Icon Properties of a Device Setup Class](./accessing-icon-properties-of-a-device-setup-class.md).

## Requirements

**Version**: Windows Vista and later versions of Windows
**Header**: Devpkey.h (include Devpkey.h)


## See also


[**INF AddReg Directive**](./inf-addreg-directive.md)

[**INF ClassInstall32 Section**](./inf-classinstall32-section.md)

[**SetupDiGetClassProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyw)

[**SetupDiGetClassPropertyEx**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyexw)

[**SetupDiDrawMiniIcon**](/windows/win32/api/setupapi/nf-setupapi-setupdidrawminiicon)

[**SetupDiLoadClassIcon**](/windows/win32/api/setupapi/nf-setupapi-setupdiloadclassicon)

 

