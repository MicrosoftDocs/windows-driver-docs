---
title: DEVPKEY_Device_Characteristics
description: DEVPKEY_Device_Characteristics
ms.assetid: 148557aa-2246-4cd9-9008-d920ffb64845
keywords: ["DEVPKEY_Device_Characteristics Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_Characteristics
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_Device_Characteristics


The DEVPKEY_Device_Characteristics device property represents the characteristics of a device instance.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_Device_Characteristics</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-int32.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_INT32&lt;/strong&gt;](devprop-type-int32.md)"><strong>DEVPROP_TYPE_INT32</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Corresponding SPDRP_</strong><em>Xxx</em> <strong>identifier</strong></p></td>
<td align="left"><p>SPDRP_CHARACTERISTICS</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The value of DEVPKEY_Device_Characteristics is a bitwise OR of the FILE_*Xxx* file characteristic flags that are defined in Wdm.h and Ntddk.h. For more information about the device characteristic flags, see the *DeviceCharacteristics* parameter of [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) and [Specifying Device Characteristics](https://msdn.microsoft.com/library/windows/hardware/ff563818).

You can set the value of DEVPKEY_Device_Characteristics by using an [**INF AddReg directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320) that is included in the [**INF DDInstall.HW section**](https://msdn.microsoft.com/library/windows/hardware/ff547330) that installs a device.

You can retrieve the value of DEVPKEY_Device_Characteristics by calling [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963).

Windows Server 2003, Windows XP, and Windows 2000 support this property, but do not support the DEVPKEY_Device_Characteristics property key. Instead, you can use the corresponding SPDRP_CHARACTERISTICS identifier to access the value of the property on these earlier versions of Windows. For information about how to access this property value on these earlier versions of Windows, see [Accessing Device Instance SPDRP_Xxx Properties](https://msdn.microsoft.com/library/windows/hardware/ff537737).

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

[**INF DDInstall.HW Section**](https://msdn.microsoft.com/library/windows/hardware/ff547330)

[**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397)

[**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963)

[**SetupDiSetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552163)

 

 






