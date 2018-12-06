---
title: DEVPKEY_Device_Siblings
description: DEVPKEY_Device_Siblings
ms.assetid: 7456c9f7-6969-4b42-a4f9-f388c731c735
keywords: ["DEVPKEY_Device_Siblings Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_Siblings
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_Device_Siblings


The DEVPKEY_Device_Siblings device property represents a list of the device instance IDs for the devices that are siblings of a device instance.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_Device_Siblings</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-string-list.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_STRING_LIST&lt;/strong&gt;](devprop-type-string-list.md)"><strong>DEVPROP_TYPE_STRING_LIST</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>Not applicable</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

You can call [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963) to retrieve the value of DEVPKEY_Device_Siblings.

Windows Server 2003, Windows XP, and Windows 2000 do not directly support this property. For information about how to retrieve device relations properties on these earlier versions of Windows, see [Retrieving Device Relations](https://msdn.microsoft.com/library/windows/hardware/ff550630).

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

 

 






