---
title: DEVPKEY_Device_ResourcePickerExceptions
description: DEVPKEY_Device_ResourcePickerExceptions
ms.assetid: 65a2c709-fe3a-44e2-90f9-4ad6dbcb50bd
keywords: ["DEVPKEY_Device_ResourcePickerExceptions Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_ResourcePickerExceptions
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_Device_ResourcePickerExceptions


The DEVPKEY_Device_ResourcePickerExceptions device property represents the resource conflicts that are allowed for a device instance.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_Device_ResourcePickerExceptions</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-string.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_STRING&lt;/strong&gt;](devprop-type-string.md)"><strong>DEVPROP_TYPE_STRING</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Corresponding registry value identifier and registry value name</strong></p></td>
<td align="left"><p>REGSTR_VAL_RESOURCE_PICKER_EXCEPTIONS</p>
<p><strong>ResourcePickerExceptions</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

You can set the value of DEVPKEY_Device_ResourcePickerExceptions by using an [**INF AddReg directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320) that is included in the [**INF *DDInstall* section**](https://msdn.microsoft.com/library/windows/hardware/ff547344) of the INF file that installs a device.

You can retrieve the value of DEVPKEY_Device_ResourcePickerExceptions by calling [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963).

Windows Server 2003, Windows XP, and Windows 2000 support this property, but do not support the DEVPKEY_Device_ResourcePickerExceptions property key. On these earlier versions of Windows, you can access the value of this property by accessing the corresponding **ResourcePickerExceptions** registry value under the software key for the device instance. For information about how to access this property value on these earlier versions of Windows, see [Accessing Device Driver Properties](https://msdn.microsoft.com/library/windows/hardware/ff537732).

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

[**INF *DDInstall* Section**](https://msdn.microsoft.com/library/windows/hardware/ff547344)

[**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963)

 

 






