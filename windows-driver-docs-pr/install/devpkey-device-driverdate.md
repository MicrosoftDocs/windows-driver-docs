---
title: DEVPKEY_Device_DriverDate
description: DEVPKEY_Device_DriverDate
ms.assetid: d1310b0f-f358-4875-a01b-8bc4cf8b8d2d
keywords: ["DEVPKEY_Device_DriverDate Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_DriverDate
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_Device_DriverDate


The PKEY_Device_DriverDate device property represents the date of the driver that is currently installed for a device instance.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_Device_DriverDate</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-filetime.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_FILETIME&lt;/strong&gt;](devprop-type-filetime.md)"><strong>DEVPROP_TYPE_FILETIME</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Corresponding registry value identifier and registry value name</strong></p></td>
<td align="left"><p>REGSTR_VAL_DRIVERDATEDATA</p>
<p><strong>DriverDateData</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The value of DEVPKEY_Device_DriverDate is supplied by the [**INF DriverVer directive**](https://msdn.microsoft.com/library/windows/hardware/ff547394) that is included in the **INF Version section** of an INF file that installs a device or by a device-specific INF **DriverVer** directive that is included in the [**INF *DDInstall* section**](https://msdn.microsoft.com/library/windows/hardware/ff547344) that installs a device.

You can call [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963) to retrieve the value of DEVPKEY_Device_DriverDate property.

Windows Server 2003, Windows XP, and Windows 2000 support this property, but do not support the DEVPKEY_Device_DriverDate property key. On these earlier versions of Windows, you can access the value of this property by accessing the corresponding **DriverDateData** registry value under the software key for the device instance. For information about how to access this property value on these earlier versions of Windows, see [Accessing Device Driver Properties](https://msdn.microsoft.com/library/windows/hardware/ff537732).

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


[**INF *DDInstall* Section**](https://msdn.microsoft.com/library/windows/hardware/ff547344)

[**INF DriverVer Directive**](https://msdn.microsoft.com/library/windows/hardware/ff547394)

**INF Version section**
[**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963)

 

 






