---
title: DEVPKEY_Device_UINumber
description: DEVPKEY_Device_UINumber
ms.assetid: 81bd0b71-909d-49c3-8d6c-258c57f80644
keywords: ["DEVPKEY_Device_UINumber Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_UINumber
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_Device_UINumber


The DEVPKEY_Device_UINumber device property represents a number for the device instance that can be displayed in a user interface item.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_Device_UINumber</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-int32.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_INT32&lt;/strong&gt;](devprop-type-int32.md)"><strong>DEVPROP_TYPE_INT32</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Corresponding SPDRP_</strong><em>Xxx</em> <strong>identifier</strong></p></td>
<td align="left"><p>SPDRP_UI_NUMBER</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Windows sets the value of DEVPKEY_Device_UINumber to the value of the UINumber member of the [**DEVICE_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure for a device instance. The bus driver for a device instance returns this value in response to an [**IRP_MN_QUERY_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff551664) request.

You can call [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963) to retrieve the value of DEVPKEY_Device_UINumber.

Windows Server 2003, Windows XP, and Windows 2000 support this property, but do not support the DEVPKEY_Device_UINumber property key. Instead, you can use the corresponding SPDRP_UI_NUMBER identifier to access the value of the property on these earlier versions of Windows. For information about how to access this property value on these earlier versions of Windows, see [Accessing Device Instance SPDRP_Xxx Properties](https://msdn.microsoft.com/library/windows/hardware/ff537737).

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


[**DEVICE_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095)

[**IRP_MN_QUERY_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff551664)

[**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963)

 

 






