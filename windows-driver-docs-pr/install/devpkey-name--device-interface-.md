---
title: DEVPKEY_NAME (Device Interface)
description: DEVPKEY_NAME (Device Interface)
ms.assetid: 276862d0-8ab9-4914-9e57-834cc17d0e59
keywords: ["DEVPKEY_NAME (Device Interface) Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_NAME (Device Interface)
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_NAME (Device Interface)


The DEVPKEY_NAME device interface property represents the name of a device interface.

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
<td align="left"><p>Read-only access by installation applications and installers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>Yes</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The value of the DEVPKEY_NAME should be used to identify an interface to an end-user in a user interface item.

The value of DEVPKEY_NAME is the same as the value of the [**DEVPKEY_DeviceInterface_FriendlyName**](devpkey-deviceinterface-friendlyname.md) device property, if DEVPKEY_DeviceInterface_FriendlyName is set. Otherwise, DEVPKEY_NAME does not exist.

You can retrieve the value of DEVPKEY_NAME by calling [**SetupDiGetDeviceInterfaceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551122).

For information about device interfaces, see [Device Interface Classes](https://msdn.microsoft.com/library/windows/hardware/ff541339) and the [**INF AddInterface Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546310).

Windows Server 2003, Windows XP, and Windows 2000 do not directly support a corresponding name property. However, these earlier versions of Windows do support a property that corresponds to DEVPKEY_DeviceInterface_FriendlyName.

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


[**DEVPKEY_DeviceInterface_FriendlyName**](devpkey-deviceinterface-friendlyname.md)

[**INF AddInterface Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546310)

[**SetupDiGetDeviceInterfaceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551122)

 

 






