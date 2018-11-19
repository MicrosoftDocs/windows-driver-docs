---
title: DEVPKEY_DeviceClass_DevType
description: DEVPKEY_DeviceClass_DevType
ms.assetid: 383f2b47-c0ee-49c2-851c-b18c98fd0303
keywords: ["DEVPKEY_DeviceClass_DevType Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DeviceClass_DevType
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_DeviceClass_DevType


The DEVPKEY_DeviceClass_DevType device property represents the default device type for a [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_DeviceClass_DevType</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-uint32.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_UINT32&lt;/strong&gt;](devprop-type-uint32.md)"><strong>DEVPROP_TYPE_UINT32</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers after a device setup class is installed</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Corresponding SPCRP_</strong><em>Xxx</em> <strong>identifier</strong></p></td>
<td align="left"><p>SPCRP_DEVTYPE</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

You can set the value of DEVPKEY_DeviceClass_DevType when an installation application installs a device setup class. For information about how to install a device setup class and setting this property, see [**INF ClassInstall32 Section**](https://msdn.microsoft.com/library/windows/hardware/ff546335) and the information about the registry entry value **DeviceType** that is provided in the "Special *value-entry-name* Keywords" section of [**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320).

The value of DEVPKEY_DeviceClass_DevType is one of the FILE_DEVICE_Xxx values that are defined in Wdm.h and Ntddk.h. For more information about device types, see the *DeviceType* parameter of the [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) function.

You can call [**SetupDiGetClassProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551086) or [**SetupDiGetClassPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/ff551090) to retrieve the value of DEVPKEY_DeviceClass_DevType.

Windows Server 2003 and Windows XP support this property, but do not support the DEVPKEY_DeviceClass_DevType property key. On these earlier versions of Windows, you can use the SPCRP_DEVTYPE identifier to access the value of this property. For information about how to access the value of this property, see [Retrieving Device Setup Class SPCRP_Xxx Properties](https://msdn.microsoft.com/library/windows/hardware/ff550644).

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


[**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397)

[**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320)

[**INF ClassInstall32 Section**](https://msdn.microsoft.com/library/windows/hardware/ff546335)

[**SetupDiGetClassProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551086)

[**SetupDiGetClassPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/ff551090)

 

 






