---
title: DEVPKEY_Device_HardwareIds
description: DEVPKEY_Device_HardwareIds
ms.assetid: 4bfd50b3-027f-4f79-8bff-d0c92c1b2386
keywords: ["DEVPKEY_Device_HardwareIds Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_HardwareIds
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_Device_HardwareIds


The DEVPKEY_DEVICE_HardwareIds device property represents the list of hardware identifiers for a device instance.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_Device_HardwareIds</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-string-list.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_STRING_LIST&lt;/strong&gt;](devprop-type-string-list.md)"><strong>DEVPROP_TYPE_STRING_LIST</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Data format</strong></p></td>
<td align="left">&quot;<em>hw-id1</em>\0<em>hw-id</em>2\0...<em>hw-idn</em>\0\0&quot;</td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Corresponding SPDRP_</strong><em>Xxx</em> <strong>identifier</strong></p></td>
<td align="left"><p>SPDRP_HARDWAREID</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The value of DEVPKEY_DEVICE_HardwareIds is set by the *hw-id* entry values for a device that are supplied by the [**INF *Models* section**](https://msdn.microsoft.com/library/windows/hardware/ff547456) of the INF file that installs a device.

You can call [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963) to retrieve the value of DEVPKEY_DEVICE_HardwareIds.

Windows Server 2003, Windows XP, and Windows 2000 support this property, but do not support the DEVPKEY_DEVICE_HardwareIds property key. Instead, you can use the corresponding SPDRP_HARDWAREID identifier to access the value of the property on these earlier versions of Windows. For information about how to access this property value on these earlier versions of Windows, see [Accessing Device Instance SPDRP_Xxx Properties](https://msdn.microsoft.com/library/windows/hardware/ff537737).

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


[**INF *Models* Section**](https://msdn.microsoft.com/library/windows/hardware/ff547456)

[**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963)

 

 






