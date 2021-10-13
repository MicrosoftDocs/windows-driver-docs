---
title: DEVPKEY_DeviceInterface_FriendlyName
description: DEVPKEY_DeviceInterface_FriendlyName
keywords: ["DEVPKEY_DeviceInterface_FriendlyName Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DeviceInterface_FriendlyName
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_DeviceInterface_FriendlyName


The DEVPKEY_DeviceInterface_FriendlyName device property represents the friendly name of a device interface.

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
<td align="left"><p>DEVPKEY_DeviceInterface_FriendlyName</p></td>
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
<td align="left"><p><strong>Corresponding registry value name</strong></p></td>
<td align="left"><p><strong>FriendlyName</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>Yes</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The **FriendlyName** registry value for a device interface class is set by an [**INF AddInterface directive**](./inf-addinterface-directive.md) that is included in the [**INF *DDInstall*.Interface section**](./inf-ddinstall-interfaces-section.md) of the INF file that installs a device interface.

Windows sets the value of the [**DEVPKEY_NAME**](devpkey-name--device-interface-.md) device property for an interface to the value of DEVPKEY_DeviceInterface_FriendlyName. To identify a device interface in a user interface item, use the value of DEVPKEY_NAME for the device interface instead of the value of DEVPKEY_DeviceInterface_FriendlyName.

You can retrieve the value of the DEVPKEY_DeviceInterface_FriendlyName by calling [**SetupDiGetDeviceInterfaceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacepropertyw) and set it by calling [**SetupDiSetDeviceInterfaceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdeviceinterfacepropertyw).

Windows Server 2003, Windows XP, and Windows 2000 support this property, but do not support the DEVPKEY_DeviceInterface_FriendlyName property key. You can access the value of this property by accessing the corresponding **FriendlyName** registry entry value for the device interface. For information about how to access a registry entry value for a device interface, see [Accessing Device Interface Properties](./accessing-device-interface-properties.md).

For information about device interfaces, see [Device Interface Classes](./overview-of-device-interface-classes.md) and the [**INF AddInterface Directive**](./inf-addinterface-directive.md).

## Requirements

**Version**: Windows Vista and later versions of Windows
**Header**: Devpkey.h (include Devpkey.h)


## See also


[**DEVPKEY_NAME (Device Interface)**](devpkey-name--device-interface-.md)

[**INF AddInterface Directive**](./inf-addinterface-directive.md)

[**INF *DDInstall*.Interface Section**](./inf-ddinstall-interfaces-section.md)

[**SetupDiGetDeviceInterfaceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacepropertyw)

[**SetupDiOpenDeviceInterfaceRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdiopendeviceinterfaceregkey)

[**SetupDiSetDeviceInterfaceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdeviceinterfacepropertyw)

 

