---
title: DEVPKEY_Device_DriverRank
description: DEVPKEY_Device_DriverRank
ms.assetid: 9a6a8e9f-fd3c-4a64-b0d2-565cda0dae52
keywords: ["DEVPKEY_Device_DriverRank Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_DriverRank
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_Device_DriverRank


The DEVPKEY_Device_DriverRank device property represents the rank of the driver that is installed for a device instance.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_Device_DriverRank</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-uint32.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_UINT32&lt;/strong&gt;](devprop-type-uint32.md)"><strong>DEVPROP_TYPE_UINT32</strong></a></p></td>
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

 

Remarks
-------

Windows sets the value of DEVPKEY_Device_DriverRank.

You can call [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963) to retrieve the value of DEVPKEY_Device_DriverRank.

Windows Server 2003, Windows XP, and Windows 2000 support this property, but do not support the DEVPKEY_Device_DriverRank property key. For information about how to access this property on these earlier versions of Windows, see [Accessing Device Driver Properties](https://msdn.microsoft.com/library/windows/hardware/ff537732).

For information about driver rank, see [How Windows Ranks Drivers](https://msdn.microsoft.com/library/windows/hardware/ff686700) .

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


[**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963)

[**SetupDiGetDriverInstallParams**](https://msdn.microsoft.com/library/windows/hardware/ff551978)

[**SP_DRVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff553290)

 

 






