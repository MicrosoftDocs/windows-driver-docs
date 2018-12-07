---
title: DEVPKEY_DeviceInterfaceClass_DefaultInterface
description: DEVPKEY_DeviceInterfaceClass_DefaultInterface
ms.assetid: dab341d1-6cab-420b-9ee0-acf6747e2dac
keywords: ["DEVPKEY_DeviceInterfaceClass_DefaultInterface Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DeviceInterfaceClass_DefaultInterface
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_DeviceInterfaceClass_DefaultInterface


The DEVPKEY_DeviceInterfaceClass_DefaultInterface device property represents the symbolic link name of the default device interface for a device interface class.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_DeviceInterfaceClass_DefaultInterface</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-string.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_STRING&lt;/strong&gt;](devprop-type-string.md)"><strong>DEVPROP_TYPE_STRING</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read and write access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

For information about how to install and using device interfaces, see [Device Interface Classes](https://msdn.microsoft.com/library/windows/hardware/ff541339) and the [**INF AddInterface Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546310).

You can retrieve the value of DEVPKEY_DeviceInterfaceClass_DefaultInterface by calling [**SetupDiGetDeviceInterfaceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551122). You can set DEVPKEY_DeviceInterfaceClass_DefaultInterface by calling [**SetupDiSetDeviceInterfaceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552158).

Windows Server 2003, Windows XP, and Windows 2000 support this property, but do not support the DEVPKEY_DeviceInterfaceClass_DefaultInterface property key. For information about how to access the default interface of a device interface class on these earlier versions of Windows, see [Accessing Device Interface Class Properties](https://msdn.microsoft.com/library/windows/hardware/ff537739).

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


[**INF AddInterface Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546310)

[**SetupDiGetClassDevs**](https://msdn.microsoft.com/library/windows/hardware/ff551069)

[**SetupDiGetDeviceInterfaceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551122)

[**SetupDiSetDeviceInterfaceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552158)

 

 






