---
title: DEVPKEY_DeviceInterfaceClass_DefaultInterface
description: DEVPKEY_DeviceInterfaceClass_DefaultInterface
keywords: ["DEVPKEY_DeviceInterfaceClass_DefaultInterface Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DeviceInterfaceClass_DefaultInterface
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_DeviceInterfaceClass_DefaultInterface


The DEVPKEY_DeviceInterfaceClass_DefaultInterface device property represents the symbolic link name of the default device interface for a device interface class.

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
<td align="left"><p>DEVPKEY_DeviceInterfaceClass_DefaultInterface</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-string.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_STRING&lt;/strong&gt;](devprop-type-string.md)"><strong>DEVPROP_TYPE_STRING</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read and write access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

## Remarks

For information about how to install and using device interfaces, see [Device Interface Classes](./overview-of-device-interface-classes.md) and the [**INF AddInterface Directive**](./inf-addinterface-directive.md).

You can retrieve the value of DEVPKEY_DeviceInterfaceClass_DefaultInterface by calling [**SetupDiGetDeviceInterfaceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacepropertyw). You can set DEVPKEY_DeviceInterfaceClass_DefaultInterface by calling [**SetupDiSetDeviceInterfaceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdeviceinterfacepropertyw).

Windows Server 2003, Windows XP, and Windows 2000 support this property, but do not support the DEVPKEY_DeviceInterfaceClass_DefaultInterface property key. For information about how to access the default interface of a device interface class on these earlier versions of Windows, see [Accessing Device Interface Class Properties](./accessing-device-interface-class-properties.md).

## Requirements

**Version**: Windows Vista and later versions of Windows
**Header**: Devpkey.h (include Devpkey.h)


## See also


[**INF AddInterface Directive**](./inf-addinterface-directive.md)

[**SetupDiGetClassDevs**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsw)

[**SetupDiGetDeviceInterfaceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacepropertyw)

[**SetupDiSetDeviceInterfaceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdeviceinterfacepropertyw)

 

