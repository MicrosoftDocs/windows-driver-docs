---
title: DEVPKEY_DeviceInterface_FriendlyName
description: DEVPKEY_DeviceInterface_FriendlyName
ms.assetid: 398618a2-621b-477f-b90b-127e8df24b3d
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

 

Remarks
-------

The **FriendlyName** registry value for a device interface class is set by an [**INF AddInterface directive**](https://msdn.microsoft.com/library/windows/hardware/ff546310) that is included in the [**INF *DDInstall*.Interface section**](https://msdn.microsoft.com/library/windows/hardware/ff547335) of the INF file that installs a device interface.

Windows sets the value of the [**DEVPKEY_NAME**](devpkey-name--device-interface-.md) device property for an interface to the value of DEVPKEY_DeviceInterface_FriendlyName. To identify a device interface in a user interface item, use the value of DEVPKEY_NAME for the device interface instead of the value of DEVPKEY_DeviceInterface_FriendlyName.

You can retrieve the value of the DEVPKEY_DeviceInterface_FriendlyName by calling [**SetupDiGetDeviceInterfaceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551122) and set it by calling [**SetupDiSetDeviceInterfaceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552158).

Windows Server 2003, Windows XP, and Windows 2000 support this property, but do not support the DEVPKEY_DeviceInterface_FriendlyName property key. You can access the value of this property by accessing the corresponding **FriendlyName** registry entry value for the device interface. For information about how to access a registry entry value for a device interface, see [Accessing Device Interface Properties](https://msdn.microsoft.com/library/windows/hardware/ff537740).

For information about device interfaces, see [Device Interface Classes](https://msdn.microsoft.com/library/windows/hardware/ff541339) and the [**INF AddInterface Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546310).

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
<td align="left"><p>Available in Windows Vista and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Devpkey.h (include Devpkey.h)</td>
</tr>
</tbody>
</table>

## See also


[**DEVPKEY_NAME (Device Interface)**](devpkey-name--device-interface-.md)

[**INF AddInterface Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546310)

[**INF *DDInstall*.Interface Section**](https://msdn.microsoft.com/library/windows/hardware/ff547335)

[**SetupDiGetDeviceInterfaceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551122)

[**SetupDiOpenDeviceInterfaceRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552075)

[**SetupDiSetDeviceInterfaceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552158)

 

 






