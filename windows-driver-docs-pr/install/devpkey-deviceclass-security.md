---
title: DEVPKEY_DeviceClass_Security
description: DEVPKEY_DeviceClass_Security
ms.assetid: e23fd11b-07ee-4375-841d-1fa9c42d5a28
keywords: ["DEVPKEY_DeviceClass_Security Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DeviceClass_Security
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_DeviceClass_Security


The DEVPKEY_DeviceClass_Security device property represents a security descriptor structure for a [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_DeviceClass_Security</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-security-descriptor.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_SECURITY_DESCRIPTOR&lt;/strong&gt;](devprop-type-security-descriptor.md)"><strong>DEVPROP_TYPE_SECURITY_DESCRIPTOR</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read and write access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Corresponding SPCRP_</strong><em>Xxx</em> <strong>identifier</strong></p></td>
<td align="left"><p>SPCRP_SECURITY</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

You can set the value of DEVPKEY_DeviceClass_Security either during or after an installation application installs a device setup class. For more information about how to set this property, see [Creating Secure Device Installations](https://msdn.microsoft.com/library/windows/hardware/ff540212).

You can retrieve the value of DEVPKEY_DeviceClass_Security by calling [**SetupDiGetClassProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551086) or [**SetupDiGetClassPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/ff551090). You can set DEVPKEY_DeviceClass_Security by calling [**SetupDiSetClassProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552128) or [**SetupDiSetClassPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/ff552132).

Windows Server 2003 and Windows XP support this property, but do not support the DEVPKEY_DeviceClass_Security property key. On these earlier versions of Windows, you can use the SPCRP_SECURITY identifier to access the value of this property. For information about how to access the value of this property, see [Retrieving Device Setup Class SPCRP_Xxx Properties](https://msdn.microsoft.com/library/windows/hardware/ff550644) and [Setting Device Setup Class SPCRP_Xxx Properties](https://msdn.microsoft.com/library/windows/hardware/ff550814).

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


[**SetupDiGetClassProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551086)

[**SetupDiGetClassPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/ff551090)

[**SetupDiSetClassProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552128)

[**SetupDiSetClassPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/ff552132)

 

 






