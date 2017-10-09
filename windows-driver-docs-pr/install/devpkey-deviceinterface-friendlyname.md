---
title: DEVPKEY\_DeviceInterface\_FriendlyName
description: DEVPKEY\_DeviceInterface\_FriendlyName
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
---

# DEVPKEY\_DeviceInterface\_FriendlyName


The DEVPKEY\_DeviceInterface\_FriendlyName device property represents the friendly name of a device interface.

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
<td align="left"><p>[<strong>DEVPROP_TYPE_STRING</strong>](devprop-type-string.md)</p></td>
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

Windows sets the value of the [**DEVPKEY\_NAME**](devpkey-name--device-interface-.md) device property for an interface to the value of DEVPKEY\_DeviceInterface\_FriendlyName. To identify a device interface in a user interface item, use the value of DEVPKEY\_NAME for the device interface instead of the value of DEVPKEY\_DeviceInterface\_FriendlyName.

You can retrieve the value of the DEVPKEY\_DeviceInterface\_FriendlyName by calling [**SetupDiGetDeviceInterfaceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551122) and set it by calling [**SetupDiSetDeviceInterfaceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552158).

Windows Server 2003, Windows XP, and Windows 2000 support this property, but do not support the DEVPKEY\_DeviceInterface\_FriendlyName property key. You can access the value of this property by accessing the corresponding **FriendlyName** registry entry value for the device interface. For information about how to access a registry entry value for a device interface, see [Accessing Device Interface Properties](https://msdn.microsoft.com/library/windows/hardware/ff537740).

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


[**DEVPKEY\_NAME (Device Interface)**](devpkey-name--device-interface-.md)

[**INF AddInterface Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546310)

[**INF *DDInstall*.Interface Section**](https://msdn.microsoft.com/library/windows/hardware/ff547335)

[**SetupDiGetDeviceInterfaceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551122)

[**SetupDiOpenDeviceInterfaceRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552075)

[**SetupDiSetDeviceInterfaceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552158)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DEVPKEY_DeviceInterface_FriendlyName%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





