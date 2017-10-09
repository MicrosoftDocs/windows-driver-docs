---
title: DEVPKEY\_DeviceClass\_Security
description: DEVPKEY\_DeviceClass\_Security
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
---

# DEVPKEY\_DeviceClass\_Security


The DEVPKEY\_DeviceClass\_Security device property represents a security descriptor structure for a [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509).

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
<td align="left"><p>[<strong>DEVPROP_TYPE_SECURITY_DESCRIPTOR</strong>](devprop-type-security-descriptor.md)</p></td>
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

You can set the value of DEVPKEY\_DeviceClass\_Security either during or after an installation application installs a device setup class. For more information about how to set this property, see [Creating Secure Device Installations](https://msdn.microsoft.com/library/windows/hardware/ff540212).

You can retrieve the value of DEVPKEY\_DeviceClass\_Security by calling [**SetupDiGetClassProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551086) or [**SetupDiGetClassPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/ff551090). You can set DEVPKEY\_DeviceClass\_Security by calling [**SetupDiSetClassProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552128) or [**SetupDiSetClassPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/ff552132).

Windows Server 2003 and Windows XP support this property, but do not support the DEVPKEY\_DeviceClass\_Security property key. On these earlier versions of Windows, you can use the SPCRP\_SECURITY identifier to access the value of this property. For information about how to access the value of this property, see [Retrieving Device Setup Class SPCRP\_Xxx Properties](https://msdn.microsoft.com/library/windows/hardware/ff550644) and [Setting Device Setup Class SPCRP\_Xxx Properties](https://msdn.microsoft.com/library/windows/hardware/ff550814).

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DEVPKEY_DeviceClass_Security%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





