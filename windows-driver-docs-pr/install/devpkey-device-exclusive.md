---
title: DEVPKEY_Device_Exclusive
description: DEVPKEY_Device_Exclusive
ms.assetid: c54c2fe3-cf57-4603-a701-8ddbc28aa47d
keywords: ["DEVPKEY_Device_Exclusive Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_Exclusive
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_Device_Exclusive


The DEVPKEY_Device_Exclusive device property represents a Boolean value that determines whether a device instance can be opened for exclusive use.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_Device_Exclusive</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-boolean.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_BOOLEAN&lt;/strong&gt;](devprop-type-boolean.md)"><strong>DEVPROP_TYPE_BOOLEAN</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read and write access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Corresponding SPDRP_</strong><em>Xxx</em> <strong>identifier</strong></p></td>
<td align="left"><p>SPDRP_EXCLUSIVE</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The value of the DEVPKEY_Device_Exclusive property is DEVPROP_TRUE if the device can be opened for exclusive use. Otherwise, the value of the property is DEVPROP_FALSE.

You can set the value of DEVPKEY_Device_Exclusive by using an [**INF AddReg directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320) that is included in the [**INF *DDInstall*.HW section**](https://msdn.microsoft.com/library/windows/hardware/ff547330) that installs a device.

You can retrieve or set the value of DEVPKEY_Device_Exclusive by calling [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963) and [**SetupDiSetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552163).

Windows Server 2003, Windows XP, and Windows 2000 support this property, but do not support the DEVPKEY_Device_Exclusive property key. Instead, you can use the corresponding SPDRP_EXCLUSIVE identifier to access the value of the property on these earlier versions of Windows. For information about how to access this property value on these earlier versions of Windows, see [Accessing Device Instance SPDRP_Xxx Properties](https://msdn.microsoft.com/library/windows/hardware/ff537737).

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


[**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320)

[**INF *DDInstall*.HW Section**](https://msdn.microsoft.com/library/windows/hardware/ff547330)

[**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963)

[**SetupDiSetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552163)

 

 






