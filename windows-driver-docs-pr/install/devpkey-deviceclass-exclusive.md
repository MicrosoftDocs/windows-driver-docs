---
title: DEVPKEY_DeviceClass_Exclusive
description: DEVPKEY_DeviceClass_Exclusive
keywords: ["DEVPKEY_DeviceClass_Exclusive Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DeviceClass_Exclusive
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 10/17/2018
ms.topic: reference
---

# DEVPKEY_DeviceClass_Exclusive


The DEVPKEY_DeviceClass_Exclusive device property represents a Boolean flag that indicates whether devices that are members of a [device setup class](./overview-of-device-setup-classes.md) are exclusive devices.

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
<td align="left"><p>DEVPKEY_DeviceClass_Exclusive</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-boolean.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_BOOLEAN&lt;/strong&gt;](devprop-type-boolean.md)"><strong>DEVPROP_TYPE_BOOLEAN</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers after a device setup class is installed</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Corresponding SPCRP_</strong><em>Xxx</em> <strong>identifier</strong></p></td>
<td align="left"><p>SPCRP_EXCLUSIVE</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

## Remarks

You can set the value of DEVPKEY_DeviceClass_Exclusive when an installation application installs a device setup class. For information about how to install a device setup class and setting this property, see [**INF ClassInstall32 Section**](./inf-classinstall32-section.md) and the information about the registry value **Exclusive** that is provided in the "Special *value-entry-name* Keywords" section of [**INF AddReg Directive**](./inf-addreg-directive.md).

You can call [**CM_Get_Class_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_class_propertyw) or [**SetupDiGetClassProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyw) to retrieve the value of DEVPKEY_DeviceClass_Exclusive.

Windows Server 2003 and Windows XP support this property, but do not support the DEVPKEY_DeviceClass_Exclusive property key. On these earlier versions of Windows, you can use the SPCRP_EXCLUSIVE identifier to access the value of this property. For information about how to access the value of this property, see [Retrieving Device Setup Class SPCRP_Xxx Properties](./accessing-device-setup-class-properties.md).

## Requirements

**Version**: Windows Vista and later versions of Windows
**Header**: Devpkey.h (include Devpkey.h)


## See also


[**INF AddReg Directive**](./inf-addreg-directive.md)

[**INF ClassInstall32 Section**](./inf-classinstall32-section.md)

[**SetupDiGetClassProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyw)
