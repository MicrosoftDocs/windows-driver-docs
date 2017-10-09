---
title: DEVPKEY\_DeviceClass\_IconPath
description: DEVPKEY\_DeviceClass\_IconPath
ms.assetid: c81ea18d-dd21-4b5e-8aba-52f7ad6931bf
keywords: ["DEVPKEY_DeviceClass_IconPath Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DeviceClass_IconPath
api_location:
- Devpkey.h
api_type:
- HeaderDef
---

# DEVPKEY\_DeviceClass\_IconPath


The DEVPKEY\_DeviceClass\_IconPath device property represents an icon list for a [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_DeviceClass_IconPath</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p>[<strong>DEVPROP_TYPE_STRING_LIST</strong>](devprop-type-string-list.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Corresponding registry value name</strong></p></td>
<td align="left"><p><strong>IconPath</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

You can call [**SetupDiGetClassProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551086) or [**SetupDiGetClassPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/ff551090) to retrieve the value of DEVPKEY\_DeviceClass\_IconPath.

A DEVPKEY\_DeviceClass\_IconPath value is a REG\_MULTI\_SZ-typed list of icon resource specifiers in the format that is used by the Windows shell. The format of an icon resource specifier is "*executable-file-path*,*resource-identifier*," where *executable-file-path* contains the fully qualified path of the file on a computer that contains the icon resource and *resource-identifier* specifies an integer that identifies the resource. For example, the icon resource specifier "%SystemRoot%\\system32\\DLL1.dll,-12" contains the executable file path "%SystemRoot%\\system32\\DLL1.dll" and the resource identifier "-12".

Windows Server 2003, Windows XP, and Windows 2000 do not support this property. For information about how to access icon information for a device setup class on these versions of Windows, see [Accessing Icon Properties of a Device Setup Class](https://msdn.microsoft.com/library/windows/hardware/ff537746).

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

[**SetupDiLoadClassIcon**](https://msdn.microsoft.com/library/windows/hardware/ff552053)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DEVPKEY_DeviceClass_IconPath%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





