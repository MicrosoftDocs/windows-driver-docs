---
title: DEVPKEY_NAME (Device Setup Class)
description: DEVPKEY_NAME (Device Setup Class)
ms.assetid: cc953918-f11a-464c-95cc-ee2a9aa68b7a
keywords: ["DEVPKEY_NAME (Device Setup Class) Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_NAME (Device Setup Class)
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_NAME (Device Setup Class)


The DEVPKEY_NAME device property represents the name of a [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_NAME</p></td>
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
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>Yes</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

You can use the value of DEVPKEY_NAME to identify a device setup class to an end-user in a user interface item.

If DEVPKEY_DeviceClass_Name is set, the value of DEVPKEY_NAME is the same as the value of the [**DEVPKEY_DeviceClass_Name**](devpkey-deviceclass-name.md) device property. Otherwise, the DEVPKEY_NAME value is the same as the value of the [**DEVPKEY_DeviceClass_ClassName**](devpkey-deviceclass-classname.md) device property.

You can call [**SetupDiGetClassProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551086) or [**SetupDiGetClassPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/ff551090) to retrieve the value of DEVPKEY_NAME for a device setup class.

Windows Server 2003, Windows XP, and Windows 2000 do not directly support a corresponding name property. However, these earlier versions of Windows do support properties that correspond to DEVPKEY_DeviceClass_Name and DEVPKEY_DeviceClass_ClassName.

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


[**DEVPKEY_DeviceClass_ClassName**](devpkey-deviceclass-classname.md)

[**DEVPKEY_DeviceClass_Name**](devpkey-deviceclass-name.md)

[**SetupDiGetClassProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551086)

[**SetupDiGetClassPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/ff551090)

[**SetupDiGetClassDescription**](https://msdn.microsoft.com/library/windows/hardware/ff551053)

[**SetupDiClassNameFromGuid**](https://msdn.microsoft.com/library/windows/hardware/ff550947)

 

 






